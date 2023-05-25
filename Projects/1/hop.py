import random

gameCheck = True
Result = []
while gameCheck == True: #This while loop check the all games to be done.
    print("Enter your name:")
    UserName = input() #It is the username of player.
    
    print("Enter a number as the hope's coefficient:") 
    hop = int(input()) #It is the coefficient of hope number.
                    
    def Computer_number():
        FirstNumber = random.randint(1,50) #It is the first number which the computer start the game with it.
    
        while FirstNumber == hop: #It is a while loop for checking that the Hope and FirstNumber not to be equal with eachother.
            FirstNumber = random.randint(1,50)
        return FirstNumber
    
    def Show_Point(Result):
        print("  Name   |  Point\n-------------------")
        length = len(Result) 
        for i in range(0,length,2):
            print("  " + Result[i] + "      " + Result[i+1] )
            
    def Check_Schedule(Result,UserName,Point):
        t=0
        for i in range(0,len(Result),2):
            if Result[i] == UserName and int(Point) > int(Result[i+1]):
                t+=1
                Result[i+1] = Point # Here the points of the UserName will be updated.        
        if ( t == 1):  
            Result.pop() # It is remove the UseNames which wrote more than one time in the Schedule. 
            Result.pop() # It is remove the UseNames which wrote more than one time in the Schedule.
                     
                
    check = True
    i = 0 #This value help us to know who is the turn for.(Player or Computer)
    checkNumber = Computer_number() - 1

    while check == True: #This while loop check a round of game only.
        i = i + 1
        checkNumber = checkNumber + 1     
        if i%2 == 1:
            print("Computer Turn's:")
            if checkNumber % hop == 0 and i != 1:
                print("hop")
            else:
                print(checkNumber)    
            check = True
        else:
            point = str((i - 1)//2)
            print(UserName + " Turn's")
            playerInput = input()

            if checkNumber % hop == 0 and playerInput == "hop":
                check = True
            elif checkNumber % hop !=0 and playerInput == "hop":
                print("You lose and your point is " + point + ".\n" + "Do you want to play again?!?\n1.Yes   2.No")
                Answer = int(input())
                if Answer == 1:
                    Result.append(UserName)
                    Result.append(point)                    
                    check = False
                    i = 0
                    checkNumber = Computer_number() - 1
                elif Answer == 2:
                    Result.append(UserName)
                    Result.append(point)
                    check = False
                    gameCheck = False
                    Check_Schedule(Result,UserName,point)    
                    Show_Point(Result)                    
            elif int(playerInput) % hop == 0:
                print("You lose and your point is " + point + ".\n" + "Do you want to play again?!?\n1.Yes   2.No")
                Answer = int(input())
                if Answer == 1:
                    Result.append(UserName)
                    Result.append(point)                    
                    check = False
                    i = 0
                    checkNumber = Computer_number() - 1
                elif Answer == 2:
                    Result.append(UserName)
                    Result.append(point)
                    check = False
                    gameCheck = False
                    Check_Schedule(Result,UserName,point)      
                    Show_Point(Result)            
            elif int(playerInput) == checkNumber:
                check = True
            else:
                print("You lose and your point is " + point + ".\n" + "Do you want to play again?!?\n1.Yes   2.No")
                Answer = int(input())
                if Answer == 1:
                    Result.append(UserName)
                    Result.append(point)                    
                    check = False
                    i = 0
                    checkNumber = Computer_number() - 1
                elif Answer == 2:
                    Result.append(UserName)
                    Result.append(point)
                    check = False 
                    gameCheck = False
                    Check_Schedule(Result,UserName,point)                     
                    Show_Point(Result)                  
                      
    print("Would you like to play again?\n1.Yes   2.No")
    a = input()
    if a=="1":
        game=False
        gameCheck = True
    elif a=="2":
        print("Thansk for using us.")
        gameCheck = False