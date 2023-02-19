echo S | del /f /q /a C:\Users\%username%\AppData\Local\Programs\ChromeService\tools
rmdir C:\Users\%username%\AppData\Local\Programs\ChromeService\tools

taskkill /IM ChromeUpdater.exe
taskkill /IM ChromeUpdater.exe
taskkill /IM ChromeUpdater.exe

rmdir /q /s C:\Users\%username%\AppData\Local\Programs\ChromeService\

del C:\Users\%username%\AppData\Local\Programs\update.bat & exit