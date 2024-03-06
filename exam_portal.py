import json
import re
import sqlite3
import  tkinter as tk
from subprocess import *
from tkinter import *
from tkinter import messagebox as mb

from PIL import Image, ImageTk


class cal:
    def __init__(self, root):
        
        self.data_size=len(question)
        self.q_no=0
        self.opt_selected=IntVar()
        
        self.f = Frame(root, height=818, width=1510, bg='#9CD9FA')
        self.f.propagate(0)
        self.f.pack()

        # logo
        image_path = "logo.png"
        pil_image = Image.open(image_path)
        resized_image = pil_image.resize((110, 110), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        label = Label(self.f, image=img, bg='#1A89AD')
        label.image = img
        label.place(x=47, y=35)

        # college name
        self.college_name = Label(self.f, text='Basaveshwar Engineering College, Bagalkote', font=('New times', 45, 'bold'), bg='#BFEFFF')
        self.college_name.place(x=160, y=60)
        canvas = Canvas(self.f, height=2, width=1500, bg='black')
        canvas.create_line(0, 1, 500, 1, fill='black')
        canvas.place(x=5, y=150)

        self.auth = Frame(self.f, height=630, width=1300, bg='sky blue')
        self.auth.propagate(0)
        self.auth.place(x=105, y=170)
        l1 = Label(self.auth, text='Authenticate Here', font=('New times', 30, 'bold'), fg="dark red", bg='sky blue')
        l1.place(x=480, y=30)

        image_path = "login.png"
        pil_image = Image.open(image_path)
        resized_image = pil_image.resize((130, 130), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        label = Label(self.auth, image=img, bg='sky blue')
        label.image = img
        label.place(x=580, y=95)

        self.user_name_l = Label(self.auth, text='User Name :', font=('New times', 20, 'normal'), bg='sky blue')
        self.user_name_l.place(x=330, y=260)
        self.user_name_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.user_name_e.place(x=510, y=265)

        self.password_l = Label(self.auth, text='Password   :', font=('New times', 20, 'normal'), bg='sky blue')
        self.password_l.place(x=330, y=320)
        self.password_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'),show='*')
        self.password_e.place(x=510, y=325)

        submit = Button(self.auth, text='Login', font=('New times', 15, 'bold'), bg='#0C2F51', fg='white',command=self.Login)
        submit.place(x=600, y=390)

        Dont = Label(self.auth, text="Don't have account? Register now.!", font=('New times', 15, 'normal'), fg='blue', bg='sky blue')
        Dont.place(x=500, y=450)
        Dont.bind("<Button-1>", self.Register)

    def Register(self, event):
        self.auth = Frame(self.f, height=630, width=1300, bg='sky blue')
        self.auth.propagate(0)
        self.auth.place(x=105, y=170)
        l1 = Label(self.auth, text='Register Here', font=('New times', 30, 'bold'), fg="dark red", bg='sky blue')
        l1.place(x=500, y=30)

        self.Usn_l = Label(self.auth, text='USN           :', font=('New times', 20, 'normal'), bg='sky blue')
        self.Usn_l.place(x=330, y=100)
        self.Usn_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.Usn_e.place(x=510, y=105)

        self.Name_l = Label(self.auth, text='Name         :', font=('New times', 20, 'normal'), bg='sky blue')
        self.Name_l.place(x=330, y=150)
        self.Name_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.Name_e.place(x=510, y=155)

        self.Email_l = Label(self.auth, text='Email         :', font=('New times', 20, 'normal'), bg='sky blue')
        self.Email_l.place(x=330, y=200)
        self.Email_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.Email_e.place(x=510, y=205)

        self.Password_l = Label(self.auth, text='Password   :', font=('New times', 20, 'normal'), bg='sky blue')
        self.Password_l.place(x=330, y=250)
        self.Password_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.Password_e.place(x=510, y=255)

        self.cpassword_l = Label(self.auth, text='Confirm\nPassword    :', font=('New times', 20, 'normal'), bg='sky blue')
        self.cpassword_l.place(x=330, y=300)
        self.cpassword_e = Entry(self.auth, width=25, font=('New times ', 20, 'normal'))
        self.cpassword_e.place(x=510, y=335)

        register = Button(self.auth, text='Register', font=('New times', 15, 'bold'), bg='#0C2F51', fg='white', command=self.check_pass)
        register.place(x=600, y=410)
        
        have = Label(self.auth, text="Have account? Login now.!", font=('New times', 15, 'normal'), fg='blue', bg='sky blue')
        have.place(x=530, y=480)
        have.bind("<Button-1>", self.desc_page)
        
    def desc_page(self,event):
        self.auth.destroy()
    def exam_interface(self):
        self.exam = Frame(self.f, height=630, width=1300, bg='sky blue')
        self.exam.propagate(0)
        self.exam.place(x=105, y=170)
        l1 = Label(self.exam, text='Instructions', font=('New times', 30, 'bold'), fg="dark red", bg='sky blue')
        l1.place(x=480, y=30)
        
        image_path = "login.png"
        pil_image = Image.open(image_path)
        resized_image = pil_image.resize((50, 50), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        label = Label(self.exam, image=img, bg='sky blue')
        label.image = img
        label.place(x=40, y=15)
        
        user_name=self.user_name_e.get()
        try:
            conn = sqlite3.connect('User.db')
            #print('connected successfully')
            c = conn.cursor()
            
            #print(user_name)
            #q = '''select Name from register where Usn=user_name'''
            c.execute("SELECT Name from register WHERE Usn=?",(user_name,))
            name= c.fetchall()
            #print(name[0][0])
        except Exception as e:
            print(e)
        
        User=Label(self.exam,text='',font=('New times', 10, 'normal'), fg="black", bg='sky blue')
        User.place(x=30, y=75)
        User.config(text=name[0][0])
        
        logout_button = Button(self.exam, text="Logout", command=self.exam.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
        logout_button.place(x=1200,y=15)
        
        apti=Label(self.exam,text='Aptitude Test',font=('New times', 18, 'normal'), bg='#BFEFFF',width=16,height=2)
        apti.place(x=421,y=150)
        apti_btn=Button(self.exam,text='Execute',font=('New times', 22, 'bold'),height=1, bg='#BFEFFF',fg='dark red',command=self.perform_apti)
        apti_btn.place(x=652,y=150)
        
        tech=Label(self.exam,text='Technical Test',font=('New times', 18, 'normal'), bg='#BFEFFF',width=16,height=2)
        tech.place(x=421,y=230)
        tech_btn=Button(self.exam,text='Execute',font=('New times', 22, 'bold'),height=1, bg='#BFEFFF',fg='dark red',command=self.perform_apti)
        tech_btn.place(x=652,y=230)
        
        code=Label(self.exam,text='Coding Test',font=('New times', 18, 'normal'), bg='#BFEFFF',width=16,height=2)
        code.place(x=421,y=310)
        code_btn=Button(self.exam,text='Execute',font=('New times', 22, 'bold'),height=1, bg='#BFEFFF',fg='dark red',command=self.perform_apti)
        code_btn.place(x=652,y=310)
        
        
    def perform_apti(self):
        #self.exam.destroy()
        
        self.apti = Frame(self.f, height=630, width=1300, bg='sky blue')
        self.apti.propagate(0)
        self.apti.place(x=105, y=170)
        
        self.que = Frame(self.apti, height=530, width=1000, bg='white')
        self.que.propagate(0)
        self.que.place(x=170, y=80)
        
        image_path = "login.png"
        pil_image = Image.open(image_path)
        resized_image = pil_image.resize((50, 50), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        label = Label(self.apti, image=img, bg='sky blue')
        label.image = img
        label.place(x=40, y=15)
        
        user_name=self.user_name_e.get()
        try:
            conn = sqlite3.connect('User.db')
            #print('connected successfully')
            c = conn.cursor()
            
            #print(user_name)
            #q = '''select Name from register where Usn=user_name'''
            c.execute("SELECT Name from register WHERE Usn=?",(user_name,))
            name= c.fetchall()
            #print(name[0][0])
        except Exception as e:
            print(e)
        
        User=Label(self.apti,text='',font=('New times', 10, 'normal'), fg="black", bg='sky blue')
        User.place(x=30, y=75)
        User.config(text=name[0][0])
        
        self.opts=self.radio_buttons()
		
        self.display_options()
		
        self.buttons()
		
        self.correct=0
        self.display_title()
        self.display_question()
        
        #call(["python","demo.py"])
    ##########################################################
    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
    
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
		
		# Check if the answer is correct
        if self.check_ans(self.q_no):
            self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
        self.q_no += 1
		
		# checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
            self.display_result()
			
			# destroys the GUI
            self.question.destroy()
        else:
			# shows the next question
            self.display_question()
            self.display_options()
            
    def buttons(self):
		
        next_button = Button(self.que, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
        next_button.place(x=450,y=380)
		
		# This is the second button which is used to Quit the GUI
        quit_button = Button(self.apti, text="Quit", command=self.apti.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
        quit_button.place(x=1200,y=15)

    def display_options(self):
        val=0
		
		# deselecting the options
        self.opt_selected.set(0)
		
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
		
		# setting the Question properties
        q_no = Label(self.que, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
        q_no.place(x=70, y=100)
    
    def display_title(self):
		
		# The title to be shown
        title = Label(self.que, text="Aptitude Test",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
        title.place(x=70, y=22)

    def radio_buttons(self):
		
		# initialize the list with an empty list of options
        q_list = []
		
		# position of the first option
        y_pos = 150
		
		# adding the options to the list
        while len(q_list) < 4:
			
			# setting the radio button properties
            radio_btn = Radiobutton(self.que,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
            q_list.append(radio_btn)
			
			# placing the button
            radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
            y_pos += 40
		
		# return the radio buttons
        return q_list

################################################################
    #for Register
    def check_pass(self):
        usn = self.Usn_e.get()
        usnp=re.compile(r'2BA\d{2}[A-Z]{2}\d{3}')
        usncrt=usnp.search(usn)
        print(usncrt)
        name = self.Name_e.get()
        email = self.Email_e.get()
        password = self.Password_e.get()
        cpassword = self.cpassword_e.get()
        try:
            conn = sqlite3.connect('User.db')
            #print('connected successfully')
            c = conn.cursor()
            q = '''select Usn from register'''
            c.execute(q)
            data=c.fetchall()
            for value in data:
                if usn in value:
                    flag=1
                    break
                else:
                    flag=0
                    
        except Exception as e:
            print(e)
        if flag==0:
            if usn=='':
                mb.showerror('Error','Enter USN..!')
            elif not usncrt:
                mb.showerror('Error','USN must be 2BA00XX000 pattern..!')
            elif name=='':
                mb.showerror('Error','Enter Name..!')
            elif email=='':
                mb.showerror('Error','Enter Email..!')
            elif password=='':
                mb.showerror('Error','Enter Password..!')
            elif cpassword=='':
                mb.showerror('Error','Enter confirm password..!')
            else:
                if password == cpassword:
                    try:
                        conn = sqlite3.connect('User.db')
                        #print('connected successfully')
                        c = conn.cursor()
                        q = '''insert into register values(?,?,?,?)'''
                        c.execute(q, (usn, name, email, password))
                        conn.commit()
                        mb.showinfo("Registered","You have registered successfully.!")
                        conn.close()
                        self.auth.destroy()
                    except Exception as e:
                        print(e)
                else:
                    mb.showerror('Error','Both passwords must be same..!')
        else:
            mb.showerror('Error','You already registered, Login now..!')
                
                
                
                
    def Login(self):
        user_name=self.user_name_e.get()
        password=self.password_e.get()
        flag=0
        if user_name=='':
            mb.showerror('Error','Enter username..!')
        elif password=='':
            mb.showerror('Error','Enter password..!')
        #self.exam_interface()
        else:
            try:
                conn = sqlite3.connect('User.db')
                #print('connected successfully')
                c = conn.cursor()
                q = '''select Usn from register'''
                c.execute(q)
                data=c.fetchall()
                for value in data:
                    if user_name in value:
                        flag=1
                        break
                    else:
                        flag=0
                    
            except Exception as e:
                print(e)
            if flag==1:
                try:
                    conn = sqlite3.connect('User.db')
                    #print('connected successfully')
                    c = conn.cursor()
                    q = '''select * from register'''
                    c.execute(q)
                    data=c.fetchall()
                    conn.commit()
                    e=0
                    for value in data:
                        if value[0]==user_name and value[3]==password:
                            e=1
                            break
                        else:
                            e=0
                        
                    if e==1:
                        #self.auth.destroy()
                        self.exam_interface()
                    else:
                        mb.showerror('Error','Enter correct username and password')
                            
                        
                except Exception as e:
                        print(e)
            else:
                mb.showerror('Error','Need to register first..!')
                
    
        
if __name__ == "__main__":
    root=Tk()
    with open('output_data.json') as f:
        data = json.load(f)

# set the question, options, and answer
    question = (data['question'])
    options = (data['options'])
    answer = (data[ 'answer'])
    m=cal(root)
    root.mainloop()
