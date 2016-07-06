'''
The NewsSearch module displays the line in the file on which the words are found. There are 2 options to find the words.
	- AND : Print the line numbers in which all the words are found.
	- OR  : Print the line numbers in which any of the words are found.
Author : Vikram Shinde	
'''

import random
import sys
import os

# Function for AND search.
def andSearch(infile, inputstring):
    inputList = inputstring.split()
    result = []
    with open(infile) as myFile:
        for num, line in enumerate(myFile, 0):
            words = line.lower().split()
            for inputWord in inputList:
                if inputWord not in words:
                    break
                elif inputWord != inputList[-1]:
                    continue
                else:
                    result.append(num)
    return result

# Function for OR search
def orSearch(infile, inputstring):
    inputList = inputstring.split()
    result = []
    with open(infile) as myFile:
        for num, line in enumerate(myFile, 0):
            words = line.lower().split()
            if any(word in inputList for word in words):
                result.append(num)
    return result


# Main function
def searchword(infile, inputstring, typeOfSearch):
    inputstring = inputstring.lower()
    typeOfSearch = typeOfSearch.lower()
    if typeOfSearch.strip() == 'and':
        result = andSearch(infile, inputstring)
    elif typeOfSearch.strip() == 'or':
        result = orSearch(infile, inputstring)
    else:
        return ('Please enter correct Type of Search')
    return result

def main():
    infile = input('Enter file name : ')
    inputstring = input('Enter the Words you want to search seperated by Space : ')
    typeOfSearch = input('Enter Type of Search (OR / AND) : ')
    result = searchword(infile, inputstring, typeOfSearch)
    print (result)

if __name__ == '__main__':
    main()
