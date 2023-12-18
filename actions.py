import exe
import os

def actionOnShutdown():
    exe.execute()
    os.system('shutdown -s -t 0')
    
def actionOnRecover():
    exe.execute()
    os.system('shutdown -r -t 0')