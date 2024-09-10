from tkinter import *
from tkinter import messagebox
from data_structure import NODE,QUEUE

class GUI():
    def __init__(self,root):
        self.queue = QUEUE()
        self.root = root
        self.root.title('Restaurant Booking')
        self.root.geometry('500x450')
        
        self.heading = Label(self.root,text="Booking Interface",font=('arial',25))
        self.heading.pack()

        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=20,pady=25)

        self.name_label = Label(self.frame1,text='Enter Name:',font=('arial',15))
        self.name_label.pack(side='left',padx=40)

        self.name_value = StringVar()
        self.name_enter = Entry(self.frame1,textvariable=self.name_value,font=('arial',15))
        self.name_enter.pack(side=RIGHT,padx=20) 
        
        self.frame2 = Frame(root)
        self.frame2.pack(padx=10,pady=10)
        
        self.people_label = Label(self.frame2,text="Number of People:",font=('arial',15))
        self.people_label.pack(side=LEFT,padx=10)

        self.people_count = IntVar()
        self.people_count.set(0)
        self.people_enter = Entry(self.frame2,textvariable=self.people_count,font=('arial',15),width=13)
        self.people_enter.pack(side=RIGHT)

        self.frame3 = Frame(root)
        self.frame3.pack(pady=20)

        self.button_add = Button(self.frame3,text="Add Booking",command=self.add_booking)
        self.button_add.pack(side=LEFT,padx=20)

        self.button_process = Button(self.frame3,text="Process Booking",command=self.process_booking)
        self.button_process.pack(side=RIGHT)

        '''
        self.frame4 = Frame(self.root)
        self.frame4.pack()

        self.button_view = Button(self.frame4,text="View Bookings",command=self.view_bookings)
        self.button_view.pack()
        '''

        self.bookings = Label(self.root,text="No bookings")
        self.bookings.pack(pady=25)
    
    def add_booking(self):
        try:
            name = self.name_value.get()
            people = self.people_count.get()

            if name == "" or people == 0:
                return messagebox.showwarning(title="Input error",message="enter a vaild name or no of people")
            
            self.queue.Enqueue(name,people)

            messagebox.showinfo(title="Processing",message="your booking is successfuly") 

            self.name_value.set("")
            self.people_count.set("")

            return self.view_bookings()
        except Exception as e:
            return messagebox.showwarning(title="Input error",message="enter a vaild input")

    def process_booking(self):
        self.queue.Dequeue()

        return self.view_bookings()
    
    def view_bookings(self):
        return self.show_bookings()

    def show_bookings(self):
        if self.queue.is_empty():
            self.bookings.config(text="No bookings in queue!!")
        else:
            self.bookings.config(text='\n'.join(self.queue.Print_test()))
