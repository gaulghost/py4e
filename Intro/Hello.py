lang = input("Which lang do u understand : en/fr/es\n")
try:
    if lang == "en" :
        m = "Hello"
    elif lang == "fr" :
        m = "Bonjour"
    elif lang == "es" :
        m = "Hola"
    #pass
except :
    #except Exception as e:
    #raise
    print("You entered wrong input")
    exit()
x = input("what is your name\n")
""" Method-1
n=5
while n>0:
    print(n)
    n-=1
print(Blastoff!)
"""
""" Method-2
for i in [5,4,3,2,1] :
    print(i)
print("Blastoff!")
"""
n = print(m,x,"Welcome to my world of python")
