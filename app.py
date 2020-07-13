#This is a python project based on api, gui and tkinter. This project is on a quiz app which extracts 10 questions and their options from api
#User have to select an option, after answering all of the question user can see hi score and leaderboard too


#importing directories used in the project

from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from dbhelper import DBhelper
import requests
import random



#defining quiz class


class quiz:


    # constructor for quiz class


    def __init__(self):
        self.total_correct_answer=0
        self.root = Tk()
        self.db=DBhelper()  #connecting DBhelper class of dbhelper.py
        self.root.title("Quizzyy") #Title of gui


        self.root.configure(bg="#ceff0a")

        self.myFont = font.Font(family='Comic Sans MS', size=10, weight='bold')

        self.root.minsize(500,700) #minimum size of gui
        self.root.maxsize(500,700) #maximum size of gui
        self.login_page()

        self.root.mainloop()  #to keep gui on screen untill interfered be any keyboard input or mouse



    # function to clear the gui


    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()



    # function for displaying login page


    def login_page(self):

        self.clear()

        self.root.configure(bg="#ceff0a")

        self.root.minsize(500, 700)
        self.root.maxsize(500, 700)

        self.label1 = Label(self.root, text="Quizzyy",fg="black", bg="#ceff0a")
        self.label1.configure(font=("Comic Sans MS", 30, "bold"))
        self.label1.pack(pady=(10, 5))

        self.alabel3 = Label(self.root,text="-"*70,fg="black", bg="#ceff0a")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.elabel = Label(self.root, text = "Email",fg="black", bg="#ceff0a")
        self.elabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.elabel.pack(pady=(40,5))

        self.email = Entry(self.root)
        self.email.pack(pady=(0, 15), ipadx=40, ipady=4)

        self.plabel = Label(self.root, text="Password", fg="black", bg="#ceff0a")
        self.plabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.plabel.pack(pady=(10, 5))

        self.password = Entry(self.root)
        self.password.pack(pady=(0, 10), ipadx=40, ipady=5)

        #login button for logging in of user when pressed
        # calls login_btn function

        self.login = Button(self.root,text="Login",fg="white",bg="#7d9c00",command=lambda :self.login_btn())
        self.login['font']=self.myFont
        self.login.pack(pady=(5, 25), ipadx=70, ipady=4)

        self.label2 = Label(self.root,text = "Not a member? Sign Up", fg="black", bg="#ceff0a")
        self.label2.configure(font=("Comic Sans MS", 20, "italic"))
        self.label2.pack(pady=(25,10))

        # registration button for registering new user when pressed
        # calls register_btn function

        self.register = Button(self.root, text="Sign Up", fg="white", bg="#7d9c00",command=lambda :self.register_btn())
        self.register['font'] = self.myFont
        self.register.pack(pady=(5, 10), ipadx=70, ipady=4)



    #functon called whenever login button is pressed
    # extract email and password inserted by user
    # and check it in the database
    # if credentials are correct user get logged in
    #otherwise user have to enter his/her details again


    def login_btn(self):
        email=self.email.get()
        password=self.password.get()

        data=self.db.check_login(email,password)

        if len(data)>0:
            self.clear()
            self.player_id=data[0][0]
            self.player_data=data[0]
            self.load_home()

        else:
            messagebox.showerror("Error","Incorrext Email/password")




    #function gets called whenever Sign Up button is pressed
    #loads the register page
    #user can register if he/she has not yet registered


    def register_btn(self):
        self.root.minsize(500,800)
        self.root.maxsize(500, 800)
        self.clear()

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#ceff0a")
        self.label1.configure(font=("Comic Sans MS", 30, "bold"))
        self.label1.pack(pady=(10, 5))

        self.alabel3 = Label(self.root,text="-"*70,fg="black", bg="#ceff0a")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.nlabel = Label(self.root, text="Full Name : ", fg="black", bg="#ceff0a")
        self.nlabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.nlabel.pack(pady=(15, 5))

        self.name = Entry(self.root)
        self.name.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.elabel = Label(self.root, text="Email : ", fg="black", bg="#ceff0a")
        self.elabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.elabel.pack(pady=(10, 5))

        self.email = Entry(self.root)
        self.email.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.plabel = Label(self.root, text="Password : ", fg="black", bg="#ceff0a")
        self.plabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.plabel.pack(pady=(10, 5))

        self.password = Entry(self.root)
        self.password.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.cplabel = Label(self.root, text="Confirm Password :", fg="black", bg="#ceff0a")
        self.cplabel.configure(font=("Comic Sans MS", 20, "italic"))
        self.cplabel.pack(pady=(10, 5))

        self.cpassword = Entry(self.root)
        self.cpassword.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.unlabel = Label(self.root, text="Username \n (You won't be able to change it later)  :", fg="black",
                             bg="#ceff0a")
        self.unlabel.configure(font=("Comic Sans MS", 18, "italic"))
        self.unlabel.pack(pady=(10, 5))

        self.username = Entry(self.root)
        self.username.pack(pady=(0, 5), ipadx=40, ipady=5)

        #register button for sending new user's data to database for entry
        # calls confirm_register function when pressed

        self.register = Button(self.root, text="Sign Up ", fg="white", bg="#7d9c00",command=lambda: self.confirm_register())
        self.register['font'] = self.myFont
        self.register.pack(pady=(5, 5), ipadx=70, ipady=4)

        self.label2 = Label(self.root, text="Already a member? Login", fg="black", bg="#ceff0a")
        self.label2.configure(font=("Comic Sans MS", 20, "italic"))
        self.label2.pack(pady=(20, 5))

        #Login button to go back to login page
        #calls login_page function when pressed

        self.login = Button(self.root, text="Login", fg="white", bg="#7d9c00", command=lambda: self.login_page())
        self.login['font'] = self.myFont
        self.login.pack(pady=(5, 10), ipadx=70, ipady=4)






    #gets called whenever register button of register page is pressed
    #extract the data entered by user and adds it into the database
    #check whether user has entered correct or not if not then user have to enter correct input


    def confirm_register(self):
        name=self.name.get()
        if len(name)<=0:
            messagebox.showerror("Error!!!","Name cannot be empty")

        else:
            email=self.email.get()

            if len(email)<=0:
                messagebox.showerror("Error!!!","Email cannot be empty")

            else:
                password = self.password.get()
                if len(password)<=0:
                    messagebox.showerror("Error!!!","Password cannot be empty")

                else:
                    cpassword = self.cpassword.get()

                    if len(cpassword)<=0:
                        messagebox.showerror("Error!!!","Confirm password cannot be empty")

                    else:
                        username = self.username.get()

                        if len(username)<=0:
                            messagebox.showerror("Error!!!","Username cannot be empty")

                        else:
                            emresponse = self.db.check_email(email)

                            if emresponse == 0:
                                messagebox.showerror("Error", "Email already taken")

                            else:

                                if password != cpassword:
                                    messagebox.showerror("Error", "Password & confirm password does not match")


                                else:

                                    if len(username) > 10:
                                        messagebox.showerror("Error!!!",
                                                             "Length of username cannot exceed 10 characters")

                                    else:
                                        uresponse = self.db.check_username(username)

                                        if uresponse == 0:
                                            messagebox.showerror("Error!!!", "Username already taken")

                                        else:
                                            response = self.db.insert_user(name, email, password, username)

                                            if response == 1:
                                                #shows a success popup if registration is successful
                                                # and goes back to login page
                                                messagebox.showinfo("Registration Successful", "You may login now")
                                                self.login_page()

                                            else:
                                                #shows error if any error occurred while registration
                                                messagebox.showerror("Error!!!", "Database error")




    #gets called if user credential is correct and login button is pressed
    #This is basically homepage of every user
    #There are total 5 options i.e., New Game, Leaderboard, Help, Change Password and logout


    def load_home(self):
        self.clear()
        self.root.configure(bg="#00FF00")

        self.root.minsize(500, 700)
        self.root.maxsize(500, 700)

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(30, 5))

        self.alabel3 = Label(self.root,text="-"*70, fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="M A I N   M E N U", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(30, 10))

        self.label2 =Label(self.root, text ="Welcome : " + self.player_data[2], fg="black", bg="#00FF00")
        self.label2.configure(font = ("Comic Sans MS",12,"bold"))
        self.label2.pack(pady=(10,5))

        #Newgame button to start a new game
        #calls level function when pressed

        self.new_game = Button(self.root, text="New Game", fg="white", bg="#008000", command=lambda: self.level())
        self.new_game['font'] = self.myFont
        self.new_game.pack(pady=(50, 10), ipadx=80, ipady=4)

        # Leaderboard button to see leaderboard
        # calls leaderboard function when pressed

        self.leaders = Button(self.root, text="Leaderboards", fg="white", bg="#008000", command=lambda: self.leaderboard())
        self.leaders['font'] = self.myFont
        self.leaders.pack(pady=(20, 10), ipadx=70, ipady=4)

        # Help button to see help
        # calls help function when pressed

        self.helpp = Button(self.root, text="Help", fg="white", bg="#008000", command=lambda: self.help())
        self.helpp['font'] = self.myFont
        self.helpp.pack(pady=(20, 10), ipadx=99, ipady=4)

        #Change password for changing password
        #call take_new_password when pressed

        self.change = Button(self.root, text="Change Password", fg="white", bg="#008000", command=lambda: self.take_new_password())
        self.change['font'] = self.myFont
        self.change.pack(pady=(20, 10), ipadx=60, ipady=4)

        # Logout button for logging out
        # goes back to login page when pressed

        self.logOut= Button(self.root, text="Log Out", fg="white", bg="#008000", command=lambda: self.logout())
        self.logOut['font'] = self.myFont
        self.logOut.pack(pady=(20, 10), ipadx=88, ipady=4)




    #functions gets called whenever new game is pressed on homepage
    #This function is for selecting the quiz level
    #There are total 3 difficulties i.e., Easy, Normal and Hard
    # There is also an extra button to go back to main menu(home page)


    def level(self):
        self.clear()

        self.root.minsize(500, 650)
        self.root.maxsize(500, 650)

        self.label1 = Label(self.root, text=" Quizzyy ", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 5))

        self.alabel3 = Label(self.root,text="-"*70,fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="N E W   G A M E", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(30, 10))

        self.label3 = Label(self.root, text="Select Difficulty", fg="black", bg="#00FF00")
        self.label3.configure(font=("Comic Sans MS", 15, "bold"))
        self.label3.pack(pady=(5, 10))

        #to set difficulty level easy
        #calls fetch_question to fetch easy level questions

        self.easy = Button(self.root, text="Easy", fg="white", bg="#008000", command = lambda: self.fetch_question(mode=0))
        self.easy['font'] = self.myFont
        self.easy.pack(pady=(30, 10), ipadx=80, ipady=4)

        # to set difficulty level normal
        # calls fetch_question to fetch normal level questions

        self.normal = Button(self.root, text="Normal", fg="white", bg="#008000", command = lambda: self.fetch_question(mode=1))
        self.normal['font'] = self.myFont
        self.normal.pack(pady=(20, 10), ipadx=73, ipady=4)

        # to set difficulty level hard
        # calls fetch_question to fetch hard level questions

        self.hard = Button(self.root, text="Hard", fg="white", bg="#008000", command = lambda: self.fetch_question(mode=2))
        self.hard['font'] = self.myFont
        self.hard.pack(pady=(20, 10), ipadx=80, ipady=4)

        #to go back to main menu

        self.back = Button(self.root, text="Main Menu", fg="white", bg="#008000", command=lambda: self.load_home())
        self.back['font'] = self.myFont
        self.back.pack(pady=(50, 10), ipadx=63, ipady=4)




    #This function gets called after selecting level
    # It fetches question from API according to difficulty level selected by user
    # The fetched data is in the form of json or in simple words key value pairs just like dictionary of python


    def fetch_question(self,mode):

        #to fetch questions of easy level using api

        if mode == 0:
            url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"
            response = requests.get(url)
            self.response=response.json()
            self.data = self.response['results']
            self.extract_question(mode=mode)

        #to fetch questions of normal level using api

        if mode == 1:
            url="https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple"
            response = requests.get(url)
            self.response=response.json()
            self.data = self.response['results']
            self.extract_question(mode=mode)

        #to fetch questions of hard level using api
        if mode == 2:
            url="https://opentdb.com/api.php?amount=10&difficulty=hard&type=multiple"
            response = requests.get(url)
            self.response=response.json()
            self.data = self.response['results']
            self.extract_question(mode=mode)




    #This functions gets called after successfully fetching 10 questions from api
    #it extract a single question from the data fetched by fetch_questions function every time it gets called
    #stores the extracted question and its option in a list
    #and stores correct aanswer in other variable


    def extract_question(self,mode,index=0):
        self.clear()
        question = ['','','','']
        options=[]
        question.insert(0,self.data[index]['question'])

        #to generate random location for storing correct option
        num = random.randint(1,4)

        #storing correct answer at randum index generated above
        question[num]=self.data[index]['correct_answer']

        #to remember location od=f right answer
        if num==1:
            self.correct_answer='A'
            self.correct_number=1

        if num==2:
            self.correct_answer='B'
            self.correct_number=2

        if num==3:
            self.correct_answer='C'
            self.correct_number=3

        if num==4:
            self.correct_answer='D'
            self.correct_number=4

        options.append(num)

        i=1
        j=0

        while i!=4:

            #generating randum locations for wrong options

            num=random.randint(1,4)
            if num not in options:

                #storing wrong options at randum indexes generated above

                question.pop(num)
                question.insert(num,self.data[index]['incorrect_answers'][j])
                options.append(num)
                i+=1
                j+=1

        #to replace special characters number with special characters

        question[0]=question[0].replace('&quot;','"')
        question[0] = question[0].replace('&#039;',"'")
        question[0] = question[0].replace('&amp;','&')
        question[0] = question[0].replace('&e', 'é')
        question[0] = question[0].replace('acute;', '-')

        question[1] = question[1].replace('&quot;', '"')
        question[1] = question[1].replace('&#039;', "'")
        question[1] = question[1].replace('&amp;', '&')
        question[1] = question[1].replace('&e', '&')
        question[1] = question[1].replace('acute;', '-')

        question[2] = question[2].replace('&quot;', '"')
        question[2] = question[2].replace('&#039;', "'")
        question[2] = question[2].replace('&amp;', '&')
        question[2] = question[2].replace('&e', 'é')
        question[2] = question[2].replace('acute;', '-')

        question[3] = question[3].replace('&quot;', '"')
        question[3] = question[3].replace('&#039;', "'")
        question[3] = question[3].replace('&amp;', '&')
        question[3] = question[3].replace('&e', 'é')
        question[3] = question[3].replace('acute;', '-')

        question[4] = question[4].replace('&quot;', '"')
        question[4] = question[4].replace('&#039;', "'")
        question[4] = question[4].replace('&amp;', '&')
        question[4] = question[4].replace('&e', 'é')
        question[4] = question[4].replace('acute;', '-')

        self.display_question(question,index=index,mode=mode)




    #This function is for displaying the extracted question and its options to user
    #User have to select an option and press next for  next question
    #Gets called after fetch_question function everytime
    #There is also a button to go back to main menu if user doesn't want to continue playing


    def display_question(self,question,index,mode):

        self.clear()

        self.root.minsize(1500, 700)
        self.root.maxsize(1500, 700)


        self.label1 = Label(self.root, text=" Quizzyy ", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 5),fill=X)

        self.label3 = Label(self.root, text="-"*100, fg="black", bg="#00FF00")
        self.label3.configure(font=("Comic Sans MS", 10))
        self.label3.pack(pady=(5, 10), fill=X)



        self.qlabel = Label(self.root, text="Q" + str(index + 1) + ". " + question[0], fg='black', bg="#00FF00")
        self.qlabel.configure(font=("Times New Roman", 18, "bold"))
        self.qlabel.pack(pady=(30, 10),fill=X)


        self.alabel1 = Label(self.root, text="A.    " + question[1], fg='black', bg="#00FF00")
        self.alabel1.configure(font=("Times New Roman", 15, "italic"))
        self.alabel1.pack(pady=(20, 10), padx=(50, 50),fill=X)


        self.alabel2 = Label(self.root, text="B.    " + question[2], fg='black', bg="#00FF00")
        self.alabel2.configure(font=("Times New Roman", 15, "italic"))
        self.alabel2.pack(pady=(10, 10), padx=(50, 50),fill=X)


        self.alabel3 = Label(self.root, text="C.    "+ question[3], fg='black', bg="#00FF00")
        self.alabel3.configure(font=("Times New Roman", 15, "italic"))
        self.alabel3.pack(pady=(10, 10), padx=(50, 50),fill=X)


        self.alabel4 = Label(self.root, text="D.    " + question[4], fg='black', bg="#00FF00")
        self.alabel4.configure(font=("Times New Roman", 15, "italic"))
        self.alabel4.pack(pady=(10, 10), padx=(50, 50),fill=X)


        self.label2 = Label(self.root, text="Enter Your Answer:", fg='black', bg='#00ff00')
        self.label2.configure(font=("Comic Sans MS", 15))
        #self.label2.place(x=50,y=570)
        self.label1.pack(pady=(30, 10), padx=(50, 50), fill=X)

        # to remove default value of answer label when user click on entry box

        def in_click(event):
            if self.answer.get() == self.answer.default_value:
                event.widget.delete(0, END)

        # to insert default value of answer label back in it if nothing is entered
        # and user go out of scope from that entry box

        def out_click(event):
            if len(self.answer.get()) == 0:
                event.widget.delete(0, END)
                event.widget.insert(0, self.answer.default_value)

        #Entry box for answer insertion
        self.answer = Entry(self.root)
        self.answer.default_value = 'Enter Your Answer'
        self.answer.insert(0, self.answer.default_value)
        self.answer.bind("<FocusIn>", in_click)
        self.answer.bind("<FocusOut>", out_click)
        self.answer.pack(pady=(0, 15), ipadx=40, ipady=4)


        # to get next question if index not equals to 9 i.e., question not equal to 0
        #calls check_answer function

        if index != 9:
            next = Button(self.root, text="Next ->", fg="white", bg="#008000",command=lambda: self.check_answers(index=index+1,mode=mode))
            next['font'] = self.myFont
            next.pack(pady=(5,10),ipadx=30,ipady=4)

        #to submit answers and to show user's score in that game
        #calls check_answer function
        if index == 9:
            next = Button(self.root, text="Submit Answers", fg="white", bg="#008000",command=lambda: self.check_answers(index=index+1,mode=mode))
            next['font'] = self.myFont
            next.pack(pady=(5, 10),ipadx=30,ipady=4)

        # to go back to main menu
        self.back = Button(self.root, text="Main Menu", fg="white", bg="#008000", command=lambda: self.confirm())
        self.back['font'] = self.myFont
        self.back.pack(pady=(50, 10), ipadx=40, ipady=4)




    # To confirm whether user really want to exit the game or not
    #gets called whenever MainMenu button of game page is pressed
    #asks whether user really wants to exit
    #if yes his progress doesn't get saved
    #otherwise user stays on game page


    def confirm(self):
        choice = messagebox.askquestion("Exit","Are you sure, Your progress won't be saved")
        if choice =='yes':
            self.load_home()




    #this function is for checking the answer given by user of a particular question is correct or not
    #If the answer is correct the total score of user gets increased by 1
    # and calls the extract_question function to extract next question
    #THis function gets called only when question number is less than 10


    def check_answers(self,index,mode):

            answer=self.answer.get()
            if index!=10:

                # to check answer of every question and increase score by 1 if answer is correct
                #gets called only when question number ranges between 1 to 10 or
                #index ranges between 0 to 9

                if answer.upper()==self.correct_answer or answer==self.correct_number:
                    self.total_correct_answer+=1

            else:
                # to check highscor after game ends and update if current game score is greater than high score
                self.check_highscore(mode,self.total_correct_answer)

            if index != 10:
                # to extract next question
                self.extract_question(mode,index)




    #This function gets called after the quiz is over
    #it is for checking whether the score obtain by user in this quiz is higher than his/her  high score of this mode
    #if it is higher than the previous high score his his high score get updated to new value


    def check_highscore(self,mode,correct):

        high=self.db.check_highscore(self.player_id,mode)
        if correct>high:

            #updating highscore

            response=self.db.update_highscore(self.player_id,mode,correct)

            if response==1:
                print("Highscore Updated")

        else:
            print("Score less than high score")

        #for showing total score of user in current game

        self.show_score(correct)




    #This function gets called after the quiz is over
    #it is for showing the total score of the user in the quiz
    #it has two buttons leaderboard to see the leaderboard and main menu to go back to main menu


    def show_score(self,correct):

        self.clear()

        self.root.minsize(450, 650)
        self.root.maxsize(450, 650)

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 5))

        self.alabel3 = Label(self.root,text="-------------------------------------------------------------------------------------------", fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="R E S U L T ", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(30, 10))

        if correct>5:

            self.label3 = Label(self.root,text="C O N G R A T S", fg="black", bg="#00FF00")
            self.label3.configure(font=("Comic Sans MS", 18, "bold"))
            self.label3.pack(pady=(30, 10))

        self.label4 = Label(self.root, text="You got"+str(correct)+"/10 correct", fg="black", bg="#00FF00")
        self.label4.configure(font=("Comic Sans MS", 15, "bold"))
        self.label4.pack(pady=(20, 10))

        #Leaderboard button to see leaderboard after game completion if user wants to

        self.leaders = Button(self.root, text="Leaderboards", fg="white", bg="#008000",command=lambda: self.leaderboard())
        self.leaders['font'] = self.myFont
        self.leaders.pack(pady=(50, 10), ipadx=70, ipady=4)

        #main menu button to go to main menu
        self.back = Button(self.root, text="Main Menu", fg="white", bg="#008000", command=lambda: self.load_home())
        self.back['font'] = self.myFont
        self.back.pack(pady=(20, 10), ipadx=63, ipady=4)






    #this function gets called whenever leaderboard button is pressed
    #user is asked which difficulty level leaderboard he want to see
    #after getting input from user as easy, normal or hard
    #fetch_leaderboard function gets called


    def leaderboard(self):
        self.clear()

        self.root.minsize(450, 650)
        self.root.maxsize(450, 650)

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 10))

        self.alabel3 = Label(self.root,text="-"*70,fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="L E A D E R B O A R D", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(30, 10))

        self.label3 = Label(self.root, text="Select Difficulty", fg="black", bg="#00FF00")
        self.label3.configure(font=("Comic Sans MS", 15, "bold"))
        self.label3.pack(pady=(5, 10))

        #for easy level scoreboard

        self.easy = Button(self.root, text="Easy", fg="white", bg="#008000",command=lambda: self.fetch_leaderboard(mode=0))
        self.easy['font'] = self.myFont
        self.easy.pack(pady=(30, 10), ipadx=80, ipady=4)

        #for normal level scoreboard

        self.normal = Button(self.root, text="Normal", fg="white", bg="#008000",command=lambda: self.fetch_leaderboard(mode=1))
        self.normal['font'] = self.myFont
        self.normal.pack(pady=(20, 10), ipadx=73, ipady=4)

        #for hard level scoreboard

        self.hard = Button(self.root, text="Hard", fg="white", bg="#008000",command=lambda: self.fetch_leaderboard(mode=2))
        self.hard['font'] = self.myFont
        self.hard.pack(pady=(20, 10), ipadx=80, ipady=4)

        #to go back to main menu

        self.back = Button(self.root, text="Main Menu", fg="white", bg="#008000", command=lambda: self.load_home())
        self.back['font'] = self.myFont
        self.back.pack(pady=(50, 10), ipadx=64, ipady=4)




    #this function gets called after selecting the level of leaderboard user want to see
    #it fetches leaderboard of that particular difficulty from database
    #and calls show_leaderboard function to show the leaderboard


    def fetch_leaderboard(self, mode):
            leader_data = self.db.fetch_leaderboard(mode)
            self.show_leaderboard(leader_data)




    #This function gets called by fetch_leaderboard function
    #and shows tha data fetched by that function i.e., leaderboard on window
    #there is a back button to go back to level selection for leaderboard


    def show_leaderboard(self, data):
        self.clear()

        self.root.minsize(600, 700)
        self.root.maxsize(600, 700)

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 10))

        self.alabel3 = Label(self.root,text="-"*85,fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="L E A D E R B O A R D", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(30, 10))

        self.label2 = Label(self.root, text="Rank \t      Username    \t   Score", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(15, 10))

        if len(data) > 5:
            lim = 5

        else:
            lim = len(data)

        for i in range(lim):
            self.label01 = Label(self.root,text=str(i + 1) + ".      \t    " + data[i][0] + "    \t    " + str(data[i][1]),fg="black", bg="#00FF00")
            self.label01.configure(font=("Footlight MT", 20, "italic"))
            self.label01.pack(pady=(15, 10))

        self.back = Button(self.root, text="<- Back", fg="white", bg="#008000", command=lambda: self.leaderboard())
        self.back['font'] = self.myFont
        self.back.pack(pady=(50, 10), ipadx=70, ipady=4)




    #This function gets called whenever help button is pressed on main menu or homepage
    #This shows details about this app and how to play it


    def help(self):
        self.clear()

        self.root.minsize(950, 900)
        self.root.maxsize(950, 900)

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 10))

        self.alabel3 = Label(self.root,text="-"*80,fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="H E L P", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "bold"))
        self.label2.pack(pady=(15, 10))

        self.help_label=Label(self.root,text="1. You have to login using your email and password.                                                         \n\n 2. If registered you will get redirected to home page otherwise you have to register.     \n\n 3. On home page you can check leaderboard, start a new game or change your password \n on starting new game you will get 3 options based on difficulty i.e., Easy, Normal, Hard.\n\n 4.Select difficulty and your game starts.                                                               "
                                             "            \n\n 5. Questions are multiple choice you will get 4 options from which you have to select one.\n\n 6. There are total of 10 questions.                                                                                     "
                                             "\n\n7. On answering all the questions you will see your score and can check leaderboard also. "
                                             "\n\n This game is developed be ATULYA KUMAR as project on Python programmin language",fg="black", bg="#00FF00")
        self.help_label.configure(font=("Comic Sans MS", 15))
        self.help_label.pack(pady=(5,10))

        self.back = Button(self.root, text="<- Back", fg="white", bg="#008000", command=lambda: self.load_home())
        self.back['font'] = self.myFont
        self.back.pack(pady=(30, 10), ipadx=70, ipady=4)




    #This function is for password updation
    #gets called whenever change password button is pressed on main menu/homepage
    #asks for users old password, new password and to confirm new password


    def take_new_password(self):
        self.clear()

        self.label1 = Label(self.root, text="Quizzyy", fg="black", bg="#00FF00")
        self.label1.configure(font=("Comic Sans MS", 40, "bold"))
        self.label1.pack(pady=(25, 10))

        self.alabel3 = Label(self.root,
                             text="-"*70,
                             fg="black", bg="#00FF00")
        self.alabel3.configure(font=("Comic Sans MS", 10))
        self.alabel3.pack(pady=(5, 10), fill=X)

        self.label2 = Label(self.root, text="Enter Old Password", fg="black", bg="#00FF00")
        self.label2.configure(font=("Comic Sans MS", 20, "italic"))
        self.label2.pack(pady=(15, 10))

        self.old_password = Entry(self.root)
        self.old_password.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.label3 = Label(self.root, text="Enter New Password", fg="black", bg="#00FF00")
        self.label3.configure(font=("Comic Sans MS", 20, "italic"))
        self.label3.pack(pady=(15, 10))

        self.new_password = Entry(self.root)
        self.new_password.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.label4 = Label(self.root, text="Confirm New Password", fg="black", bg="#00FF00")
        self.label4.configure(font=("Comic Sans MS", 20, "italic"))
        self.label4.pack(pady=(15, 10))

        self.con_new_password = Entry(self.root)
        self.con_new_password.pack(pady=(0, 5), ipadx=40, ipady=5)

        self.next = Button(self.root, text="Change Password", fg="white", bg="#008000",
                           command=lambda: self.update())
        self.next['font'] = self.myFont
        self.next.pack(pady=(50, 10), ipadx=55, ipady=4)

        self.back = Button(self.root, text="Main Menu", fg="white", bg="#008000", command=lambda: self.load_home())
        self.back['font'] = self.myFont
        self.back.pack(pady=(30, 10), ipadx=75, ipady=4)




    #extract old password new password and confirm new password from take_new_password
    #if old password is correct and new password and confirm new password matches
    #users password gets updated to new password


    def update(self):
        player = self.player_id
        password = self.old_password.get()
        new_password = self.new_password.get()
        con_new_password = self.con_new_password.get()

        #to check password length is not empty
        if len(new_password) <= 0:
            messagebox.showerror("Error", "Password cannot be empty")

        else:
            if new_password != con_new_password:
                messagebox.showerror("Error", "New Password and Confirm Password doesn't match")

            else:
                #updation of password
                response = self.db.update_password(player, password, new_password)

                if response == -1:
                    messagebox.showerror("Error", "Old Password does not match")

                elif response == 1:
                    messagebox.showinfo("Updated", "Password Updated Successfully")
                    self.load_home()

                else:
                    messagebox.showerror("Error", "Some error occurred")




    #This functions gets called when logout button is pressed on main menu/homepage
    #function clears all the data extractes from database of users which gets extracted at the time of login
    #calls login_page function to load login page for looging in of other user


    def logout(self):
        response = messagebox.askquestion("Confirm", "Are you sure you want to logout?")
        if response == 'yes':

            #deletion of user data before logging out which is fetched from database at time of login

            self.player_id = ''
            self.player_data = []

            #going back to login page

            self.login_page()



#object declaration of quiz class
q = quiz()












































































