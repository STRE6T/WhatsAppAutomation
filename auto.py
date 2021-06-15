import pywhatkit as kit
from tkinter import *
from tkinter import messagebox
import datetime

# Create window object
app= Tk()

#def send_msg(Number,message,TimeHour,TimeMin):
    #kit.sendwhatmsg(Number,message,TimeHour,TimeMin)
  
#funcations
def Send():
    now = datetime.datetime.now()
    hrs_now = now.strftime("%H")
    min_now = now.strftime("%M")
  
    if mobiles.get() == "":
        messagebox.showinfo("Message Box","Number isn't long enough or empty try again.. eg +27 73 9987 9191")
        mobiles.set("+27 ")
    elif fmsg.get() == "":
        messagebox.showinfo("Message Box","message box empty try again...")      
    elif lhrs.get() == "":
        messagebox.showinfo("Message Box","Hours box empty try again...")
    elif lmins.get() == "":
        messagebox.showinfo("Message Box","Minute box empty try again...")
    else:  
        moblies=mobiles.get()
        message=fmsg.get()
        hours = int(lhrs.get())    
        mintues = int(lmins.get())
        min_now_to_seconds = int(min_now) * 60
        minutes_to_seconds = (mintues * 60) 
        seconds_left = minutes_to_seconds - min_now_to_seconds
        hours_left = int(hrs_now) - hours
        hours_to_seconds = hours_left * 3600
        final_message = hours_to_seconds + seconds_left
        #notifaction
        messagebox.showinfo("Message Box","Your Message is going to be sent in " + str( final_message)+ " seconds")
        #Funcation to send message
        kit.sendwhatmsg(moblies,message,hours,mintues)   

    
def clear_information():
    fmsg.set("")

    lhrs.set("")
    lmins.set("")
    mobiles.set("+27 ")

#Saving input into variable
fmsg = StringVar()
lhrs = StringVar()
lmins = StringVar()
mobiles = StringVar()
mobiles.set("+27 ")


#Number

num_label = Label(app, text='Enter Number',font=('bold',11), pady=20)
num_label.grid(row=0, column=0, sticky=W)
num_entry= Entry(app,textvariable=mobiles,font=('Helvetica',8),width=40)
num_entry.grid(row=0, column=1)
num = num_entry.get()


#Message
msg_label = Label(app, text='Enter message',font=('bold',11), pady=20)
msg_label.grid(row=0, column=2, sticky=W)
msg_entry= Entry(app,textvariable=fmsg, width=40, font=('Helvetica',8))

msg_entry.grid(row=0, column=3)

#Time in Hours
hrs_label = Label(app, text='Enter hour of the day',font=('bold',11), pady=20)
hrs_label.grid(row=1, column=0, sticky=W)
hrs_entry= Entry(app,textvariable=lhrs,font=('Helvetica',8),width=40)
hrs_entry.grid(row=1, column=1)

#Time in Min
min_label = Label(app, text='Enter Min of the day',font=('bold',11), pady=20)
min_label.grid(row=1, column=2, sticky=W)
min_entry= Entry(app,textvariable=lmins,font=('Helvetica',8), width=40)
min_entry.grid(row=1, column=3)

app.title('WhatsApp Automate')
app.geometry('800x300')

#Buttons

send_btn = Button(app, text='Send Message', width=12, command=Send)
send_btn.grid(row=2,column=1, pady=20)

clear_btn = Button(app, text='Clear Information', width=12, command=clear_information)
clear_btn.grid(row=2,column=2)

#start of the program
app.mainloop()

