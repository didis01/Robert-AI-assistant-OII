import OpenAI_Interface as OpenAI_Module  # Importa el módulo OpenAI_Interface como OpenAI_Module
import Speech_interface as Speech_Module  # Importa el módulo Speech_interface como Speech_Module
import Memory_interface as Memory_Module  # Importa el módulo Memory_interface como Memory_Module

system_prompt = "Eres un robot de asistencia para mayores, utilizas una raspberry pi 5, cámaras y un lidar para funcionar. Tu idioma es el español. Tu objetivo es ayudar a las personas con la soledad no deseada, no estás hecho para reemplazar un humano, pero tienes que dar conversacion a tu usuario. Por favor, sé amable y educado. Si no sabes qué decir, puedes decir 'No sé qué decir', pero intenta dar siempre conversación."


def main():
    while True:  # Bucle infinito para mantener el programa en ejecución
        user_input = input("user -> ")  # Solicita la entrada del usuario
        memory = Memory_Module.Load_memory()
        response = OpenAI_Module.getResponseFromOpenAi(user_input, system_prompt + "Aquí tienes un resumen de las conversaciones anteriores: " + memory)  # Obtiene la respuesta de OpenAI
        print("Robert -> " + response)  # Imprime la respuesta de OpenAI
        # Speech_Module.speak(response)  # Utiliza el módulo Speech_interface para hablar la respuesta
        Memory_Module.Save_memory(user_input, response)  # Guarda la conversación en memoria


while True:
    main()