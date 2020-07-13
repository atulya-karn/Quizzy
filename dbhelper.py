#This program is to help app.py in doing database related work
#like extracting data, inserting user, fetching score updating password etc


import mysql.connector



#---class definition of DBhelper class---


class DBhelper:


    #---constructor of DBhelper class---

    def __init__(self):
        try:
            #---to connect to the database---
            self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='quizzy')
            self.mycursor=self.conn.cursor()
            print("connected to Database")

        except Exception as e:
            print(e)



    #to check email or password entered by user is correct or not at the time of login
    #if correct it will return complete data of user on frontend


    def check_login(self,email,password):
        # to check username and password with database at time of logging in
        self.mycursor.execute("SELECT * FROM players WHERE email LIKE '{}' AND pin LIKE '{}'".format(email,password))
        data = self.mycursor.fetchall()
        return data



    #function to insert a new user into the database
    #return 1 if user is added sucessfully
    #otherwise  return 0


    def insert_user(self, name, email, password, username):

        try:
            self.mycursor.execute("INSERT INTO players (player_id,name,username,email,pin) VALUES (NULL,'{}','{}','{}','{}')".format(name,username, email,password))
            self.conn.commit()
            return 1
        except Exception as e:
            print(e)
            return 0




    #This function is for checking whether username entered by user at the time of registration is available or not
    #if available it returns 1 otherwise 0


    def check_username(self,username):

        try:
            self.mycursor.execute("SELECT username FROM players")
            usernamedata = self.mycursor.fetchall()
            usernames = []
            for i in usernamedata:
                usernames.append(i[0])
            if username not in usernames:
                return 1
            else:
                return 0


        except Exception as e:
            print(e)



    #function to check whether email entered by username is taken/available or not
    #if taken return 0
    #else return 1
    def check_email(self, email):

        try:
            self.mycursor.execute("SELECT email FROM players")
            emaildata = self.mycursor.fetchall()
            emails=[]
            for i in emaildata:
                emails.append(i[0])
            if email in emails:
                return 0
            else:
                return 1

        except Exception as e:
            print(e)




    #function to update password
    # takes player_id, old password and username and updates password
    #if old password does not match with password in database returns -1
    #else update password; if updated successfully returns1
    #else shows error


    def update_password(self,id,password,np):
        try:
            self.mycursor.execute("SELECT pin FROM players WHERE player_id LIKE {}".format(id))
            pin = self.mycursor.fetchall()
            if pin[0][0] != password:
                return -1
            else:
                self.mycursor.execute("UPDATE players SET pin='{}' WHERE player_id LIKE {}".format(np,id))
                self.conn.commit()
                return 1

        except Exception as e:
            print(e)

    #function to fetch leaderboard take mode/level
    #return highest scorers of that mode in descending order
    def fetch_leaderboard(self,mode):

        # for easy level

        if mode==0:
            try:
                self.mycursor.execute("SELECT username, games_played, high_score_easy FROM players ORDER BY high_score_easy DESC")
                data=self.mycursor.fetchall()
                return data
            except Exception as e:
                print(e)


        #for normal level

        elif mode==1:
            try:
                self.mycursor.execute("SELECT username, games_played, high_score_normal FROM players ORDER BY high_score_normal DESC")
                data=self.mycursor.fetchall()
                return data
            except Exception as e:
                print(e)


        #for hard level

        elif mode==2:
            try:
                self.mycursor.execute("SELECT username, games_played, high_score_hard FROM players ORDER BY high_score_hard DESC")
                data=self.mycursor.fetchall()
                return data
            except Exception as e:
                print(e)




    #function to fetch and return highscore of a particular user in a particular mode


    def check_highscore(self,id,mode):

        #for easy level

        if mode==0:
            try:
                self.mycursor.execute("SELECT high_score_easy FROM players WHERE player_id LIKE {}".format(id))
                data = self.mycursor.fetchall()
                return data[0][0]

            except Exception as e:
                print(e)

        #for normal level

        elif mode==1:
            try:
                self.mycursor.execute("SELECT high_score_normal FROM players WHERE player_id LIKE {}".format(id))
                data = self.mycursor.fetchall()
                return data[0][0]

            except Exception as e:
                print(e)


        #for hard level

        elif mode==2:
            try:
                self.mycursor.execute("SELECT high_score_hard FROM players WHERE player_id LIKE {}".format(id))
                data = self.mycursor.fetchall()
                return data[0][0]

            except Exception as e:
                print(e)




    # function to update high score after every games played
    #if score in that match is higher than high score
    #highscore gets updated
    #else remains same


    def update_highscore(self,id,mode,score):


        #for easy level

        if mode == 0:
            try:
                self.mycursor.execute("UPDATE players SET high_score_easy = {} WHERE player_id LIKE {}".format(score,id))
                self.conn.commit()
                return 1

            except Exception as e:
                print(e)
                return 0


        #for normal level

        elif mode == 1:
            try:
                self.mycursor.execute("UPDATE players SET high_score_normal = {} WHERE player_id LIKE {}".format(score,id))
                self.conn.commit()
                return 1

            except Exception as e:
                print(e)
                return 0


        #for hard level

        elif mode == 2:
            try:
                self.mycursor.execute("UPDATE players SET high_score_hard = {} WHERE player_id LIKE {}".format(score,id))
                self.conn.commit()
                return 1

            except Exception as e:
                print(e)
                return 0
















