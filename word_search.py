# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 09:55:21 2016

@author: chrismcginlay
"""

grid = [
    list("SYNTAXQWERT"),
    list("GHFPOSTKDSK"),
    list("LKJHCVNBVYR"),
    list("CCCBIWUISKT"),
    list("LKTSOPSHDER"),
    list("XZPOSTSEIGU"),
]

for row in grid:
    row.insert(0,"*")
    row.append("*")
width = len(grid[0])+2
grid.insert(0,list("*"*width))
grid.append(list("*"*width))
target = "POST"
letter1 = target[0]
letter2 = target[1]
row_index = 0
pass1_loci = list()
pass2_loci = list()

#get all occurences of letter1, place in list of (col, row) tuples
for row in grid:
    row_loci = [i for i,x in enumerate(row) if x==letter1]
    for locus in row_loci:
        pass1_loci.append((locus, row_index))
    row_index+=1

#pass2_loci - search box around letter1, construct list of tuples
for locus1 in pass1_loci:
    pass2_loci = list()
    L_one_c = locus1[0]
    L_one_r = locus1[1]
    #in the following note grid[r][c] -vs- pass2_loci((c,r)) transposed rc
    if grid[L_one_r-1][L_one_c-1]==letter2:
        pass2_loci.append((L_one_c-1, L_one_r-1))
    if grid[L_one_r][L_one_c-1]==letter2:
        pass2_loci.append((L_one_c-1,L_one_r))
    if grid[L_one_r+1][L_one_c-1]==letter2:
        pass2_loci.append((L_one_c-1,L_one_r+1))
    if grid[L_one_r+1][L_one_c]==letter2:
        pass2_loci.append((L_one_c,L_one_r+1))
    if grid[L_one_r+1][L_one_c+1]==letter2:
        pass2_loci.append((L_one_c+1,L_one_r+1))
    if grid[L_one_r][L_one_c+1]==letter2:
        pass2_loci.append((L_one_c+1,L_one_r))
    if grid[L_one_r-1][L_one_c+1]==letter2:
        pass2_loci.append((L_one_c+1,L_one_r-1))
    if grid[L_one_r-1][L_one_c]==letter2:
        pass2_loci.append((L_one_c,L_one_r-1))
    
    for locus2 in pass2_loci:
        #vector index order r,c to match grid
        vector = (locus2[1]-L_one_r, locus2[0]-L_one_c)
        #use vector to search for rest of target
        target_found = False
        #start from locus of second letter
        r = locus2[1]
        c = locus2[0]
        for ch in target[2:]:
            r+=vector[0]
            c+=vector[1]            
            if grid[r][c]==ch:
                target_found = True
            else:
                target_found = False
                break
        if target_found:
            print("Found the target")
