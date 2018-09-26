import random
def cube():
    a,b=int(random.random()*7),int(random.random()*7)
    if (a==0) or (b==0):
        return cube()
    if (a==6) and (b==6):
        print("You are very lucky today!\n",a,"&",b,"Rolled!")
    elif(a==b):
        print("Nice Rolling!\n",a,"&",b,"Rolled!")
    else:
        print(a ,"&", b ,"Rolled!")
    return
cube()
