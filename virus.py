import winreg
import os
path = os.getcwd()
key_path = str(path+r"\弹窗1.0.0.exe")

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion")
winreg.SetValue(key, "Run", winreg.REG_SZ, key_path)

winreg.CloseKey(key)
print("创建成功")

