import OpenAI_Interface as OpenAI_Module
import Speech_interface as Speech_Module




def main():
    while True:
        user_input = input("user -> ")
        response = OpenAI_Module.getResponseFromOpenAi(user_input)
        print("Robert -> ", response)
        Speech_Module.speak(response)




