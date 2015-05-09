# Martin Heinrich 113260
# Daniel Wittmann 113017
#
# Python-Version 3.4.3

#***************************************************************************
# Python-Script zur Lösung der Aufgabe 5 auf den 3. Übungsblatt. Es wird 
# eine Differential Distribution Table, einer gegebenen S-Box erstellt. Die 
#S-box wird als .txt - Datei als Kommandozeilen Parameter entgegen genommen.
#***************************************************************************

import sys
#sbox_data = open(sys.argv[1], 'r').read()
sbox_data = open('s_box.txt', 'r').read() 

#***************************************************************************
# Initialisiert eine Matrix, in welcher die Werte der DDT eingetragen werde.
def create_matrix (string) :
    string.split('\n')
    x = 2** int(string[2])
    y = 2** int(string[0])
    matrix = [[0 for i in range(x)] for j in range(y)]

    return matrix
#***************************************************************************

#***************************************************************************
# Erstellt die Sbox in form einer zwei-dimensionalen Liste. Erste Spalte, 
# enthält den Sbox-Input, die zweite Spalte den Sbox-Output.
def create_sbox (string) :
    string.split('\n')
    x = 2** int(string[0])

    sbox = [0 for i in range(x)]
    j = 0

    for i in range(4,len(string),2) :
        sbox[j] = int(string[i],16)
        j+=1
    
    return sbox
#***************************************************************************

#def print_matrix(matrix) :
    


#***************************************************************************
def DDT(matrix, sbox) :
    for i in range(len(sbox)) :
        for j in range(len(sbox)) :
            matrix[(sbox[i] ^ sbox[j])][(j ^ i)] += 1

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