from OpenAI_Interface import getResponseFromOpenAi

system_prompt = "Resume esta conversación. Ten en cuenta que tienes que preservar todos los detalles."

def Save_memory(user_input, robert_response, path="temp/LTM.txt"):
    with open(path, 'a') as file:
        file.write("User: "+ user_input + "\nRobert: " + robert_response + "\n")
    with open(path, 'w') as file:
        memory = getResponseFromOpenAi(file.read(), system_prompt)
        file.write(memory)
    
    print("Memory saved in ", path)
    return

    