import random
totalstreaks = 0
results = [0]
streaktarget = 0

def rlistgen(n):
    global results
    results = results*(n)

def trail(rl):
    for i in range((len(rl))):
        print(rl[i], end='')

def toss(i):
    for i in range(i):
        if (random.randint(0, 1)) == 1:
            results[(i-1)] = ('H')
        else:
            results[(i-1)] = ('T')

def targetstreak(target, fliplist):
    global totalstreaks
    global streaktarget
    streaktarget = target
    currentstreak = 1
    streaknum = 0
    for i in range((len(fliplist))-1):
        if fliplist[i] == fliplist[(i+1)]:
            currentstreak += 1
            if currentstreak >= target:
                streaknum += 1
                break
        else:
            currentstreak = 1
    totalstreaks += streaknum

def experiment(numofflips, timesrepeated, streakaim):
    rlistgen(numofflips)
    for i in range(timesrepeated):
        toss(numofflips)
        targetstreak(streakaim, results)
    print('A steak of ' + (str(streaktarget)) + ' occured ' + (str(totalstreaks)) + ' times in total across '+(str(numofflips*timesrepeated))+' coin flips')
    print('According to this experiment there is a ' + (str((totalstreaks/timesrepeated)*100)) + ' percent chance of a streak of ' + (str(streaktarget)) + ' occuring in '+(str(numofflips)) + ' coin flips.')
experiment(100, 10000, 6)
