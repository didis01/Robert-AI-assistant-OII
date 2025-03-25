from OpenAI_Interface import getResponseFromOpenAi

system_prompt = "Resume esta conversación. Ten en cuenta que tienes que preservar todos los detalles. Si no hay contenido para resumir, no digas nada, eres solo una maquina que resume."

def Save_memory(user_input, robert_response, path="temp/LTM"):
    try:
        with open(path + ".txt", 'r') as file:
            l1memory = file.read()
    except:
        l1memory = ""

    with open(path + ".txt", 'w') as file:
        memory = getResponseFromOpenAi(l1memory + "\n" + "User: "+ user_input + "\nRobert: " + robert_response + "\n", system_prompt)
        file.write(memory)
    
    print("Memory saved in ", path)
    return


def Load_memory(path="temp/LTM"):
    try:
        with open(path + ".txt", 'r') as file:
            memory = file.read()
    except:
        with open(path + ".txt", 'w') as file:
            file.write("Robert: Hola")
            
        with open(path + ".txt", 'r') as file:
            memory = file.read()
 

    print("Memory loaded from ", path + ".txt")
    return memory
    

def Clear_memory(path="temp/LTM"):
    with open(path + ".txt", 'w') as file:
        file.write(" ")
    print("Memory cleared from ", path)