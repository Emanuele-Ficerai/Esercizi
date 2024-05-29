#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
def check_parentheses(expression: str) -> bool:
    if () in str:
        return True
    else:
        return False