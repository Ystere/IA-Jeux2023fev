# coding=utf-8
# 3700946 wguillaume28@gmail.com | wesley.guillaume@etu.sorbonne-universite.fr

def readFile(f): #Q1
    TEST = 3
    p_file = open(f, "r")
    lines = p_file.readlines()

    file_len = len(lines)
    for i in range (1, file_len):
        lines[i]=lines[i].split()
    print("Selected test line : ",TEST+1,"\n",lines[TEST],"\n")
    return lines

def displayLines(T):
    return

mat_pref_etu = readFile("PrefEtu.txt")
mat_pref_master = readFile("PrefSpe.txt")
print(mat_pref_etu)

