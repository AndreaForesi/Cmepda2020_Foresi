""" first assignement of the course "CMEPDA" for the year 2020

--- Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.

--- Specifications
- the program should have a --help option summarizing the usage
- the program should accept the path to the input file from the command line
- the program should print out the total elapsed time
- the program should have an option to display a histogram of the frequences
- [optional] the program should have an option to skip the parts of the text
  that do not pertain to the book (e.g., preamble and license)
- [optional] the program should have an option to print out the basic book
  stats (e.g., number of characters, number of words, number of lines, etc.)

"""

import argparse
import logging
import time
import string
import matplotlib.pyplot as plt
#import re

""" Read and analysis the file input_file and print charachter"""

def process (FilePath, LetterType, histo=False):

    StartTime = time.time()

    logging.info("Reading the file %s..\n", FilePath)

    with open(FilePath) as InputFile:
        text = InputFile.read()

            #Ricerca lettere
        if LetterType=='lower':
            logging.info("Ricerca delle lettere minuscole..")
            Char_enum = {ch: 0 for ch in string.ascii_lowercase}
            LetterType = 'minuscole'

        if LetterType=='upper':
            logging.info("Ricerca delle lettere maiuscole..")
            Char_enum = {ch: 0 for ch in string.ascii_uppercase}
            LetterType='maiuscole'

        if LetterType=='every':
            logging.info("Ricerca di tutte le lettere")
            Char_enum = {ch: 0 for ch in string.ascii_letters}
            LetterType='maiuscole e minuscole'

            #Counting
        logging.info('Counting letter...')
        Char_enum = Counter(FilePath , text , Char_enum , LetterType)
        FinalTime=time.time()

            #Making histogram
        if histo:
            logging.info('Making histogram...')
            plt.bar((Char_enum.keys()),(Char_enum.values()))
            plt.xlabel('Letters')
            plt.ylabel('Letters frequencies [%]')
            plt.title(f'Frequencies of letters of {FilePath}')
            FinalTime=time.time()
            plt.show()

            #time
        elapsed_time = FinalTime - StartTime
        print(f"\nDone in {elapsed_time:.3f} s \n")


""" Counting the letter and return its percentual as value of every key
    The total return is used to statistics (probably)
"""
def Counter (path, file , dict , LT):
    #Inserire if con inizio fine
    for ch in file:#inserire le statistiche
        if ch in dict:
            dict[ch] += 1
    Tot=sum(dict.values())
    for ch,num in dict.items():
        #trasormazione in percentuale
        num=num/Tot*100
        #output
        print(f"There's {num:.3f}% of {ch} in {path}")
    print(f"\nLettere {LT} totali {Tot}")
    return dict


if __name__=='__main__':
          #inizializzazione analizzatore
    parser = argparse.ArgumentParser(usage='Letter Counter of a text',)
        #Aggiunte argomenti al parser
    parser.add_argument('infile', type = str , help = 'path to input file')
    parser.add_argument('LetterType', type = str , choices = ['lower' , 'upper' , 'every'] , help = 'select upper, lower or every type of letter you want to count')
        #inserisco sia per info che per debug perché usando l'opzione debug stmapo anche i debugger di matplotlib
    parser.add_argument('-info', action='store_true' , help='Print info messages')
    parser.add_argument('-debug', action='store_true' , help='Print debugger messages')

        #differenze tra singola o doppia lineetta?
    #parser.add_argument('--part', default='False' , action='store_true', help='you cuold select only a part,section, paragraph of you text')
    parser.add_argument('--histo', action='store_true' , help = 'Show a digram of letter percentage' )
        #analizza il parser e assegna i campi ad args
    args = parser.parse_args()

    if args.info: #questo argmento non va dato alla funzione process
        logging.basicConfig(level=logging.info)
    if args.debug:
        logging.basicConfig(level=logging.debug)

    process(args.infile, args.LetterType, args.histo)
