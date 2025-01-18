#fun game using python

import random as rand

def game(com,user):
    if com==user:
        print("tie")
        print(f'computer : {com} - user : {user}')
        return
    elif com =='r' and user=='p':
        print("User win ")
        print(f'computer : {com} - user : {user}')
        return
    elif com =='r' and user=='s':
        print("computer win ")
        print(f'computer : {com} - user : {user}')
        return  
    elif com =='p' and user=='r':
        print("computer win ")
        print(f'computer : {com} - user : {user}')
        return  
    elif com =='p' and user=='s':
        print("user win ")
        print(f'computer : {com} - user : {user}')
        return   
    elif com =='s' and user=='r':
        print("user win ")
        print(f'computer : {com} - user : {user}')
        return 
    elif com =='s' and user=='p':
        print("computer win ")
        print(f'computer : {com} - user : {user}')
        return
    
while True:
        comp=None
        num=rand.randint(1,3)
        if(num==1):
            comp='s'
        elif (num==2):
            comp='r'
        elif (num==3):
            comp='p'
            print('\n***************************\n')
        user = input("\tcomputer choose \n\n Your turns [r-rock,p-paper,s-sesior] Q-quite : ")
        
        if(user=='q'or user =='Q'):
            break
        game(com=comp,user=user)
        # print(num)