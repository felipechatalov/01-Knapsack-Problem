import os
import time
import subprocess

def main():
    subprocess.call(["python", "./write_test.py"])

    subprocess.call(["python", "./mochila.py"])
    
    # subprocess.call(["gcc", "./mochila.c", "-o", "./mochila"])
    # subprocess.call([".\mochila.exe"])

main()



