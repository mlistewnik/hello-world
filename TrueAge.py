wiek =  int(input("Ile masz lat?\n"))
if wiek == 18:
    print("Jesteś szczylem!")
elif wiek > 18 and wiek <=30:
    print("Twój wiek to %d" % wiek)
else:
    print("Masz 18 + VAT")