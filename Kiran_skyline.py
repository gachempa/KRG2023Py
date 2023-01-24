#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:31:24 2023

@author: kiranjames
"""

def building (alist, blist, hlist):

   solution_list = []
   if ((find_copy(alist, hlist, 0))):
       solution_list.append([alist[0], hlist[0]])


   for i in range(1, len(alist)):
        a1 = True
        for j in range(0, i):
            if hlist[i]<=hlist[j]:
                a1 = False
        if (a1==True and find_copy(alist, hlist, i)):
            solution_list.append([alist[i], hlist[i]])
        
            
            
   while (len(blist)>1):
       min_index = blist.index(min(blist))
       a = hlist[min_index]
       m = True
       for i in range(0, len(hlist)):
           if  i != min_index and a <= hlist[i]:
               m = False
       if (m):
            del hlist[min_index]
            solution_list.append([min(blist), max(hlist)])
            del blist[min_index]
       else:
            del blist[min_index]
            del hlist[min_index]
   solution_list.append([blist[0], 0])
        
   return solution_list
    



def inputFunction (alist, blist, hlist):
    list_break = [0]
    k = 0
    for i in range(1, len(alist)):
        a = True
        for j in range(k, i):
            if alist[i]<=blist[j]:
                a = False
              
        if a == True:
            list_break.append(i)
            k=i
    return list_break



def break_apart(alist, blist, hlist, list_break):
    list1 = []
    if len(list_break)==0:
        list1 = list1 + building(alist, blist, hlist)
    
    for i in range(0, len(list_break)-1):
        list1 = list1 + building(alist[list_break[i]: list_break[i+1]], 
                                blist[list_break[i]: list_break[i+1]],
                                hlist[list_break[i]: list_break[i+1]])
        
    
    list1 = list1 + building(alist[list_break[len(list_break)-1]:len(alist)],
                            blist[list_break[len(list_break)-1]:len(blist)],
                            hlist[list_break[len(list_break)-1]:len(hlist)])
    return list1
                                       
def find_copy(alist, hlist, l):
    list2 = []
    l1=l
    while (l1 != len(alist)-1 and alist[l1]==alist[l1+1]):
        list2.append(l1)
        l1=l1+1
    
    g = True
    if (len(list2)>1):
        for i in (1, len(list2)):
            if hlist[l] <= hlist[list2[i]]:
                g = False
    return g




#list1 = [[0,2,3],[2,5,3]]
#list1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
list1 = [[2,9,10], [2,10,8], [3,7,15],[5,12,12],[15,20,10],[19,24,8]]

alist = []
blist = []
hlist = []
    
    
for i in list1:
    alist.append(i[0])
    
for i in list1:
    blist.append(i[1])

for i in list1:
    hlist.append(i[2])
    
    
print(break_apart(alist, blist, hlist, inputFunction(alist, blist, hlist)))