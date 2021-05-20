import time

def read_file(path): 
    with open(path) as f:
       for l in f:
            ana(l.rstrip("\n"))

dic = {}
def ana(word):
    key = str(sorted(word))
    if key in dic:
        dic[key].append(word)
    else: 
        dic.setdefault(key, [])
        dic[key].append(word)



start_time = time.time()
read_file(r"C:\Users\Emily\Desktop\1.Tendencias\Tendencias en Desarrollo de Aplicaciones\Anagramatest\wordlist.txt")
end_time = time.time()


count = 0     
for key, value in dic.items():
    if  len(value) > 1:
        print(value)
        count += 1
print(count)
print(end_time-start_time )
