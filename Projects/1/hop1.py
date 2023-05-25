import random

players = []
scores = []

def menu():
    print("1:Start game")
    print("2:Exit")

def turn(n):
    if ( n%2==0 ):
        return "player"
    else:
        return "computer"
    
def check_result(players,scores,name,score):
    t = 0 
    for i in range(0,len(players),2):
        if players[i] == name and score >= scores[i]:
            t = t + 1
            scores[i]=score
    if ( t == 1 ):
        players.pop()
        scores.pop()                

def resultshow():
    print("\n")
    for i in range(0,len(players)):
        print(players[i]+"  score :"+str(scores[i]))
 
gameRand = 0
game=True
while game:
    print("whats your name?")
    name=input()
    print("Enter the coefficient:")
    zarib = int(input())
        
    x=True
    while x:
        start = random.randint(0,30)
        if start%zarib!=0:
            x=False
            
        print("The game starts from the number:"+str(start))

        score=0
        gameRand = gameRand + 1

        a=True
        while a:
            gameRand = gameRand + 1
            print("player:")
            n=input()
            if (start + 1) % zarib == 0:
                if n != "hop":
                    print("you failed!")
                    print(name + "   score : " + str(score))
                    players.append(name)
                    scores.append(score)
                    check_result(players,scores,name,score) 
                    a = False
                    x = False

            elif n != "hop":
                if int(n) != start + 1:
                    print("you failed!")
                    print(name + "   score : " + str(score))
                    players.append(name)
                    scores.append(score)
                    check_result(players,scores,name,score)                      
                    a = False
                    x = False
 
            elif n == "hop":
                if (start + 1) % zarib != 0:
                    print("you failed")
                    print(name + "   score : " + str(score))
                    players.append(name)
                    scores.append(score) 
                    check_result(players,scores,name,score)                     
                    a = False
                    x = False

        
            score += 1
            start = start + 2
        
            if start % zarib == 0:
                print("computer:hop")
            else:
                print("computer:"+str(start))
                  
 
            
        print("Would you like to play again?")
        print("1:yes")
        print("2:no")
        if input()=="1":
            x=False
            game = True
        else:
            game = False
            x = False
            resultshow()
                

            
            
            
        
                    
            
        
        
        
        
        
        
