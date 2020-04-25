
import tkinter as tk
import matrix
import fileOperations
from tkinter import filedialog


import pygame
from timeit import default_timer as timer
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import multiprocessing


import time

class Gui:

    def guiInit(self):

        self.f01 = fileOperations.fileOperations()
        self.window = tk.Tk()


        self.window.state('zoomed')
        self.window.update()


        frame_inclusionBefore = LabelFrame(self.window, text="Inclusion before symulation", )
        frame_inclusionBefore.grid(row=4, column=0, rowspan=22, columnspan=1)
        frame_inclusionAfter = LabelFrame(self.window, text="Inclusion after symulation")
        frame_inclusionAfter.grid(row=4, column=1, rowspan=22, columnspan=1)



        xDimention = IntVar()
        yDimention = IntVar()
        amountOfGrains = IntVar()
        MCS = IntVar()
        numberGrainSelect = IntVar()
        inclusionBefore = IntVar()
        inclusionTypeBefore = StringVar()
        inclusionSizeBefore = IntVar()
        inclusionAfter = IntVar()
        inclusionTypeAfter = StringVar()
        inclusionSizeAfter = IntVar()


        xDimention.set(150)
        yDimention.set(150)
        amountOfGrains.set(100)
        MCS.set(4)
        numberGrainSelect.set(2)
        inclusionBefore.set(2)
        inclusionSizeBefore.set(10)
        inclusionAfter.set(2)
        inclusionSizeAfter.set(5)

        self.size_x_canvas = int(self.window.winfo_screenwidth()*0.68)
        self.size_y_canvas = int(self.window.winfo_screenheight()*0.87)



        # generate dwawing space
        self.canvas = tk.Canvas(self.window, width=self.size_x_canvas, height=self.size_y_canvas, bg="blue")
        self.canvas.grid(row=0, column=4, rowspan=110,
                         columnspan=4)  # plansza do rysowania bedzie zajmowac 100 wierszy i 4 kolumny

        ################# GUI of space generation ##########################

        label_xDimention = ttk.Label(self.window, text="X space dimention").grid(column=0, row=0, sticky=E)
        label_yDimention = ttk.Label(self.window, text="Y space dimention").grid(column=0, row=1, sticky=E)
        label_amountOfGrain = ttk.Label(self.window, text="Amount of grain").grid(column=0, row=2, sticky=E)
        label_neighbourhood = ttk.Label(self.window, text="Neighbourhood type").grid(column=0, row=3, sticky=E)
        label_inclusionBefore = ttk.Label(frame_inclusionBefore, text="     Amount  ").grid(column=0, row=0, sticky=W)
        label_inclusionTypeBefore = ttk.Label(frame_inclusionBefore, text="     Type  ").grid(column=0, row=1, sticky=W)
        label_inclusionSizeBefore = ttk.Label(frame_inclusionBefore, text="     Size  ").grid(column=0, row=2, sticky=W)
        label_inclusionAfter = ttk.Label(frame_inclusionAfter, text="    Amount     ").grid(column=0, row=0, sticky=W)
        label_inclusionTypeAfter = ttk.Label(frame_inclusionAfter, text="    Type").grid(column=0, row=1, sticky=W)
        label_inclusionSizeAfter = ttk.Label(frame_inclusionAfter, text="    Size").grid(column=0, row=2, sticky=W)

        entry_xDimention = ttk.Entry(self.window, textvariable=xDimention).grid(column=1, row=0)
        entry_yDimention = ttk.Entry(self.window, textvariable=yDimention).grid(column=1, row=1)
        entry_amountOfGrain = ttk.Entry(self.window, textvariable=amountOfGrains).grid(column=1, row=2)
        entry_inclusionBefore = ttk.Entry(frame_inclusionBefore, textvariable=inclusionBefore).grid(column=1, row=0, sticky=W)
        entry_inclusionSizeBefore = ttk.Entry(frame_inclusionBefore, textvariable=inclusionSizeBefore).grid(column=1, row=2, sticky=W)
        entry_inclusionAfter = ttk.Entry(frame_inclusionAfter, textvariable=inclusionAfter).grid(column=1, row=0,sticky=W)
        entry_inclusionSizeAfter = ttk.Entry(frame_inclusionAfter, textvariable=inclusionSizeAfter).grid(column=1, row=2, sticky=W)


        neighbourhoodType= StringVar()
        combobox_neighbourhoodType = ttk.Combobox(self.window, textvariable=neighbourhoodType, state='readonly')  # nie mozna wpisac wlasnej liczby zamiast tych do wybrania
        combobox_neighbourhoodType['values'] = ("VonNeumann", "Moore")
        combobox_neighbourhoodType.grid(column=1, row=3)
        combobox_neighbourhoodType.current(0)

        combobox_inclusionTypeBefore = ttk.Combobox(frame_inclusionBefore, textvariable=inclusionTypeBefore, state='readonly')  # nie mozna wpisac wlasnej liczby zamiast tych do wybrania
        combobox_inclusionTypeBefore['values'] = ("circual", "square")
        combobox_inclusionTypeBefore.grid(column=1, row=1)
        combobox_inclusionTypeBefore.current(0)

        combobox_inclusionTypeAfter = ttk.Combobox(frame_inclusionAfter, textvariable=inclusionTypeAfter, state='readonly')  # nie mozna wpisac wlasnej liczby zamiast tych do wybrania
        combobox_inclusionTypeAfter['values'] = ("circual", "square")
        combobox_inclusionTypeAfter.grid(column=1, row=1)
        combobox_inclusionTypeAfter.current(1)



        button_startCA = ttk.Button(self.window, text="Start CA",
                                   command=lambda: self.startCA(xDimention.get(), yDimention.get(), amountOfGrains.get(), neighbourhoodType.get(),
                                                                inclusionBefore.get(), inclusionTypeBefore.get(), inclusionSizeBefore.get(),
                                                                inclusionAfter.get(), inclusionTypeAfter.get(), inclusionSizeAfter.get()
                                                                )
                                   ).grid(column=0, columnspan=2, row=26)  #uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        button_findBorders = ttk.Button(self.window, text="Find borders",
                                    command=lambda: self.findBorders(xDimention.get(), yDimention.get())
                                    ).grid(column=0, columnspan=2, row=28)  # uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        ############# end of space generation ##############################




        #################            MENU             ##########################
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Save As txt", command=self.saveAsTxt)
        self.fileMenu.add_command(label="Save As bmp", command=self.saveAsBmp)
        self.fileMenu.add_command(label="Open...", command=self.load)
        self.fileMenu.add_separator()

        self.fileMenu.entryconfig(1, state="disabled")
        self.fileMenu.entryconfig(2, state="disabled")


        ########################################################################

        #self.f01.loadTxt("lplps")
        #self.f01.loadBmp("lplps, self.")
        #self.f01.loadBmp("C:/Users/poten/Desktop/malyObraz.bmp")

        self.window.mainloop()
    ##############################################################################################






    def startCA(self, x, y, n, neighbourhoodType, inclusionBefore, inclusionTypeBefore, inclusionSizeBefore,  inclusionAfter, inclusionTypeAfter, inclusionSizeAfter):

        self.m01 = matrix.Matrix(x, y, n)
        self.m01.addInclusion(inclusionBefore, inclusionTypeBefore, inclusionSizeBefore)
        self.m01.createGrains()
        self.m01.randomizeGrainPosition()
        self.showImage(x, y, "")
        self.fileMenu.entryconfig(1, state="active")
        self.fileMenu.entryconfig(2, state="active")
        self.fileMenu.entryconfig(3, state="disabled")

        while True:
            start = timer()
            flaga = self.m01.algorithmCA(neighbourhoodType)
            stop = timer()
            #print("Obliczenia:  %s" % (stop - start))
            start = timer()
            #self.showImage(x, y, "")
            stop = timer()
            #print("Wyswietlenie:  %s" %(stop-start))
            if flaga:
                break

        self.m01.addInclusion(inclusionAfter, inclusionTypeAfter, inclusionSizeAfter)
        self.showImage(x, y, "")





    #####################################################################

    def createRectangles(self, x, y):
        x_size = self.size_x_canvas / x
        y_size = self.size_y_canvas / y
        x_pointer = 0
        y_pointer = 0

        self.rectangleTab = [[None for y in range(y)] for x in range(x)]


        for i in range(0, self.size_x_canvas, int(x_size+1)):
            for j in range(0, self.size_y_canvas, int(y_size+1)):

                if self.m01.grain[x_pointer][y_pointer] == -2:
                    kolor = "black"
                else:
                    kolor = self.m01.getColour(self.m01.grain[x_pointer][y_pointer])

                self.rectangleTab[x_pointer][y_pointer] = self.canvas.create_rectangle(i, j, i + x_size+1, j + y_size+1, outline="", fill=kolor) #"
                y_pointer += 1
            x_pointer += 1
            y_pointer = 0


    #################################################################
    def showImage(self, x, y, flag):
        if flag == "":
            self.canvas.delete("all")
            self.createRectangles(x, y)
            self.canvas.update()

    def findBorders(self,x,y):
        self.m01.findBorders()
        print("Znaleziono granice")
        self.showImage(x, y, "")

    def saveAsTxt(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("txt file", "*.txt"), ("all files", "*.*")))
        print(filename)
        self.f01.saveTxt(filename + ".txt", self.m01)

    def saveAsBmp(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("bmp file", "*.bmp"), ("all files", "*.*")))
        print(filename)
        self.f01.saveBmp(filename + ".txt")

    def load(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("all files", "*.*"), ("bmp files", "*.bmp"), ("txt files", "*.txt")))
        print(filename)
        print("load")
        self.f01.loadTxt(filename)