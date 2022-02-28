from random import randint
 

length = int(input("how many characters you wana"))

dinosaur = input("do you not want symbols? If so press 's'")

if dinosaur == "s":
    numberz = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lletter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    uletter = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

    random_total = []

    def random_char(lletter, uletter, smbol): #Generates random letters without symbols
        charl = lletter[randint(0, len(lletter) -1)]
        charul = uletter[randint(0, len(uletter) -1)]
        charn = numberz[randint(0, len(numberz) -1)]
        rchar = [charl, charul, charn]
        char = rchar[randint(0, len(rchar)-1)]
        return char
    
    for i in range(length):
        random_total.append(random_char(lletter,uletter,numberz))

    for i in random_total:
        print (i,end="") #Gets rid of list format
    
else:
    numberz = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lletter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    uletter = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    smbol = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+','{','[','}',']','|',';',':','<','>','?']

    random_total = [] #Same code, except it has symbols

    def random_char(lletter, uletter, smbol):
        charl = lletter[randint(0, len(lletter) -1)]
        charul = uletter[randint(0, len(uletter) -1)]
        chars = smbol[randint(0, len(smbol) -1)]
        charn = numberz[randint(0, len(numberz) -1)]
        rchar = [charl, charul, chars, charn]
        char = rchar[randint(0, len(rchar)-1)]
        return char
    
    for i in range(length):
        random_total.append(random_char(lletter,uletter,smbol))

    for i in random_total:
        print (i,end="")