from OpenAI_Interface import getResponseFromOpenAi

def Save_memory(memory, path="temp/LTM.txt"):
    with open(path, 'a') as file:
        file.write(memory + "\n")
    print("Memory saved in ", path)
    return

    