import datetime

def getContext():
    context = ("La fecha y hora actual es: " + str(datetime.datetime.now()) + 
               ""
               )
    return context