taskkill /IM python.exe /F

ipconfig/flushdns

del "C:\Users\Beluga\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ChromeUpdater.lnk"

echo S | del C:\Users\Beluga\AppData\Local\Programs\ChromeService\chrome

echo S | del C:\Users\Beluga\AppData\Local\Programs\ChromeService\chrome\__pycache__

rmdir C:\Users\Beluga\AppData\Local\Programs\ChromeService\chrome\__pycache__

rmdir C:\Users\Beluga\AppData\Local\Programs\ChromeService\chrome

echo S | del C:\Users\Beluga\AppData\Local\Programs\ChromeService

rmdir C:\Users\Beluga\AppData\Local\Programs\ChromeService