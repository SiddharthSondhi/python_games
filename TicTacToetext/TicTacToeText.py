import time

d={1:'*' ,2:'*' ,3:'*' ,4:'*' ,5:'*' ,6:'*' ,7:'*' ,8:'*' ,9:'*' }
def t():
    for i in d:
        print(d[i],end=" ")
        if i == 3 or i==6:
            print('')
win=False
def checkwin():
    global win
    for n in range(1,10,3):
        if d[n]==d[n+1]==d[n+2]!='*':
            print (' ')
            print ('Player',d[n],'wins.')
            win =True
    for n in range(1,3,1):
        if d[n]==d[n+3]==d[n+6]!='*':
            print (' ')
            print ('Player',d[n],'wins.')
            win =True

    if d[1] == d[5] == d[9] and d[1]!='*':
        print (' ')
        print ('Player',d[1],'wins.')
        win =True
        
    if d[7] == d[5] == d[3] and d[7]!='*':
        print (' ')
        print ('Player',d[1],'wins.')
        win =True

t()
p = ['X','O']
n=0
for g in range (0,9):
    print ('')
    print ('Player ',p[n], 'chose a square.')
    a=int(input())
    while d[a]!= '*':
        print ('Player ',p[n], 'chose a square.')
        a=int(input())
    d[a]=p[n]
    t()
    checkwin()
    if win == True:
        time.sleep(5)
        break
    n=n+1
    if n >1:
        n=0


    ###comment####
   

        
