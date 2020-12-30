
import matplotlib
from matplotlib import rc
from sympy.abc import x
from sympy import *
from fractions import Fraction
from sympy.polys.polyfuncs import interpolate
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from tkinter.messagebox import showinfo
import Integration
from functools import partial
matplotlib.use('TkAgg')


init_printing()

# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n

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
            plt.plot(x_rect, y_rect, "m")
        yflist_fine = [f(x) for x in xlist_fine]
        plt.plot(xlist_fine, yflist_fine)  # plot de f(x)
        plt.plot(xl, yl, "cs")  # point support
        plt.ylabel(' f ( x ) ')
        plt.title(' Methode des Trapèzes')

        showinfo("Integration value", 'I_{} ={:0.8f}'.format(
            resolution, self.integrate(f)))


class mclass:

    def __init__(self, window):
        self.mylist = []
        self.mylist1 = []
        self.supp = []

        self.window = window

        self.button3 = Button(window, text="Finish & Plot", width=15, font=("Arial", 13),
                              command=self.plot, borderwidth=4, bg="SteelBlue1", fg='gray1')
        self.button3.pack(side='top', pady=10)

        self.button4 = Button(window, text='Clear all', width=15, font=("Arial", 13),
                              command=self.Clear, borderwidth=4, bg="SteelBlue1", fg='gray1')

        self.button4.pack(side='top', pady=10)

        self.button5 = Button(
            window, text='Integrate this function', command=self.intergrat, borderwidth=4, bg="SteelBlue1", fg='gray1', width=20, font=("Arial", 13),)
        self.button5.pack(side='top', pady=10)
        self.button5.pack()
        self.var1 = StringVar()
        self.var1.set("X Values:")
        label1 = Label(window, textvariable=self.var1,
                       height=2, font=("Arial", 10))
        label1.pack()

        ID1 = StringVar()
        self.box1 = Entry(window, bd=4, width=80, textvariable=ID1)
        self.box1.pack()

        var2 = StringVar()
        var2.set("Y Values:")
        label2 = Label(window, textvariable=var2, height=2, font=("Arial", 10))
        label2.pack()

        ID2 = StringVar()
        self.box2 = Entry(window, bd=4, width=80, textvariable=ID2)
        self.box2.pack()
        var3 = StringVar()
        self.label3 = Entry(window, width=200,
                            textvariable=var3, font=("Courier", 14))

        def onclick(event):

            self.a.cla()
            self.a.set_xlim([-10, 10])
            self.a.set_ylim([-10, 10])
            self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
            self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
            self.a.grid(True)

            if self.verif(event):
                plt.plot(round(event.xdata), round(event.ydata), 'bo')

                self.mylist.append(str(round(event.xdata)))
                self.mylist1.append(str(round(event.ydata)))
                self.supp.append(
                    (int(round(event.xdata)), int(round(event.ydata))))
            self.a.scatter([u for u, v in iter(self.supp)], [
                v for u, v in iter(self.supp)], color='red')
            f = lambdify((x,), interpolate(self.supp, x))
            T = np.linspace(-10, 10, 1000)
            ft = [f(i) for i in T]
            plt.plot(T, ft, 'g')
            plt.title(r"$P_n(x)="+latex(interpolate(self.supp, x)) +
                      "$", fontsize=12, color='red')
            ID1.set(self.mylist)
            ID2.set(self.mylist1)
            ch = "{}".format(interpolate(self.supp, x))

            var3.set(ch)
            self.label3.pack()
            self.fig.canvas.draw()

        self.fig = plt.figure(figsize=(7, 7))
        self.a = self.fig.add_subplot(111)
        self.a.set_xlim([-10, 10])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.cid = self.fig.canvas.mpl_connect('button_press_event', onclick)
        self.canvas.get_tk_widget().pack()

    def read_inputs(self):
        x_input = self.box1.get()

        y_input = self.box2.get()
        self.mylist = x_input.split(' ')
        self.mylist1 = y_input.split(' ')

        def convert_to_float_list(x_in):
            x_list = x_in.split(' ')

            x_floats = [float(x) for x in x_list]
            return x_floats

        x_array = (convert_to_float_list(x_input))
        y_array = (convert_to_float_list(y_input))

        return x_array, y_array

    def plot(self):

        self.a.cla()
        self.a.set_xlim([-10, 10])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)

        W, V = self.read_inputs()

        W = [w for w in W]
        V = [v for v in V]
        self.supp = [(0, 0) for i in W]
        i = 0
        while i < len(W):
            print(self.supp)
            self.supp[i] = (int(round(W[i])), int(round(V[i])))

            i += 1

        plt.plot(W[-1], V[-1], 'bo')
        self.a.scatter([u for u, v in iter(self.supp)], [
                       v for u, v in iter(self.supp)], color='red')
        self.supp.sort(key=lambda x: x[0])
        print(self.supp)
        f = lambdify((x,), interpolate(self.supp, x))
        T = np.linspace(-10, 10, 1000)
        ft = [f(i) for i in T]
        plt.plot(T, ft, 'g')

        plt.title(r"$P_n(x)="+latex(interpolate(self.supp, x)) +
                  "$", fontsize=12, color='red')

        self.a.set_ylabel("Y", fontsize=14)
        self.a.set_xlabel("X", fontsize=14)
        ch = "{}".format(interpolate(self.supp, x))

        self.label3.delete(0, END)
        self.label3.insert(0, ch)
        self.label3.pack()
        self.fig.canvas.draw()

    def Clear(self):
        self.fig.clf()

        self.a = self.fig.add_subplot(111)
        self.a.cla()
        self.a.set_xlim([-10, 10])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)
        self.fig.canvas.draw()
        self.mylist = []
        self.mylist1 = []
        self.supp = []
        self.box1.delete(0, END)
        self.box2.delete(0, END)

        self.label3.delete(0, END)

    def verif(self, event):
        for i in range(len(self.mylist)):
            if self.mylist[i] == str(round(event.xdata)):
                return false
        return True

    def intergrat(self):
        def func(x): return eval(self.label3.get())

        R = Trapezoidal(-5, 5, 10, func)
        self.a.cla()
        self.a.set_xlim([-5, 5])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-5, 5, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)
        R.Graph(func)
        self.fig.canvas.draw()


def inter():
    global window

    window = Toplevel(main)

    window.configure(background='white')
    window.geometry("1900x900")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    start = mclass(window)

    window.mainloop()


main = Tk()
main.geometry('768x460')
c = Canvas(main, bg="blue", height=460, width=768)
main.config(background='light blue')

photo = PhotoImage(file='bgimage.png')
background_label = Label(main, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


Label1 = Label(main, text='Analyse Numérique', bg='light blue',
               fg='midnight blue', font=("Arial", 25))
Label1.pack(pady=50)


button1 = Button(main, text="Interpolation Polynomiale", width=30, font=(
    "Arial", 15), bg='RoyalBlue4', fg='white', command=inter)
button2 = Button(main, text="Intégration Numérique", width=30,
                 font=("Arial", 15), bg='RoyalBlue4', fg='white', command=partial(Integration.integ, main))
button1.pack(pady=15)
button2.pack(pady=15)
Bouton1 = Button(main, text='Quitter', command=main.destroy,
                 width=15, font=("Arial", 15), bg='gray6', fg='white')
Bouton1.pack(pady=15)

c.pack()
main.mainloop()
