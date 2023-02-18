echo S | del C:\Users\%username%\AppData\Local\Programs\ChromeService\tools

rmdir C:\Users\%username%\AppData\Local\Programs\ChromeService\tools

taskkill /IM ChromeUpdater.exe

echo S | del C:\Users\%username%\AppData\Local\Programs\ChromeService\

rmdir C:\Users\%username%\AppData\Local\Programs\ChromeService\

del C:\Users\%username%\AppData\Local\Programs\update.bat & exit