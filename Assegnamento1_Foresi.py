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

logging.basicConfig(level=logging.DEBUG)

""" Read and analysis the file input_file and print charachter"""

def process (input_file):

    start_time = time.time()

    logging.info('\n Reading the file %s..\n', input_file)

    with open(input_file) as file:

        #for text in file.readline:
        text = file.read()

        Char_enum = {ch: 0 for ch in string.ascii_lowercase}
        #Char_enum = {ch: 0 for ch in string.ascii_uppercase}
        #Char_enum = {ch: 0 for ch in string.ascii_letters}

        elapsed_time = start_time - time.time()

        logging.info('\n Done in %.4f \n', elapsed_time)


        print(f'there is {Char_enum}')



if __name__=='__main__':

    #logging.info('Il file è eseguito come main, inizializzo il parser')
    parser = argparse.ArgumentParser()          #inizializzazione analizzatore

        #Aggiunte argomenti al parser
    parser.add_argument('infile', type = str , help = 'path to input file')
        #analizza il parser e assegna i campi ad args
    args = parser.parse_args()
    #print(type(args),'\n')
    file_path = args.infile

    process(file_path)
