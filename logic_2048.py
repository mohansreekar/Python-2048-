# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:22:34 2024

@author: Mohan Sreekar
"""

import random
#functionn for starting game
def start():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    print("Commands are")
    print("w or W for moving up")
    print("s or S for moving down")
    print("a or A for moving left")
    print("d pr D for moviing rightt")
    #function for adding a 2 in each step
    mat_2(mat)
    return mat
#function to add 2
def mat_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
#function to check wheter the game is completed or not
def game_status(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "CONGRATULATIONS"
    #loop to check if there is atleast one empty cell
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "Game is still on"
    #checking if the games can continue if two cells merge
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return "Game is still on"
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "Game is still on"
    for i in range(3):
        if mat[3][i]==mat[3][i+1]:
            return "Game is still on"
    return "Game Over"
#function ffor moving the elemsnts present in matrix to leftmost
def move(mat):
    a= False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    a= True
                pos+=1
    return new_mat,a
#we check if the adjacent elements are same and then we merge them 
def merge(mat):
    a=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                a=True
    return mat,a
#function for reversing matrix mainly the rows
def rev(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat.append(mat[i][3-j])
    return new_mat
#function for transpose of a matrix
def trans(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat.append(mat[i][j])
    return new_mat
#function for when typed 'a'
def movea(mat):
    new_mat,change1=move(mat)
    new_mat,change2=merge(new_mat)
    change=change1 or change2
    new_mat,a=move(new_mat)
    return new_mat,change
#funtion to move when presses 'd'
def moved(mat):
    new_mat=rev(mat)
    new_mat,change=movea(new_mat)
    new_mat=rev(new_mat)
    return new_mat,change
#function to move when w is pressed
def movew(mat):
    new_mat=trans(mat)
    new_mat,change=movea(new_mat)
    new_mat=trans(new_mat)
    return new_mat,change
#function to move when s is pressed
def moves(mat):
    new_mat=trans(mat)
    new_mat,change=moved(new_mat)
    new_mat=trans(new_mat)
    return new_mat,change
if __name__=='__main__':
    mat=start()
    while(True):
        x=print("enter the input command")
        if(x == 'W' or x == 'w'):
        # call the movew function
            mat, flag = move_w(mat)
 
        # get the current state and print it
            status = game_status(mat)
            print(status)
 
        # if game not over then continue
            if(status == 'Game is still on'):
                mat_2(mat)
        # else break the loop 
            else:
                break
 
    # the above process will be followed
    # in case of each type of move
    # below
 
    # to move down
        elif(x == 'S' or x == 's'):
            mat, flag =moves(mat)
            status = game_status(mat)
            print(status)
            if(status == 'Game is still on'):
                mat_2(mat)
            else:
                break
 
    # to move left
        elif(x == 'A' or x == 'a'):
            mat, flag = movea(mat)
            status = game_status(mat)
            print(status)
            if(status == 'Game is still on'):
                mat_2(mat)
            else:
                break
 
    # to move right
        elif(x == 'D' or x == 'd'):
            mat, flag = moved(mat)
            status = mat_2(mat)
            print(status)
            if(status == 'Game is still on'):
                mat_2(mat)
            else:
                break
    else:
        print("Invalid Key Pressed")
        

        
    