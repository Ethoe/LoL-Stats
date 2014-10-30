from datetime import *
from time import sleep
import sys
now = datetime.now()
def lpRecording(lp, League_Points):
    add_nulls = lambda number : "{0:0{1}d}".format(number, 2)
    date = ("{}/{}/{}: ".format(now.month, now.day, now.year)) + '\n'
    if League_Points >0:
        x = "+"+add_nulls(League_Points)
    else:
        x = "-" + add_nulls(abs(League_Points))
    with open('Ethoe.txt','r') as myfile:
        r=myfile.readlines()
    if date in r: 
        with open('Ethoe.txt','a+') as myfile:
            myfile.write("LP: " + lp + " ({})".format(x))
            myfile.write('\n')
    elif date not in r:
        with open('Ethoe.txt','a+') as myfile:
            myfile.write(date)
            myfile.write("LP: " + lp + " ({})".format(x))
            myfile.write('\n')
def lpGain(League_Points):
    r=findLastLine('LP: ')
    add_nulls = lambda number : "{0:0{1}d}".format(number, 3)
    lp=int(r)+League_Points
    if lp <= 0:
        lp = add_nulls(0)
    elif lp >= 100:
        lp = add_nulls(100)
    else:
        lp = add_nulls(lp)
    if lp == 100:
        promotions()
    else:
        lpRecording(str(lp), League_Points)
    return lp

def findLastLine(myWord):
    answer = []
    with open('Ethoe.txt') as myfile:
        lines = myfile.readlines()
    for line in lines:
        if myWord in line:
            answer.append(line)
    answer = answer[len(answer)-1]
    answer = answer[4:7:1]
    return answer
def promotions():
    pass
def summoners():
    summoner = input('What is your summoner name? ')
    with open('Summoner.txt','r') as line:
        lines = line.readlines()
    count = 0
    for line in lines:
        if summoner in line:
            return summoner
        else:
            count += 1
        if count == len(lines):
            newSummoner(summoner)
    
def newSummoner(summoner):
    newSummoner = input('Would you like to make a new file? ')
    if newSummoner == 'yes':
        date = ("{}/{}/{}: ".format(now.month, now.day, now.year)) + '\n'
        lpNew=int(input('What is your current LP? '))
        add_nulls = lambda number : "{0:0{1}d}".format(number, 3)
        x = add_nulls(lpNew)
        with open('{}.txt'.format(summoner),'w') as newfile:
            newfile.write(date + "LP: {}".format(x))
        sleep(2)
        sys.exit()

if __name__ == '__main__':
    print (summoners())
    '''
    League_Points= int(input('How much lp did you get?: '))
    print ("Current lp: " + str(lpGain(League_Points)))
    sleep(5)
    '''
