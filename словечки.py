a = []
while True:
    b = input("Ваши словечки? ")
    if b == "стоп":
        break
    a.append(b)
for b in a:
    print(b)