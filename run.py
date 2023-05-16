import requests
import os




def write_f(file):
    #if open(f"C:\TURBOC3\BIN\{file}",'a'):
    #    os.remove(file)
    url = f"https://raw.githubusercontent.com/anubis-tyrant/DAA-sus/main/codes/{file}"
    print(url)
    str = requests.get(url)
    with open(f"C:\TURBOC3\BIN\{file}",'w') as f:
        f.write(str.text)

for i in range(1,9):
    write_f(f"A{i}.CPP")