l1 = ['1','2','3']
l2 = ['4','5','6']
l3 = ['7','8','9']
def displayfxn():
    print(" | ".join(l1))
    print(" | ".join(l2))
    print(" | ".join(l3))
list123 = []
def p(x):
    while 1:
        i = input(f'Enter position for {x} (1-9): ')
        if i.isdigit()== True and int(i) in list123:
            print("Don't Overwrite")
            i = "qw"
        if i.isdigit() and 0<int(i)<10:
            i = int(i)
            if 1<=i<=3:
                l1[i - 1] = x
            if 4<=i<=6:
                l2[i - 4] = x
            if 7<=i<=9:
                l3[i - 7] = x
            list123.append(i)
            displayfxn()
            break
        else:
            print('Invalid Input! Try Again')
l1 = [' ',' ',' ']
l2 = [' ',' ',' ']
l3 = [' ',' ',' ']
list123 = []
def reset():
    global l1,l2,l3,list123
    l1 = [' ',' ',' ']
    l2 = [' ',' ',' ']
    l3 = [' ',' ',' ']
    list123 = []
def Game():
    print('Please memorize positions!')
    print(" | ".join(['1','2','3']))
    print(" | ".join(['4','5','6']))
    print(" | ".join(['7','8','9']))
    while 1:
        while 1:
            i = input("Do you want X or O: ")
            if i == 'X':
                j = 'O'
                break
            elif i == 'O':
                j = 'X'
                break
            else:
                print('Please enter either X or O')
        p(i)
        p(j)
        p(i)
        p(j)
        while 1:
            p(i)
            if len(list123) == 9:
                print('Game has been Tied!')
                break
            if l1 == [i,i,i] or l2 == [i,i,i] or l3 == [i,i,i]:
                print(f"{i} has won")
                break
            elif l1[0]==l2[0]==l3[0]==i or l1[1]==l2[1]==l3[1]==i or l1[2]==l2[2]==l3[2]==i:
                print(f"{i} has won")
                break
            elif l1[0]==l2[1]==l3[2]==i or l3[0]==l2[1]==l1[2]==i:
                print(f"{i} has won")
                break
            p(j)
            if len(list123) == 9:
                print('Game has been Tied!')
                break
            if l1 == [j,j,j] or l2 == [j,j,j] or l3 == [j,j,j]:
                print(f"{j} has won")
                break
            elif l1[0]==l2[0]==l3[0]==j or l1[1]==l2[1]==l3[1]==j or l1[2]==l2[2]==l3[2]==j:
                print(f"{j} has won")
                break
            elif l1[0]==l2[1]==l3[2]==j or l3[0]==l2[1]==l1[2]==j:
                print(f"{j} has won")
                break
        
        while 1:
            i = input('Do you want to Play Again? (Y/N): ')
            if i == 'Y':
                reset()
                break
            elif i == 'N':
                reset()
                return
            else:
                print('Invalid Input!')

Game()