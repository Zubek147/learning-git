#Zadanie 1
print('Zadanie 1')
print('')
lista_zakupów = {
    'Piekarnia' : ['Chleb', 'Bułki', 'Pączek'],
    'Warzywniak' : ['Marchew', 'Seler', 'Rukola']
}
print('Lista Zakupów')
for klucz, wartosc in lista_zakupów.items():
    print(f"Idę do {klucz} i kupuję tam następujące rzeczy: {wartosc}")
print(f"W sumie kupiłem {len(lista_zakupów['Piekarnia']) + len(lista_zakupów['Warzywniak'])} produktów.")
print('')

print("'Hiszpańska Inkwizycja'to najlepszy skecz")
