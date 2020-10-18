""" first assignementof the course "CMEPDA" of 2020 year"""

import argparse
import logging
import time

logging.basicConfig(level=logging.DEBUG)

""" Read and analysis the file input_file and print charachter"""

def process (input_file):

    start_time = time.time()

    logging.info('\n Reading the file %s..\n', input_file)

    with open(input_file) as file:

        for text in file.readline:
            #text = file.readline()
            print('%s',text)
        elapsed_time = start_time - time.time()


 
        logging.info('\n Done in %.4f \n', elapsed_time)


if __name__=='__main__':

    logging.info('Il file è eseguito come main, inizializzo il parser')
    parser = argparse.ArgumentParser()          #inizializzazione analizzatore

        #Aggiunte argomenti al parser
    parser.add_argument('infile', type = str , help = 'path to input file')
        #analizza il parser e assegna i campi ad args
    args = parser.parse_args()
    print(type(args),'\n')
    file_path = args.infile

    process(file_path)
