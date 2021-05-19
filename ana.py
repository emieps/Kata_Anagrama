def read_file(path): 
    with open(path, "r") as f:
       for l in f:
            ana(l)
           




def ana(word):
    dic = {}
    key = sorted(word)
    if key[0] in dic:
        dict[key[0]].apped(word)
    else: 
        dic[key[0]] = word 
    print(dic)


if __name__ == '__main__':
    read_file(r"C:\Users\Emily\Desktop\1.Tendencias\Tendencias en Desarrollo de Aplicaciones\Anagramatest\wordlist.txt")

