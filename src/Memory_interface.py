from OpenAI_Interface import getResponseFromOpenAi

system_prompt = "Resume esta conversación. Ten en cuenta que tienes que preservar todos los detalles. Si no hay contenido para resumir, no digas nada, eres solo una maquina que resume."

def Save_memory(user_input, robert_response, path="temp/LTM"):
    with open(path + ".txt", 'a') as file:
        file.write("User: "+ user_input + "\nRobert: " + robert_response + "\n")
    
    with open(path + ".txt", 'r') as file:
        lmemory = file.read()

    with open(path + ".txt", 'w') as file:
        memory = getResponseFromOpenAi(lmemory, system_prompt)
        file.write(memory)
    
    print("Memory saved in ", path)
    return


def Load_memory(path="temp/LTM"):
    with open(path + ".txt", 'r') as file:
        memory = file.read()

    print("Memory loaded from ", path + ".txt")
    return memory
    