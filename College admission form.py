from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv
from win32api import GetSystemMetrics


#print("Width = ", GetSystemMetrics(0))
#print("Height = ",GetSystemMetrics(1))
w=GetSystemMetrics(0)/1536
h=GetSystemMetrics(1)/864


db=[]

def load_db():
    try:
        with open('database.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
        db.append(lines)
    except:
        if len(db) == 0:
            fields = ["Student's Name", "D.O.B", "Gender", "Contact NO.1", "Contact NO.2", "Email-ID", "Hobbies",
                      "Food Preferences", "Student's Address", "Alternate Address", "Guardian's Name",
                      "Guardian's Occupation", "Gudarian's Permanent Address", "Guardian's Contact No","Guardian's Email-ID",
                      "Local Guardian's Name", "Local Guardian's Occupation",
                      "Local Gudarian's Permanent Address", "Local Guardian's Contact No", "Local Guardian's Email-ID",
                      "School", "Board", "Marks", "Percentage"]
            write(fields)
def config_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1495*w,height=590*h)
def createLabel(win,text,font=("Aeril",20),bg="#EADAEA"):
    label=Label(win,text=text,font=font,bg=bg)
    return label

def createEntry(win,width,font=("Aeril", 15)):
    entry=Entry(win,width=width)
    entry.config(font=font)
    return entry

def messagetoscreen(msg):
    tkinter.messagebox.showwarning('', msg)

def checkName(name,msg):
    l=[chr(x) for x in range(48,58)]
    for i in name:
        if i in l:
            messagetoscreen(msg)
            return -1
    return 0

def checkContact(cont,msg):
    l=[chr(x) for x in range (48,58)]
    if (len(cont)==10):
        for i in cont:
            if i not in l:
                messagetoscreen(msg)
                return -1
        return 0
    else:
        messagetoscreen("Contact No. must be of 10 digits only")
        return -1

def checkPin(pin,msg):
    l = [chr(x) for x in range(48, 58)]
    if (len(pin) == 6):
        for i in pin:
            if i not in l:
                messagetoscreen(msg)
                return -1
        return 0
    else:
        messagetoscreen("Pin No. must be of 6 digits only")
        return -1

def checkDate(day,month,y,msg):
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if ((y%400==0) or (y%4==0 and y%100!=0)):
        days[2]=29
    if month>12 or month<0 or day<0 or day>days[month]:
        messagetoscreen(msg)
        return -1
    return 0

def convertDate(d,m,y,msg):
    mon={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
    try:
        date=int(d)
        month=mon[m]
        year=int(y)
        return date,month,year
    except:
        return -1,-1,-1

def checkMail(mail,msg):
    l=["@","."]
    for i in l:
        if i not in mail:
            messagetoscreen(msg)
            return -1
    return 0
def checkMarks(marks,msg):
    if marks<0 or marks>100:
        messagetoscreen(msg)
        return -1
    return 0

def write(info):
    if info in db:

        messagetoscreen("Already Registered!!!")
        return
    db.append(info)
    with open("database.csv", 'a') as cv:
        csvwriter = csv.writer(cv)
        csvwriter.writerow(info)
    #tkinter.messagebox.showinfo("", "Details uploaded successfully.")
    clearFields()

#clear data
def clearFields():
    tkinter.messagebox.showinfo("", "Details uploaded successfully.")
    entry_fname.delete(0,END)
    entry_mname.delete(0,END)
    entry_lname.delete(0,END)
    day.delete(0,END)
    day.insert(0,"DAY")
    month.delete(0,END)
    month.insert(0,"MONTH")
    year.set("YEAR")
    i.set(0)
    entry_hobby.delete(0,END)
    entry_cont1.delete(0,END)
    entry_cont2.delete(0,END)
    entry_email.delete(0,END)
    j.set(0)
    entry_hname.delete(0,END)
    entry_street.delete(0,END)
    entry_local.delete(0,END)
    entry_city.delete(0,END)
    entry_pin.delete(0,END)
    entry_po.delete(0,END)
    entry_ps.delete(0,END)
    entry_state.delete(0,END)
    country.delete(0,END)
    country.insert(0,"SELECT A COUNTRY")
    k.set(0)
    entry_alt_add.delete(1.0,END)
    entry_guarname.delete(0, END)
    entry_occu.delete(0, END)
    entry_addr.delete(0, END)
    entry_guar_cont.delete(0, END)
    entry_gemail.delete(0, END)
    entry_lguarname.delete(0, END)
    entry_occu2.delete(0, END)
    entry_addr2.delete(0, END)
    entry_lguar_cont.delete(0, END)
    entry_lgemail.delete(0, END)
    entry_school.delete(0, END)
    entry_board.delete(0, END)
    entry_phy.delete(0, END)
    entry_chem.delete(0, END)
    entry_math.delete(0, END)
    entry_eng.delete(0, END)
    entry_prcnt.delete(0, END)
    entry_prcnt.insert(0,"0.00%")

#window creation
root=Tk()
sizex=5000
sizey=4000
posx=0
posy=0
root.wm_geometry("%dx%d+%d+%d" % (sizex*h, sizey*w, posx, posy))
root.config(bg="light blue")
root.title("Admission Form")

#place frame on root
mainframe=Frame(root,relief=GROOVE,width=sizex,height=sizey,bd=1)
mainframe.place(x=10,y=90)

#place canvas on frame
canvas=Canvas(mainframe,bg="#EADAEA")

#place model frame on canvas
frame=Frame(canvas,bg="#EADAEA")

#scroll bars to be set
scrolly=Scrollbar(mainframe,orient=VERTICAL,command=canvas.yview)
scrollx=Scrollbar(mainframe,orient=HORIZONTAL,command=canvas.xview)
canvas.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
scrolly.pack(side="right",fill="y")
scrollx.pack(side="bottom",fill="x")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",config_canvas)

#student details
title=createLabel(root,text="Admission Form",font=("Baskerville Old Face", 42, 'bold '),bg="light blue")
title.config(fg="green")
title.grid(row=0,column=0,padx=550,pady=10)
subhead = createLabel(frame, text="Personal Details",font=('Courier', 25, 'bold underline'))
subhead.config(fg="#0F5E8D")
subhead.grid(row=2, column=0,sticky=W,pady=5)

#Student Name
fname=createLabel(frame,text="First Name",font=("Aeril",20))
fname.grid(row=4,column=0,padx=0,pady=0,sticky=W)
mname=createLabel(frame,text="Middle Name",font=("Aeril",20))
mname.grid(row=6,column=0,padx=0,pady=0,sticky=W)
lname=createLabel(frame,text="Last Name",font=("Aeril",20))
lname.grid(row=8,column=0,padx=0,pady=0,sticky=W)
entry_fname=createEntry(frame,30,font=("Aeril",15))
entry_fname.grid(row=4,column=1)
entry_mname = createEntry(frame, 30, font=("Aeril", 15))
entry_mname.grid(row=6, column=1)
entry_lname = createEntry(frame, 30, font=("Aeril", 15))
entry_lname.grid(row=8, column=1)

#Date Of Birth
dob=createLabel(frame,"Date Of Birth",font=("Aeril",20))
dob.grid(row=10,column=0,sticky=W)
day=ttk.Combobox(frame, values=[i for i in range(1,32)])
day.set("DATE")
day.bind("<<ComboboxSelected>>")
day.config(font=("Aerial", 15),width=5)
day.grid(row=10,column=1,sticky=W)
month=ttk.Combobox(frame, values=["January","February","March","April","May","June","July","August","September","October","November","December"])
month.set("MONTH")
month.bind("<<ComboboxSelected>>")
month.config(font=("Aerial", 15))
month.grid(row=10,column=1,sticky=E)
year = ttk.Combobox(frame, values=[i for i in range(1995, 2019)])
year.set("YEAR")
year.bind("<<ComboboxSelected>>")
year.config(font=("Aerial", 15),width=5)
year.grid(row=10,column=2,sticky=W,padx=20)

#Gender
gender=createLabel(frame,"Gender",("Aeril",20))
gender.grid(row=12,column=0,sticky=W)
i=IntVar()
male=Radiobutton(frame,text="Male",value=1,variable=i)
male.config(font=("Aerial",15),bg="#EADAEA")
male.grid(row=12,column=1,sticky=W)
female=Radiobutton(frame,text="Female",value=2,variable=i)
female.config(font=("Aerial",15),bg="#EADAEA")
female.grid(row=12,column=1,sticky=W,padx=100)
other=Radiobutton(frame,text="Others",value=3,variable=i)
other.config(font=("Aerial",15),bg="#EADAEA")
other.grid(row=12,column=1,sticky=E)

#Contact Numbers
cont1=createLabel(frame,"Contact No 1")
cont1.grid(row=14,column=0,sticky=W)
entry_cont1=createEntry(frame, 30, font=("Aeril", 15))
entry_cont1.grid(row=14,column=1)
cont2=createLabel(frame,"Contact No 2")
cont2.grid(row=16,column=0,sticky=W)
entry_cont2=createEntry(frame, 30, font=("Aeril", 15))
entry_cont2.grid(row=16,column=1)

#Email ID
email=createLabel(frame,"Email ID")
email.grid(row=18, column=0,sticky=W)
entry_email=createEntry(frame, 30, font=("Aeril", 15))
entry_email.grid(row=18,column=1)

#Hobbies
hobby=createLabel(frame,"Hobbies")
hobby.grid(row=20,column=0,sticky=W)
entry_hobby=createEntry(frame, 30, font=("Aeril", 15))
entry_hobby.grid(row=20,column=1)

#Food preference
food=createLabel(frame,"Food Preference")
food.grid(row=22,column=0,sticky=W)
j=IntVar()
veg=Radiobutton(frame,text="Veg",value=1,variable=j)
veg.config(font=("Aerial",15),bg="#EADAEA")
veg.grid(row=22,column=1,sticky=W)
nveg=Radiobutton(frame,text="Non-Veg",value=2,variable=j)
nveg.config(font=("Aerial",15),bg="#EADAEA")
nveg.grid(row=22,column=1,sticky=W,padx=80)


#Residential details
subhead2 = createLabel(frame, text="Residential Details",font=('Courier', 25, 'bold underline'))
subhead2.config(fg="#0F5E8D")
subhead2.grid(row=24, column=0,sticky=W,pady=20)
#House No
hname=createLabel(frame,"House No")
hname.grid(row=26,column=0,sticky=W)
entry_hname=createEntry(frame, 30, font=("Aeril", 15))
entry_hname.grid(row=26,column=1)

#Street name
street=createLabel(frame,"Street Name")
street.grid(row=28,column=0,sticky=W)
entry_street=createEntry(frame, 30, font=("Aeril", 15))
entry_street.grid(row=28,column=1)

#Locality
locality=createLabel(frame,"Locality")
locality.grid(row=30,column=0,sticky=W)
entry_local=createEntry(frame, 30, font=("Aeril", 15))
entry_local.grid(row=30,column=1)

#City
city=createLabel(frame,"City")
city.grid(row=32,column=0,sticky=W)
entry_city=createEntry(frame, 20, font=("Aeril", 15))
entry_city.grid(row=32,column=1,sticky=W)

#Pin code
pin=createLabel(frame,"Pin Code")
pin.grid(row=32,column=2,sticky=W)
entry_pin=createEntry(frame, 10, font=("Aeril", 15))
entry_pin.grid(row=32,column=3,sticky=W)

#PO
po=createLabel(frame,"Post Office(P.O.)")
po.grid(row=34,column=0,sticky=W)
entry_po=createEntry(frame, 20, font=("Aeril", 15))
entry_po.grid(row=34,column=1,sticky=W)

#PS
ps=createLabel(frame,"Police Station(P.S.)")
ps.grid(row=34,column=2,sticky=W)
entry_ps=createEntry(frame, 20, font=("Aeril", 15))
entry_ps.grid(row=34,column=3,sticky=W)

#Urban/Rural
urban=createLabel(frame,"Urban/Rural")
urban.grid(row=36,column=0,sticky=W)
k=IntVar()
urb=Radiobutton(frame,text="Urban",value=1,variable=k)
urb.config(font=("Aerial",15),bg="#EADAEA")
urb.grid(row=36,column=1,sticky=W)
rur=Radiobutton(frame,text="Rural",value=2,variable=k)
rur.config(font=("Aerial",15),bg="#EADAEA")
rur.grid(row=36,column=1,sticky=W,padx=90)

#State
state=createLabel(frame,"State")
state.grid(row=38,column=0,sticky=W)
entry_state=createEntry(frame,20,font=("Aeril", 15))
entry_state.grid(row=38,column=1,sticky=W)

#Country
cntry=createLabel(frame,"Country")
cntry.grid(row=38,column=2,sticky=W)
country=ttk.Combobox(frame, values=["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrai","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic (CAR)","Chad","Chile","China","Colombia","Comoros","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Cyprus","Czechia","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini (formerly Swaziland)","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malt","Marshall Islands","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar(formerly Burma)","Namibia","Nauru"
,"Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia (formerly Macedonia)","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo,Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates (UAE)","United Kingdom (UK)","United States of America (USA)","Uruguay","Uzbekistan","Vanuatu","Vatican City (Holy See)","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"])
country.set("SELECT A COUNTRY")
country.bind("<<ComboboxSelected>>")
country.config(font=("Aerial", 15),width='30')
country.grid(row=38,column=3,sticky="W",columnspan=2)

#Alternate Address
alt_add=createLabel(frame,"Alternate Address(if any)")
alt_add.grid(row=40,column=0,sticky=W)
entry_alt_add=Text(frame,width=40,height=5)
entry_alt_add.grid(row=40,column=1,sticky=W)
#check equaltiy


#Guardian's Details
subhead3=createLabel(frame,"Guardian's Details",font=('Courier', 25, 'bold underline'))
subhead3.config(fg="#0F5E8D")
subhead3.grid(row=46, column=0,sticky=W,pady=20)

#Guardian's Name
gname=createLabel(frame,"Guardian's Name")
gname.grid(row=48,column=0,sticky=W)
entry_guarname=createEntry(frame,30)
entry_guarname.grid(row=48,column=1,sticky=W)

#Occupation
occu=createLabel(frame,"Occupation")
occu.grid(row=50,column=0,sticky=W)
entry_occu=createEntry(frame,30)
entry_occu.grid(row=50,column=1,sticky=W)

#Guardian's address
gaddr=createLabel(frame,"Permanent Address")
gaddr.grid(row=52,column=0,sticky=W)
entry_addr=createEntry(frame,30)
entry_addr.grid(row=52,column=1,sticky=W)

#Guardian's contact no
gcont=createLabel(frame,"Contact No")
gcont.grid(row=54,column=0,sticky=W)
entry_guar_cont=createEntry(frame,30)
entry_guar_cont.grid(row=54,column=1,sticky=W)

#Guardian's email id
gemail=createLabel(frame,"Email ID")
gemail.grid(row=56,column=0,sticky=W)
entry_gemail=createEntry(frame,30)
entry_gemail.grid(row=56,column=1,sticky=W)

#Local Guardian's Name
lgname=createLabel(frame,"Local Guardian's Name")
lgname.grid(row=48,column=2,sticky=W,padx=20)
entry_lguarname=createEntry(frame,30)
entry_lguarname.grid(row=48,column=3,sticky=W)

#Occupation
occu2=createLabel(frame,"Occupation")
occu2.grid(row=50,column=2,sticky=W,padx=20)
entry_occu2=createEntry(frame,30)
entry_occu2.grid(row=50,column=3,sticky=W)

#Local Guardian's address
lgaddr=createLabel(frame,"Permanent Address")
lgaddr.grid(row=52,column=2,sticky=W,padx=20)
entry_addr2=createEntry(frame,30)
entry_addr2.grid(row=52,column=3,sticky=W)

#Local Guardian's contact no
lgcont=createLabel(frame,"Contact No")
lgcont.grid(row=54,column=2,sticky=W,padx=20)
entry_lguar_cont=createEntry(frame,30)
entry_lguar_cont.grid(row=54,column=3,sticky=W)

#Local Guardian's email id
lgemail=createLabel(frame,"Email ID")
lgemail.grid(row=56,column=2,sticky=W,padx=20)
entry_lgemail=createEntry(frame,30)
entry_lgemail.grid(row=56,column=3,sticky=W)

#Educational Details
subhead4=createLabel(frame,"Educational Details",font=('Courier', 25, 'bold underline'))
subhead4.config(fg="#0F5E8D")
subhead4.grid(row=58, column=0,sticky=W,pady=20)

#school
school=createLabel(frame,"School")
school.grid(row=60,column=0,sticky=W)
entry_school=createEntry(frame,30)
entry_school.grid(row=60,column=1,sticky=W)

#board
board=createLabel(frame,"Board of Examination")
board.grid(row=60,column=2,sticky=W,padx=20)
entry_board=createEntry(frame,15)
entry_board.grid(row=60,column=3,sticky=W)

#marks
txt=createLabel(frame,"Marks Obtained",font=("Aeril",20,'bold underline'))
txt.grid(row=62,column=0,sticky=W)
phy=createLabel(frame,"Physics")
phy.grid(row=64,column=0,sticky=W)
entry_phy=createEntry(frame,10)
entry_phy.insert(END,0)
entry_phy.grid(row=64,column=0,sticky=E)
chem=createLabel(frame,"Chemistry")
chem.grid(row=64,column=1,sticky=W,padx=5)
entry_chem=createEntry(frame,10)
entry_chem.insert(END,0)
entry_chem.grid(row=64,column=1,sticky=E)
maths=createLabel(frame,"Maths")
maths.grid(row=66,column=0,sticky=W)
entry_math=createEntry(frame,10)
entry_math.insert(END,0)
entry_math.grid(row=66,column=0,sticky=E)
eng=createLabel(frame,"English")
eng.grid(row=66,column=1,sticky=W,padx=5)
entry_eng=createEntry(frame,10)
entry_eng.insert(END,0)
entry_eng.grid(row=66,column=1,sticky=E)

#Percentage

##percent=createLabel(frame,"PCM Percentage")
#percent.grid(row=64,column=1,sticky=W)
entry_prcnt=Entry(frame,width=10,font=("Aeril",15))
entry_prcnt.insert(END,"0.0%")
entry_prcnt.grid(row=66,column=3,sticky=W,padx=15)

#Confirmation
prcn=0.0
def percent_calculate(event):
    global entry_prcnt,prcn
    try:
        prcn=float(entry_phy.get())+float(entry_chem.get())+float(entry_math.get())
        prcn/=3
        prcn=round(prcn,2)
        if prcn>100:
            raise ValueError
        entry_prcnt.delete(0,END)
        entry_prcnt.insert(END,str(prcn)+"%")
    except:
        entry_prcnt.delete(0,END)
        entry_prcnt.insert(END,"ERROR!")

confirm=Button(frame,text="Calculate PCM Percentage",font=("Ariel",15),bg="green",
              fg="white",relief=GROOVE,bd=4,padx=20,
              pady=10)
confirm.bind("<Button-1>",percent_calculate)
confirm.grid(row=66,column=2,sticky=E)

#Agreement Checkbox
text="I agree that above details are true and the form is liable to be cancelled in case of discrepency"
chkB=IntVar()
chk=Checkbutton(root,text=text,bg="light blue",font=("Aeril",15),variable=chkB)
chk.place(x=0*w,y=715*h)

#Cancel button
cancel=Button(root,text="Cancel",font=("Ariel",15),bg="blue",
              fg="white",relief=GROOVE,bd=4,width=int(5*w),padx=20,
              pady=10,command=root.destroy)
cancel.place(x=1260*w,y=720*h)

#Submit Button
def load():
    info = []
    name = str(entry_fname.get()) + str(entry_mname.get()) + str(entry_lname.get())
    if name == "":
        messagetoscreen("Student Name is mandatory.")
        return
    if(checkName(name, "Student Name Invalid.")==-1):
        return
    info.append(name)
    date, Mon, yr = convertDate(day.get(), month.get(), year.get(), "Invalid Date of Birth.")
    if(checkDate(date, Mon, yr, "Invalid Date of Birth.")==-1):
        return
    birth = str(date) + "/" + str(Mon) + "/" + str(yr)
    info.append(birth)
    gen = ["Male", "Female", "Others"]
    try:
        if i.get()==0:
            raise ValueError
        gend = gen[int(i.get()) - 1]
    except:
        messagetoscreen("Gender is a mandatory field.")
        return
    info.append(gend)
    con1 = entry_cont1.get()
    if con1 == "":
        messagetoscreen("Student contact number is mandatory")
        return
    if(checkContact(con1, "Student contact number invalid.")==-1):
        return
    info.append(con1)
    con2 = entry_cont2.get()
    if len(con2) > 0:
        if(checkContact(con2, "Student contact number invalid.")==-1):
            return
    info.append(con2)
    emailid = entry_email.get()
    if(checkMail(emailid, "Student Email ID invalid.")==-1):
        return
    info.append(emailid)
    hob = entry_hobby.get()
    info.append(hob)
    foodie = ["Veg", "non-Veg"]
    try:
        if j.get()==0:
            raise ValueError
        foo = foodie[int(j.get()) - 1]
    except:
        messagetoscreen("Food preference should be mentioned.")
        return
    info.append(foo)

    # residential details
    address = str(entry_hname.get()) + " "+ str(entry_street.get()) + "," + str(entry_local.get()) + str(entry_city.get()) + "-"
    if entry_street.get()=="" or entry_local.get()=="" or entry_city.get()=="":
        messagetoscreen("Student address needs to be completely mentioned.")
        return
    p = entry_pin.get()
    if(checkPin(p, "Pin Code should be of 6 digits.")==-1):
        return
    address = address + p + ",P.O.-" + str(entry_po.get()) + ",P.S.-" + str(entry_ps.get()) + "," + str(
        entry_state.get()) + "," + str(country.get()) + ",Address category:"
    if entry_state.get()=="" or country.get()=="SELECT A COUNTRY":
        messagetoscreen("State and Country is a mandatory field.")
        return
    ty = ["Urban", "Rural"]
    try:
        if k.get()==0:
            raise ValueError
        typ = ty[int(k.get()) - 1]
    except:
        messagetoscreen("Address type Urban/Rural to be mentioned.")
        return
    address += typ
    info.append(address)
    alternate = entry_alt_add.get("1.0",END)
    info.append(alternate)
    guard = str(entry_guarname.get())
    if guard == "":
        messagetoscreen("Guardian's Name is mandatory")
        return
    if(checkName(guard, "Guardian's Name invalid.")==-1):
        return
    info.append(guard)
    occup = str(entry_occu.get())
    if occup == "":
        messagetoscreen("Guardian's Occupation is a mandatory field.")
        return
    info.append(occup)
    gaddress = entry_addr.get()
    if gaddress == "":
        messagetoscreen("Guardian's Address is a mandatory field.")
        return
    info.append(gaddress)
    gcon, gemailid = str(entry_guar_cont.get()), str(entry_gemail.get())
    if gcon == "":
        messagetoscreen("Guardian's Contact Number is a mandatory field.")
        return
    if(checkContact(gcon, "Guardian's Contact Number invalid.")==-1) :
        return
    info.append(gcon)
    if len(gemailid)>0:
        if(checkMail(gemailid,"Guardian's Email ID invalid."==-1)):
            return
    info.append(gemailid)
    # local guardian
    lg = [str(entry_lguarname.get()), str(entry_occu2.get()), str(entry_addr2.get())]
    checkName(lg[0], "Local Guardian's Name invalid.")
    info.append(lg[0])
    info.append(lg[1])
    info.append(lg[2])
    lcon = str(entry_lguar_cont.get())
    if len(lcon) > 0:
        if(checkContact(lcon, "Local Guardian's Contact Number Invalid.")==-1):
            return
    info.append(lcon)
    lmail = str(entry_lgemail.get())
    if len(lmail) > 0:
        if(checkMail(lmail, "Local Guardian's Email ID Invalid.")==-1):
            return
    info.append(lmail)
    # edu details
    sch, boa = str(entry_school.get()), str(entry_board.get())
    if sch == "" or boa == "":
        messagetoscreen("School and board of examination are mandatory fields")
        return
    info.append(sch)
    info.append(boa)
    try:
        p, c, m, e = int(entry_phy.get()), int(entry_chem.get()), int(entry_math.get()), int(entry_eng.get())
        if(checkMarks(p, "Physics marks invalid.")==-1) or(checkMarks(c, "Chemistry marks invalid.")==-1) or (checkMarks(m, "Maths marks invalid.")==-1) or(checkMarks(e, "English marks invalid.")==-1):
            return
    except:
        messagetoscreen("Invalid Marks entered.")
        return
    info.append([p, c, m, e])
    per = str(entry_prcnt.get())
    info.append(per)
    load_db()
    write(info)



def submitData(event):
    if chkB.get() == 1:

        answer = tkinter.messagebox.askquestion("", "Confirm Submission?")
        if answer == "yes":
            load()
            #print("yes")# here call loading function
    else:
        tkinter.messagebox.showwarning('', 'Click on I agree!!')

submit=Button(root,text="Submit",font=("Ariel",15),bg="blue",
              fg="white",relief=GROOVE,bd=4,width=int(5*w),padx=20,
              pady=10)
submit.bind("<Button-1>",submitData)
submit.place(x=1380*w,y=720*h)

root.mainloop()







