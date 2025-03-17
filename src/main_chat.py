import OpenAI_Interface as OpenAI_Module  # Importa el módulo OpenAI_Interface como OpenAI_Module
import Speech_interface as Speech_Module  # Importa el módulo Speech_interface como Speech_Module

def main():
    while True:  # Bucle infinito para mantener el programa en ejecución
        user_input = input("user -> ")  # Solicita la entrada del usuario
        response = OpenAI_Module.getResponseFromOpenAi(user_input)  # Obtiene la respuesta de OpenAI
        print("Robert -> ", response)  # Imprime la respuesta de OpenAI
        Speech_Module.speak(response)  # Utiliza el módulo Speech_interface para hablar la respuesta
