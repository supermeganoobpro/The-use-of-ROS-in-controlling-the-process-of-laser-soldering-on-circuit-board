#!/usr/bin/env python
 
# version 1.2 - improved kinematics / to do: implemente speed dependent moves
import rospy
from std_msgs.msg import String
from tkinter import *
import math
from tkinter.filedialog import askopenfilename
# variaveis
n = 0
a = 0
filename = ''
data = ''

valores = 0
flag = False
flag1 = False
flag2 = False
flag3 = False
flag5 = False
#variaveis antigas
z = 0.1
x = 0.1
y = 0.1
f = 1
x0 = 1
y0 = 60
z0 = 100
Dx = 0
Dy = 0
Dz = 0
kx = 0
ky = 0
kz = 0
kv = 0
mi0 = 0
phi0 = 0
teta0 = 0
mi = 0
phi = 0
teta = 0
flagx = 0
flagy = 0
flagz = 0
iF = 0
fx = 0
fy = 0
fz = 0
#variaveis novas
lx = 0
q = 180
c = 269
time = 5

master = Tk()
master.title = "Philon Tech"
master.geometry("680x600")

Label(master, text="x° position:", bd=1, relief="solid").grid(row=5)  # relief me da a borda e bd a largura da borda
Label(master, text="y° position:", bd=1, relief="solid").grid(row=6)
Label(master, text="z° position:", bd=1, relief="solid").grid(row=7)



def rostalk(income):   #funcao do ros que publica a string que controla os motores
    pub = rospy.Publisher('arduino', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 10hz
    rospy.loginfo(str(income))
    pub.publish(str(income))
    rate.sleep()
	
def ajustefunxp():   #resolver a questão da cinematica nova
    global mi
    global mi0
    global phi0
    global teta0
    global x0
    global phi
    global teta
    x0 = 10 + x0

#new
    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0


    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 


def ajustefunxm():
    global mi0
    global phi0
    global teta0
    global x0

    x0 = x0 - 10

    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0

    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 
     

def ajustefunyp():
    global mi0
    global phi0
    global teta0
    global y0

    y0 = 10 + y0
    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0

    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 
     

def ajustefunym():
    global mi0
    global phi0
    global teta0
    global y0

    y0 = y0 - 10

    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0

    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 
     

def ajustefunzp():
    global mi0
    global phi0
    global teta0
    global z0

    z0 = 10 + z0
    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0

    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 
     

def ajustefunzm():
    global mi0
    global phi0
    global teta0
    global z0

    z0 = z0 - 10

    if x0 == 0:
        mi = 90
    else:
        mi = float(math.atan(x0 / y0))


    lx = y0 / (1 / (math.degrees(math.sin(mi))))
    l = lx + 15  # buffer de distancia da base
    a = math.sqrt((z0 ** 2) + (l ** 2))
    alfa = math.degrees(math.atan(z / l))
    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

    teta = alfa + beta
    phi = 0

    dM = float(mi - mi0) / 1.8
    dP = float(phi - phi0) / 1.8
    dT = float(teta - teta0) / 1.8
    mi0 = float(mi)
    phi0 = float(phi)
    teta0 = float(teta)
    data = {dM,dT}
    promptprint('angleS')
    promptprint(data)
    promptprint(' ')
    rostalk(data) 
     

xbutp = Button(master, text="+", command=ajustefunxp, height=1, width=2)
xbutp.grid(row=5, column=1)
xbutm = Button(master, text="-", command=ajustefunxm, height=1, width=2)
xbutm.grid(row=5, column=2)

ybutp = Button(master, text="+", command=ajustefunyp, height=1, width=2)
ybutp.grid(row=6, column=1)
ybutm = Button(master, text="-", command=ajustefunym, height=1, width=2)
ybutm.grid(row=6, column=2)

zbutp = Button(master, text="+", command=ajustefunzp, height=1, width=2)
zbutp.grid(row=7, column=1)
zbutm = Button(master, text="-", command=ajustefunzm, height=1, width=2)
zbutm.grid(row=7, column=2)


# prompt{

def promptprint(text):
    text = str(text)
    tex.insert(1.0, text + "\n")


Label(text="robot prompt", bd=1, relief="solid").grid(row=8, column=3, columnspan=1)
tex = Text(master)
tex = Text(width=40, height=10, bd=1, relief="solid", wrap=WORD)
tex.grid(row=9, rowspan=9, column=3, columnspan=2, padx=20)


def stop():
    promptprint('stop the code')
    global flag
    flag = not flag


stop = Button(master , text="STOP!", command=stop, bg='red', height=4, width=10)
stop.grid(row=1, column=6)


def toggle():
    global shown
    if shown:
        l.grid_remove()
    else:
        l.grid(row=4, column=6, sticky=E)
    shown = not shown


efe = Frame(master)
efe.grid(row=4, column=4)
shown = False
Button(efe, text="LASER!", command=toggle, bg='red', height=2, width=5).grid(row=4, column=5, ipadx=8, ipady=8)
l = Label(efe, text="laser on")


def grey(*args, **kwargs):
    master.configure(background="grey")


master.configure(background='grey')


def file():
    global filename
    filename = askopenfilename()
    return filename


w = Button(master, text="arquivos executaveis", command=file)
w.grid(row=1, column=3)


def ok():
    if flag == False:
        if filename == '':
            file()

        promptprint(filename)
        global flag1
        global flag2
        global flag3
        global flag5
        global z
        global x
        global y
        global f
        global x0
        global y0
        global z0
        global kx
        global ky
        global kz
        global kv
        global mi0
        global phi0
        global teta0
        global flagx
        global flagy
        global flagz
        global iF
        global fx
        global fy
        global fz
        global lx
        global q
        global c
        s = open(filename, 'r')

        # main loop
        for line in s:
            if line.startswith('G'):
                promptprint('{} sua linha'.format(line))
                ix = line.find("X")
                xStr = ''
                flag1 = False
                for letter in line[ix + 1:]:
                    if letter != ' ' and flag1 == False:
                        if letter.isalpha() == True:
                            flag1 = True
                            break

                        if letter == '-':
                            x = -x
                        else:
                            xStr = xStr + letter
                            x = float(xStr)

                promptprint(x)

                iy = line.find("Y")
                yStr = ''
                flag2 = False
                for letter in line[iy + 1:]:
                    if letter != ' ' and flag2 == False:
                        if letter.isalpha() == True:
                            flag2 = True
                            break

                        if letter == '-':
                            y = -y
                        else:
                            yStr = yStr + letter
                            y = float(yStr)

                promptprint(y)

                iz = line.find("Z")
                zStr = ''
                flag3 = False
                for letter in line[iz + 1:]:
                    if letter != ' ' and flag3 == False:
                        if letter.isalpha() == True:
                            flag3 = True
                            break

                        if letter == '-':
                            z = -z
                        else:
                            zStr = zStr + letter
                            z = float(zStr)

                promptprint(z)

                ig = line.find("G")
                gStr = ''
                gStr = line[ig + 1]
                g = int(gStr)

                promptprint(g)

                iF = line.find("F")
                fStr = ''
                flag5 = False
                for letter in line[iF + 1:]:
                    if letter != ' ' and flag5 == False:
                        if letter.isalpha() == True:
                            flag5 = True
                            break

                        if letter == '-':
                            f = -f
                        else:
                            fStr = fStr + letter
                            f = float(fStr)

                promptprint(f)

                # preparação para o loop
                deltax = abs(float(x - x0))
                promptprint('deltas')
                promptprint(deltax)

                deltay = abs(float(y - y0))
                promptprint(deltay)

                deltaz = abs(float(z - z0))
                promptprint(deltaz)


                    # G0
                if g == 0:
                    promptprint('g0')
                    if x0 == 0 or x==0:
                        mi = 90
                    else:
                        mi = float(math.atan(y / x))

                    lx = deltax / (1/(math.degrees(math.sin(mi))))
                    l = lx + 15  # buffer de distancia da base

                    a = math.sqrt((deltaz ** 2) + (l ** 2))
                    alfa = math.degrees(math.atan(deltaz / l))
                    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

                    teta = alfa + beta
                    phi = 85

                    dM = float(mi) / 1.8
                    dP = float(phi) / 1.8
                    dT = float(teta) / 1.8

                    data = {dM,dT}
                    promptprint('angleS')
                    promptprint(dP)
                    promptprint(dT)
                    promptprint(dM)
                    promptprint(' ')
                    rostalk(data)  
                     

                # G1
                if g == 1:
                    promptprint('g1')
                    if x0 == 0 or x == 0:
                        mi = 90
                    else:
                        mi = float(math.atan(deltax / deltay))

                    lx = deltax / (1/(math.degrees(math.sin(mi))))
                    l = lx + 15  # buffer de distancia da base

                    a = math.sqrt((deltaz ** 2) + (l ** 2))
                    alfa = math.degrees(math.atan(deltaz / l))
                    beta = math.degrees(math.acos(((a ** 2) + (c ** 2) - (q ** 2)) / (2 * a * c)))

                    teta = alfa + beta
                    phi = 85
                    dM = float(mi) / 1.8
                    dP = float(phi) / 1.8
                    dT = float(teta) / 1.8

                    data = {dM,dT}
                    promptprint('angleS')
                    promptprint(dP)
                    promptprint(dT)
                    promptprint(dM)
                    promptprint(' ')
                    rostalk(data) 

                    x0 = x
                    y0 = y
                    z0 = z


button = Button(master, text="RUN!", command=ok, height=1, width=5)  # para o butão de ok, executa a função principal
button.grid(row=1, column=4)

mainloop()
