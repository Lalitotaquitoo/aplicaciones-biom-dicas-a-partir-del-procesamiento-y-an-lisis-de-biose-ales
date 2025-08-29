import threading
import time
import os
import subprocess
import sys

class SillaRuedas:
                
        def mover(self,x: int, y: int ,z: int, f:int):
                subprocess.Popen(["adb", "shell", "input", "swipe" ,f"{str(x)}" ,f"{str(y)}" ,f"{str(z)}" ,f"{str(f)}" ,"50000"])
                
        def parar(self):
                subprocess.Popen(["adb", "shell", "input", "tap" ,"0","0" ])




                