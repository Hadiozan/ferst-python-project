from tkinter import *
# from customtkinter import*
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from time import *

# from tkinter import scrolledtext

w=Tk()
# w.geometry('1900x1500')
width= w.winfo_screenwidth() 
height= w.winfo_screenheight()
w.geometry("%dx%d" % (width, height))
# w.attributes('-fullscreen',True)
w.resizable(1,1)
w.title('.  :  ferst project  :  .')

img = ImageTk.PhotoImage(Image.open("ba.jpg"))

######################################################################################
###################################      CODES      ############      Backend      ###
######################################################################################
# بعد از اتمام و در هنگام تبدیل کد به اگزه این کد زیر باید فعال شود تا درست کار کند
# fuserinfo=open('usernameT.txt','a')
# fuserinfo.write(f'name:h   password:H   age:20   number:099999999999   native code:PPPPPPPPPP  po=T\n')
# fuserinfo.close()

def delit_txt(ferst):
    ferst.delete(1.0,'end-1c')
def delisign():
    txtsige1.delete(1.0,'end-1c')
    txtsige2.delete(1.0,'end-1c')
    txtsige4.delete(1.0,'end-1c')
    txtsige5.delete(1.0,'end-1c')
    txtsige6.delete(1.0,'end-1c')
def delilog():
    txtlog1.delete(1.0,'end-1c')
    txtlog2.delete(1.0,'end-1c')
def delitf():
    txtf1.delete(1.0,'end-1c')
    txtf4.delete(1.0,'end-1c')
    txtf5.delete(1.0,'end-1c')
    txtf6.delete(1.0,'end-1c')
    motien1()
    motien2()

def motien1():
    global bx
    w.after(1,motien1)
    if bx<463:
        bx+=7
        imoje.place(x=bx,y=697)
def motien2():
    global bx2
    w.after(1,motien2)
    if bx2<600:
        bx2+=7
        imoje2.place(x=bx2,y=697)        
def reipmotion():
    bx=-50
    imoje.place(x=bx,y=697)
    bx2=-50
    imoje2.place(x=bx2,y=697)

def riplog():
    lbllog42.place(x=-840,y=450)
    lbllog4.place(x=-840,y=450)

def listboxes(listname):
        listname.insert(END, itemoflb[each_item]) 
        listname.itemconfig(each_item,bg='#FFEFDB' if each_item %2==0 else 'gray75') 
# imoje.place(x=467,y=697)



####    page2    codes

def tiyp():
    Teachcod='123456789'
    Studentcod='987654321'

    tnamelog=txtsige1.get(1.0,'end-1c')
    tpasswordlog=txtsige2.get(1.0,'end-1c')
    tagelog=txtsige3.get()
    tnativecodlog=txtsige4.get(1.0,'end-1c')
    tnumberlog=txtsige5.get(1.0,'end-1c')
    tpos=txtsign7.get()
    tin=txtsige6.get(1.0,'end-1c')
    with open(r'usernameT.txt', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            pass
    with open(r'usernameS.txt', 'r') as fp:
        lines = fp.readlines()
        for row2 in lines:
            pass
    
    # print(tnamelog)
    # print(tpasswordlog)
    # print(tagelog)
    # print(tnativecodlog)
    # print(tnumberlog)
    if tpos=='Teacher' :
        if len(tnamelog)>5:
            if len(tpasswordlog)>8:
                if tin==Teachcod:
                    if tnumberlog.isdigit()==True:
                        if len(tnumberlog)==11:
                            if tnativecodlog.isdigit()==True:
                                if len(tnativecodlog)==10:
                                    if row.find(tnativecodlog)==-1:    
                                        fuserinfo=open('usernameT.txt','a')
                                        fuserinfo.write(f'name:{tnamelog}   password:{tpasswordlog}   age:{tagelog}   number:{tnumberlog}   native code:{tnativecodlog}  po=T\n')
                                        fuserinfo.close()
                                        page1.tkraise()
                                        delisign()
                                    else:messagebox.showerror('Repetitious','The national code used is already registered')
                                else:messagebox.showerror('Naitve Code', "Your Naitve code must have 10 digits")
                            else:messagebox.showerror('Only digit', "Your Naitve code must be digits")
                        else:messagebox.showerror('Number', "Your number must have 11 digits")
                    else:messagebox.showerror('Only digit', "Your Number must be digits")
                else:messagebox.showerror('Invented Cod', "your Invented Cod is incorecct")
            else:messagebox.showerror('Password', "your Password most more than 8 part")    
        else:messagebox.showerror('User name', "your User name most more than 5 part")
    elif tpos=='Student':
        if len(tnamelog)>5:
            if len(tpasswordlog)>8:
                if tin==Studentcod:
                    if tnumberlog.isdigit()==True:
                        if len(tnumberlog)==11:
                            if tnativecodlog.isdigit()==True:
                                if len(tnativecodlog)==10:
                                    if row2.find(tnativecodlog)==-1:  
                                        fuserinfo=open('usernameS.txt','a')
                                        fuserinfo.write(f'name:{tnamelog}   password:{tpasswordlog}   age:{tagelog}   number:{tnumberlog}   native code:{tnativecodlog}  po=S\n')
                                        fuserinfo.close()
                                        page1.tkraise()
                                        delisign()
                                    else:messagebox.showerror('Repetitious','The national code used is already registered')
                                else:messagebox.showerror('Naitve Code', "Your Naitve code must have 10 digits")
                            else:messagebox.showerror('Only digit', "Your Naitve code must be digits")
                        else:messagebox.showerror('Number', "Your number must have 11 digits")
                    else:messagebox.showerror('Only digit', "Your Number must be digits")
                else:messagebox.showerror('Invented Cod', "your Invented Cod is incorecct")
            else:messagebox.showerror('Password', "your Password most more than 8 part")    
        else:messagebox.showerror('User name', "your User name most more than 5 part")







########################   log find fang 
def erorlog():
    pass
# # دارای ارور 
#     tuserlog=txtlog1.get(1.0,'end-1c')
#     tpasslog=txtlog2.get(1.0,'end-1c')
#     if len(tuserlog)<2:
#         txtlog1.delete()
#         messagebox.showerror('User name', "your User name most more than 5 part")
#     if len(tpasslog)<2:
#         txtlog2.delete()
#         messagebox.showerror('Password', "your Password most more than 6 part") 
#     else:pass
def loginp1(event):
    read1()
    if 1==1:
        delilog()


def read1():
    pos1=txtlog3.get()
    if pos1=='Teacher':
        with open(r'usernameT.txt', 'r') as fp:
                lines = fp.readlines()
                file1=open('usernameT.txt')
                file2=file1.readlines()
                for row in lines:
                    tuserlog=txtlog1.get(1.0,'end-1c')
                    tpasslog=txtlog2.get(1.0,'end-1c')
                    word = tuserlog
                    if row.find(word) != -1:
                        oo=(lines.index(row))
                        linefind=file2[oo]
                        f1=linefind.find(' ',5)
                        nhowsave=linefind[5:f1]
                        if nhowsave==word:
                            f2=linefind.find('pass')
                            f22=linefind.find(':',f2)
                            f23=linefind.find(' ',f22)
                            passhowsaved=linefind[f22+1:f23]
                            if passhowsaved==tpasslog:
                                page6.tkraise()
                                delilog()
                                lbllog42.place(x=-840,y=450)
                                lbllog4.place(x=-840,y=450)
                                # lblinfop4.config(text=f'     user name:{tuserlog}')
                                lblnamep6u.config(text=f'        user name : {tuserlog}')
                                lblnamep6u.place(x=0,y=0)
                                lblnamep6u.tkraise()
                                # lblinfop4.tkraise()
                            else:
                                lbllog4.place(x=840,y=450)
                                lbllog4.tkraise()
                    else:
                        lbllog42.place(x=840,y=450)
                        lbllog42.tkraise()
    if pos1=='Student':
        with open(r'usernameS.txt', 'r') as fp:
                lines = fp.readlines()
                file1=open('usernameS.txt')
                file2=file1.readlines()
                for row in lines:
                    tuserlog=txtlog1.get(1.0,'end-1c')
                    tpasslog=txtlog2.get(1.0,'end-1c')
                    erorlog()
                    word = tuserlog
                    if row.find(word) != -1:
                        oo=(lines.index(row))
                        linefind=file2[oo]
                        f1=linefind.find(' ',5)
                        nhowsave=linefind[5:f1]
                        if nhowsave==word:
                            f2=linefind.find('pass')
                            f22=linefind.find(':',f2)
                            f23=linefind.find(' ',f22)
                            passhowsaved=linefind[f22+1:f23]
                            if passhowsaved==tpasslog:
                                page5.tkraise()
                                delilog() # type: ignore
                                lbllog42.place(x=-840,y=450)
                                lbllog4.place(x=-840,y=450)
                                lblinfop5.config(text=f'     user name : {tuserlog}')
                                lblinfop5.tkraise()
                            else:
                                lbllog4.place(x=840,y=450)
                                lbllog4.tkraise()
                    else:
                            lbllog42.place(x=840,y=450)     
                            lbllog42.tkraise()



# def forget():
#     tgf1=txtf1.get(1.0,'end-1c')
#     tgf2=txtf4.get(1.0,'end-1c')
#     tgf3=txtf5.get(1.0,'end-1c')
#     tgf4=txtf6.get(1.0,'end-1c')




################         page 3 codes
# def getall():
#     findtf1=txtf1.get(1.0,'end-1c')
#     findtf2=txtf4.get(1.0,'end-1c')
#     findtf3=txtf5.get(1.0,'end-1c')
#     findtf4=txtf6.get(1.0,'end-1c')
#     findtf5=txtf7.get()
def findfpage():
    findtf1=txtf1.get(1.0,'end-1c')
    findtf2=txtf4.get(1.0,'end-1c')
    findtf3=txtf5.get(1.0,'end-1c')
    findtf4=txtf6.get(1.0,'end-1c')
    findtf5=txtf7.get()
    if findtf5=='Teacher':
        with open(r'usernameT.txt', 'r') as fp:
                lines = fp.readlines()
                file1=open('usernameT.txt')
                file2=file1.readlines()
                for row in lines:
                    word = findtf1
                    if row.find(word) != -1:
                        oo=(lines.index(row))
                        linefind=file2[oo]
                        f1=linefind.find(' ',5)
                        nhowsave=linefind[5:f1]
                        if nhowsave==word:
                            f2=linefind.find('native')
                            f22=linefind.find(':',f2)
                            f23=linefind.find(' ',f22)
                            nativhowsave=linefind[f22+1:f23]
                            if nativhowsave==findtf2:
                                n2=linefind.find('number')
                                n22=linefind.find(':',n2)
                                n23=linefind.find(' ',n22)
                                numberhowsave=linefind[n22+1:n23]
                                if findtf3==numberhowsave:
                                    if findtf4=='123456789':
                                        p2=linefind.find('pass')
                                        p22=linefind.find(':',p2)
                                        p23=linefind.find(' ',p22)
                                        passhowsave=linefind[p22+1:p23]
                                        lblf7.config(text=passhowsave)
                                        lblf8.place(x=-495,y=650)
                                        delitf()
                                        page3_clear()
                                        lblf8.place(x=-495,y=650)
                                    else:
                                        lblnonfound1.place(x=-900,y=355)
                                        lblnonfound2.place(x=-900,y=405)
                                        lblnonfound3.place(x=-900,y=455)
                                        lblnonfound4.place(x=750,y=505)
                                        # messagebox.showerror('Invented Cod', "your Invented Cod is incorecct")
                                else:
                                    lblnonfound1.place(x=-900,y=355)
                                    lblnonfound2.place(x=-900,y=405)
                                    lblnonfound3.place(x=750,y=455)
                                    lblnonfound4.place(x=-900,y=505)
                                    # messagebox.showerror('Number', "Your number incorecct or not found")
                            else:
                                lblnonfound1.place(x=-900,y=355)
                                lblnonfound2.place(x=750,y=405)
                                lblnonfound3.place(x=-900,y=455)
                                lblnonfound4.place(x=-900,y=505)
                                # messagebox.showerror('Naitve Code', "Your Naitve code not found")
                        else:
                            lblnonfound1.place(x=750,y=355)
                            lblnonfound2.place(x=-900,y=405)
                            lblnonfound3.place(x=-900,y=455)
                            lblnonfound4.place(x=-900,y=505)
    elif findtf5=='Student':
        with open(r'usernameS.txt', 'r') as fp:
                lines = fp.readlines()
                file1=open('usernameS.txt')
                file2=file1.readlines()
                for row in lines:
                    word = findtf1
                    if row.find(word) != -1:
                        oo=(lines.index(row))
                        linefind=file2[oo]
                        f1=linefind.find(' ',5)
                        nhowsave=linefind[5:f1]
                        if nhowsave==word:
                            f2=linefind.find('native')
                            f22=linefind.find(':',f2)
                            f23=linefind.find(' ',f22)
                            nativhowsave=linefind[f22+1:f23]
                            if nativhowsave==findtf2:
                                n2=linefind.find('number')
                                n22=linefind.find(':',n2)
                                n23=linefind.find(' ',n22)
                                numberhowsave=linefind[n22+1:n23]
                                if findtf3==numberhowsave:
                                    if findtf4=='987654321':
                                        p2=linefind.find('pass')
                                        p22=linefind.find(':',p2)
                                        p23=linefind.find(' ',p22)
                                        passhowsave=linefind[p22+1:p23]
                                        lblf7.config(text=passhowsave)
                                        delitf()
                                        page3_clear()
                                        lblf8.place(x=-495,y=650)
                                    else:
                                        lblnonfound1.place(x=-900,y=355)
                                        lblnonfound2.place(x=-900,y=405)
                                        lblnonfound3.place(x=-900,y=455)
                                        lblnonfound4.place(x=750,y=505)
                                        # messagebox.showerror('Invented Cod', "your Invented Cod is incorecct")
                                else:
                                    lblnonfound1.place(x=-900,y=355)
                                    lblnonfound2.place(x=-900,y=405)
                                    lblnonfound3.place(x=750,y=455)
                                    lblnonfound4.place(x=-900,y=505)
                                    # messagebox.showerror('Number', "Your number incorecct or not found")
                            else:
                                lblnonfound1.place(x=-900,y=355)
                                lblnonfound2.place(x=750,y=405)
                                lblnonfound3.place(x=-900,y=455)
                                lblnonfound4.place(x=-900,y=505)
                                # messagebox.showerror('Naitve Code', "Your Naitve code not found")
                        else:
                            lblnonfound1.place(x=750,y=355)
                            lblnonfound2.place(x=-900,y=405)
                            lblnonfound3.place(x=-900,y=455)
                            lblnonfound4.place(x=-900,y=505)
                    
def haid(event):
    lblf8.place(x=495,y=650)
    lblf8.tkraise()                   
def page3_clear():
    lblnonfound1.place(x=-900,y=355)
    lblnonfound2.place(x=-900,y=355)
    lblnonfound3.place(x=-900,y=355)
    lblnonfound4.place(x=-900,y=355)
    lblf8.place(x=495,y=650)
    lblf8.tkraise()



# #  teacher page4
# def page4s(event):
#     lbls1.config(bg='#A70050',fg='white')
#     lblt2.config(bg='#97FFFF',fg='#DC143C')
#     lblm.config(bg='#97FFFF',fg='#DC143C')
#     bs1.place(x=1640,y=95)
#     bs2.place(x=1640,y=125)
#     bs3.place(x=1640,y=155)
#     bs4.place(x=1640,y=185)
#     bs1.tkraise()
#     bs2.tkraise()
#     bs3.tkraise()
#     bs4.tkraise()
# def page4t(event):
#     lbls1.config(bg='#97FFFF',fg='#DC143C')
#     lblt2.config(bg='#A70050',fg='white')
#     lblm.config(bg='#97FFFF',fg='#DC143C')
#     bt1.place(x=1640,y=95)
#     bt2.place(x=1640,y=125)
#     bt3.place(x=1640,y=155)
#     bt4.place(x=1640,y=185)
#     bt1.tkraise()
#     bt2.tkraise()
#     bt3.tkraise()
#     bt4.tkraise()
# def page4m(event):
#     lbls1.config(bg='#97FFFF',fg='#DC143C')
#     lblt2.config(bg='#97FFFF',fg='#DC143C')
#     lblm.config(bg='#A70050',fg='white')    
#     bm1.place(x=1640,y=95)
#     bm2.place(x=1640,y=125)
#     bm3.place(x=1640,y=155)
#     bm4.place(x=1640,y=185)
#     bm1.tkraise()
#     bm2.tkraise()
#     bm3.tkraise()
#     bm4.tkraise()


#student page 5
def page4s2(event):
    lbls21.config(bg='#A70050',fg='white')
    # lblt2.config(bg='#97FFFF',fg='#DC143C')
    lblm2.config(bg='#97FFFF',fg='#DC143C')
    bs21.place(x=1640,y=95)
    bs22.place(x=1640,y=125)
    bs23.place(x=1640,y=155)
    bs24.place(x=1640,y=185)
    bs21.tkraise()
    bs22.tkraise()
    bs23.tkraise()
    bs24.tkraise()

def page4m2(event):
    lbls21.config(bg='#97FFFF',fg='#DC143C')
    # lblt2.config(bg='#97FFFF',fg='#DC143C')
    lblm2.config(bg='#A70050',fg='white')    
    bm21.place(x=1640,y=95)
    bm22.place(x=1640,y=125)
    bm23.place(x=1640,y=155)
    bm24.place(x=1640,y=185)
    bm21.tkraise()
    bm22.tkraise()
    bm23.tkraise()
    bm24.tkraise()


def rimbut(x,y,z,q,e):
    x.place(x=-9000,y=-9000)
    y.place(x=-9000,y=-9000)
    z.place(x=-9000,y=-9000)
    q.place(x=-9000,y=-9000)
    e.place(x=-9000,y=-9000)
    # t.place(x=-900,y=-900)اگه نیاز به فعال شدن داشت چند جای دیگه باید ترش (همون لیبل اضافی )اظاف کنی 
def chengcolor(L,B,C,D,F):
    L.config(bg='#A70050',fg='white')
    B.config(bg='#97FFFF',fg='#DC143C')
    C.config(bg='#97FFFF',fg='#DC143C')
    D.config(bg='#97FFFF',fg='#DC143C')
    F.config(bg='#97FFFF',fg='#DC143C')

def chengbackcolor(l):
    l.config(bg='#97FFFF',fg='#DC143C')

# ######  page6

def p6txtn():
    rimbut(listp6,bp6sho,bp6shr,lblp6sl,trash)
    txtp6A.place(x=1300,y=100)
    lblp6nf.place(x=1150,y=98)
    bp6sa.place(x=1530,y=98)

def p6xtc():
    rimbut(txtp6A,lblp6nf,bp6sa,trash,trash)
    listp6.place(x=1350,y=125)
    bp6sho.place(x=1530,y=128)
    bp6shr.place(x=1530,y=168)
    lblp6sl.place(x=1230,y=125)

# تغییرات دکمه ها 

def page6ts(event):
    chengcolor(lblti1,lblti2,lblti3,lblti4,lblti5)
    rimbut(listp6A,bp6aa,bp6aa2,txtp6aa,lblp6asn)
    rimbut(listp6R,bp6aR,Canp6br,listnamep6R,Bcanp6r2)
    rimbut(cbp6s1,cbp6s2,lblp6asnr,cbp6s3,Bcanp6r)
    rimbut(listp6S,bp6aS,trash,trash,trash)
    rimbut(listp6p,bp6ap,Canp6bp,cbp6s3p,Bcanp6rp)
    rimbut(cbp6s1p,cbp6s2p,Bcanp6r2p,trash,trash)
    btisarA1.place(x=1640,y=95)
    btisarA2.place(x=1640,y=125)

def page6t1(event):
    chengcolor(lblti2,lblti1,lblti3,lblti4,lblti5)
    rimbut(bp6sho,bp6shr,btisarA1,btisarA2,listp6A)
    rimbut(bp6sa,txtp6A,listp6,lblp6nf,lblp6sl)
    rimbut(listp6A,bp6aa,bp6aa2,txtp6aa,lblp6asn)
    rimbut(listp6S,bp6aS,trash,trash,trash)
    rimbut(listp6p,bp6ap,Canp6bp,cbp6s3p,Bcanp6rp)
    rimbut(cbp6s1p,cbp6s2p,Bcanp6r2p,listnamp6p,trash)
    listp6R.place(x=txR,y=129)
    bp6aR.place(x=1600,y=130)
    motip6R()
    # listp6A.configure(width=1)
    

def page6t2(event):
    chengcolor(lblti3,lblti2,lblti1,lblti4,lblti5)
    rimbut(bp6sho,bp6shr,btisarA1,btisarA2,Bcanp6r2)
    rimbut(bp6sa,txtp6A,listp6,lblp6nf,lblp6sl)
    rimbut(listp6R,bp6aR,lblp6asnr,Canp6br,listnamep6R)
    rimbut(cbp6s1,cbp6s2,trash,cbp6s3,Bcanp6r)
    rimbut(listp6S,bp6aS,trash,trash,trash)
    rimbut(listp6p,bp6ap,Canp6bp,cbp6s3p,Bcanp6rp)
    rimbut(cbp6s1p,cbp6s2p,Bcanp6r2p,listnamp6p,trash)
    listp6A.place(x=tx,y=129)
    bp6aa.place(x=bxa,y=130)
    motip6A()

def page6t4(event):
    chengcolor(lblti4,lblti3,lblti2,lblti1,lblti5)
    rimbut(bp6sho,bp6shr,btisarA1,btisarA2,Bcanp6r2)
    rimbut(bp6sa,txtp6A,listp6,lblp6nf,lblp6sl)
    rimbut(listp6R,bp6aR,lblp6asnr,Canp6br,listnamep6R)
    rimbut(cbp6s1,cbp6s2,lblp6asnr,cbp6s3,Bcanp6r)
    rimbut(listp6A,bp6aa,bp6aa2,txtp6aa,lblp6asn)
    rimbut(listp6p,bp6ap,Canp6bp,cbp6s3p,Bcanp6rp)
    rimbut(cbp6s1p,cbp6s2p,listnamp6p,Bcanp6r2p,trash)
    listp6S.place(x=txS,y=129)
    bp6aS.place(x=1600,y=130)
    motip6S()

def page6t5(event):
    chengcolor(lblti5,lblti3,lblti2,lblti1,lblti4)
    rimbut(bp6sho,bp6shr,btisarA1,btisarA2,Bcanp6r2)
    rimbut(bp6sa,txtp6A,listp6,lblp6nf,lblp6sl)
    rimbut(listp6R,bp6aR,lblp6asnr,Canp6br,listnamep6R)
    rimbut(cbp6s1,cbp6s2,lblp6asnr,cbp6s3,Bcanp6r)
    rimbut(listp6A,bp6aa,bp6aa2,txtp6aa,lblp6asn)
    rimbut(listp6S,bp6aS,trash,trash,trash)
    
    listp6p.place(x=txp,y=129)
    bp6ap.place(x=1600,y=130)
    motip6p()



def EmergenciR(event):
    rimbut(listp6A,bp6aa,listp6R,bp6aR,trash)
    rimbut(listp6R,bp6aR,listp6p,listp6S,bp6aS)

    # rimbut(bp6ap,trash,trash,trash,trash)
def EmergenciR2(event):
    rimbut(listp6R,bp6aR,listp6p,listp6S,bp6aS)
    rimbut(bp6ap,trash,trash,trash,trash)
def EmergenciR3(event):
    rimbut(bp6ap,bp6aS,listp6p,listp6S,listp6A)
    rimbut(bp6aa,trash,trash,trash,trash)
def EmergenciR4(event):
    rimbut(listp6A,bp6aa,listp6R,bp6aR,trash)
    rimbut(listp6R,bp6aR,listp6p,trash,trash)

def bp6aad():# باید تغییر کنه تا کاربر یکی از لیست را انتخاب نکند اجرا نشود
    try:
        listp6A.get(listp6A.curselection())
         
        bp6aa2.place(x=1310,y=130)
        txtp6aa.place(x=1100,y=133)
        lblp6asn.config(text='Student name :',width=20,fg='gray10',bg='#FFD39B')  
        lblp6asn.place(x=900,y=132)
    except:
        lblp6asn.config(text='chose a file ❌',width=15,fg='red',bg='#7FFFD4')        
        lblp6asn.place(x=1200,y=132)
        

        

def bp6aa2d():
    delit_txt(txtp6aa)
    global lmy
    global lmy2
    global mtim
    lmy=-20
    lmy2=50
    mtim=1 
    masigsec()
def bp6aa2dB(event):
    delit_txt(txtp6aa)
    global lmy
    global lmy2
    global mtim
    lmy=-20
    lmy2=50
    mtim=1 
    masigsec()


#
#
# ⭕
#
# انمیشن موقت 
def motip6A():
    global tx
    global bxa
    global widthA
    w.after(1,motip6A)
    if tx>1400:
        tx-=5
        bxa-=4
        listp6A.place(x=tx,y=129)
        if bxa>1600:bp6aa.place(x=bxa,y=130)
        else:bp6aa.place(x=1600,y=130)
    if tx<1700:
        if tx %15==0:    
            widthA+=1
            if widthA<25:
                listp6A.configure(width=widthA)

def motip6p():
    global txp
    global bxp
    global widthp
    w.after(1,motip6p)
    if txp>1400:
        txp-=5
        bxp-=4
        listp6p.place(x=txp,y=129)
        if bxp>1600:bp6ap.place(x=bxp,y=130)
        else:bp6ap.place(x=1600,y=130)
    if txp<1700:
        if txp%15==0:
            widthp+=1
            if widthp<22:
                listp6p.configure(width=widthp)

def motip6S():
    global txS
    global bxS
    global widthS
    w.after(10,motip6S)
    if txS>1400:
        txS-=5
        bxS-=4
        listp6S.place(x=txS,y=129)
        if bxS>1602:bp6aS.place(x=bxS,y=130)
        else:bp6aS.place(x=1602,y=130)
    if txS<1700:
        if txS%5==0:
            widthS+=1
            if widthS<22:
                listp6S.configure(width=widthS)
    # motionp6(listp6S,bp6aS)
def motip6R():
    global txR
    global bxR
    global widthR
    w.after(1,motip6R)
    if txR>1400:
        txR-=5
        bxR-=4
        listp6R.place(x=txR,y=129)
        if bxR>1600:bp6aR.place(x=bxR,y=130)
        else:bp6aR.place(x=1600,y=130)
    if txR<1700:
        if txR%5==0:
            widthR+=1
            if widthR<22:
                listp6R.configure(width=widthR)
    # motionp6(listp6R,bp6aR)
     
# def masigsec(l1):
    
#     w.after(1,masigsec)
#     if l1<=50:
#         l1+=2
#         lblp6massec.place(x=900,y=l1)
#     if l1==50:
#         masigsec2()
def masigsec():
    global lmy
    w.after(10,masigsec)
    if lmy >-21:
        if lmy<=50:
            lmy+=2
            lblp6massec.place(x=900,y=lmy)
        if lmy==50:
            masigsec2()
        if lmy==50:
            if lmy>-20:
                lmy-=80
            # quit() 
            # return 'none()'
def masigsec2():
    global lmy2
    global mtim
    global lmy
    if mtim>0:
        w.after(10,masigsec2)
        if mtim<500:
            mtim+=2
        if mtim>195:
                if lmy2>-30:
                    lmy2-=2
                    lblp6massec.place(x=900,y=lmy2)
                    if lmy2<-25:
                        lmy2+=90
                        mtim-=700

def canp6D():
    try:
        listnamep6r=listp6R.get(listp6R.curselection())
        if len(listnamep6r)>16:listnamep6R.config(text=listnamep6r,width=22)
        else:listnamep6R.config(text=listnamep6r,width=20)
        listnamep6R.place(x=750,y=52)
        listnamep6R.tkraise()
        Canp6br.place(x=50,y=50)
        cbp6s1.place(x=63,y=63)
        cbp6s2.place(x=63,y=93)
        cbp6s3.place(x=63,y=123)
        Bcanp6r.place(x=1029,y=55)
        lblp6asnr.place(x=-1000,y=132)
        Bcanp6r2.place(x=944,y=924)
        Bcanp6r2.tkraise()
    except:
        lblp6asnr.config(text='chose a file ❌',width=15,fg='red',bg='#7FFFD4')        
        lblp6asnr.place(x=1200,y=132)


def canp6pD():
    try:
        listnamep6P=listp6p.get(listp6p.curselection())
        if len(listnamep6P)>16:listnamp6p.config(text=listnamep6P,width=22)
        else:listnamp6p.config(text=listnamep6P,width=20)
        listnamp6p.place(x=750,y=52)  
        listnamp6p.tkraise()
        Canp6bp.place(x=50,y=50)
        cbp6s1p.place(x=63,y=63)
        cbp6s2p.place(x=63,y=93)
        cbp6s3p.place(x=63,y=123)
        Bcanp6rp.place(x=1029,y=55)
        lblp6asnr.place(x=-1000,y=132)
        Bcanp6r2p.place(x=944,y=924)
    except:
        lblp6asnr.config(text='chose a file ❌',width=15,fg='red',bg='#7FFFD4')        
        lblp6asnr.place(x=1200,y=132)
        
def bcanp6D():
    rimbut(cbp6s1,cbp6s2,Canp6br,cbp6s3,Bcanp6r)
    rimbut(listnamep6R,Bcanp6r2,Canp6br,cbp6s3,trash)
    rimbut(cbp6s1p,cbp6s2p,Canp6bp,cbp6s3p,Bcanp6rp)
    rimbut(listnamep6R,Bcanp6r2p,Canp6bp,cbp6s3p,listnamp6p)
    



def lip6s():
    pass
#               

# ⭕














#
###
######
#########                                                                                   
############################   #     #####################                        ####                       #### 
#############################  ##  #    ######################                  #########                 ############
#####################          ###   ##      ####################           #################       #######################
####################           ###    ####       ###################      #####################  #############################
####################           ###     ####          ################      ##################################################
####################           ###     ####             ###########          #############################################
####################           ###    ####           ############               ######################################
####################           ###   ####        ##############                    ################################
#####################          ###  ##       ################                         ##########################
#############################  ##   #   ###################                                #################
############################   #     ###################                                       ##########
########                                                                                          #####
#####                                                                                               #
###
#

#  it's just trash
#########################################################
############################ fangshens




############################  Frames

page1=Frame(w)
page2=Frame(w)
page3=Frame(w)
page4=Frame(w)
page5=Frame(w)
page6=Frame(w)
page7=Frame(w)


page1.grid( row=0 , column=0, sticky='nsew' ) 
page2.grid(row=0 , column=0 ,sticky='nsew')
page3.grid(row=0, column=0,sticky='nsew')
page4.grid(row=0, column=0,sticky='nsew')
page5.grid(row=0, column=0,sticky='nsew')
page6.grid(row=0, column=0,sticky='nsew')
page7.grid(row=0, column=0,sticky='nsew')

# با صفر گذاشتن پد ایکس و ایگرگ از گوشه شروع به چیدن میکند 
page1.config(padx=0 ,pady=0 )
page2.config(padx=9500 ,pady=500 )
# برای پیج سوم نیازی نیود حداقل تا الان سعی کن استفاده نکنی یکم اذیت میکنه خیلی اذیت میکنه
# page3.config(bg='black',padx=500 , pady=500)

# photo
frame = Frame(page1, width=600, height=1000)
frame2=Frame(page2, width=600, height=1000)
frame3=Frame(page3, width=600, height=1000)
frame4=Frame(page4, width=600, height=1000)
frame5=Frame(page5, width=600, height=1000)
frame6=Frame(page6, width=600, height=1000)
frame7=Frame(page7, width=600, height=1000)
frame.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
frame7.pack()
# برای آوردن عکس به وسط از ریل ایکس و
# برای فیکس عکس از اینجا استفاده کنید
frame.place(anchor='center', relx=0.462, rely=0.4529)
frame2.place(anchor='center', relx=0.135, rely=0.005)
frame3.place(anchor='center', relx=0.486, rely=0.490)
frame4.place(anchor='center', relx=0.486, rely=0.490)
frame5.place(anchor='center', relx=0.486, rely=0.490)
frame6.place(anchor='center', relx=0.486, rely=0.490)
frame7.place(anchor='center', relx=0.486, rely=0.490)

# frame.lift()
 
label1 = Label(frame, image = img)
label1.pack(fill=BOTH)
label2 = Label(frame2, image = img)
label2.pack(fill=BOTH)
label3 = Label(frame3, image = img)
label3.pack(fill=BOTH)
label4 = Label(frame4, image = img)
label4.pack(fill=BOTH)
label5 = Label(frame5, image = img)
label5.pack(fill=BOTH)
label6 = Label(frame6, image = img)
label6.pack(fill=BOTH)
label7 = Label(frame7, image = img)
label7.pack(fill=BOTH)



#  trash
trash=Label(page1)
trash.place(x=-9000,y=-9000)




####################################################
################################## ⭕ page 1 ######
####################################################

# label
lbllog=Label(page1,text='In the name of God',foreground='black' ,background='red',font=('April 30 '))
lbllog.place(x=760 ,y=0)
lbllog1=Label(page1,text=' User name :',fg='red',bg='black',font=('April 10 bold italic'))
lbllog1.place(x=765 ,y=350)
lbllog2=Label(page1,text=' Password :',fg='red',bg='black',font=('April 10 bold italic'))
lbllog2.place(x=765 ,y=380)
lbllog3=Label(page1,text='''didn't have                 ?''',bg='#D6D6D6', fg='red',font=('April 15 bold italic' ))
lbllog3.place(x=1650 ,y=950)
lbllog4=Label(page1,text='pass word incorecct',width=17,fg='#FF3030',bg='#363636',font=('April 15 bold italic'))
lbllog42=Label(page1,text='user name not found',width=17,fg='#FF3030',bg='#363636',font=('April 15 bold italic'))
lbllog5=Label(page1,text='your position? *',bg='black' ,fg='red',font=('April 10 bold italic'))
lbllog5.place(x=765,y=420)

# Button
blog1=Button(page1,text='log in',bg='#C7C7C7',fg='red',width=20,font=('April 15 '),cursor='hand2' ,relief='groove',bd=3,command=lambda:[read1()])
blog1.place(x=830 ,y=500)
blog2=Button(page1,text='sign up',bg='#D6D6D6',fg='blue',font=('April 10 '),width=5,activebackground='#00B2EE',activeforeground='red',cursor='hand2',command=lambda:[page2.tkraise(),delilog(),riplog()],relief='flat')
blog2.place(x=1780 ,y=950)
blog3=Button(page1,text='forget your password', bg='#D6D6D6',fg='blue',font=('April 10 bold'),width=20,activebackground='#00B2EE',activeforeground='red',cursor='hand2',command=lambda:[page3.tkraise(),delilog(),riplog()],relief='groove',bd=3)
blog3.place(x=865 ,y=600)


# text

txtlog1=Text(page1 ,fg='black',bg='#8F8F8F',font=15, width=20,height=1)
txtlog1.place(x=870,y=350)
txtlog2=Text(page1 ,fg='#0000CD',bg='#8F8F8F',font=15, width=20,height=1)
txtlog2.place(x=870,y=380)
txtlog3=ttk.Combobox(page1,width=27,background='#8F8F8F',foreground='#0000CD')
txtlog3['value']=('Teacher','Student')
txtlog3.config(state='readonly')
txtlog3.current(1)
txtlog3.place(x=870,y=420)


####################################################
################################## ⭕ page 2 ######
####################################################


# label
lblsign1=Label(page2,text=' User name : *',fg='red',bg='black',font=('April 10 bold italic'))
lblsign1.place(x=-220 ,y=-200)
lblsign2=Label(page2,text=' Password : *',fg='red',bg='black',font=('April 10 bold italic'))
lblsign2.place(x=-220 ,y=-150)
lblsign3=Label(page2,text='Your age ?',bg='black' ,fg='red',font=('April 10 bold italic') )
lblsign3.place(x=-220,y=-50)
lblsign4=Label(page2,text='National Code? *',bg='black' ,fg='red',font=('April 10 bold italic') )
lblsign4.place(x=-220,y=50)
lblsign5=Label(page2,text='Your number? *',bg='black' ,fg='red',font=('April 10 bold italic') )
lblsign5.place(x=-220,y=-0)
lblsign6=Label(page2,text='Invented code? *',bg='black' ,fg='red',font=('April 10 bold italic') )
lblsign6.place(x=-220,y=-100)
lblsign7=Label(page2,text='your position? *',bg='black' ,fg='red',font=('April 10 bold italic'))
lblsign7.place(x=-220,y=100)


# Button

b2=Button(page2, text='')
b2.grid(row=1, column=1, sticky='nsew')
b3=Button(page2,text='you can sign in now ' , command=lambda:[tiyp()],width=20, bg='#104E8B',fg='white',font=('April 10 bold italic'))
b3.place(x=-100 ,y=200)
bback=Button(page2,text='back to start page' , command=lambda:[page1.tkraise(),delisign()],width=17, bg='#A70050',fg='white',font=('April 10 bold italic'))
bback.place(x=-86,y=250)
# text
txtsige1=Text(page2 ,fg='black',bg='#8F8F8F',font=10, width=20,height=1)
txtsige1.place(x=-90,y=-200)

txtsige2=Text(page2 ,fg='#0000CD',bg='#8F8F8F',font=15, width=20,height=1)
txtsige2.place(x=-90,y=-150)

txtsige3=ttk.Combobox(page2 ,width=27,background='#8F8F8F',foreground='#0000CD')
txtsige3['value']=list(range(17,99))
txtsige3.config(state='readonly')
txtsige3.place(x=-90,y=-50)

txtsige4=Text(page2 ,fg='#0000CD',bg='#8F8F8F',font=15, width=20,height=1)
txtsige4.place(x=-90,y=50)

txtsige5=Text(page2 ,fg='#0000CD',bg='#8F8F8F',font=15, width=20,height=1)
txtsige5.place(x=-90,y=0)

txtsige6=Text(page2 ,fg='#0000CD',bg='#8F8F8F',font=15, width=20,height=1)
txtsige6.place(x=-90,y=-100)


txtsign7=ttk.Combobox(page2,width=27,background='#8F8F8F',foreground='#0000CD')
txtsign7['value']=['Teacher','Student']
txtsign7.current(0)
txtsign7.config(state='readonly')
txtsign7.place(x=-90,y=100)











####################################################
################################## ⭕ page 3 ######
####################################################

# label

lblf1=Label(page3,text=' User name :',fg='red',bg='black',font=('April 10 bold italic'))
lblf1.place(x=350 ,y=350)
lblf4=Label(page3,text='National Code ?',bg='black' ,fg='red',font=('April 10 bold italic') )
lblf4.place(x=350,y=400)
lblf5=Label(page3,text='Your number ?',bg='black' ,fg='red',font=('April 10 bold italic') )
lblf5.place(x=350,y=450)
lblf6=Label(page3,text='Invented code ?',bg='black' ,fg='red',font=('April 10 bold italic') )
lblf6.place(x=350,y=500)
lblf7=Label(page3,text='your pass word',bg='black' ,fg='red',font=('April 10 bold italic') )
lblf7.place(x=495,y=650)
lblf8=Label(page3,text='your pass word',bg='black' ,fg='red',font=('April 10 bold italic') )

lblnonfound1=Label(page3,text='❌ your username not found',bg='#98F5FF' ,fg='red',font=('April 10 bold italic') )
lblnonfound2=Label(page3,text='❌ Your Naitve code not found',bg='#98F5FF' ,fg='red',font=('April 10 bold italic') )
lblnonfound3=Label(page3,text='❌Your number incorecct or not found',bg='#98F5FF' ,fg='red',font=('April 10 bold italic') )
lblnonfound4=Label(page3,text='❌ your Invented Cod is incorecct',bg='#98F5FF' ,fg='red',font=('April 10 bold italic') )

imoje=Label(page3,text='⏩',height=1,bg='#98F5FF',fg='red',font=('April 15 bold'))
bx=-50
imoje.place(x=bx,y=697)
imoje2=Label(page3,text='⏪',height=1,bg='#98F5FF',fg='red',font=('April 15 bold'))
bx2=-50
imoje2.place(x=bx,y=697)

# text
txtf1=Text(page3 ,fg='black',bg='#8F8F8F',font=10, width=20,height=1)
txtf1.place(x=480,y=350)
txtf4=Text(page3 ,fg='black',bg='#8F8F8F',font=10, width=20,height=1)
txtf4.place(x=480,y=400)
txtf5=Text(page3 ,fg='black',bg='#8F8F8F',font=10, width=20,height=1)
txtf5.place(x=480,y=450)
txtf6=Text(page3 ,fg='black',bg='#8F8F8F',font=10, width=20,height=1)
txtf6.place(x=480,y=500)
txtf7=ttk.Combobox(page3,width=25)
txtf7['value']=['Teacher','Student']
txtf7.current(0)
txtf7.config(state='readonly')
txtf7.place(x=480,y=550)



# Butten
bf1=Button(page3,text='Code recovery',command=lambda:[findfpage()],width=13,bg='#104E8B',fg='white',font=('April 10 bold italic'))
bf1.place(x=490 ,y=600)
bf2=Button(page3,text='Finish' , command=lambda:[page1.tkraise(),reipmotion(),page3_clear()],width=10, bg='#A70050',fg='white',font=('April 10 bold italic'))
bf2.place(x=505 ,y=700)
# پک کردن این را داخل فانگشن بذار 
# داخل فانشن کانفیگ تکست را تغییر بده

# bf3=ttk.Button(page3,text='BACK' , command=lambda:[page1.tkraise()])

# bf3.place(x=555 ,y=700)





####################################################
################################## ⭕ page 4 ######
####################################################

###############################   Labels

# lbls1=Label(page4,text='Student',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
# lbls1.place(x=1780,y=130)
# lblt2=Label(page4,text='Techers',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
# lblt2.place(x=1780,y=100)
# lblm=Label(page4,text='More',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
# lblm.place(x=1780,y=160)
# lblinfop4=Label(page4,text='',bg='#76EE00',fg='#030303',font=('April 12 bold italic'),width=22)
# lblinfop4.place(x=0,y=0)


# ##############################    Buttons

# bs1=Button(page4,text='Accunt' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bs2=Button(page4,text='Lessons' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bs3=Button(page4,text='Scores' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bs4=Button(page4,text='Presents' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))

# bt1=Button(page4,text='Edit students' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'),command=lambda:[page6.tkraise()])
# bt2=Button(page4,text='Remove student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bt3=Button(page4,text='Scours student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bt4=Button(page4,text='Presents student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))

# bm1=Button(page4,text='About' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bm2=Button(page4,text='Log out' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bm3=Button(page4,text='Chenge pass word' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
# bm4=Button(page4,text='Back' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))



####################################################
################################## ⭕ page 5 ######
####################################################



################################  Labels

lbls21=Label(page5,text='Student',width=15, cursor='hand2',bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lbls21.place(x=1780,y=100)
# lblt22=Label(page5,text='Techers',width=15, bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
# lblt22.place(x=1780,y=130)
lblm2=Label(page5,text='More',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblm2.place(x=1780,y=130)
lblinfop5=Label(page5,text='',bg='#76EE00',fg='#030303',font=('April 12 bold italic'),width=22)
lblinfop5.place(x=0,y=0)
# Buttens


##############################    Buttons

bs21=Button(page5,text='Accunt' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bs22=Button(page5,text='Lessons' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bs23=Button(page5,text='Scores' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bs24=Button(page5,text='Presents' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))

bt21=Button(page5,text='Add student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bt22=Button(page5,text='Remove student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bt23=Button(page5,text='Scours student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bt24=Button(page5,text='Presents student' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))

bm21=Button(page5,text='About' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bm22=Button(page5,text='Log out' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bm23=Button(page5,text='Chenge pass word' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))
bm24=Button(page5,text='Back' ,width=15, bg='#104E8B',fg='white',font=('April 10 bold italic'))








####################################################
################################## ⭕ page 6 ######
####################################################

####   labes


lbltita=Label(page6,text='Edit students',width=20,bg='#97FFFF',fg='#DC143C',font=('ScriptMTBold 10 bold italic'))#تغییر رنگ و حالت نیاز دارد به عنوان تایتل 
lbltita.place(x=1750,y=0)

lblti1=Label(page6,text='Show',width=15, cursor='hand2',bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblti1.place(x=1780,y=100)
lblti2=Label(page6,text='Remove',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblti2.place(x=1780,y=160)
lblti3=Label(page6,text='Add',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblti3.place(x=1780,y=130)
lblti4=Label(page6,text='sccures',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblti4.place(x=1780,y=190)
lblti5=Label(page6,text='presence',width=15, cursor='hand2', bg='#97FFFF',fg='#DC143C',font=('April 10 bold italic'))
lblti5.place(x=1780,y=220)
lblnamep6u=Label(page6,text='',bg='#76EE00',fg='#030303',font=('April 12 bold italic'),width=22)


lblinfop6=Label(page6,text='',bg='#76EE00',fg='#030303',font=('April 12 bold italic'),width=22)
lblinfop6.place(x=0,y=0)

####click Labels
lblp6nf=Label(page6,text='Name of new file :',width=15,bg='#7FFFD4',font=('April 11 bold italic'),fg='#0000CD')
lblp6sl=Label(page6,text='Your list :',width=10,bg='#7FFFD4',font=('April 11 bold italic'),fg='#0000CD')
lblp6aa=Label(page6,text='Your list :',width=10,bg='#7FFFD4',font=('April 11 bold italic'),fg='#0000CD')
lblp6asn=Label(page6,text='Student name :',width=20,bg='#7FFFD4',font=('April 11 bold italic'),fg='#0000CD')
lblp6asnr=Label(page6,text='chose a file ❌',width=15,bg='#7FFFD4',font=('April 11 bold italic'),fg='red')
listnamep6R=Label(page6,text='',fg='gray10',width=20,bg='gray85',font=('Algerian 13 bold italic'))
listnamp6p=Label(page6,text='',fg='gray10',width=20,bg='gray85',font=('Algerian 13 bold italic'))

# lmx=
lblp6massec=Label(page6,text='Add successful',width=20,bg='#7FFF00',font=('Algerian 13 bold italic'),fg='#050505',relief='groove',bd=3)
lblp6massecn=Label(page6,text='Add unsuccessful',width=20,bg='red',font=('Algerian 13 bold italic'),fg='#050505',relief='groove',bd=3)
# lblp6massecn.place(x=120,y=300)
#### Buttons

btisarA1=Button(page6,text='New file' ,width=15,cursor='hand2', bg='#104E8B',fg='white',font=('April 10 bold italic'),command=lambda:[p6txtn()])
btisarA2=Button(page6,text='File list' ,width=15,cursor='hand2', bg='#104E8B',fg='white',font=('April 10 bold italic'),command=lambda:[p6xtc()])
#click Buttons
bp6sa=Button(page6,text='Save' ,width=10,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'))
# برای سیو یک مسیج باکس آیا مطمئن هستید بذار اگه یس بود اوکی کن
bp6sho=Button(page6,text='Open' ,width=10,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'))
bp6shr=Button(page6,text='Remove' ,width=10,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'))
bp6aa=Button(page6,text='Add student' ,width=10,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'),command=lambda:[bp6aad()])
bp6aa2=Button(page6,text='➕' ,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'),command=lambda:[bp6aa2d()])#با زدن این یا اینتر باکس پاک بشه و اسم به لیست اظاف بشه 
bp6aR=Button(page6,text='Remove student' ,width=14,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'),command=lambda:[canp6D()])
bp6aS=Button(page6,text='select file' ,width=14,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'),command=lambda:[])
bp6ap=Button(page6,text='chose a file' ,width=14,cursor='hand2', bg='#800000',fg='gray98',font=('April 10 bold italic'),command=lambda:[canp6pD()])

#   texts
txtp6A=Text(page6,width=25,height=1,font=('BodoniMT 10 bold italic'))
txtp6aa=Text(page6,width=28,height=1,font=('BodoniMT 10 bold italic'))

######   listbox
itemoflb=['milad sh alsdl','asdjfas']
widthA=widthS=widthp=widthR=1
txp=txS=txR=tx=1780
bxS=bxR=bxa=bxp=1900

listp6=Listbox(page6,bg='gray60',width=18,relief='sunken',bd=1,font=('April 13 bold'),fg='gray30',activestyle='none')
for each_item in range(len(itemoflb)):listboxes(listp6)

listp6A=Listbox(page6,bg='gray60',width=widthA,relief='sunken',bd=1,font=('April 13 bold'),fg='gray30',activestyle='none')
for each_item in range(len(itemoflb)):listboxes(listp6A)

listp6R=Listbox(page6,bg='gray60',width=widthR,relief='sunken',bd=1,font=('April 13 bold'),fg='gray30',activestyle='none')
for each_item in range(len(itemoflb)):listboxes(listp6R)

listp6S=Listbox(page6,bg='gray60',width=widthS,relief='sunken',bd=1,font=('April 13 bold'),fg='gray30',activestyle='none')
for each_item in range(len(itemoflb)):listboxes(listp6S)

listp6p=Listbox(page6,bg='gray60',width=widthp,relief='sunken',bd=1,font=('April 13 bold'),fg='gray30',activestyle='none')
for each_item in range(len(itemoflb)):listboxes(listp6p)


Canp6br=Canvas(page6,width=1005,height=905,bg='gray85')
c1p6l1=Canp6br.create_line(10,10,975,10,975,35,1000,35,1000,870,889,870,889,900,10,900,10,10)
c1p6l1=Canp6br.create_line(8,8,973,8,973,33,998,33,998,868,887,868,887,898,8,898,8,8)
cbp6s1=Checkbutton(page6,text='student 1',bg='gray85',activebackground='gray85')
cbp6s2=Checkbutton(page6,text='student 2',bg='gray85',activebackground='gray85')
cbp6s3=Checkbutton(page6,text='student 3',bg='gray85',activebackground='gray85')
Bcanp6r=Button(page6,text='❌',bg='gray85',fg='red',activebackground='red',activeforeground='gray10',command=lambda:[bcanp6D()])
Bcanp6r2=Button(page6,text='Remove',bg='gray85',fg='red',activebackground='red',activeforeground='gray10',width=12,font=('April 10 bold italic'))


Canp6bp=Canvas(page6,width=1005,height=905,bg='gray85')
c1p6l1p=Canp6bp.create_line(10,10,975,10,975,35,1000,35,1000,870,889,870,889,900,10,900,10,10)
c1p6l1p=Canp6bp.create_line(8,8,973,8,973,33,998,33,998,868,887,868,887,898,8,898,8,8)
cbp6s1p=Checkbutton(page6,text='student 1',bg='gray85',activebackground='gray85')
cbp6s2p=Checkbutton(page6,text='student 2',bg='gray85',activebackground='gray85')
cbp6s3p=Checkbutton(page6,text='student 3',bg='gray85',activebackground='gray85')
Bcanp6rp=Button(page6,text='❌',bg='gray77',fg='red',activebackground='red',activeforeground='gray10',command=lambda:[bcanp6D()])
Bcanp6r2p=Button(page6,text='finish',bg='#7FFFD4',fg='gray15',activebackground='red',activeforeground='gray10',width=12,font=('April 10 bold italic'))







#####################################
############################    binds
#####################################

# page 1
txtf1.bind('<Button-1>',haid)
txtf4.bind('<Button-1>',haid)
txtf5.bind('<Button-1>',haid)
txtf6.bind('<Button-1>',haid)
txtlog1.bind('<Return>',loginp1)
txtlog2.bind('<Return>',loginp1)

# page4
# lbls1.bind('<Enter>',page4s)
# lblt2.bind('<Enter>',page4t)
# lblm.bind('<Enter>',page4m)

# page5
lbls21.bind('<Enter>',page4s2)
lblm2.bind('<Enter>',page4m2)

# page6


btisarA1.bind('<Enter>',EmergenciR)
btisarA2.bind('<Enter>',EmergenciR)
btisarA1.bind('<Leave>',EmergenciR)
btisarA2.bind('<Leave>',EmergenciR)

lblti1.bind('<Enter>',page6ts)
lblti1.bind('<Leave>',EmergenciR2)
lblti2.bind('<Enter>',page6t1)#remove
lblti2.bind('<Leave>',EmergenciR3)#remove
lblti3.bind('<Enter>',page6t2)#add
lblti4.bind('<Enter>',page6t4)
lblti4.bind('<Leave>',EmergenciR4)
lblti5.bind('<Enter>',page6t5)
lblti3.bind('<Leave>',EmergenciR2)
txtp6aa.bind('<Return>',bp6aa2dB)#بعد از اجرا این باید یک لیبل موقت 5 ثانیه ایی ایجاد کنی که بگه عملیات افزودن موفق بوده 
#البته دقت داشته باش که این لیبل باید در پایان افزودن پک بشه در ضمن اینکه احتمالا با کتابخانه تایم به مشکال میخوری پس بهتره از
#از موشن استفاده کنی از گوشهبیاد و سرعتش کم بشه بعد دوباره برگرده بره

# موقت=Button(page4,text='===EX====', command=lambda:[page1.tkraise()]).place(x=1640,y=400)
# موقت=Button(page4,text='===NX====', command=lambda:[page5.tkraise()]).place(x=1640,y=450)
# موقتی=Button(page5,text='===EX====', command=lambda:[page4.tkraise()]).place(x=1640,y=400)
# موقتی=Button(page5,text='===NX====', command=lambda:[page6.tkraise()]).place(x=1640,y=450)
# موقتی=Button(page6,text='===EX====', command=lambda:[page5.tkraise()]).place(x=1640,y=400)


page1.tkraise()
w.mainloop()













