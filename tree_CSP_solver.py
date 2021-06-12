#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
start_time = time.time()

X_top = []
parentlist = ['']

def topologicalSORT(C, root):
    global X_top, parentlist

    if parentlist[-1] != root:              #if the last element is the same as the actual: we dont want it to get in parentlist
        parentlist = parentlist + [root]    #introduce in parentlist the root to go back in anycase
    
    while bool(C):
        son = C[root][0]
        X_top = X_top + [[root] + [son]]        #introduce in X_top the parent and the son
        C[root].pop(0)                          #remove the son element from the parent
        C[son].remove(root)                     #remove the parent element from the son
        
        if not bool(C[parentlist[-1]]):         #remove from C and from the parentlist the element it is empty
            C.pop(parentlist[-1])
            parentlist.pop(-1)

        if not bool(C[son]):                    #if the son if empty:
            C.pop(son)                          #delete it from C
            topologicalSORT(C, parentlist[-1])  #need to go back

        else:
            topologicalSORT(C, son)             #move forward
            
    return X_top

def make_arc_consistent(parent,son):
    global D
    failure = False
    for ds in D[son]:
        dp = D[parent[0]][0]
        if dp == ds:
            D[son].remove(ds)
    if not bool(D[son]): #if it is empty
        failure = True
    return failure
    

def tree_CSP_solver(X,D,C):
    n = len(X)
    assingment = []
    root = X[0]
    X = [root] + topologicalSORT(C,root)
    print('topologicalSORT returns: ', X)
    for i in range(1,n-1):
        if make_arc_consistent(X[i][0],X[i][1]):
            print('NO SOLUTION')

    for j in range(0,n):
        assingment = assingment + [ [X[j][-1]] + [D[X[j][-1]][0]] ]
    return assingment


#------------------------MAIN PROGRAM------------------------#

#variables
X = [x for x in "ABCDEFGH"]

#constraints
C = {												
    "A": ["D"],
    "B": ["D","E"],
    "C": ["E"],
    "D": ["A","B","F","G"],
    "E": ["B","C","H"],
    "F": ["D"],
    "G": ["D"],
    "H": ["E"]
}

#domains
D = {str(k):["g","b"] for k in X}



print('Solved problem: ',tree_CSP_solver(X,D,C))
print("--- %s seconds ---" % (time.time() - start_time))