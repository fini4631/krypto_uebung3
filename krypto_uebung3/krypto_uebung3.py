# -*- coding: utf-8 -*- 

# Martin Heinrich 
# Daniel Wittmann 113017
#
# Python-Version 3.4.3

#***************************************************************************
# Python-Script zur Loesung der Aufgabe 5 auf den 3. Uebungsblatt. Es wird 
# eine Differential Distribution Table, einer gegebenen S-Box erstellt. Die 
#S-box wird als .txt - Datei als Kommandozeilen Parameter entgegen genommen.
#***************************************************************************

import sys
#sbox_data = open(sys.argv[1], 'r').read()
sbox_data = open('s_box.txt', 'r').read() 

def toBinary(n,length):
# https://stackoverflow.com/questions/699866/python-int-to-binary/20643178#20643178
#                                                Länge des jeweiligen Bit. zb 64 oder hier 8
    return ''.join(str(1 & int(n) >> i) for i in range(int(float(length)))[::-1])



#***************************************************************************
# Initialisiert eine Matrix, in welcher die Werte der DDT eingetragen werde.
def create_matrix (string) :
    string.split('\n')
    x = 2** int(string[2])
    #print(x,string[2])
    y = 2** int(string[0])
    #print(y,string[0])
    matrix = [[0 for i in range(x)] for j in range(y)]

    #print(matrix)
    return matrix
#***************************************************************************

#***************************************************************************
# Erstellt die Sbox in form einer zwei-dimensionalen Liste. Erste Spalte, 
# enthaelt den Sbox-Input, die zweite Spalte den Sbox-Output.
def create_sbox (string) :
    string.split('\n')
    x = 2** int(string[0])

    sbox = [[0 for i in range(x)]for j in range(2)]
    b = int(string[0])
    c = int(string[2])

    for i in range(x):
        sbox [0][i] = i

    temp_list = string[4:len(string)]

    temp_list=temp_list.split(",")
    
    for i in range(x):
        sbox[1][i] = int(temp_list[i],16)

    return sbox
#***************************************************************************

#def print_matrix(matrix) :
    
#***************************************************************************
def DDT(matrix, sbox) :

    for i in range(len(sbox)) :
        for j in range(len(sbox)) :
            print(i,j,sbox[1][i],sbox[1][j]) 
            value_i = (int(sbox[1][i]) ^ int(sbox[1][j]))
            value_j = (j ^ i)
            print(value_i,value_j)
            matrix[value_i][value_j] += 1
            print(matrix)

#create_sbox(sbox_data)
#print(create_matrix(sbox_data))
#print(create_sbox(sbox_data))
print(DDT(create_matrix(sbox_data),create_sbox(sbox_data)))


#TODO***********************************************************************
#
# Ausgabe der Matrix schreiben
# Martix mit hilfe der Sbox füllen
#
# dann fertig
