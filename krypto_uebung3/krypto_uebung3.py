# -*- coding: utf-8 -*- 
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

if __name__ == '__main__':
    if (len(sys.argv)==2):
        try:
            sbox_data = open(sys.argv[1], 'r').read()
        except IOError:
            print("Exeption: File dosnt exist.")
            exit()   
    else :
        print("Computes the difference distribution table for a given s-box.\nusage: "+sys.argv[0]+" <sbox path>\n\t- <sbox path>: Path to a given S-box difinition")
        exit()
else :
    try:
        sbox_data = open('s_box.txt', 'r').read() 
    except IOError:
        print("Exeption: File dosnt exist.")
        exit()

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
# Erstellt die Sbox in form einer Liste. Der Inize ist gleich den Sbox Input,
# das dzugehörige Element ist gleich den jeweiligen Sbox Output
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



#***************************************************************************
# Erstellt mit hilfe der Matrix und der Sbox die Verteilungstabelle 
def DDT(matrix, sbox) :

    for i in range(len(sbox)) :
        for j in range(len(sbox)) :
           
            matrix[ (j ^ i) % len(matrix) ][(sbox[i] ^ sbox[j]) % len(matrix[0])] += 1
    return matrix
#***************************************************************************

#***************************************************************************
# Ausgabe der Matrix. Erste Zeile enthält die verschiedenen Sbox-Werte. Die 
# Erste Spalte enthält die verschiedenen Werte, welche mit Hilfe der Sbox
# abgebildet werden können.
def printMatrix(matrix) :
    seperator = " "
    
    Ausgabe = seperator + seperator
    for i in range(len(matrix[0])) :
        Ausgabe += str(i) + seperator
    Ausgabe += "\n"
    for i in range(len(matrix)) :
        Ausgabe += str(i) + seperator
        for j in range(len(matrix[0])) :
            Ausgabe += str(matrix[i][j]) + seperator
        Ausgabe += "\n"
    return Ausgabe


print(printMatrix(DDT(create_matrix(sbox_data),create_sbox(sbox_data))))
