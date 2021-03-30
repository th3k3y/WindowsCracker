import ctypes, sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

