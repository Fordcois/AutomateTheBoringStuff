import random
totalstreaks=0
results=[0]

def rlistgen(n):
    global results
    results=results*(n)

def trail(rl):
    for i in range ((len(rl))):
        print(rl[i], end='')

def toss():
    for i in range (10):
        if (random.randint(0,1))==1:
            results[(i-1)]=('H')
        else:
            results[(i-1)]=('T')

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
    global totalstreaks
    currentstreak=1
    streaknum=0
    for i in range ((len(fliplist))-1):
        if fliplist[i]==fliplist[(i+1)]:
            currentstreak+=1
            if currentstreak>= target:
                streaknum+=1
        else:
            currentstreak=1
    totalstreaks+=streaknum
    print ('A Streak of ' + (str(target)) + ' happened ' + (str(streaknum)) + ' times.' )

rlistgen(10)
for i in range (5):
    toss()
    trail(results)
    longstreak(results)
    targetstreak(3,results)
print ('A steak of 3 occured '+ (str(totalstreaks)) + ' times in total.')
