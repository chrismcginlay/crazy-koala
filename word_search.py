grid = [
    list("SYNTAXQWERT"),
    list("GHFPOSTKDSK"),
    list("LKJHCVNBVYR"),
    list("CCCBIWUISKT"),
    list("LKJVMDSHDER"),
    list("XZKGEDSEIGP"),
]

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
for locus in pass1_loci:
    pass2_loci = list()
    l_one_c = locus[0]
    l_one_r = locus[1]
    if grid[l_one_c-1][l_one_r-1]==letter2:
        pass2_loci.append((l_one_c-1, l_one_r-1))
    if grid[l_one_c-1][l_one_r]==letter2:
        pass2_loci.append((l_one_c-1,l_one_c))
    if grid[l_one_c-1][l_one_r+1]==letter2:
        pass2_loci.append((l_one_c-1,l_one_c+1))
    if grid[l_one_c][l_one_r+1]==letter2:
        pass2_loci.append((l_one_c,l_one_c+1))
    if grid[l_one_c+1][l_one_r+1]==letter2:
        pass2_loci.append((l_one_c+1,l_one_c+1))
    if grid[l_one_c+1][l_one_r]==letter2:
        pass2_loci.append((l_one_c+1,l_one_r))
    if grid[l_one_c+1][l_one_r-1]==letter2:
        pass2_loci.append((l_one_c+1,l_one_r-1))
    if grid[l_one_c][l_one_r-1]==letter2:
        pass2_loci.append((l_one_c,l_one_r-1))
    
    for locus in pass2_loci:
        vector = (pass2_loci(0)-l_one_c, pass2_loci(1)-l_one_r)
        #use vector to search for rest of target
        target_found = False
        r = pass2_loci(1)
        c = pass2_loci(0)
        for ch in target[2:]:
            if grid[r][c]==ch:
                target_found = True
            else:
                target_found = False
                break
            
        if target_found:
            print("Found the target")

