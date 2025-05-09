from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv, find_dotenv  # Importa funciones para cargar variables de entorno desde un archivo .env
from pathlib import Path  # Importa Path para manejar rutas de archivos
import logging
import os
import requests
import OpenAI_Interface as OpenAI_Module  # Importa el módulo OpenAI_Interface como OpenAI_Module
import Speech_interface as Speech_Module  # Importa el módulo Speech_interface como Speech_Module
import Memory_interface as Memory_Module  # Importa el módulo Memory_interface como Memory_Module
import Context_interface as Context_Module  # Importa el módulo Context_interface como Context_Module
system_prompt = "Eres un robot de asistencia para mayores llamado Robert, utilizas una raspberry pi 5, cámaras y un lidar para funcionar. También eres un robot sostenible, ya que utilizas baterías recicladas y también una tpu y un ordenador de bajo consumo. Tu idioma es el español. Tu objetivo es ayudar a las personas con la soledad no deseada, no estás hecho para reemplazar un humano, pero tienes que dar conversacion a tu usuario. Por favor, sé amable y educado. Si no sabes qué decir, puedes decir 'No sé qué decir', pero intenta dar siempre conversación."


load_dotenv(Path(".env"))  # Carga las variables de entorno desde el archivo .env
api_key = os.getenv("bot_api_key")  # Inicializa el cliente OpenAI con la clave API


# Enable logging
logging.basicConfig(
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}! Soy Robert, un robot asistencial.",
        reply_markup = ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Habla y Robert te responde! \nPara consultar la memoria: /memory \nPara borrar la memoria: /clearmem")

async def memory_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    memory = Memory_Module.Load_memory("temp/" + str(user.id))
    await update.message.reply_text("Memoria: " + memory)

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    Memory_Module.Clear_memory("temp/" + str(user.id))
    await update.message.reply_text("Memoria borrada")


    

async def text_handeler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user = update.effective_user
    memory = Memory_Module.Load_memory("temp/" + str(user.id))
    user_input = update.message.text  # Solicita la entrada del usuario
    response = OpenAI_Module.getResponseFromOpenAi(user_input, system_prompt + "Aquí tienes un resumen de las conversaciones anteriores: " + memory, Context_Module.getContext())  # Obtiene la respuesta de OpenAI
    print("Robert -> " + response)  # Imprime la respuesta de OpenAI
    await update.message.reply_text(response)
    Speech_Module.speak(response)  # Utiliza el módulo Speech_interface para hablar la respuesta
    Memory_Module.Save_memory(user_input, response, "temp/" + str(user.id))  # Guarda la conversación en memoria




async def voice_handeler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    try:
        os.remove("temp/"+ str(user.id) + ".oga")

    except:
        print("No temp .oga file to remove")

    new_file = await context.bot.get_file(update.message.voice.file_id)
    open("temp/"+ str(user.id) + ".oga", 'wb').write(requests.get(new_file.file_path).content)
    try:
        os.remove("temp/"+ str(user.id) + ".wav")

    except:
        print("No temp .wav file to remove")

    os.system("ffmpeg -i temp/"+ str(user.id) + ".oga temp/"+ str(user.id) + ".wav")
    transcription = OpenAI_Module.SttOpenAi("temp/"+ str(user.id) + ".wav")
    print("User -> " + transcription)

    memory = Memory_Module.Load_memory("temp/" + str(user.id))
    user_input = transcription
    response = OpenAI_Module.getResponseFromOpenAi(user_input, system_prompt + "Aquí tienes un resumen de las conversaciones anteriores: " + memory, Context_Module.getContext())  # Obtiene la respuesta de OpenAI
    print("Robert -> " + response)  # Imprime la respuesta de OpenAI
    await update.message.reply_text(response)
    Speech_Module.speak(response)  # Utiliza el módulo Speech_interface para hablar la respuesta
    Memory_Module.Save_memory(user_input, response, "temp/" + str(user.id))  # Guarda la conversación en memoria

    



def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(api_key).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("memory", memory_command))
    application.add_handler(CommandHandler("clearmem", clear_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handeler))
    application.add_handler(MessageHandler(filters.VOICE, voice_handeler))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    



if __name__ == "__main__":
    main()