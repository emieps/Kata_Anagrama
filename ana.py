import time
from typing import Dict

def read_file(path): 
    with open(path) as f:
       for l in f:
            ana(l.rstrip("\n"))

dic: Dict = {}
def ana(word):

    key = str(sorted(word))
    if key in dic:
        dic[key].append(word)
    else: 
        dic.setdefault(key, [])
        dic[key].append(word)


if __name__ == '__main__':
    start_time = time.time()
    read_file(r"C:\Users\Emily\Desktop\1.Tendencias\Tendencias en Desarrollo de Aplicaciones\Anagramatest\wordlist.txt")
    
    resul = ""
    count = 0     
    for key, value in dic.items():
        if  len(value) > 1:    
            resul += str(value) + '\n'
            count += 1
    
    print(resul)
    end_time = time.time()
    print(end_time-start_time )
    print(count)
