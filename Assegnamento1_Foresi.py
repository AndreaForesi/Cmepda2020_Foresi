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

""" Read and analysis the file input_file and print charachter"""

def process (input_file, lower=True, upper=False, histo=False):

    start_time = time.time()

    logging.info("Reading the file %s..\n", input_file)

    with open(input_file) as file:

        text = file.read() #pratica ridefinizione

            #Ricerca lettere
        if lower:
            logging.info("Ricerca lettere minuscole..")
            Char_enum = {ch: 0 for ch in string.ascii_lowercase}
            for ch in text:
                if ch in Char_enum:
                    Char_enum[ch] += 1
            TotLetter=sum(Char_enum.values())
            for ch,num in Char_enum.items():
                print(f"The number of '{ch}' in text {input_file} is {num} and is the {(num / TotLetter *100 ):.2f}%\n")
            print(f"\nLettere minuscole totali {TotLetter}")

        if upper:
            logging.info("Ricerca lettere maiuscole..")
            Char_enum = {ch: 0 for ch in string.ascii_uppercase}
            for ch in text:
                if ch in Char_enum:
                    Char_enum[ch] += 1
            TotLetter=sum(Char_enum.values())
            for ch,num in Char_enum.items():
                print(f"The number of '{ch}' in text {input_file} is {num} and is the {(num / TotLetter *100 ):.2f}%\n")
            print(f"\nLettere maiuscole totali {TotLetter}")

        #if histo:


            #time
        elapsed_time = -start_time + time.time()
        print(f"\nDone in {elapsed_time:.3f} \n")


if __name__=='__main__':
          #inizializzazione analizzatore
    parser = argparse.ArgumentParser()
        #Aggiunte argomenti al parser
    parser.add_argument('infile', type = str , help = 'path to input file')
    parser.add_argument('-debug', action='store_true' , help='Print debugger messages')
    parser.add_argument('-lower', action='store_false' , help = 'search the lowercase letters')
    parser.add_argument('-upper', action='store_true' , help = 'search the uppercase letters')
    parser.add_argument('-histo', action='store_true' , help = 'Show a digram of letter percentage' )
        #analizza il parser e assegna i campi ad args
    args = parser.parse_args()

    if args.debug: #questo argmento non va dato alla funzione process
        logging.basicConfig(level=logging.DEBUG)

    process(args.infile, args.lower, args.upper, args.histo)
