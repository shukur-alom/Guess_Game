#Guess Game
print('\n\n                                                                             --WELCOME TO GUESS GAME--                    \n\n')
my_hide=23
l=1
Tring_Time=10
try:
    while l<=100:
        User_input=int(input("Enter Your Guess: "))
        if User_input <=5:
            print('Incrise the number more more,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input==my_hide:
            print('Successful,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
            break
        elif User_input<=15:
            print('Incrise the number more,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=16 and User_input<=20:
            print('Incrise the number less,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=21 and User_input<=22:
            print("Incrise the number a little more,",end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=24 and User_input<=27:
            print("Decrease the number a little more,",end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=28 and User_input<=35:
            print('Decrease the number less,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=36 and User_input<=41:
            print('Decrease the number more,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        elif User_input >=42:
            print('Decrease the number more more,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
        if l==Tring_Time:
            print('Game Over,',end='')
            print('\t\tYou have tring',':',l,'\t','You have',':',Tring_Time-l,'try')
            break
        l+=1
except:
    print('\n\t\t\t\tInput a number\n')
        