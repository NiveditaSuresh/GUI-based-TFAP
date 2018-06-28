from tkinter import*
import cmath
import math
import tkinter.messagebox
root  =Tk()
root.configure(bg='#eedd82')
rnum= [ ];
rden = [ ];
inum =  [ ];
iden= [ ];
wr = [0] ;
sc=[];
root.title("wm min/max")
root.resizable(0,0)
global h
global t
global p
global q
global gain
global name
global Wn
global delta
zcount=0;
pcount=0;
q=0;
h=0;
t=0;
p=0;
global k
global l
k=0;
l=0;
def helpmenu() :
    sub3 = Toplevel(root)
    sub3.title("wm min/max")
    sub3.title('HELP')
    sub3.resizable(0,0)

    var="""
INTRODUCTION 

The program is a GUI based transfer function analysis package .It takes in
the values of poles, zeroes and the gain factor of a transfer function.
From this it gives the frequency plot, both absolute and bode, and the
time response which includes step and impulse response. It can also be
used for estimating the stability of the system.
This software gives the user, better understanding on how the frequency
and time response depends on the poles, zeroes and the gain factor.
It helps the user to export the project and study it in other softwares. 

ABOUT THE SOFTWARE
           
Graphical User Interface (GUI) is a type of interface that allows users to
interact with electronic devices through graphical icons and visual indicators.
Programming in GUI needs a language as a platform. The software adapts Python
to develop a code which gives the desired output.
Using GUI programming in Python, a package  is  designed to obtain the
frequency and time response of a system by computing its transfer function.
Python provides various options for developing graphical user interfaces (GUIs)
out of which one is Tkinter. Tkinter is the standard GUI library for Python.
Python when combined with Tkinter provides a fast and easy way to create
GUI applications.



INPUT FEATURES

•   Magnitude and angle of the poles and zeroes can be located graphically
    with the help of an expandable circle and a movable line controlled
    using the arrow keys or mouse.
    {Left and Right arrow keys for angle variations of 1 degrees
     Up and Down keys for magnitude variations by 0.1}
•   The assigned poles are marked by ‘x’ mark and zeroes by ‘o’ mark.
•   Poles can be entered by using ENTER key or the right click of the mouse.
    The zeroes are entered using the SHIFT key or left click of the mouse.
•   The user may give the gain factor in the entry box.
•   The user can specify the frequency range in which he/she may want to
    view the output.
•   Click on the Edit button to edit the poles and zeroes after their
    entry is done.



MAIN WINDOW COMPONENTS

A menu bar is provided containing the following:

FILE:
    New project : To create a new project .
    Save project : To save the project.
    Load project: To import and read from a text file.
    Exit: To exit the program.

FREQUENCY RESPONSE:
    Absolute response: |H(jw)| vs w and <H(jw)  vs  w  are plotted.
    Bode plot:  20 log|H(jw)| vs w and corresponding phase plot is plotted.

TIME RESPONSE:
    Step response : Gives the response of the system when a unit step
    function is applied to the system as input.
    Impulse response: Gives the response of the system when a unit impulse
    function is applied to the system as input.

HELP  : Opens the help window.

EXIT : Exits the program.


OUTPUT FEATURES

. Frequency response both absolute and bode plot can be obtained from the
  frequency response menu .
. Time response both step and impulse can be obtained from the time response
  menu button .
. Click on save image button to save in .png format.
. Click on export to mat button to export it to .mat format and save.

    
"""
    scrollbar = Scrollbar(sub3)
    scrollbar.pack( side = RIGHT, fill=Y )
    canvash=Canvas(sub3,width=500,height=300,bg='#eeeee0',yscrollcommand=scrollbar.set,scrollregion=(0,0,600,1200))    
    canvash.create_text(250,620,text= var)
    canvash.pack()
    scrollbar.config( command = canvash.yview,orient= VERTICAL )    
    sub3.mainloop()

def freqbodeop () :
    sub2 = Toplevel(root)
    sub2.title("wm min/max")
    sub2.resizable(0,0)
    sub2.title("BODE PLOT")
    frame=Frame(sub2)
    frame.pack()
    bottomframe=Frame(sub2)
    bottomframe.pack(side= BOTTOM)
    w=0
    mag= 1;
    ang= 0;
    xvar = [ ];
    wm = [ ];
    Ang = [ ];
    numa=0;
    dena=0;
    global k
    global l
    
    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = BOTTOM, fill=Y )
    canvas3 = Canvas(frame,width=600,height=300,bg='#eeeee0',xscrollcommand=scrollbar.set,scrollregion=(0,0,1110,1110))
    canvas3.pack()
    scrollbar1 = Scrollbar(bottomframe)
    scrollbar1.pack( side = BOTTOM, fill=Y )
    canvas4 = Canvas(bottomframe,width=600,height=300,bg='#cdcdc1',xscrollcommand=scrollbar.set,scrollregion=(0,0,1110,1110))
    canvas4.pack()
    scrollbar.config( command = canvas3.xview,orient= HORIZONTAL )
    scrollbar1.config( command = canvas4.xview,orient= HORIZONTAL )
    canvas3.create_line(100,250,100,50,width=2)
    canvas3.create_line(100,150,1100,150,width=2)
    canvas4.create_line(100,250,100,50,width=2)
    canvas4.create_line(100,150,1100,150,width=2)
    canvas3.create_text(20,80,text="\n".join("MAGNITUDE"), anchor="nw")
    canvas3.create_text(300,20,text="MAGNITUDE PLOT")
    canvas3.create_text(300,280,text="FREQUENCY (in rad/s)")    
    canvas4.create_text(20,120,text="\n".join("ANGLE"), anchor="nw")
    canvas4.create_text(300,20,text="ANGLE PLOT")
    canvas4.create_text(300,280,text="FREQUENCY (in rad/s)") 
    mag1=0
    d=0;
    ang1=0
    angmax=0
    magmax=0
    
    while(d<1000):
        num=1;
        den=1;
        numa=0;
        dena=0;
        w=pow(10,((d-200)/200))
        for g in range (k) :
            num= num * cmath.sqrt(pow((w-inum[g]),2) + pow(rnum[g],2));
            m=math.degrees(math.atan2((w-inum[g]),rnum[g]))
            if(m<0):
                m=m+360
            
            numa = numa + m;
        for m in range (l) :
            den= den* cmath.sqrt(pow((w-iden[m]),2) + pow(rden[m],2));
            md=math.degrees(math.atan2((w-iden[m]),rden[m]))
            if(md<0):
                md=md+360
            dena = dena + md;
        mag=mag1;
        ang = ang1;
        mag1=20*math.log10(abs(gain*num/den));        
        ang1=(numa - dena);
        if(abs(mag1)>magmax) :
            magmax=abs(mag1)
            rem=magmax
            f=-1
            while(rem>=10) :
                rem= rem/ 10
                f=f+1;
            div=int(rem+1)*pow(10,f)
            if(magmax <1):
                rem1 = magmax
                f=0
                while(rem1<=1):
                    rem1=rem1*10;
                    f=f-1;
                div=int(rem1+1)*pow(10,f-1)

        if(abs(ang1)>angmax) :
            angmax=abs(ang1)
            rema=angmax
            f1=1
            if(rema>=45) :
                rema= int(rema/ 180)
                f1=f1+rema;
            if(angmax <45):
                rema1 = angmax
                f1=(1/4.5)
                
        d=d+1
    d=0
    mag1=0
    ang1=0
    while(d<1000):
        num=1;
        den=1;
        numa=0;
        dena=0;
        w=pow(10,((d-200)/200))
        for g in range (k) :
            num= num * cmath.sqrt(pow((w-inum[g]),2) + pow(rnum[g],2));
            m=math.degrees(math.atan2((w-inum[g]),rnum[g]))
            if(m<0):
                m=m+360
            numa = numa + m;
        for m in range (l) :
            den= den* cmath.sqrt(pow((w-iden[m]),2) + pow(rden[m],2));
            md=math.degrees(math.atan2((w-iden[m]),rden[m]))
            if(md<0):
                md=md+360
            dena = dena + md;
        mag=mag1;
        ang=ang1;
        mag1=20*math.log10(abs(gain*num/den));        
        ang1=(numa - dena);
        canvas3.create_line(d+100,(150-(10*mag/div)),d+101,(150-(10*mag1/div)),width=2)
        canvas4.create_line(d+100,(150-((25*ang)/(45*f1))),d+101,(150-((25*ang1)/(45*f1))),width=2)
        d=d+1;
        
    for i in range(6):
        x= 100 + (i*200)
        canvas3.create_line(x,150,x,145,width=2)
        canvas3.create_text(x,155,text='%.1f'%(pow(10,(i-1))),anchor="ne")
    for j in range(11):
        y= 250 - (j*20)
        canvas3.create_line(100,y,105,y,width=2)
        canvas3.create_text(95,y,text='%.3f'%((-5 +j)* 2*div),anchor=E)
    for i in range(6):
        x= 100 +  (i*200)
        canvas4.create_line(x,150,x,145,width=2)
        canvas4.create_text(x,155,text='%.1f'%(pow(10,(i-1))),anchor="ne")
    for j in range(9):
        y= 250 - (j*25)
        canvas4.create_line(100,y,105,y,width=2)
        canvas4.create_text(95,y,text='%.2f'%((-4 +j)*45*f1),anchor=E)


def freqop () :
    global canvas1
    sub1 = Toplevel(root)
    sub1.title("wm min/max")
    sub1.resizable(0,0)
    sub1.title("ABSOLUTE PLOT")
    frame=Frame(sub1)
    frame.pack()
    bottomframe=Frame(sub1)
    bottomframe.pack(side= BOTTOM)
    w=0
    mag= 1;
    ang= 0;
    xvar = [ ];
    wm = [ ];
    Ang = [ ];
    numa=0;
    dena=0;
    global k
    global l
    sc.append(0);
    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = BOTTOM, fill=Y )
    canvas1 = Canvas(frame,width=600,height=300,bg='#eeeee0',xscrollcommand=scrollbar.set,scrollregion=(0,0,5000,5000))
    canvas1.pack()
    scrollbar1 = Scrollbar(bottomframe)
    scrollbar1.pack( side = BOTTOM, fill=Y )
    canvas2 = Canvas(bottomframe,width=600,height=300,bg='#cdcdc1',xscrollcommand=scrollbar.set,scrollregion=(0,0,5000,5000))
    canvas2.pack()
    scrollbar.config( command = canvas1.xview,orient= HORIZONTAL )
    scrollbar1.config( command = canvas2.xview,orient= HORIZONTAL )
    canvas1.create_text(20,80,text="\n".join("MAGNITUDE"), anchor="nw")
    canvas1.create_text(300,20,text="MAGNITUDE PLOT")
    canvas1.create_text(300,280,text="FREQUENCY (in rad/s)")    
    canvas2.create_text(20,120,text="\n".join("ANGLE"), anchor="nw")
    canvas2.create_text(300,20,text="ANGLE PLOT")
    canvas2.create_text(300,280,text="FREQUENCY (in rad/s)") 
    
    
    if(len(sc)==1) :
        scale = 0.005
        
        
    else :
        sc.remove(0)
        scale= 0.005*min(sc)
       
    UL= scale*500
    ful=-1
    remul=UL
    while(remul>=1) :
        remul= remul/ 10
        ful=ful+1;
    if(UL <1):
        rem1ul = UL
        ful=0
        while(rem1ul<=1):
            rem1ul=rem1ul*10;
            ful=ful-1;
    UL= pow(10,(ful+1))
    canvas1.create_line(100,250,100,50,width=2)
    canvas1.create_line(100,250,100+(UL/scale),250,width=2)
    canvas2.create_line(100,250,100,50,width=2)
    canvas2.create_line(100,150,100+(UL/scale),150,width=2)
    it=0
    
    
    mag1=0
    w=0;
    n=0;
    magmax=0
    ang1=0
    angmax=0
    while(w<UL):
        num=1;
        den=1;
        numa=0;
        dena=0;
        for g in range (k) :
            num= num * cmath.sqrt(pow((w-inum[g]),2) + pow(rnum[g],2));
            m=math.degrees(math.atan2((w-inum[g]),rnum[g]))
            if(m<0):
                m=m+360
            
            numa = numa + m;
        for m in range (l) :
            den= den* cmath.sqrt(pow((w-iden[m]),2) + pow(rden[m],2));
            md=math.degrees(math.atan2((w-iden[m]),rden[m]))
            if(md<0):
                md=md+360
            dena = dena + md;
        mag=mag1;
        ang=ang1;
        mag1=abs(num/den);        
        ang1=(numa - dena);
        if(mag1>magmax) :
            magmax=mag1
            rem=magmax
            f=-1
            while(rem>=10) :
                rem= rem/ 10
                f=f+1;
            div=int(rem+1)*pow(10,f)
            if(magmax <1):
                rem1 = magmax
                f=0
                while(rem1<=1):
                    rem1=rem1*10;
                    f=f-1;
                    div= int(rem1+1)*pow(10,f-1)
        if(abs(ang1)>angmax) :
            angmax=abs(ang1)
            rema=angmax
            f1=1
            if(rema>=45) :
                rema= int(rema/ 180)
                f1=f1+rema;
            if(angmax <45):
                rema1 = angmax
                f1=(1/4.5)
        w=w+scale;
        n=n+1;

    mag1=0
    ang1=0
    w=0;
    n=0;    
    while(w<UL):
        num=1;
        den=1;
        numa=0;
        dena=0;
        for g in range (k) :
            num= num * cmath.sqrt(pow((w-inum[g]),2) + pow(rnum[g],2));
            m=math.degrees(math.atan2((w-inum[g]),rnum[g]))
            if(m<0):
                m=m+360
            
            numa = numa + m;
        for m in range (l) :
            den= den* cmath.sqrt(pow((w-iden[m]),2) + pow(rden[m],2));
            md=math.degrees(math.atan2((w-iden[m]),rden[m]))
            if(md<0):
                md=md+360
            dena = dena + md;
        mag=mag1;
        ang=ang1;
        mag1=abs(num/den);        
        ang1=(numa - dena);             
        canvas1.create_line(100+n,(250-(20*mag/div)),100+n+1,(250-(20*mag1/div)),width=2)
        canvas2.create_line(n+100,(150-((25*ang)/(45*f1))),n+101,(150-((25*ang1)/(45*f1))),width=2)
        w=w+scale;
        n=n+1;
    for i in range(21):
        x= 100 + (i*(UL/(scale*20)))
        canvas1.create_line(x,250,x,245,width=2)
        canvas1.create_text(x,255,text='%.2f'%(i*UL/20),anchor="ne")
    for j in range(11):
        y= 250 - (j*20)
        canvas1.create_line(100,y,105,y,width=2)
        canvas1.create_text(95,y,text='%.4f'%(j* div),anchor=E)
    for i in range(21):
        x= 100 + (i*(UL/(scale*20)))
        canvas2.create_line(x,150,x,145,width=2)
        canvas2.create_text(x,155,text='%.2f'%(i*UL/20),anchor="ne")
    for j in range(9):
        y= 250 - (j*25)
        canvas2.create_line(100,y,105,y,width=2)
        canvas2.create_text(95,y,text='%.3f'%((-4 +j)*45*f1),anchor=E)

def time_imp():
    global l;
    global k;
    lnum=1
    lden=1
    sa=0
    gh=0
    xy=[]
    xy1=[]
    xy2=[]
    ab=[];
    abc=[];
    nv=0
    scale= 1/(150*abs(max(rden)))
    UL= 3/abs(min(rden))
    ful=-1
    remul=UL
    while(remul>=1) :
        remul= remul/ 10
        ful=ful+1;
    if(UL <1):
        rem1ul = UL
        ful=0
        while(rem1ul<=1):
            rem1ul=rem1ul*10;
            ful=ful-1;
    UL= pow(10,(ful+1))
    while(nv<l):
        a=[];
        s=(rden[nv]+iden[nv]*(1j))
        for hop in range(l) :
            a.append(rden[hop]+iden[hop]*(1j))
        a.remove(s)
        sb=l-1
        while(sa<k):
            lnum=lnum*(s-(rnum[sa]+inum[sa]*(1j)))
            sa=sa+1
        while(gh<sb):
            lden=lden*(s-a[gh])
            gh=gh+1
        lm=(lnum/lden)
        if(iden[nv]==0):
            ab.append(lm)
            abc.append(math.exp(-1*s.real))
        else:
            xy.append(lm)
            xy1.append(rden[nv])
            xy2.append(iden[nv])
        nv=nv+1
    uq=0
    xyz=[]
    xyz1=[]
    xyz2=[]
    while(uq<len(xy)):
        xyz.append(xy[uq]+xy[uq+1])
        xyz1.append(xy1[uq])
        xyz2.append(xy2[uq])
        uq=uq+2
    

    sub8 = Toplevel(root)
    sub8.title("wm min/max")
    sub8.resizable(0,0)
    sub8.title("IMPULSE RESPONSE")
    frame8=Frame(sub8)
    frame8.pack()

    scrollbar = Scrollbar(frame8)
    scrollbar.pack( side = BOTTOM, fill=Y )
    canvas8 = Canvas(frame8,width=600,height=300,bg='#eeeee0',xscrollcommand=scrollbar.set,scrollregion=(0,0,5000,5000))
    canvas8.pack()
    scrollbar.config( command = canvas8.xview,orient= HORIZONTAL )
    mag1=0
    canvas8.create_line(100,250,100,50,width=2)
    canvas8.create_line(100,150,100+(UL/scale),150,width=2)
    canvas8.create_text(20,80,text="\n".join("MAGNITUDE"), anchor="nw")
    canvas8.create_text(300,20,text="IMPULSE RESPONSE")
    canvas8.create_text(300,280,text=" TIME(in s)") 
    t=0
    while(t<UL) :
        mag=mag1
        for go in range (len(ab)) :
            mag1=mag1+ ((ab[go]).real* pow(abc[go],t))
        for go1 in range (int(uq/2)) :
            mag1 = mag1 + ((xyz[go1]).real * math.exp(-1*xyz1[go1]*t)*math.cos(xyz2[go1] *t))
        magmax=0
        if(abs(mag1)>magmax) :
            magmax=abs(mag1)
            rem=magmax
            f=-1
            while(rem>=10) :
                rem= rem/ 10
                f=f+1;
            div=int(rem+1)*pow(10,f)
            if(magmax <1):
                rem1 = magmax
                f=0
                while(rem1<=1):
                    rem1=rem1*10;
                    f=f-1;
                div=int(rem1+1)*pow(10,f-1)
        t=t+scale
        
    mag1=0
    t=0
    n=0
    while(t<UL) :
        mag=mag1
        for go in range (len(ab)) :
            mag1=mag1+ ((ab[go]).real*math.pow(abc[go],t))
        for go1 in range (int(uq/2)) :
            mag1 = mag1 + ((xyz[go1]).real * math.exp(-1*xyz1[go1]*t)*math.cos(xyz2[go1] *t))
        
        canvas8.create_line((100+n),(150-(10*mag/div)),(101+n),(150-(10*mag1/div)),width=2)
        t=t+scale
        n=n+1

    for i in range(11):
        x= 100 + (i*(0.1*UL/scale))
        canvas8.create_line(x,150,x,145,width=2)
        canvas8.create_text(x,155,text='%.1f'%(i*0.1*UL),anchor="ne")
    for j in range(11):
        y= 250 - (j*20)
        canvas8.create_line(100,y,105,y,width=2)
        canvas8.create_text(95,y,text='%.2f'%((-5 +j)* 2*div),anchor=E)


def time_step():
    global l;
    global k;
    lnum=1
    lden=1
    sa=0
    gh=0
    xy=[]
    xy1=[]
    xy2=[]
    ab=[];
    abc=[];
    nv=0
    scale= 1/(150*abs(max(rden)))
    UL= 3/abs(min(rden))
    ful=-1
    remul=UL
    while(remul>=1) :
        remul= remul/ 10
        ful=ful+1;
    if(UL <1):
        rem1ul = UL
        ful=0
        while(rem1ul<=1):
            rem1ul=rem1ul*10;
            ful=ful-1;
    UL= pow(10,(ful+1))

    while(nv<l):
        a=[0];
        s=(rden[nv]+iden[nv]*(1j))
        for hop in range(l) :
            a.append(rden[hop]+iden[hop]*(1j))
        a.remove(s)
        sb=l
        while(sa<k):
            lnum=lnum*(s-(rnum[sa]+inum[sa]*(1j)))
            sa=sa+1
        while(gh<sb):
            lden=lden*(s-a[gh])
            gh=gh+1
        lm=(lnum/lden)
        if(iden[nv]==0):
            ab.append(lm)
            abc.append(math.exp(-1*s.real))
        else:
            xy.append(lm)
            xy1.append(rden[nv])
            xy2.append(iden[nv])
        nv=nv+1
    uq=0
    xyz=[]
    xyz1=[]
    xyz2=[]
    while(uq<len(xy)):
        xyz.append(xy[uq]+xy[uq+1])
        xyz1.append(xy1[uq])
        xyz2.append(xy2[uq])
        uq=uq+2
    

    sub8 = Toplevel(root)
    sub8.title("wm min/max")
    sub8.resizable(0,0)
    sub8.title("STEP RESPONSE")
    frame8=Frame(sub8)
    frame8.pack()
    scrollbar = Scrollbar(frame8)
    scrollbar.pack( side = BOTTOM, fill=Y )
    canvas8 = Canvas(frame8,width=600,height=300,bg='#eeeee0',xscrollcommand=scrollbar.set,scrollregion=(0,0,5000,5000))
    canvas8.pack()
    scrollbar.config( command = canvas8.xview,orient= HORIZONTAL )
    mag1=0
    canvas8.create_line(100,250,100,50,width=2)
    canvas8.create_line(100,150,100+(UL/scale),150,width=2)
    canvas8.create_text(20,80,text="\n".join("MAGNITUDE"), anchor="nw")
    canvas8.create_text(300,20,text="STEP RESPONSE")
    canvas8.create_text(300,280,text=" TIME(in s)") 
    t=0
    while(t<UL) :
        mag=mag1
        for go in range (len(ab)) :
            mag1=mag1+ ((ab[go]).real* pow(abc[go],t))
        for go1 in range (int(uq/2)) :
            mag1 = mag1 + ((xyz[go1]).real * math.exp(-1*xyz1[go1]*t)*math.cos(xyz2[go1] *t))
        magmax=0
        if(abs(mag1)>magmax) :
            magmax=abs(mag1)
            rem=magmax
            f=-1
            while(rem>=10) :
                rem= rem/ 10
                f=f+1;
            div=int(rem+1)*pow(10,f)
            if(magmax <1):
                rem1 = magmax
                f=0
                while(rem1<=1):
                    rem1=rem1*10;
                    f=f-1;
                div=int(rem1+1)*pow(10,f-1)
        t=t+scale
        
    mag1=0
    t=0
    n=0
    while(t<UL) :
        mag=mag1
        for go in range (len(ab)) :
            mag1=mag1+ ((ab[go]).real*math.pow(abc[go],t))
        for go1 in range (int(uq/2)) :
            mag1 = mag1 + ((xyz[go1]).real * math.exp(-1*xyz1[go1]*t)*math.cos(xyz2[go1] *t))
        
        canvas8.create_line((100+n),(150-(10*mag/div)),(101+n),(150-(10*mag1/div)),width=2)
        t=t+scale
        n=n+1

    for i in range(11):
        x= 100 + (i*(0.1*UL/scale))
        canvas8.create_line(x,150,x,145,width=2)
        canvas8.create_text(x,155,text='%.1f'%(i*0.1*UL),anchor="ne")
    for j in range(11):
        y= 250 - (j*20)
        canvas8.create_line(100,y,105,y,width=2)
        canvas8.create_text(95,y,text='%.2f'%((-5 +j)* 2*div),anchor=E)
        
        
def close_window ():
    root.destroy()
def newcd() :
    root.destroy()
    import TFAP
    

def saving() :
    global sub4
    global name
    global e3
    fo = open('%s.txt'%(e3.get()) , 'w')    
    for g in range (k) :
        fo.write( str(rnum[g]) + ' ' + str(inum[g]) + '\n' )
    fo.write( '\n' )        
    for m in range (l) :
        fo.write( str(rden[m]) + ' ' + str(iden[m]) + '\n' )
            
    fo.close()
    sub4.destroy()
    flag=1
   
def savefn () :
    global sub4
    global name
    global e3
    sub4=Toplevel(root)
    sub4.title("wm min/max")
    sub4.resizable(0,0)
    sub4.title('SAVE')
    sub4.minsize(300,50)
    l3 = Label(sub4,text='FILE NAME : ')
    l3.grid(column=0,row=0)
    l3.pack()
    e3 = Entry(sub4)
    e3.grid(column=1,row=0)
    e3.pack()
    
    b3= Button(sub4,text='SAVE',command=saving)
    
    b3.grid(column=1,row=1)
    b3.pack()
    sub4.mainloop()
      
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=newcd)
filemenu.add_command(label="Save",command=savefn)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=close_window)
menubar.add_cascade(label="File", menu=filemenu)
freqmenu = Menu(menubar, tearoff=0)
freqmenu.add_command(label="Absolute Plot",command=freqop)
freqmenu.add_command(label="Bode Plot",command = freqbodeop)
menubar.add_cascade(label="Frequency Response", menu=freqmenu,state='disabled')
timemenu = Menu(menubar, tearoff=0)
timemenu.add_command(label="Step Response",command=time_step)
timemenu.add_command(label="Impulse Response",command=time_imp)
menubar.add_cascade(label="Time Response", menu=timemenu,state='disabled')
menubar.add_cascade(label="Help",command=helpmenu)
menubar.add_cascade(label="Exit",command=close_window)
root.config(menu=menubar)     
    
def motion(event) :
    global t
    global h
    global p
    global q
    global but
    t = ((450-event.y)/20)-10
    h=((event.x-50)/20)-10
    p =math.sqrt(math.pow(h,2) + math.pow(t,2))
    q= math.degrees(math.atan2(t,h))
    if(p>10) :
        p=10
        canvas.itemconfigure(tag,text="(-,-)")
        canvas.coords(oval,(250-20*10,250-20*10,250+20*10,250+20*10))
        canvas.coords(lin,(250,250,250,250))
    else :
        canvas.coords(oval,(250-20*p,250-20*p,250+20*p,250+20*p))
        canvas.coords(lin,(250,250,event.x,event.y))
        canvas.itemconfigure(tag,text="%.2f"%p  + "  < " + "%.2f"%q )
def zeroes(event) :
    global but
    but.config(state='active')
    global k
    global h
    global t
    global p
    global zcount
    if(h in rnum and t in inum) :
        messagebox.showerror("ERROR", "MULTIPLE ORDERS ARE NOT PERMITTED" )
    else :
        if(p<10) :
            if(t==0) :
                zcount=zcount+1;
                rnum.append(h)
                inum.append(t)
                if(pow(t,2) > 2*pow(h,2)) :
                    Wr= math.sqrt(pow(t,2) - pow(h,2))
                    wr.append(Wr)
                gat2= canvas.create_text(478,70+25*(zcount),text="",anchor="nw")
                canvas.itemconfigure(gat2,text="%.2f"%h + " + " + "%.2f"%t + " i")
                gat3= canvas.create_text(((10+h)*20+50),(450-(10+t)*20),text="")
                canvas.itemconfigure(gat3,text="o")
                k=k+1
            else :
                zcount=zcount+1;
                rnum.append(h)
                inum.append(t)
                rnum.append(h)
                inum.append(-1*t)
                if(pow(t,2) > 2*pow(h,2)) :
                    Wr= math.sqrt(pow(t,2) - pow(h,2))
                    wr.append(Wr)
                    Wn=math.sqrt(pow(h,2) + pow(t,2))
                    delta = h/ Wn
                    sc.append(Wn*(1 - 2*pow(delta,2)+ math.sqrt( 2- 4*pow(delta,2) + 4*pow(delta,4))))
                gat= canvas.create_text(478,70+25*zcount,text="",anchor="nw")
                gat1= canvas.create_text(578,70+25*zcount,text="",anchor="nw")
                gat5= canvas.create_text(((10+h)*20+50),(450-(10+t)*20),text="")
                canvas.itemconfigure(gat5,text="o")
                gat4= canvas.create_text(((10+h)*20+50),(450-(10-t)*20),text="")
                canvas.itemconfigure(gat4,text="o")
                canvas.itemconfigure(gat,text="%.2f"%h + " + " + "%.2f"%t + " i")
                canvas.itemconfigure(gat1,text="%.2f"%h + " + " + "%.2f"%(-1*t) + " i")
                k=k+2
        

def poles(event) :
    global but
    but.config(state='active')
    global l
    global h
    global t
    global p
    global q
    global pcount
    if(h in rden and t in iden) :
        messagebox.showerror("ERROR", "REPEATED POLES AND ZEROES ARE NOT PERMITTED" )
    else:
        if(p<10) :
            if(t==0) :
                pcount=pcount+1;
                rden.append(h)
                iden.append(t)
                if(pow(t,2) > 2*pow(h,2)) :
                    Wr= math.sqrt(pow(t,2) - pow(h,2))
                    wr.append(Wr)
                cat2= canvas.create_text(700,70+25*pcount,text="",anchor="nw")
                canvas.itemconfigure(cat2,text="%.2f"%h + " + " + "%.2f"%t + " i")
                cat3= canvas.create_text(((10+h)*20+50),(450-(10+t)*20),text="")
                canvas.itemconfigure(cat3,text="x")
                l=l+1
            else :
                pcount=pcount+1;
                rden.append(h)
                iden.append(t)
                rden.append(h)
                iden.append(-1*t)
                if(pow(t,2) > 2*pow(h,2)) :
                    Wr= math.sqrt(pow(t,2) - pow(h,2))
                    wr.append(Wr)
                    Wn=math.sqrt(pow(h,2) + pow(t,2))
                    delta = h/ Wn
                    sc.append(Wn*(1 - 2*pow(delta,2)+ math.sqrt( 2- 4*pow(delta,2) + 4*pow(delta,4))))
                cat= canvas.create_text(700,70+25*pcount,text="",anchor="nw")
                cat1= canvas.create_text(800,70+25*pcount,text="",anchor="nw")
                cat5= canvas.create_text(((10+h)*20+50),(450-(10+t)*20),text="")
                canvas.itemconfigure(cat5,text="x")
                cat4= canvas.create_text(((10+h)*20+50),(450-(10-t)*20),text="")
                canvas.itemconfigure(cat4,text="x")
                canvas.itemconfigure(cat,text="%.2f"%h + " + " + "%.2f"%t + " i")
                canvas.itemconfigure(cat1,text="%.2f"%h + " + " + "%.2f"%(-1*t) + " i")
                l= l+2

def up(event) :
    global h
    global t
    global p
    global q
    p= p+0.1
    h= p*math.cos(math.radians(q))
    t = p*math.sin(math.radians(q))
    if(q==180) :
        t=0
    
    if(p>10) :
        p=10
        canvas.itemconfigure(tag,text="(-,-)")
        canvas.coords(oval,(250-20*10,250-20*10,250+20*10,250+20*10))
        canvas.coords(lin,(250,250,250,250))
    else :
        canvas.coords(oval,(250-20*p,250-20*p,250+20*p,250+20*p))
        canvas.coords(lin,(250,250,50+20*(10+h),450-20*(10+t)))
        canvas.itemconfigure(tag,text="%.2f"%p  + "  < " + "%.2f"%q )
def down(event) :
    global h
    global t
    global p
    global q
    p= p-0.1
    if(p<0) :
        p=0
    h= p*math.cos(math.radians(q))
    t = p*math.sin(math.radians(q))
    if(q==180) :
        t=0
    canvas.coords(oval,(250-20*p,250-20*p,250+20*p,250+20*p))
    canvas.coords(lin,(250,250,50+20*(10+h),450-20*(10+t)))
    canvas.itemconfigure(tag,text="%.2f"%p  + "  < " + "%.2f"%q )
def left(event) :
    global h
    global t
    global p
    global q
    q= q + 1 
    h= p*math.cos(math.radians(q))
    t = p*math.sin(math.radians(q))
    if(q==180) :
        t=0
    if(p>10) :
        p=10
        canvas.itemconfigure(tag,text="(-,-)")
        canvas.coords(oval,(250-20*10,250-20*10,250+20*10,250+20*10))
        canvas.coords(lin,(250,250,250,250))
    else :
        canvas.coords(oval,(250-20*p,250-20*p,250+20*p,250+20*p))
        canvas.coords(lin,(250,250,50+20*(10+h),450-20*(10+t)))
        canvas.itemconfigure(tag,text="%.2f"%p  + "  < " + "%.2f"%q )
def right(event) :
    global h
    global t
    global p
    global q
    q= q - 1   
    h= p*math.cos(math.radians(q))
    t = p*math.sin(math.radians(q))
    if(q==180) :
        t=0
    if(p>10) :
        p=10
        canvas.itemconfigure(tag,text="(-,-)")
        canvas.coords(oval,(250-20*10,250-20*10,250+20*10,250+20*10))
        canvas.coords(lin,(250,250,250,250))
    else :
        canvas.coords(oval,(250-20*p,250-20*p,250+20*p,250+20*p))
        canvas.coords(lin,(250,250,50+20*(10+h),450-20*(10+t)))
        canvas.itemconfigure(tag,text="%.2f"%p  + "  < " + "%.2f"%q )

def done() :

    canvas.unbind('<Motion>')
    canvas.unbind('<Button-1>')
    canvas.unbind('<Button-3>')
    root.unbind('<Return>')
    root.unbind('<Shift_L>')
    root.unbind('<Up>')
    root.unbind('<Down>')
    root.unbind('<Right>')
    root.unbind('<Left>')    
    canvas.itemconfigure(tag,text="(-,-)")
    canvas.coords(oval,(250,250,250,250))
    canvas.coords(lin,(250,250,250,250))
    menubar.entryconfig("Frequency Response",state='normal')
    menubar.entryconfig("Time Response",state='normal')
    but1.config(state='normal')
    but.config(state='disabled')
    if(k>=l):
        messagebox.showerror("ERROR", "THE NUMBER OF POLES MUST BE MORE THAN THE NUMBER OF ZEROES. PLEASE EDIT THE ENTRY" )
        addpz()
        

def addpz():
    canvas.bind('<Motion>',motion)
    canvas.bind('<Button-1>',poles)
    canvas.bind('<Button-3>',zeroes)
    root.bind('<Return>',poles)
    root.bind('<Shift_L>',zeroes)
    root.bind('<Up>',up)
    root.bind('<Down>',down)
    root.bind('<Right>',right)
    root.bind('<Left>',left)    
    menubar.entryconfig("Frequency Response",state='disabled')
    menubar.entryconfig("Time Response",state='disabled')
    but1.config(state='disabled')
    but.config(state='normal')
root.title('GUI SYSTEM RESPONSE PACKAGE ')
canvas = Canvas(root,width=900,height=500,bg='#eee8aa')

tag= canvas.create_text(10,10,text="",anchor="nw")
canvas.pack()

canvas.create_line(470,0,470,500,width=2,fill='white')
canvas.create_line(50,250,450,250,width=2)
canvas.create_line(250,450,250,50,width=2)
canvas.create_text(550,60,text="ZEROES")
canvas.create_text(780,60,text="POLES")
canvas.create_text(680,20,text="Use SHIFT/RIGHT CLICK for entry of zeroes \n   and ENTER/LEFT CLICK for entry of poles")
canvas.create_text(250,480,text="Use UP and DOWN arrow keys for magnitude adjustments \n and LEFT and RIGHT arrow keys for angle adjustments")
oval=canvas.create_oval(250,250,250,250,width=1)
lin=canvas.create_line(250,250,250,250)


canvas.bind('<Motion>',motion)
canvas.bind('<Button-1>',poles)
canvas.bind('<Button-3>',zeroes)
root.bind('<Return>',poles)
root.bind('<Shift_L>',zeroes)
root.bind('<Up>',up)
root.bind('<Down>',down)
root.bind('<Right>',right)
root.bind('<Left>',left)
    



for i in range(21):
    x= 50 + (i*20)
    canvas.create_line(x,250,x,245,width=2)
    canvas.create_text(x,254,text='%d'%(i-10),anchor=N)
for j in range(21):
    y= 450 - (j*20)
    canvas.create_line(250,y,255,y,width=2)
    canvas.create_text(245,y,text='%d'%(j-10),anchor=E)
x=0;
y=0;

l1= Label(root,text='GAIN')
l1.pack(side='left')
z1=Entry(root)
z1.pack(side='left')
z1.insert(3,'1')

gain=float(z1.get())
but=Button(root,text='DONE',command=done,state='disabled')
but.pack(side=RIGHT)
but1=Button(root,text='ADD POLES AND ZEROES ',state='disabled',command=addpz)
but1.pack(side=BOTTOM)


root.mainloop()
