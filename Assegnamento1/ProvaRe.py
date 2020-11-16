import re
import argparse
import logging

logging.basicConfig(level=logging.INFO)

ReWord = re.compile(r'volta$')
ReSpace = re.compile('$')
ReStop = re.compile('Stop')
start='r'+'Devo correggere perche. non prende'
#RePhraseSTA = re.compile(r'Devo correggere perche. non prende')
RePhraseSTA = re.compile(start)
RePhraseEND = re.compile(r'Ho vinto io\!\!\!')

"""\w singolo carattere , \w+ parola
    \. tutti i caratteri tranne newline
"""

def ProvaRe (File_Path, part):
    NL , LSS = 0 , 0



    with open(File_Path) as file:
        line=file.readline()
        if part==1:
            while RePhraseSTA.match(line) == None:
                line=file.readline()
        print(line)
        logging.info('start to calculate stats')
        for line in file:
            print(line)
            if part==1 and RePhraseEND.match(line):
                logging.info('end calculate stats')
                break
        #print(f'lines read until your ending selected {NL} and {LSS} of them skipped for the intro')

        #text=file.read()
        #print(text)
    #    TextLines=re.split('\n+', file.readline())
    #print(TextLines)

    #  line=file.readline()
     # while ReSpace.search(line):
    #      print(line)
    #      print(f'match {ReSpace.match(line)}')
    #      #match funziona solo con la prima stringa del file
    #      print(f'SEARCH {ReSpace.search(line)}')
          #cerca in tutto il file ma si ferma alla prima crrispondenza
    #      print(f'findall {ReSpace.findall(line)}, {len(ReSpace.findall(line))}')
    #      line=file.readline()



    #      if len(ReSpace.findall(line))==1:
    #        print(line)
    #        break



if __name__=='__main__':
  parser= argparse.ArgumentParser()

  parser.add_argument('input_file')
  parser.add_argument('-part', action = 'store_true' , default = 'False')

  args = parser.parse_args()

  ProvaRe(args.input_file, args.part)
