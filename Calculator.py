import tkinter as tk


class Calculator:

    def __init__(self):

        self.master = tk.Tk()
        self.master.configure(bg="powder blue")
        self.master.resizable(height=False, width=False)
        self.master.title("Hesap Makinesi")
        self.degisken = tk.StringVar()
        self.yazi_bolumu()
        self.tuslar()
        self.ekleyici = ""

    def yazi_bolumu(self):

        yazi = tk.Entry(master=self.master,
                        textvariable=self.degisken,
                        font=("arial", 20, "bold"),
                        bd=30, #Kenar genişliği
                        insertwidth=4, #Yanıp sönen yazı çubuğunun kalınlığı
                        justify=tk.RIGHT) #Sağdan yazmaya başlatma
        yazi.grid(columnspan=4) #Entrynin altını 4 sütuna böler ve yerleştirme yaptırır


    def tuslar(self):

        #----------------birinci sıra-----------------------

        tus7 = tk.Button(master=self.master,
                        text=7,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(7),
                        padx=16) #Padding 16 piksel widgetı doldurur x boyunca
        tus7.grid(row=1, column=0)

        tus8 = tk.Button(master=self.master,
                        text=8,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(8),
                        padx=16)
        tus8.grid(row=1, column=1)

        tus9 = tk.Button(master=self.master,
                        text=9,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(9),
                        padx=16)
        tus9.grid(row=1, column=2)

        tusarti = tk.Button(master=self.master,
                        text="+",
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma("+"),
                        padx=16)
        tusarti.grid(row=1, column=3)

        #----------------ikinci sıra-----------------------

        tus4 = tk.Button(master=self.master,
                        text=4,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(4),
                        padx=16)
        tus4.grid(row=2, column=0)

        tus5 = tk.Button(master=self.master,
                        text=5,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(5),
                        padx=16)
        tus5.grid(row=2, column=1)

        tus6 = tk.Button(master=self.master,
                        text=6,
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma(6),
                        padx=16)
        tus6.grid(row=2, column=2)

        tuseksi = tk.Button(master=self.master,
                        text="-",
                        font=("arial", 20, "bold"),
                        bd=8,
                        bg="powder blue",
                        command=lambda: self.yazdirma("-"),
                        padx=16)
        tuseksi.grid(row=2, column=3)

        # ----------------üçüncü sıra-----------------------

        tus1 = tk.Button(master=self.master,
                         text=1,
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma(1),
                         padx=16)
        tus1.grid(row=3, column=0)

        tus2 = tk.Button(master=self.master,
                         text=2,
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma(2),
                         padx=16)
        tus2.grid(row=3, column=1)

        tus3 = tk.Button(master=self.master,
                         text=3,
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma(3),
                         padx=16)
        tus3.grid(row=3, column=2)

        tuscarpi = tk.Button(master=self.master,
                            text="x",
                            font=("arial", 20, "bold"),
                            bd=8,
                            bg="powder blue",
                             command=lambda: self.yazdirma("*"),
                            padx=16)
        tuscarpi.grid(row=3, column=3)

        # ----------------Dördüncü sıra-----------------------

        tusparantez1 = tk.Button(master=self.master,
                         text="(",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma("("),
                         padx=16)
        tusparantez1.grid(row=4, column=0)

        tus0 = tk.Button(master=self.master,
                         text=0,
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma(0),
                         padx=16)
        tus0.grid(row=4, column=1)

        tusparantez2 = tk.Button(master=self.master,
                         text=")",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma(")"),
                         padx=16)
        tusparantez2.grid(row=4, column=2)


        tusbolme = tk.Button(master=self.master,
                            text="/",
                            font=("arial", 20, "bold"),
                            bd=8,
                            bg="powder blue",
                            command=lambda: self.yazdirma("/"),
                            padx=16)
        tusbolme.grid(row=4, column=3)


        # ----------------Beşinci sıra-----------------------

        tussilme = tk.Button(master=self.master,
                         text="C",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="red",
                         command=lambda: self.toptan_silme(),
                         padx=16)
        tussilme.grid(row=5, column=0)

        tusteksilme = tk.Button(master=self.master,
                         text="<",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.tek_tek_silme(),
                         padx=16)
        tusteksilme.grid(row=5, column=1)

        tusnokta = tk.Button(master=self.master,
                         text=".",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="powder blue",
                         command=lambda: self.yazdirma("."),
                         padx=16)
        tusnokta.grid(row=5, column=2)


        tusesittir = tk.Button(master=self.master,
                         text="=",
                         font=("arial", 20, "bold"),
                         bd=8,
                         bg="orange",
                         command=lambda: self.hesapla(),
                         padx=16)
        tusesittir.grid(row=5, column=3)



    def yazdirma(self, parametre):

        self.ekleyici += str(parametre)
        self.degisken.set(self.ekleyici)

    def toptan_silme(self):

        self.ekleyici = ""
        self.degisken.set(self.ekleyici)

    def tek_tek_silme(self):
        uzunluk = len(self.ekleyici)
        self.ekleyici = self.ekleyici[0:uzunluk-1]
        self.degisken.set(self.ekleyici)

    def hesap_makinesini_calistir(self):
        self.master.mainloop()

    def hesapla(self):
        try:
            sonuc = eval(self.ekleyici)

        except:
            self.ekleyici = ""
            self.degisken.set("error")

        else:
            self.ekleyici = ""
            self.degisken.set(sonuc)



