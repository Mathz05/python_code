tabuada= int(input('Coloque um número para motar uma tabuada: '))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))