import random
import time
from sys import exit


#Powitanie
print('''
----------------------------------------------------------------
Witamy w grze logicznej "12 KULEK"!

    Masz do dyspozycji 12 identycznie wyglądających kulek (k1,k2
, ... ,k12) oraz wagę szalkową. Twoim zadaniem jest za pomocą tr
zech ważeń wskazać kulkę, która jako jedyna różni się wagą od in
nych kulek oraz napisać czy jest ona lżejsza czy cięższa od pozo
stałych.

Powodzenia!
----------------------------------------------------------------
''')
time.sleep(4)



#ETAP 1 - Losowanie kulki i zmiana jej wagi
kulki = {'k1': 1,'k2': 1,'k3':1,'k4':1,'k5':1,'k6':1,'k7':1,'k8':1,'k9':1,'k10':1,'k11':1,'k12':1}
#tabKom = [['a','b'],['c','d']]
#print(tabKom[1],tabKom[1][1])
#exit()
losKulka = random.choice(['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12'])
losWaga = random.choice(['lżejsza','cięższa'])
#print('Wylosowano: '+losWaga+' '+losKulka)

if losWaga == 'lżejsza':
    kulki.update({losKulka:0.5})
else:
    kulki.update({losKulka:1.5})





#ETAP 2 - Pierwsze ważenie wskazanych kulek
szL = {}
szP = {}

print('''
Pierwsze ważenie.

    Musisz wskazać kulki które zostaną umieszczone na lewej, a p
óźniej na prawej szalce wagi. Wynik ważenie zostanie przedstawio
ny "graficznie" za pomoca znaków ">", "<" oraz "=". Kulki podaje
sz za pomocą cyfr oddzielonych spacjami.
''')
#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszL = input("Które kulki umieścić na lewej szalce wagi? ").split()
    TXTszL = ''
    OUTszL = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszL:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szL:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        else:
            szL['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszL = TXTszL + 'k' + str(i) + ' '
            OUTszL += kulki.get('k'+str(i))
    print('\nSzalka lewa zawiera:',TXTszL[:-1])
    ZAPszL = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszL == 't' or ZAPszL == 'tak':
        break
    elif ZAPszL == 'n' or ZAPszL == 'nie':
        szL.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szL.clear()
        continue

#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszP = input("\nKtóre kulki umieścić na prawej szalce wagi? ").split()
    TXTszP = ''
    OUTszP = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszP:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szP:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        elif 'k'+str(i) in szL:
            print('kulka nr.'+i+' została już raz ustawiona na lewej szalce\n')    
        else:
            szP['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszP = TXTszP + 'k' + str(i) + ' '
            OUTszP += kulki.get('k'+str(i))
    print('\nSzalka prawa zawiera:',TXTszP[:-1])
    ZAPszP = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszP == 't' or ZAPszP == 'tak':
        break
    elif ZAPszP == 'n' or ZAPszP == 'nie':
        szP.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szP.clear()
        continue

#Graficzne porównanie wagi lewej i prawej szalki
print('\nWynik pierwszego ważenie to:')
if OUTszL < OUTszP:
    print('szalka lewa ['+TXTszL[:-1]+'] < szalka prawa ['+TXTszP[:-1]+']')
elif OUTszL > OUTszP:
    print('szalka lewa ['+TXTszL[:-1]+'] > szalka prawa ['+TXTszP[:-1]+']')
else:
    print('szalka lewa ['+TXTszL[:-1]+'] = szalka prawa ['+TXTszP[:-1]+']')
print('----------------------------------------------------------------\n')




#ETAP 3 - Drugie ważenie wskazanych kulek
szL2 = {}
szP2 = {}

print('''
Drugie ważenie.
''')
#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszL2 = input("Które kulki umieścić na lewej szalce wagi? ").split()
    TXTszL2 = ''
    OUTszL2 = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszL2:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szL2:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        else:
            szL2['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszL2 = TXTszL2 + 'k' + str(i) + ' '
            OUTszL2 += kulki.get('k'+str(i))
    print('\nSzalka lewa zawiera:',TXTszL2[:-1])
    ZAPszL2 = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszL2 == 't' or ZAPszL2 == 'tak':
        break
    elif ZAPszL2 == 'n' or ZAPszL2 == 'nie':
        szL2.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szL2.clear()
        continue

#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszP2 = input("\nKtóre kulki umieścić na prawej szalce wagi? ").split()
    TXTszP2 = ''
    OUTszP2 = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszP2:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szP2:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        elif 'k'+str(i) in szL2:
            print('kulka nr.'+i+' została już raz ustawiona na lewej szalce\n')    
        else:
            szP2['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszP2 = TXTszP2 + 'k' + str(i) + ' '
            OUTszP2 += kulki.get('k'+str(i))
    print('\nSzalka prawa zawiera:',TXTszP2[:-1])
    ZAPszP2 = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszP2 == 't' or ZAPszP2 == 'tak':
        break
    elif ZAPszP2 == 'n' or ZAPszP2 == 'nie':
        szP2.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szP2.clear()
        continue

#Graficzne porównanie wagi lewej i prawej szalki
print('\nWynik drugiego ważenie to:')
if OUTszL2 < OUTszP2:
    print('szalka lewa ['+TXTszL2[:-1]+'] < szalka prawa ['+TXTszP2[:-1]+']')
elif OUTszL2 > OUTszP2:
    print('szalka lewa ['+TXTszL2[:-1]+'] > szalka prawa ['+TXTszP2[:-1]+']')
else:
    print('szalka lewa ['+TXTszL2[:-1]+'] = szalka prawa ['+TXTszP2[:-1]+']')
print('----------------------------------------------------------------\n')





#ETAP 4 - Trzecie ważenie wskazanych kulek
szL3 = {}
szP3 = {}

print('''
Trzecie ważenie.
''')
#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszL3 = input("Które kulki umieścić na lewej szalce wagi? ").split()
    TXTszL3 = ''
    OUTszL3 = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszL3:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szL3:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        else:
            szL3['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszL3 = TXTszL3 + 'k' + str(i) + ' '
            OUTszL3 += kulki.get('k'+str(i))
    print('\nSzalka lewa zawiera:',TXTszL3[:-1])
    ZAPszL3 = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszL3 == 't' or ZAPszL3 == 'tak':
        break
    elif ZAPszL3 == 'n' or ZAPszL3 == 'nie':
        szL3.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szL3.clear()
        continue

#pętla główna z zapytaniem końcowym czy zostawiamy wybór czy go zmieniamy
while True:
    INszP3 = input("\nKtóre kulki umieścić na prawej szalce wagi? ").split()
    TXTszP3 = ''
    OUTszP3 = 0
#pętla ze sprawdzaniem kul (istnieje? już wskazana?) i zsumowaniem wagi
    for i in INszP3:
        if 'k'+str(i) not in kulki:
            print('kulka nr.'+i+' nie istnieje i nie zostanie ustawiona na szalce\n')
        elif 'k'+str(i) in szP3:
            print('kulka nr.'+i+' została już raz ustawiona na szalce\n')
        elif 'k'+str(i) in szL3:
            print('kulka nr.'+i+' została już raz ustawiona na lewej szalce\n')    
        else:
            szP3['k'+str(i)] = kulki.get('k'+str(i),0)
            TXTszP3 = TXTszP3 + 'k' + str(i) + ' '
            OUTszP3 += kulki.get('k'+str(i))
    print('\nSzalka prawa zawiera:',TXTszP3[:-1])
    ZAPszP3 = input('Zatwierdzasz ten wybór? (t)ak/(n)ie ')
    if ZAPszP3 == 't' or ZAPszP3 == 'tak':
        break
    elif ZAPszP3 == 'n' or ZAPszP3 == 'nie':
        szP3.clear()
        continue
    else:
        print('Złe polecenie. Umieść kulki na szalce jeszcze raz...')
        szP3.clear()
        continue

#Graficzne porównanie wagi lewej i prawej szalki
print('\nWynik trzeciego ważenie to:')
if OUTszL3 < OUTszP3:
    print('szalka lewa ['+TXTszL3[:-1]+'] < szalka prawa ['+TXTszP3[:-1]+']')
elif OUTszL3 > OUTszP3:
    print('szalka lewa ['+TXTszL3[:-1]+'] > szalka prawa ['+TXTszP3[:-1]+']')
else:
    print('szalka lewa ['+TXTszL3[:-1]+'] = szalka prawa ['+TXTszP3[:-1]+']')
print('----------------------------------------------------------------\n')





#ETAP 5 - Wskazanie prawidłowej kulki i określenie jej wagi względem pozostałych
print('''
To już końcówka zabawy.
Musisz wskazać prawidłową kulę oraz okreslić czy jest ona (l)żej
sza czy (c)ięższa od pozostałych. Kulkę podajesz za pomocą liczb
y, a różnicę wagi wprowadzasz po spacji, np. "1 c" - kula k1 jes
t cięższa od pozostałych
''')
while True:
    wynik = input("Wskaż kulkę: ").split()
    #print(wynik)

    wynKulka = 'k'+str(wynik[0])

    if wynik[0] not in ['1','2','3','4','5','6','7','8','9','10','11','12'] or wynik[1] not in ['l','c']:
        print('\nŹle wprowadzona odpowiedź...\n')
        time.sleep(2)
        continue
    else:
        if wynik[1] == 'l':
            wynWaga = 0.5
        else:
            wynWaga = 1.5

        if kulki.get(wynKulka) == wynWaga:
            print('\nBrawo, WYGRAŁEŚ!')
            break
        else:
            print('\nPrzykro mi, ale prawidłowa odpowiedź to: kulka nr '+losKulka+' i jest ona \n'+losWaga+' od pozostałych kulek.')
            break

exit('\n----------------------------------------------------------------\nDziękuję za udział w grze "12 Kulek"\n(c)PawliK 2022\n----------------------------------------------------------------\n')