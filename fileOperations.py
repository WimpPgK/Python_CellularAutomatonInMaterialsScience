import numpy as np
import matrix

from PIL import Image
class fileOperations:

    def __init__(self):
        print("FileOperations Class")

    def saveTxt(self, path, matrix):

        file = open(path, "w")
        file.write(str(matrix.x) +" "+ str(matrix.y) + "\n")
        for i in range (matrix.x):
            for j in range(matrix.y):
                file.write(str(i) +" "+ str(j) + " " + str(matrix.grain[i][j]) + "\n")


        file.close()

    def saveBmp(self, path):
        print ("SaveToTxt")

    def loadTxt(self, path):

        dane = []  # deklarujemy pustą listę
        if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
            with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
                for linia in zawartosc:
                    linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                    linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                    linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
                    # dodajemy elementy do tupli a tuplę do listy
                    dane.append(tuple(linia.split(",")))
        else:
            print
            "Plik z danymi", plikcsv, "nie istnieje!"

        return tuple(dane)  # przekształcamy listę na tuplę i zwracamy ją

    def loadBmp(self, path):
        image = Image.open(path);
        size = width, height = image.size
        #obrazek = image.getData();
        #for i in range
        print(width)
        print(height)

        colourR = np.full((width, height), 0, dtype=int)
        colourG = np.full((width, height), 0, dtype=int)
        colourB = np.full((width, height), 0, dtype=int)

        for i in range (width):
            for j in range (height):
                coordinate = i , j
                colourR[i][j] = image.getpixel(coordinate)[0]
                colourG[i][j] = image.getpixel(coordinate)[1]
                colourB[i][j] = image.getpixel(coordinate)[2]

        #print(*image.getdata())
        del image



        #TO DO
        # teraz trzeba zrobic tak, zeby sprawdzic ile jest roznych kolorow,
        # potem stworzyc tablice w ktorym kazdy kolor bedzie mial id
        # i potem mozna juz robic tak jak normalnie

        for i in range (width):
            for j in range(height):
                print ("Ciastko z kremem")




        print("LoadBmp")

