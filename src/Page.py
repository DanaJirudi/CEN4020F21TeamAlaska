import re
from src.database_access import database_access as Database
from src.User import *
from src.PostedJob import PostedJob
db = Database("InCollege.sqlite3")


class Page:
    # each page will "render" the appropriate "form" or prompt
    def __init__(self):
        # current login info
        self.user = User("", "", "", "", "english",
                         True, True, True, False, db)
        # stack is to implement the navigation functionality
        self.page_stack = [0]
        # Numbered pages so they're easily added to the stack and then called
        self.index = {
            0: {
                "view": self.home_page
            },
            1: {
                "view": self.play_video_page
            },
            2: {
                "view": self.find_people_page
            },
            3: {
                "view": self.register_page
            },
            4: {
                "view": self.login_page
            },
            5: {
                "view": self.post_job_page
            },
            6: {
                "view": self.skills_page
            },
            7: {
                "view": self.useful_links_page
            },
            8: {
                "view": self.general_page
            },
            9: {
                "view": self.important_links_page
            },
            10: {
                "view": self.privacy_page
            },
            11: {
                "view": self.guest_controls_page
            },
            12: {
                "view": self.language_page
            },
            13: {
                "view": self.option_switch_page
            }
        }

    def home_page(self):
        # I want the home page to view different option depending on whether or not the user is authenticated
        if not self.user.authorized:
            c = int(input("Welcome to InCollege: *** Where you're no longer going to be broke ***\nAll of our broke students managed to find job!!!"
                          "\n\n1 - Play Video\n2 - People you may know\n3 - Register\n4 - Login\n5 - Useful Links\n6 - InCollege Important Links\nEnter a choice: "))
            if c == 1:
                self.page_stack.append(1)
                self.play_video_page()
            if c == 2:
                self.page_stack.append(2)
                self.find_people_page()
            if c == 3:
                self.page_stack.append(3)
                self.register_page()
            if c == 4:
                self.page_stack.append(4)
                self.login_page()
            if c == 5:
                self.page_stack.append(7)
                self.useful_links_page()
            if c == 6:
                self.page_stack.append(9)
                self.important_links_page()
        else:
            c = int(input(
                "1 - Search for a job\n2 - Find people you may know\n3 - learn a new skill\n4 - Useful Links\n5 - InCollege Important Links\nEnter a choice: "))
            if c == 1:
                self.page_stack.append(5)
                self.post_job_page()
            if c == 2:
                self.page_stack.append(2)
                self.find_people_page()
            if c == 3:
                self.page_stack.append(6)
                self.skills_page()
            if c == 4:
                self.page_stack.append(7)
                self.useful_links_page()
            if c == 5:
                self.page_stack.append(9)
                self.important_links_page()

    def useful_links_page(self):
        # select from links
        choice = int(input(
            "1 - General\n2 - Browse InCollege\n3 - Business Solutions\n4 - Directories\n5 - Previous Page\nEnter a choice: "))

        # general
        if choice == 1:
            self.page_stack.append(8)
            self.general_page()

        # browse incollege
        if choice == 2:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # business solutions
        if choice == 3:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # directories
        if choice == 4:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # previous page
        if choice == 5:
            self.back_page()

    def general_page(self):
        # select from links under the general page
        choice = int(input(
            "1 - Sign Up\n2 - Help Center\n3 - About\n4 - Press\n5 - Blog\n6 - Careers\n7 - Developers\n8 - Previous Page\nEnter a choice: "))

        # sign up/log in
        if choice == 1:
            logORreg = int(
                input("Do you already have an account?\n1 - Yes\n2 - No\nEnter a choice: "))
            if logORreg == 1:
                self.page_stack.append(4)
                self.login_page()
            if logORreg == 2:
                self.page_stack.append(3)
                self.register_page()

        # help center
        if choice == 2:
            self.page_stack.append(-1)
            print("We're here to help")
            self.back_option()

        # about
        if choice == 3:
            self.page_stack.append(-1)
            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
            self.back_option()

        # press
        if choice == 4:
            self.page_stack.append(-1)
            print(
                "In College Pressroom: Stay on top of the latest news, updates, and reports")
            self.back_option()

        # blog
        if choice == 5:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # careers
        if choice == 6:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # developers
        if choice == 7:
            self.page_stack.append(-1)
            # FUNCTION TO BE ADDED IN FUTURE EPICS
            # MAKE SURE YOU ADD AN INDIVIDUAL BACK OPTION FOR THE FUNCTION INSERTED OR LEAVE THE ONE CURRENTLY IN PLACE
            print("Under construction")
            self.back_option()

        # previous page
        if choice == 8:
            self.back_page()

    def important_links_page(self):
        choice = int(input("1 - Copyright Notice\n2 - About\n3 - Accessibility\n4 - User Agreement\n5 - Privacy Policy"
                           "\n6 - Cookie Policy\n7 - Copyright Policy\n8 - Brand Policy\n9 - Languages\n10 - Previous Page\nEnter a choice: "))

        # copyright notice
        if choice == 1:
            self.page_stack.append(-1)
            print("(c) 2021 InCollege. All rights reserved")
            self.back_option()

        # about
        if choice == 2:
            self.page_stack.append(-1)
            print("InCollege is an application designed to allow college students to search and apply for jobs and connect with other students.")
            self.back_option()

        # accessibility
        if choice == 3:
            self.page_stack.append(-1)
            print("Here at InCollege we continue to develop our user experience. Keep an eye out for new accessibility features in the future.")
            self.back_option()

        # user agreement
        if choice == 4:
            self.page_stack.append(-1)
            print(
                "As a user of InCollege you give us the right to use any and all of your data for free.")
            self.back_option()

        # privacy policy
        if choice == 5:
            self.page_stack.append(10)
            self.privacy_page()

        # cookie policy
        if choice == 6:
            self.page_stack.append(-1)
            print("At the moment InCollege does not collect cookies.")
            self.back_option()

        # copyright policy
        if choice == 7:
            self.page_stack.append(-1)
            print("No image or information from this site may be reproduced or copied without written permission from the InCollege legal team.")
            self.back_option()

        # brand policy
        if choice == 8:
            self.page_stack.append(-1)
            print(
                "Our brand aims to bring the best talent to the workforce by connecting people.")
            self.back_option()

        # languages
        if choice == 9:
            self.page_stack.append(12)
            self.language_page()
            # self.back_page()

        # Previous Page
        if choice == 10:
            self.back_page()

    def play_video_page(self):
        print("Video is now playing...")
        # back_option prompts the user to enter 0 if they wanna go back
        self.back_option()

    def login_page(self):
        res = self.login()
        if res:
            self.user.authorize()
        # Once the user logs in, they get redirected to the home page
        self.page_stack.append(0)
        self.home_page()

    def register_page(self):
        res = self.register()
        if res:
            # the user is now authenticated, they'll view things slightly different
            self.user.authorize()
        # Once the user logs in, they get redirected to the home page
        self.page_stack.append(0)
        self.home_page()

    def find_people_page(self):
        fname = input("Enter your friend's firstname: ")
        lname = input("Enter your friend's lastname: ")
        find_friend = (
            'SELECT * FROM users WHERE firstname = ? AND lastname = ?')
        # the friend input is searched for in the db
        res = db.execute(find_friend, (fname, lname))
        # if the friend exits in our database
        if res:
            print("They are a part of the InCollege system")
            # if the user hasn't logged in, they'll view the below options
            if not self.user.authorized:
                c = int(
                    input("Would you like to join?\n1-Regiser\n2-Login\n0 - To go back: "))
                if c == 1:
                    self.page_stack.append(3)
                    self.register_page()
                elif c == 2:
                    self.page_stack.append(4)
                    self.login_page()
                elif c == 0:
                    self.back_page()
        else:
            # your friend is imaginary and doesn't exist
            print("They are not yet a part of the InCollege system yet")
            self.back_option()

    # function to post a job to the database, returns true if successful, false otherwise
    def postjob(self):
        # check if there are more than 5 jobs
        numjobs = len(db.execute('SELECT * FROM jobs'))
        if(numjobs >= 5):
            print("There are already 5 jobs. Please try again later\n")
            return False

        else:
            temp = PostedJob
            temp.name = self.user.username
            temp.title = input("Please enter the job's title: ")
            temp.description = input("Please enter a description of the job: ")
            temp.employer = input("Who is the employer of the job? ")
            temp.location = input("Where is this job located? ")
            while True:
                try:
                    temp.salary = float(
                        input("Please estimate the salary of the job (only numbers): "))
                    break
                except Exception:
                    print("Not a valid number. Try again.")

            # insert object member values into database
            db.execute('INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?)', [
                       temp.name, temp.title, temp.description, temp.employer, temp.location, temp.salary])

            print("Thanks your job was posted! Returning to the previous menu...")
            return True

    def post_job_page(self):
        if self.user.authorized:
            self.postjob()
            # this is to go back a level
            self.back_option()

    def skills_page(self):
        skill = input(
            '\n1 - JavaScript\n2 - Python\n3 - SQL Sever\n4 - MongoDB\n5 - Design Patterns\nEnter a choice: ')
        if skill:
            print('under construction')
        self.back_option()

    def language_page(self):
        print("Select a language:")
        language = input(
            '1 - English\n2 - Spanish\n3 - Previous Page\nEnter a choice: ')
        # Previous Page
        if language == '3':
            self.back_page()
        # Try to set language until valid input is entered
        try:
            self.user.set_language(language)
            print("Language set.\n")
            self.back_page()
        except ValueError as e:
            print("{} Please try again.".format(e))
            self.language_page()

    def option_switch_page(self) -> bool or None:
        switch = input("1 - On\n2 - Off\n3 - Previous Page\nEnter Choice: ")
        if switch == '1':
            return True
        elif switch == '2':
            return False
        else:
            return None

    def privacy_page(self):
        print("Here at InCollege we do not guarantee the security of your data.")
        privacy_option = int(
            input("1 - Guest Controls\n2 - Previous Page\nEnter a choice: "))
        # gues control
        if privacy_option == 1:
            self.page_stack.append(11)
            self.guest_controls_page()
        # Previous Page
        elif privacy_option == 2:
            self.back_page()

    def guest_controls_page(self):
        option = input(
            '\n1 - Email Notifications\n2 - SMS notifications\n3 - tareted ads\n4 - Previous Page\nEnter a choice: ')
        # Email notifications
        if option == '1':
            self.page_stack.append(13)
            switch = self.option_switch_page()
            if switch:
                self.user.set_email_notification(switch)
            else:
                self.back_page()
        # sms notifications
        elif option == '2':
            self.page_stack.append(13)
            switch = self.option_switch_page()
            if switch:
                self.user.set_sms_notification(switch)
            else:
                self.back_page()
        # targeted ads
        elif option == '3':
            self.page_stack.append(13)
            switch = self.option_switch_page()
            if switch:
                self.user.set_ad_notification(switch)
            else:
                self.back_page()
        # previous page
        elif option == '4':
            self.back_page()

    # goes up a level to the previous page
    def back_page(self):
        # call the function for the previous page
        self.page_stack.pop()
        prev = self.page_stack[-1]
        self.index[prev]['view']()

    def back_option(self):
        c = input("0 - To go back: ")
        if c == '0':
            self.back_page()

    ################ OLD FUNCTIONS ##############
    def get_credentials(self, register: False):
        # returns the credentials. Called either in login() or register()
        user = input('Enter username: ')
        password = input('Enter password: ')
        if register:
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            return (user, password, firstname, lastname)
        return (user, password)

    def login(self):
        while True:
            cred = self.get_credentials(False)
            # checks if the credentials exist in the users table
            user = get_user_by_login(cred[0], cred[1], db)
            if user:
                self.user = user
                print('You have successfully logged in\n')
                return True
            else:
                print('Incorrect username / password, please try again\n')
                return False

    def register(self):
        # checking the number of accounts already registered
        num_accounts = len(db.execute('SELECT * FROM users'))
        if int(num_accounts) >= 5:
            print("All permitted accounts have been created, please come backlater\n")
        else:
            # if a new user is allowed to register, it prompts them to enter credentials
            cred = self.get_credentials(True)
            # the below function returns a boolean as to whether or not the password is secure
            satisfies = self.is_password_secure(cred[1])
            if satisfies:
                # posting data to the database
                self.user = create_user(cred, db)
                print("An account for " +
                      cred[0] + " was registered successfully")
                return True
            else:
                print('Weak Password')
                return False

    def is_password_secure(self, pw):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%^()*#?&])[A-Za-z\d@$!#%^()*?&]{8,12}$"
        pattern = re.compile(reg)
        res = re.match(pattern, pw)
        return res != None
