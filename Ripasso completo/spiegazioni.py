#come si dichiara una variabile:
nome_variabile: int = 10 #massimo 32 bit
#al posto degli spazi si usano gli underscore\ successivamente tipo di variabile che può essere int o str o float o bool  
# poi uguale e il valore che deve corrispondere al tipo di dato dichiarato; così da errore anche se è giusto in teoria:
nome_variabile: int = 10.0
#esempio con stringa:
nome_variabile: str = "lazio" #con il sigolo o con il doppio apice, è la stessa cosa
# esempio con float, numero con la virgola finito, massimo 32 bit
nome_variabile: float = 10.1
#esempio con bool, cioè o vero o falso
nome_variabile: bool = True
nome_variabile: bool = False
#una stessa variabile può cambiare il valore all'interno dello stesso codice, e solo in python possiamo cambiargli anche il tipo
# e passare ad esempio, da un intero ad una stringa

#cosa si può fare con queste variabili, molte operazioni
nome_variabile: int = 10
nome_variabile = nome_variabile + 5 # qui sto sommando, per farlo il tipo di dato deve essere lo stesso, 
#uguale
nome_variabile += 5                                   #se proprio dobbiamo sommare un intero con un float, 
                                    #trasformiamo il "10"(valore intero) in un float"10.0,
                                #in questo solo in python caso nome_variabile è sostituito dal varole assegnato in precedenza a questa variabile

# infine stampo e visualizzo il risulatato sul terminale
print(nome_variabile)

nome_variabile = nome_variabile % 3 #qui sto facendo il modulo di 20, che è il valore della variabile "nome_variabile"
                                    # il 3 nel 20 ci sta sei volte con il resto di due, ed eè proprio 2 che ho in output sul terminale
print(nome_variabile)

#possiamo utilizzare anche dei comparatori come:
nome_variabile == nome_variabile  # le due variabili messe a confronto sono identiche si fa con 2 uguali e NON con 1 uguale
                                  # con 1 uguale assegno un valore ad una variabile
print(nome_variabile)

nome_variabile != nome_variabile  #le due variabili messe a confronto sono diverse si indica con "!="
print(nome_variabile)

#con queste variabili si possono fare anche delle divisioni
lunghezza_lista: int = 7 #perchè la lungheza di una lista non è con la virgola
punto_di_mezzo = 7 / 2 #così il risultato sarà 3.5
punto_di_mezzo = 7 // 2 #con 2 barre facciamo una floor division, così avremo come risultato 3, 
                        #prende sempre il valore intero anche se avessimo avuto come risultato 3.9

#come valutare i booleani
var_1: bool = True
var_2: bool = False

#le operazioni che possiamo fare con i numeri booleani sono le seguenti:
print(var_1 and var_2)# and ci fa visualizzare sul terminale False, and è il prodotto, solo quando entrambi sono True ci da True
print(var_1 or var_2)#or ci fa visualizzare sul terminale True, or è la somma, infatti 1(associato al True) e 0 (al False) ci da True
                     #basta che un valore è true e ci darà true sul terminale
print(not var_1) # not ci fa visualizzare sul terminale il contrario, in questo caso darà False, perchè var_1 è True. 

#PRECEDENZA
# in python ci sono degli operatori di precedenza, ma se vogliamo stabilire noi le precedenze utilizziamo le parentesi "()"

#A CAPO
#\n, manda a capo sul terminale, è come premere il tasto: invio  

# I CONDIZIONALI
#iniziamo dagli if
if var_1 and var_2:  #parola chiave if(cioè il "se"), la condizione e poi i 2 pounti
    print(f"{var_1 and var_2}")           # e stampo identato dello all' "if" con il tast "tab", il terminale ci da False
# nella condizione se voglio dire che una cosa è uguale ad un'altra, lo faccio con 2 uguali attaccati "==", 
#con un solo uguale si dichiara una variabile "="
#sempre negli if abbiamo altre due condizioni: elif, che significa "altrimenti se", ed else, che significa "altrimenti e basta"
elif var_1 or var_2:
    pass
else:
    pass

#con il tasto "TAB", mi identa giustamente il posto in cui scrivere 

#FORMATTER
#a cosa serve il formatter? 
#si usa solitamente nel print, serve ad inserire le variabili all'interno delle stringhe, che sono molto flessibili
x: int = 100
print(f"a:{x}")#come vedo sul terminale, mi associa il valore (100) della variabile tra parentesi(x), e lo associa alla stringa "a"
            # la sintassi è: f(lettera chiave per il formatter), ""apro apici in cui scrivo, la stringa, i 2 punti, 
            #apro {} apro le graffe con i tasti: shift, Alt Gr, e tasto dove sono le parentesi quadre,
            #poi scrivo la variabile di cui voglio il valore, ed infine chiudo apici e parentesi

#COLLECTION, all'interno si deve utilizzare sempre lo stesso tipo di dato 

#LISTA
#    posizioni:0, 1, 2, 3/-1
lista: list = [1, 2, 3, 5] #faccio una lista= nome lista, : , tipo(list), =, apro parentesi QUADRE "[]", scrivo numeri interi all'interno
lista_stringa: list = ["ciao", "hello", "arigatò" ]# lista di stringhe, l'unica differenza è che le stringhe vanno tra apici
lista.pop(2) #con questo comando  tolgo il 3 dala mia lista, il 3 perchè è in posizione 2 
print(lista)

#SET
#anche il set, chiamato anche insieme, è una collection e non permette duplicati
insieme: set = {1, 1, 2, 3, 4, 7}
print(insieme) # infatti sul terminale mi stampa solo un uno
 
#DIZIONARI
# sono chiavi con corrispondenti valori, e come si fanno?
anagrafe: dict={
                "persona_1": "Flavio",   # la chiave è "persona_1" ed il valore è "Flavio"
                "persona_2": "Emanuele"
                }
#quindi se io voglio avere in output Emanuele faccio questo:
print(anagrafe["persona_2"])

#TUPLE
#dal punto di vista sintattico le tuple si indicano come le liste solo che le tuple si usano le parentesi tonde "()"
#le tuple non sono modificabili, non possiamo agiungiere, rimuovere, NON SI POSSONO MODIFICARE
spesa: tuple = ("milan", "inter")
print(spesa)

#I CICLI, vengono utilizzati per iterare su ogni elemento di una variabile, di una collection ecc...

#CICLO FOR
# il ciclo for è un costrutto in python che ci permette di andare a prendere i singoli valori
for numero in lista: # in questo caso prendiamo ogni valore della lista,li scorriamo ad uno ad uno
    print(f"x^2: {numero**2}")# stampa ogni valore nella lista elevato (con **) alla seconda, assocciato alla stringa x^2
# con il ciclo for si usano molte le funzioni: range, ci ritornano le posizioni, range(10) tornano i numeri da 0 a 9
# // //:len, ci ritorna la lunghezza, cioè quanti indici ci sono all'interno di una lista, gli indici sono separati da una virgola
#invece per prendere e stampare i singolo valori all'interno di una lista, si fa così:
print(lista[2])# sul terminale mi darà in output il 3 perchè è il numero alla posizione 2

#CICLO WHILE
# il ciclo while serve per ripetere più volte lo stesso comando. Itera su una certa porzione di codice finchè essa si verifica
i: int = 0
#while i < len(list): 
# fino ai 2 punti si fa così, ho commentato per vedere i risultati sul terminale while significa (mentre), poi c'è la condizione
    #print(list)

#PER ENTRMBI I CICLI:
#break si utilizza per interrompere il ciclo
#continue si utilizza per continuare il ciclo 

#FUNZIONI
#esistono 2 tipi di funzioni:
#quelle standard già memorizzate in python, per esempio: len()- sum()- range()- len()
# e funzioni che definiamo noi stessi:
def print_somma(param1, param2):# def, la parola chiave per definire una funzione, poi il nome della funzione che scegliamo noi 
                                 # riferito anche a quello che in effetti andrà a fare la funzione
                                 #apro tonde e all'interno inserisco i miei parametri, che possono essere:variabili,collection,classi
                                # due punti, invio e indento per bene il corpo della funzione
                                #visto che devo stampare, stampo il corpo dela funzione
                                # e a questo punto posso usare la mia funzione definita
                 somma = param1 +param2
                 print(somma) 
print_somma(10, 20)   #la mia funzione che ho definito esegue perettemente una somma, e visulizzo in output sul terminale: 30      

def add(a, b):
      result = a +b
      return result #qui la stessa cosa solo che invece di un print, ho un return