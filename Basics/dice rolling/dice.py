# Program : Dice Rolling Simulator
# User_Name : Abhishek jaiswal
# User_ID : https://github.com/abhishek-iiit
# 
# Feel Free for Pull Request and to contribute to this Project
 
import random
print("This is Dice Simulator by Abhishek")
x = "y" or " Y"
i =1
while x=="y" or x=="Y":
    num = random.randint(1,6)
    if num==1:
        print("-----------")
        print("|         |")
        print("|    *    | This is your " + str(i) + " trial")
        print("|         |")
        print("-----------")
    if num==2:
        print("-----------")
        print("|         |")
        print("|  *   *  | This is your " + str(i) + " trial")
        print("|         |")
        print("-----------")
    if num==3:
        print("-----------")
        print("|  *      |")
        print("|    *    | This is your " + str(i) + " trial")
        print("|      *  |")
        print("-----------")
    if num==4:
        print("-----------")
        print("|  *   *  |")
        print("|         | This is your " + str(i) + " trial")
        print("|  *   *  |")
        print("-----------")
    if num==5:
        print("-----------")
        print("|  *   *  |")
        print("|    *    | This is your " + str(i) + " trial")
        print("|  *   *  |")
        print("-----------")
    if num==6:
        print("-----------")
        print("|  *   *  |")
        print("|  *   *  | This is your " + str(i) + " trial")
        print("|  *   *  |")
        print("-----------")
    x = input("Enter y/Y to play again ,else PRESS ANY KEY TO EXIT\n")
    i+=1


