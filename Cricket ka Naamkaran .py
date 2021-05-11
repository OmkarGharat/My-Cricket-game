# Cricket ka Naamkaran

# Rules :

# 1. Enter name of any cricketer in format ( Name <space> Surname )

# 2. Then according to last letter of cricketer's name , enter cricketer's name

# 3. Game will continues

while True :
    wish = input("#### Do you want to continue game (y/n) : ")
    if wish != "y" and wish != "n" :
        print("=============================================================================") 
        print(">> Invalid character ! << ")
        print(">> Run the program again << ")
        print("=============================================================================") 
        break
    if wish == "y" : 
        print("=============================================================================") 
        cric1 = input("Enter name of the Cricketer : ")
        print("Name of cricketer : ",cric1)
        print("Last letter = ",cric1[len(cric1) - 1])
        print("Now , the next name of cricketer starts with letter", cric1[len(cric1) - 1])
        print("=============================================================================")
        cric2 = input("Enter name of cricketer : ")
        print(cric2)
        print("Last letter = ",cric2[len(cric2) - 1] )
        print("Now , the next name of cricketer starts with letter", cric2[len(cric2) - 1])
        print("=============================================================================")
        continue
    if wish == "n" :
        break

'''
    else:
        break
'''

 #if wish != "n" : 

 
