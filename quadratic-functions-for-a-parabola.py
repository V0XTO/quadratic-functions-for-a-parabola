import math
import os
print("______________   _____   _   _ ")
print("| ___ \ ___ \ \ / / _ \ | \ | |")
print("| |_/ / |_/ /\ V / /_\ \|  \| |")
print("| ___ \    /  \ /|  _  || . ` |")
print("| |_/ / |\ \  | || | | || |\  |")
print("\____/\_| \_| \_/\_| |_/\_| \_/")
                   

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

            
                               
def states(a,b, c):


    if(b**2 - 4*a*c==0):
        print("una raiz real")

        xone = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        xtwo = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        values = [xone, xtwo]
        return values
       
    elif(b**2 - 4*a*c>0):
        print("dos raices reales")
        
        xone = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        xtwo = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        values = [xone, xtwo]
        return values
        

    elif(b**2 - 4*a*c<0):
        print("Ninguna raiz real")
        xtwo=0
        xone=0
        values=[xone,xtwo]
        return values
    

def intercepty(a,b,c):
    y = a*0-b*0+c
    return y


def vertice(a, b, c):
    vone = -b / (2 * a)
    vtwo = a * vone**2 + b * vone + c
    return [vone, vtwo]
    

os.system("cls")    


states1,states2 = states(a,b,c)

print(f"Las raices son {states1}, {states2}")
print(f"El intercepto en Y es {intercepty(a,b,c)}")
print(f"El vertice es {vertice(a,b,c)[0]}, {vertice(a,b,c)[1]}")
