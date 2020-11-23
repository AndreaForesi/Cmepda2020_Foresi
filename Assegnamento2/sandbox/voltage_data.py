"""Module: basic Python
Assignment #2 (October 12, 2020)


--- Goal
Write a class to handle a sequence of voltage measurements at different times.

--- Specifications
- the print() function must work on class instance. The output must show one
  entry (time and voltage), as well as the entry index, per line.
- the class must have a plot() method that plots data using matplotlib.
  The plot function must accept 'ax' argument, so that the user can select
  the axes where the plot is added (with a new figure as default). The user
  must also be able to pass other plot options as usual.
"""


import numpy
from matplotlib import pyplot as plt


class VoltageData:
    """Class for handling a set of measurements of the voltage at different
    times."""
    #per prima cosa il costruttore con self come primo argomento
    #poi la specifica, ovvero le due iterabili same length
    """- the class name must be VoltgeData"""
    def __init__(self, times, voltages):
        """ -times and voltages are two iterable of the same length
            -the class must be initialized with two generic iterables of the same length
            holding the numerical values of times and voltages
        usiamo la composizione
        """
        #creo i due iterabili
        t = numpy.array(times, dtype=numpy.float64)      #attenzione all'ordine degliargomenti
        v = numpy.array(voltages, dtype=numpy.float64)    #dtype indica il tipo delle variabili
        #ok però questi due array dovranno essere atributi
        """- the class must expose two attributes: 'times' and 'voltages', each returning
          a numpy array of type numpy.float64 of the corresponding quantity.
          perciò al posto delle righe sopra devo farli essere degli attributi della classe VoltageData
        """
        #self.timestamps = numpy.array(times, dtype=numpy.float64)
        #self.voltages = numpy.array(voltages, dtype=numpy.float64)

        self._data = numpy.column_stack([t, v])   #ho utilizzato la forma con t e v perché non mi serve tenerli 2 volte salvati, li ho già in data(privati)
        #print(self._data)
        #adesso abbiamo salvato i dati e vale con dei generici iterabili ma serve ricreare timestamps e voltages
        """ emulare l'esistenza di un atributo che non esiste, useremo due metodi con il nome degli attributi
            ma voglio che questo metodo venga chiamato come atributo,uso le properties, queste amulano finti attributi
        """
        #dobbiamo aggiungere il simbolo properties
        #Sono nuovi attributi perciò non devono essere indentati due volte
    @property                   #con la chiocciola sono decoratori
    def timestamps(self):
        return self._data[:,0]#seleziona : cioè tutte le righe e la colonna 1

    @property
    def voltages(self):
        return self._data[:,1]

    """Se definissi il @voltages.setter a quel punto vuol dire che p possibile cambiare quell'argomento
    @voltages.setter
    def voltages(self, new_values):
        self.data = numpy.column_stack([self.timestamps, newvalues])
    ma lo teniamo commentato per far sì che siano ??ridolli??"""

    """Testiamo che abbiano la stessa lunghezza con 'assert' """
    #lo commmentiamo perché questa verifica è già fatt da column_stack
    #assert len(self.times) == len(self.voltages)        #verifica per l'uguale lunghezza dei dati
    # non tutti gli iterabili ammettono la funzione len, in generale si
    #modifico len con la lnghezza della prima dimensione, delle righe
    """Per il momento si è fermato al controllo su len quindi tutto ok"""
    """- calling the len() function on a class instance must return the number of
         entries
    Serve un metodo len per assicurarci che la nostra classe sia iterabili e ammetta
    """
    #dobbimo definire len come built-in della nostra classe, non è uno shadowing, perché non sto definendo una nuova funzione len
    #ma sto applicando una definizione di len per la nostra classe, in modo che la funzione len vada a richiamare l'argomento len della classe
    def __len__(self, ):
        """return the number of entries (measurements)"""
        return(len(self._data))     #andava bene anche self.voltages,prima che definissi self._data perché abbiamo già verificato la medesima lunghezza
            #però potremmo fare qualcosa di più per verificare la stessa lunghezza dei due iterabili

            # è necessario che si chiami timestamps e non times come da verifica sotto perciò modifico il nome sopra
            # adesso gli assert con numpy.all sta verificando che i dati letti dalla mia classe siano uguali a v letti da main test


    """- the values should be accessible with the familiar square parenthesis syntax:
        the first index must refer to the entry, the second selects time (0) or
        voltage (1). Slicing must als work. il file deve accettare la forma con le [],
        ovvero una matrice 2d, con la prima colonna avrò times, con la seconda voltages.
        """
        #modifico il costruttore aggiungendo un pezzetto self._data co l'underscore vuol dire che è privato
        #adesso serve un metodo spciale ben preciso: __getitem__

    def __getitem__(self, index):       #l'indice può esere qualsiasi cosa copia slice
        """Random access"""         #si chiama random access per motivi storici, ma è inutile
        return self._data[index]
        #adesso dovrebbe funzionare l'assert che selezion degli elementi ben precisi tramite parentesi qudre

    """- the class must be iterable: at each iteration, a numpy array of two
        values (time and voltage) corresponding to an entry in the file must be
        returned
        """
    #ad ogni iterazione dobbiamo ottenere un array di coppie (tempo, tensione)
    #in questo caso il test ha bypassato il for, ma senza iter, questo perchè python è molto intelligente
    #python ha creato un iter utilizzando il __getitem__, ma non è molto affidabile e potrebbe essere rimossa in futuro
    """ Definiano il metodo __iter__ """
    def __iter__(self):
        return iter(self._data)     #abbiamo utilizzato la funzione built-in iter di numpy

if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will se in a future lesson."""
    # Load some data
    t, v = numpy.loadtxt('sandbox/sample_data_file.txt', unpack=True)
    #l'alternativa è scriverli a mano forse faremo una prova. loadtxt è più veloce
    # Thest the constructor
    v_data = VoltageData(t, v)     #v[:-1]per predere tutti i valori meno l'ultimo
    # Test len()
    assert len(v_data) == len(t)
    # Test the timestamps attribute
    assert numpy.all(v_data.voltages == v)
    # Test the voltages attribute
    assert numpy.all(v_data.timestamps == t)
    # Test square parenthesis
    assert v_data[3, 1] == v[3]
    assert v_data[-1, 0] == t[-1]
    # Test slicing
    assert numpy.all(v_data[1:5, 1] == v[1:5])
    # Test iteration
    for i, entry in enumerate(v_data):
        #eumerate looppa tenendo l'indice dell'iterazione corrente
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    # Test printing
    print(v_data)
    # Test plotting
    v_data.plot(fmt='ko', markersize=5, label='normal voltage')
    x_grid = numpy.linspace(min(t), max(t), 200)
    plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
    plt.legend()
    plt.show()
