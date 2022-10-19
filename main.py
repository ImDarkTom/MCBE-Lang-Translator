#!.\venv\Scripts\python.exe
from translate import trans
from datetime import datetime
import easygui, os

def main():
    regionDict = {
        "bg": ['bg_BG'],
        "cs": ['cs_CZ'],
        "da": ['da_DK'],
        "de": ['de_DE'],
        "el": ['el_GR'],
        "en": ['en_GB', 'en_US'],
        "es": ['es_ES', 'es_MX'],
        "fi": ['fi_FI'],
        "fr": ['fr_CA', 'fr_FR'],
        "hu": ['hu_HU'],
        "id": ['id_ID'],
        "it": ['it_IT'],
        "ja": ['ja_JP'],
        "ko": ['ko_KR'],
        "no": ['nb_NO'],
        "nl": ['nl_NL'],
        "pl": ['pl_PL'],
        "pt": ['pt_BR', 'pt_PT'],
        "ru": ['ru_RU'],
        "sk": ['sk_SK'],
        "sv": ['sv_SE'],
        "tr": ['tr_TR'],
        "uk": ['uk_UA'],
        "zh-TW": ['zh_TW'],
        "zh-CN": ['zh_CN']
    }

    prettyLangList =  [
        "Bulgarian (bg)",
        "Czech (cs)",
        "Danish (da)",
        "German (de)",
        "Greek (el)",
        "English (en)",
        "Spanish (es)",
        "Finnish (fi)",
        "French (fr)",
        "Hungarian (hu)",
        "Indonesian (id)",
        "Italian (it)",
        "Japanese (ja)",
        "Korean (ko)",
        "Norwegian (no)",
        "Dutch (nl)",
        "Polish (pl)",
        "Portugese (pt)",
        "Russian (ru)",
        "Slovak (sk)",
        "Swedish (sv)",
        "Turkish (tr)",
        "Ukranian (uk)",
        "Simplified Chinese (zh-CN)",
        "Traditional Chinese (zh-TW)"
    ]

    #Select the lang file until given valid lang file
    print('Choosing lang file...')
    langFile = ''
    while langFile[-5:] != '.lang':
        langFile = easygui.fileopenbox(title='MCBE Lang Translator',msg='Select a valid lang file...')

    fileLanguage = langFile[-10:-8]
    print(f"Detected file as '{fileLanguage}'...")

    #Get languages to be translated to
    reply = []
    while len(reply) < 1:
        reply = easygui.multchoicebox(title='MCBE Lang Translator',msg=f'Selected file "{langFile}"...\nChoose the languages to be translated to...', choices=prettyLangList, preselect=-1)

    selectedLangs = []
    for lang in reply:
        selectedLangs.append(lang[lang.find("(")+1 : lang.find(")")]) #Get the text between the brackets to get the language
    print(f"Selected languages: {str(selectedLangs)}")

    #Make output folder
    folderName = f'./translations{datetime.now().strftime(r"%Y%m%d-%H%M%S")}'
    try:
        os.mkdir(folderName)
        print('Created output folder...')
    except:
        print('[WARNING] Folder already exists, continuing write...')

    #Translate and output into files
    for lang in selectedLangs:
        translated = trans(input=fileLanguage, output=lang, filePath=langFile)

        for regionFile in regionDict[lang]:

            with open(f'./{folderName}/{regionFile}.lang', 'w', encoding='utf-8') as file:
                file.write(translated)
            file.close()

            print(f"Finished file '{regionFile}.lang'...")

    rawOutFolderName = folderName.split('/')[1]
    outputPath = f"{os.getcwd()}\{rawOutFolderName}"
    print(f"Output folder located at '{outputPath}'")

    #Open folder location or exit
    finalOutput = easygui.buttonbox(title='MCBE Lang Translator', msg=f"Completed all translations! Translations folder located at '{outputPath}'",choices=["Open folder location", 'Exit'])
    if finalOutput == 'Open folder location':
        os.system(f'explorer.exe "{outputPath}"')

    input("Press enter to exit...")


if __name__ == "__main__":
    main()