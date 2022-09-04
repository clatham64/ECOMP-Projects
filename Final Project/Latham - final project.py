#Final Project, Climate Change Ap
import time
from tkinter import *

#initialize climate change variables and equations
pe = 450
pes = 1.0
pd = 800
pds = 1.0
ps = 1.0
ie = 450
ies = 1.0
indd = 1500
indds = 1.0
icd = 640
icds = 1.0
inds = 1.0
te = 400
tes = 1.0
tp =128
tps = 1.0
tc = 912
tcs = 1.0
ttr = 416
ttrs = 1.0
to = 150
tos = 1.0
ts = 1.0
at = 660
agms = 1.0
ags = 1.0
es = 1.0
modtotal = (pe*pes+pd*pds)*ps+(ie*ies+indd*indds+icd*icds)*inds+\
           (te*tes+tp*tps+tc*tcs+ttr*ttrs+to*tos)*ts\
               +(at*.5+at*.5*agms)*ags

xdraw = 20
ydraw = 50

def update_totals ():
    global pe, pd, ie, indd, icd, te, tp, tc, ttr, to, at, totalUS, total, totalChina\
           , pes, pds, ies, indds, icds, tes, tps, tcs, ttrs, tos, ps, inds, ts, ags,\
           modtotal, agms, es
    modtotal = (pe*pes*es+pd*pds)*ps+(ie*ies*es+indd*indds+icd*icds)*inds+\
               (te*tes*es+tp*tps+tc*tcs+ttr*ttrs+to*tos)*ts\
               +(at*.5+at*.5*agms)*ags
#    print(modtotal)

def drawbar():
    global line_percent, modtotal,total
    line_percent = modtotal/total
    canvas.coords(greybar,330,bartop,370,bartop+(barbot-barbot)*line_percent)
    non_eq = 3800 / total
    eq_sus = 950/total
    


#set total values
total = pe+pd+ie+indd+icd+te+tp+tc+ttr+to+at
    
#line stuff
line_percent = modtotal/total

#make the window    
window = Tk()
window.title('C02 Meter')
#window.geometry("400x700")
#make the canvas
canvas = Canvas(window, height = 700, width = 400)#, bg = "black")
canvas.pack()
#Add the title
canvas.create_text(200, 30, text = "U.S. CO2 Emissions",\
                   font = ("Helvetica", 15), fill = "black",\
                   justify = "center")

#deal with the bars
bartop = 50
barbot = 650
bar = canvas.create_rectangle(330,bartop,370,barbot,fill = "green")
greybar = canvas.create_rectangle(330,bartop,370,bartop,fill = "black")
non_eq = 3800/total
eq_sus = 950/total
canvas.create_text(280, bartop+(barbot-bartop)*(1-non_eq), text = "Sustainable at \ncurrent world\npercent",\
                   fill = "purple", font=('Helvetica', 8))
sus_line = canvas.create_rectangle(325, bartop+(barbot-bartop)*\
                    (1-non_eq),375,bartop+(barbot-bartop)*(1-non_eq)+5, fill = "purple")
canvas.create_text(280, bartop+(barbot-bartop)*(1-eq_sus), text = "Sustainable with \nglobal equity",\
                   fill = "purple", font=('Helvetica', 8))
sus_line = canvas.create_rectangle(325, bartop+(barbot-bartop)*\
                    (1-eq_sus),375,bartop+(barbot-bartop)*(1-eq_sus)+5, fill = "purple")

# Define Our Images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")

#set up the buttons
b_list=[]

#button format: b_list.append(["scaling_factor_name","scaling_factor_variable", 20])

#all electricity
b_list.append(["All electricty","es", 20,'p'])

#home and bussiness electric
b_list.append(["Personal electricity","pes", 20,'s'] )

#Industry electric
b_list.append(["Industry electricity","ies", 20,'s'] )

#Transportation Electricty
b_list.append(["Transportation \\nelectricty","tes", 35,'s'])

#private homes list
b_list.append(["Home and business\\nheating", "pds", 35,'p'])

#Other industry emissions
b_list.append(["Other industry\\nemissions","indds", 35,'p'] )

#Transport
b_list.append(["All transport","ts", 20,'p'])

#Just Cars
b_list.append(["Only cars","tcs", 20,'s'])

#Just airplanes
b_list.append(["Just airplanes","tps", 20,'s'])

#Just trucks
b_list.append(["Just trucks","ttrs", 20,'s'])

#Agriculture
b_list.append(["All agriculture","ags", 20,'p'])

#Just meat
b_list.append(["Just meat","agms", 20,'s'])



for n in range(len(b_list)):
    exec("""
#global is_on
is_on"""+str(n)+""" = True

# Create Label
my_label"""+str(n)+""" = Label(canvas,
    text = \""""+b_list[n][0]+""" ",
    fg = "green",
    font = ("Helvetica", 8),
    justify = "left",
    anchor = "w")
if b_list[n][3] == "s":
    xdraw += 20
#draw the label and adjust where the next one is
my_label"""+str(n)+""".place(x = xdraw,y=ydraw)
ydraw += b_list[n][2]

# Define our switch function
def switch"""+str(n)+"""():
    global is_on"""+str(n)+"""
    global """+b_list[n][1]+"""
    global greybar
    global canvas
    
    # Determine is on or off
    if is_on"""+str(n)+""":
        b"""+str(n)+""".config(image = off)
        my_label"""+str(n)+""".config(text = \""""+b_list[n][0]+""" ",
                        fg = "grey")
        """+b_list[n][1]+"""=0.0
        update_totals()
        is_on"""+str(n)+""" = False
        line_percent = modtotal/total
        canvas.coords(greybar,330,bartop,370,bartop+(barbot-bartop)*(1-line_percent))
        
    else:       
        b"""+str(n)+""".config(image = on)
        my_label"""+str(n)+""".config(text = \""""+b_list[n][0]+""" ", fg = "green")
        """+b_list[n][1]+"""=1.0
        update_totals()
        is_on"""+str(n)+""" = True
        line_percent = modtotal/total
        canvas.coords(greybar,330,bartop,370,bartop+(barbot-bartop)*(1-line_percent))

# Create A Button


b"""+str(n)+""" = Button(canvas, image = on, bd = 0,
                   command = switch"""+str(n)+""")
b"""+str(n)+""".place(x=xdraw, y=ydraw)

if b_list[n][3] == "s":
    xdraw -= 20

if ydraw > 620:
    ydraw = 50
    xdraw += 100
else:
    ydraw += 25

""")

canvas.config(height = 700, width = 400)

window.mainloop()
