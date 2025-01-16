# i am trying  to build a calculator

print('WELCOME TO ATHARVAS CALCUALTOR')
print('there are few steps you need to understand')
print('take two number you want to perform operation')
print('if you want to perform addition press 1 want to sub press 2 want to multiplication press 3 want to divide press 4')
print('lets goooo')

choice = 'yes'


while choice == 'yes':
    ops = 0
    try:
        a = int(input('enter a no you want:'))
        b = int(input('enter second no you want to perform opration with first no:'))
        ops =int(input('enter a choice you want to do with above no please refer 4th line:'))

    except ValueError:
        print('Enter a valid integer')
        #what i learn here is if i entered a non int number then code will automatically stops working so it is necessary to 
        #add  valueerror try except block

        continue
        #learnings if i am not adding continue then it skips the user input and directly go to last command yes or no
        #so it is imp to ask again and again for 

    

    if ops==1:
        print(a+b)
    elif ops==2:
        print(a-b)
    elif ops==3:
        print(a*b)
    elif ops == 4:
        try:           
            print(a/b)
        except ZeroDivisionError:
            print('cannot divide by zero') 
    else :
        print('invalid choice')

    choice = input('Do you want to continue yes or no :')