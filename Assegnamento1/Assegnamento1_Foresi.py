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
import re

ReWord = re.compile(r'\b\w+\b')

""" Read and analysis the file input_file and print charachter"""

def process (FilePath, LetterType, histo=False, part=False):
    StartTime = time.time()

            #Read the input Lettertype
    if LetterType=='lower':
        logging.info("Ricerca delle lettere minuscole..")
        Char_enum = {ch: 0 for ch in string.ascii_lowercase}

    if LetterType=='upper':
        logging.info("Ricerca delle lettere maiuscole..")
        Char_enum = {ch: 0 for ch in string.ascii_uppercase}

    if LetterType == 'every':
        logging.info("Ricerca di tutte le lettere")
        Char_enum = {ch: 0 for ch in string.ascii_letters}

    if LetterType == 'stats':
        logging.info('Ricerca delle letterre e caratteri...')
        Char_enum = {ch: 0 for ch in string.printable}


            #Counting with secondary function
    logging.info('Counting letter...')
    Char_enum , TotChar , InputTime = Counter(FilePath , Char_enum , LetterType , part)
    FinalTime=time.time()

            # calculate time
    elapsed_time = FinalTime - StartTime - InputTime
    print(f"\nDone in {elapsed_time:.3f} s \n")

            #Making histogram
    if histo==True:     #lo stta correttamente tra True e false ma senza == non lo prende
        import matplotlib.pyplot as plt
        logging.info('Making histogram of the letter only...')
        if LetterType=='stats':         #it's necessary to read only letter caracthers
            #import numpy   Già importato tramite matplotlib
            n=numpy.zeros(len(string.ascii_letters))
            for i in range(len(string.ascii_letters)):
                n[i]=Char_enum[string.ascii_letters[i]]*100/TotChar
            plt.bar([ch for ch in string.ascii_letters],n)
        else:
            plt.bar((Char_enum.keys()),([num / TotChar * 100 for num in Char_enum.values()]))
        plt.xlabel('Letters')
        plt.ylabel('Letters frequencies [%]')
        plt.title(f'Frequencies of letters of {FilePath}')
        plt.show()







""" Counting the letter and return its percentual as value of every key
    The total return is used to statistics (probably)
"""
def Counter (path , dict , LT, part):
    logging.info(f"Reading the file {path}..")

    NumWord , NumLines = 0 , 0

    logging.info('opening file..')
    with open(path) as file:
        if part==True:
            #interactive section of the module.
            """You can select youself the first and last line do you want to let
                the program analys
            """
            #Start line input
            print('Write the first line you want let the program read')
            logging.debug('Some of the special characters like "*" need the backslash before it: right \*, wrong only * ')
            #i decide to eliminate the input time from the total time used to compile the program
            t1=time.time()
            Start=input()
            t2=time.time()
            StartParagraph=re.compile(Start)
            #Stop line input
            print('And the last line do you want to let the program read')
            logging.debug('Some of special characters need the backslash before: write \* not only * ')
            #same as before
            t3=time.time()
            Stop=input()
            t4=time.time()
            StopParagraph=re.compile(Stop)
        #analisis
            logging.info('searching starting line')
            line=file.readline()
            while StartParagraph.match(line) == None:
                line=file.readline()
            #necessary to not jump over forst line
            NumLines+=1
            NumWord += len(ReWord.findall(line))
            for ch in line:
                if ch in dict:
                    dict[ch] += 1
        else:
            t1=t2=t3=t4=0

        logging.info('Start Calculate Stats')
        for line in file:
            if part==True and StopParagraph.match(line):
                logging.info('Find your selected last line')
                break
            NumLines+=1
            NumWord += len(ReWord.findall(line))
            for ch in line:
                if ch in dict:
                    dict[ch] += 1
        Tot=sum(dict.values())

        #output
        print(f"\nTotal readed charachters: {Tot}")
        print(f"\nTotal readed word: {NumWord}")
        print(f"\nTotal readed line: {NumLines} \n")

        #correzione per eliminare i caratteri speciali e restituire solo lettere
        if LT == 'stats':
            #calcolo sole lettere
            TotLett=0
            #first of all calculate the total number of letter only
            for ch in string.ascii_letters: TotLett+=dict[ch]   #I select only the letters charachters
            #output only
            for ch in string.ascii_letters:                     #even there
                print(f"There's {dict[ch]/TotLett*100:.2f}% of {ch} in {path}")

        else:
            #simple count of the charachters readed, this time every charachter is a letter
            for ch,num in dict.items():      #I select only the letters charachters
                TotLett=Tot             # per l'output
                num=num/Tot*100         #percentual trasformation
                print(f"There's {num:.2f}% of {ch} in {path}")      #output
    #i calculate the delay time in which the user write the lines of start and stop
    InTime = t2-t1 + t4-t3
    return dict , TotLett , InTime







if __name__=='__main__':
          #inizializzazione analizzatore
    parser = argparse.ArgumentParser(usage='Letter Counter of a text',)
        #Aggiunte argomenti al parser
    parser.add_argument('infile', type = str , help = 'path to input file')
    parser.add_argument('LetterType', type = str , choices = ['lower' , 'upper' , 'every' , 'stats'] , help = 'select an option to have statistics about lower (lower) or upper (upper) case letters, every letters with (stats) or without (every) charachters')
        #inserisco sia per info che per debug perché usando l'opzione debug stmapo anche i debugger di matplotlib
    parser.add_argument('-info', action='store_true' , help='Print info messages')
    parser.add_argument('-debug', action='store_true' , help='Print debugger messages')

        #differenze tra singola o doppia lineetta?
    parser.add_argument('--part', default='False' , action='store_true', help='you cuold select only a part,section, paragraph of you text')
    parser.add_argument('--histo', action='store_true' , default = 'False' , help = 'Show a digram of only letter percentage' )
        #analizza il parser e assegna i campi ad args
    args = parser.parse_args()

    if args.info: #questo argmento non va dato alla funzione process
        logging.basicConfig(level=logging.INFO)
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    process(args.infile, args.LetterType, histo=args.histo, part=args.part)
