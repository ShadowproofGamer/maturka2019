import math
plik = open('liczby.txt')
dane_tekst = plik.read().split()
dane_liczbowe = []
for i in dane_tekst:
    dane_liczbowe.append(int(i))
#print(dane_liczbowe)
potegi_trojki = []
for j in range(11):
    potegi_trojki.append(3**j)
#print(potegi_trojki)
count_potegi = 0
for k in dane_liczbowe:
    if potegi_trojki.count(k)>0:
        count_potegi+=1
print(count_potegi)


factoriale = []
for ii in dane_tekst:
    liczba = []
    suma = 0
    for ij in range(len(ii)):
        liczba.append(int(ii[ij]))
    for ik in liczba:
        suma += math.factorial(ik)
    if int(ii) == suma:
        factoriale.append(suma)
print(factoriale)

kolejne = []
nwd = 0
for iii in range(len(dane_liczbowe)-1):
    temp_kolejne = []
    temp_nwd = math.gcd(dane_liczbowe[iii], dane_liczbowe[iii + 1])

    if temp_nwd > 1:
        temp_kolejne.append(dane_liczbowe[iii])
        temp_kolejne.append(dane_liczbowe[iii+1])
        for iij in range(len(dane_liczbowe)-iii):
            nwd_itr = math.gcd(temp_nwd, dane_liczbowe[iii + 1 + iij])
            if nwd_itr > 1:
                temp_nwd = nwd_itr
                temp_kolejne.append(dane_liczbowe[iii + 1 + iij])
            elif len(temp_kolejne)>len(kolejne):
                kolejne = temp_kolejne
                nwd = temp_nwd
                break
            else:
                break
print('liczba w tablicy: ', len(kolejne)-1)
print('pierwsza liczba: ', kolejne[0])
print('nwd: ', nwd)