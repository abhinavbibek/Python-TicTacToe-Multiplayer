# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:53:07 2023

@author: bibek
"""
arr=[[' ' for _ in range(3)]for _ in range(3)]
p1=input("player 1 enter your name:")
p2=input("player 2 enter your name:")
turn=0

def check_win(player_symbol):
    for i in range(3):
        if(arr[i][0]==arr[i][1]==arr[i][2]==player_symbol):
            return True
    for i in range(3):
        if(arr[0][i]==arr[1][i]==arr[2][i]==player_symbol):
            return True
    if(arr[0][0]==arr[1][1]==arr[2][2]==player_symbol):
        return True
    if(arr[0][2]==arr[1][1]==arr[2][0]==player_symbol):
        return True
    return False

    
while(1):
    print("\n")
    if(turn%2==0):
        print(p1," your turn")
        player_symbol='X'
    else:
        print(p2," your turn")
        player_symbol='O'
    row=int(input("enter row:"))
    column=int(input("enter column:"))
    if(arr[row][column]==' '):
        arr[row][column]=player_symbol
    else:
        print("cell already occupied try again")
        continue  
    for i in range(3):
        print("["," ",end='')
        for j in range (3):
            print(arr[i][j]," ",end='')
        print("]",end='')
        print("")       
    turn=turn+1
    if (check_win(player_symbol)):
        print("congratulations ",player_symbol,"wins.")
        break
    if(turn==9):
        print("its a draw")
        break
    
    



        

