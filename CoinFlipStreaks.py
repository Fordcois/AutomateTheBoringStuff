import random
results=[]
def trail(rl):
    for i in range ((len(rl))):
        print(rl[i], end='')

def toss():
    for i in range (10):
        if (random.randint(0,1))==1:
            results.append('H')
        else:
            results.append('T')

def longstreak(fliplist):
    currentstreak=1
    higheststreak=0
    streaknum=0
    for i in range ((len(fliplist))-1):
        if fliplist[i]==fliplist[(i+1)]:
            currentstreak+=1
            if currentstreak>= higheststreak:
                higheststreak=currentstreak
        else:
            currentstreak=1
    print (' - Highest streak was ' + (str(higheststreak)))

def targetstreak (target,fliplist):
    currentstreak=1
    streaknum=0
    for i in range ((len(fliplist))-1):
        if fliplist[i]==fliplist[(i+1)]:
            currentstreak+=1
            if currentstreak>= target:
                streaknum+=1
        else:
            currentstreak=1
    print ('A Streak of ' + (str(target)) + ' happened ' + (str(streaknum)) + ' times.' )

def experiment(timesrun):
    for y in range (timesrun):
        toss()
        trail(results)
        longstreak(results)
        targetstreak(3,results)

experiment(3)