import sys
import os

if len(sys.argv) < 2:
    print("Nem adtál meg file nevet!")
    print(f"Helyesesn py {sys.argv[0]} filenév")
elif not os.path.exists(sys.argv[1]):
    print("Nem létezik a file!")
else:
    filenev = sys.argv[1]
    print (filenev)

    file = open(filenev)

    sorok = file.readlines()
    file.close

    for i in range(len(sorok)):
        print(sorok[i].strip())