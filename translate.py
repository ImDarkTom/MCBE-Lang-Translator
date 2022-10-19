import googletrans

#

def trans(input:str, output:str, filePath:str):
    #Todo:
    #-Optimise the id and name splitting
    
    #Reads the file and gets all lines
    langFile = open(filePath)
    originalText = langFile.readlines()
    langFile.close()

    itemNames = ""
    itemDefs = ""

    #Splits item names and ids into different strings
    for line in originalText:
        try:
            itemName = line.split('=')[1]
            itemDef = line.split('=')[0]
        except IndexError:
            itemName = ''
        
        if itemName == '':
            pass
        else:
            itemDefs += f"{itemDef}\n"
            itemNames += itemName

    #Actual translation
    translated = googletrans.Translator().translate(text=itemNames, src=input, dest=output).text

    #Splits the strings into lists (prob gonna optimise this later)
    translatedList = []
    for translation in translated.split('\n'):
        translatedList.append(translation)

    defsList = []
    for defi in itemDefs.split('\n'):
        defsList.append(defi)

    #Final compilation into a singlular string that is going to be sent back
    finalList = ""
    for i in range(len(translated.split('\n'))):
        finalList += f"{defsList[i]}={translatedList[i]}\n"
    
    #Sending back final string
    return finalList