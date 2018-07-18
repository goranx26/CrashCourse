    
class User():

    def __init__(self, first_name,last_name,login_name,title):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.title = title
        self.login_attempts = 0        

    def describe_user(self):
        print("Name: " + self.first_name.title()+ " " +self.last_name.title())
        print("Title: " + self.title.title())
        print("Login: " + self.login_name)

    def greet_user(self):
        print("Welcome " + self.title.title() + " " +self.first_name.title())
        print("Have a pleasant stay today.")

    def increment_login_attempts(self):
         self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0


goran = User('goran','andersson','root','unethical hacker')

goran.greet_user()

goran.describe_user()

i=1
while i<10:
    goran.increment_login_attempts()
    print("Login attempts: " + str(goran.login_attempts))
    i += 1

goran.reset_login_attempts()
print("RESET, login attempts now: " + str(goran.login_attempts))
