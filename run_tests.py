import os
import time
import subprocess

def main():
    # escreve novos testes aleatorios
    subprocess.call(["python", "./write_test.py"])

    # roda os testes
    subprocess.call(["python", "./test.py"])

main()



