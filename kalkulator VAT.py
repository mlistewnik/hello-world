cena_bez_vat = float (input ("Podaj cenę bez VAT: "))
stawka_vat = float (input ("Podaj stawkę VAT: "))
cena_koncowa = cena_bez_vat + cena_bez_vat*(stawka_vat/100)
print ("Do zapłaty &f" % cena_koncowa)