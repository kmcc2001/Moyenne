list_notes = [5, 7, 10, 9, 16]  

indice = int(input("donnez l'indice à ne pas considérer : "))

if indice < 0 or indice >= len(list_notes):
    print("Indice invalide.")
else:
    somme = sum(list_notes) - list_notes[indice]
    moyenne = somme / (len(list_notes) - 1)
    print("La moyenne de ToTo est", moyenne)
