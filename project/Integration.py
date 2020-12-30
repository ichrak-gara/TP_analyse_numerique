
from numpy import sin, cos, exp, log, sqrt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
matplotlib.use('TkAgg')


class RectangleG (object):
    def __init__(self, a, b, n, f, aa):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x
        y = [f(xx) for xx in x]
        h = float(x[1] - x[0])
        s = sum(y[0: -1])
        return h * s

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            # abscisses des sommets
            x_rect = [xl[i], xl[i], xl[i + 1], xl[i+1], xl[i]]
            y_rect = [0, yl[i], yl[i], 0, 0]  # ordonnees des sommets
            self.aa.plot(x_rect, y_rect, 'r')
        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine)
        self.aa.plot(xl, yl, "bo")
        showinfo("Integration value", '____I_{} ={:0.8f}____'.format(
            self.n, self.integrate(f)))


class Simpson(object):
    def __init__(self, a, b, n, f, aa):  # initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)  # les pts supports
        self.f = f
        self.n = n  # nombre de subdivision
        self.c = aa
    # calculer la somme ((b-a)/6*n)*[f(a)+2*sum(xi)+4*sum(mi)+f(b)]

    def integrate(self, f):
        x = self.x  # les points supports xi #x(0)=a-->x(n)=b
        y = [f(xx) for xx in x]  # yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])  # pas h=(b-a)/2*n
        n = len(x) - 1  # nombre subdivision
        if n % 2 == 1:  # si le reste de la division =1 impaire
            n -= 1  # ☺nombre de sub ywali paire
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        # y[1:-1:2] min impaire loulla m0 lil 9bal likhrania 5ater 3anna deja y(n) par pas de 2== mi
        # calculer la somme
        # T(-1] dernier valeur dans le tableau)
        return h * s / 3.0

    def Graph(self, f, resolution=1001):  # 1000 points 1001 résolution juste pour dessiner f
        xl = self.x  # pt support
        yl = [f(x) for x in xl]  # yi
        xlist_fine = np.linspace(self.a, self.b, resolution)
        # pour le graph de la fonction f #intervalle ab subdiviser en 1000 poitns
        for i in range(self.n):  # range intervalle 0 à n
            xx = np.linspace(xl[i], xl[i+1], resolution)
            # pour chaque subdivisuion  on doit dessiner polynome dnc on doit aussi le subdiviser
            m = (xl[i]+xl[i+1])/2  # pt milieu
            aa = xl[i]  # borne gauche
            bb = xl[i+1]  # borne droite
            l0 = (xx-m)/(aa-m)*(xx-bb)/(aa-bb)
            l1 = (xx-aa)/(m-aa)*(xx-bb)/(m-bb)
            l2 = (xx-aa)/(bb-aa)*(xx-m)/(bb-m)
            P = f(aa)*l0 + f(m)*l1 + f(bb)*l2  # fonction dde polynome
            self.c.plot(xx, P, 'b')  # dessiner polynome d'interpolation
            self.c.plot(m, f(m), "r*")
        yflist_fine = [f(x) for x in xlist_fine]  # fontion f
        self.c.plot(xlist_fine, yflist_fine, 'g')
        self.c.plot(xl, yl, 'bo')  # point support en bleu rond
        showinfo("Integration value", '____I_{} ={:0.8f}____'.format(
            self.n, self.integrate(f)))


class Milieu(object):  # class rectange
    def __init__(self, a, b, n, f, aa):  # initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x  # contiens les xi
        h = float(x[1] - x[0])
        s = 0
        for i in range(self.n):
            s = s+f((x[i]+x[i+1])*0.5)
        return h*s

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            m = (xl[i]+xl[i+1])/2
            # abscisses des sommets
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]]
            y_rect = [0, f(m), f(m), 0, 0]  # ordonnees des sommets
            self.aa.plot(x_rect, y_rect, "r")
            self.aa.plot(m, f(m), "b*")

        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine, 'g')
        showinfo("Integration value", '____I_{} ={:0.8f}____'.format(
            self.n, self.integrate(f)))


class Trapezoidal(object):
    def __init__(self, a, b, n, f, aa):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x
        y = [f(xx) for xx in x]
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            # abscisses des sommets
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]]
            y_rect = [0, yl[i], yl[i+1], 0, 0]  # ordonnees des sommets
            self.aa.plot(x_rect, y_rect, "m")
        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine)  # plot de f(x)
        self.aa.plot(xl, yl, "cs")  # point support

        showinfo("Integration value", '____I_{} ={:0.8f}____'.format(
            self.n, self.integrate(f)))


class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window, highlightbackground="black",
                         highlightthickness=2, width=100, height=100, bd=5, bg='white')
        self.fr2 = Frame(window, highlightbackground="darkgray",
                         highlightthickness=2, width=100, height=100, bd=5)
        self.func_txt = StringVar()
        self.func_txt.set("La fonction f:")
        self.label_func = Label(
            self.fr1, textvariable=self.func_txt, justify=RIGHT, height=4, bg='white')
        self.label_func.grid(row=1, column=0)
        self.a_txt = StringVar()
        self.a_txt.set("a:")
        self.label_a = Label(self.fr1, textvariable=self.a_txt, font=("Arial", 10),
                             justify=RIGHT, anchor="w", height=4, bg='white')
        self.label_a.grid(sticky=E, row=2, column=0)
        self.boxa = Entry(self.fr1, width=10, borderwidth=3, bg="powder blue")
        self.boxa.grid(sticky=W, row=2, column=1)
        self.boxa.insert(0, '1')

        self.b_txt = StringVar()
        self.b_txt.set("b:")
        self.label_b = Label(self.fr1, textvariable=self.b_txt, font=("Arial", 10),
                             justify=RIGHT, anchor="w", height=4, bg='white')
        self.label_b.grid(sticky=E, row=3, column=0)
        self.boxb = Entry(self.fr1, width=10, borderwidth=3, bg="powder blue")
        self.boxb.grid(sticky=W, row=3, column=1)

        self.box = Entry(self.fr1, borderwidth=3, bg="powder blue")
        self.box.grid(row=1, column=1)
        self.boxn = Entry(self.fr1, borderwidth=3,
                          bg="powder blue", textvariable="3")
        self.boxn.grid(sticky=W, row=4, column=1)
        self.boxn.delete(0, END)
        self.boxn.insert(0, "3")
        self.n_txt = StringVar()
        self.n_txt.set("N:")
        self.label_n = Label(self.fr1, textvariable=self.n_txt,
                             justify=RIGHT, anchor="w", height=4, bg='white')
        self.label_n.grid(sticky=E, row=4, column=0)
        self.c_txt = StringVar()
        self.c_txt.set("Integration methode")
        self.label_in = Label(
            self.fr1, textvariable=self.c_txt, justify=RIGHT, anchor='w', height=4, bg='white')
        self.label_in.grid(sticky=E, row=5, column=0)
        self.combo = Combobox(self.fr1)
        self.combo['values'] = (' Simpson',
                                ' Trapèze',
                                ' rectangle',
                                ' Point Milieu')
        self.combo.grid(sticky=W, row=5, column=1)
        self.combo.current(0)
        self.button = Button(self.fr1, width=35, text="plot & integrate function",
                             bg='powder blue', command=self.plot)
        self.button.grid(row=6, column=0, columnspan=3)
        self.fr1.grid(row=1, column=0, padx=10, pady=10, sticky="ns")
        self.fr2.grid(row=1, column=1, padx=10, pady=10)

        self.fig = Figure(figsize=(6, 6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.boxb.insert(0, "3")
        self.box.insert(0, 'cos(x)')

    def plot(self):
        def f(x): return eval(self.box.get())

        x = np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        pp = f(x)
        self.a.cla()
        self.a.set_ylim([-3, 10])
        self.a.xaxis.set_ticks(
            np.arange(-3, 8, 1))
        self.a.yaxis.set_ticks(
            np.arange(-3, 8, 1))
        self.a.set_title("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        self.a.plot(x, f(x), color='blue')
        dic = {' rectangle': RectangleG, ' Trapèze': Trapezoidal,
               ' Point Milieu': Milieu, ' Simpson': Simpson}
        s = self.combo.get()
        R = dic[s](float(self.boxa.get()), float(
            self.boxb.get()), int(self.boxn.get()), f, self.a)
        R.Graph(f)
        self.fig.canvas.draw()


def integ(main):
    global window
    window = Toplevel(main)

    start = mclass(window)

    window.mainloop()
