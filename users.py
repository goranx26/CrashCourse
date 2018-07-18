    
class User():

    def __init__(self, first_name,last_name,login_name,title):
        self.first_name = first_name
        self.last_name = last_name
        self.login_name = login_name
        self.title = title
        

    def describe_user(self):
        print("Name: " + self.first_name.title()+ " " +self.last_name.title())
        print("Title: " + self.title.title())
        print("Login: " + self.login_name)

    def greet_user(self):
        print("Welcome " + self.title.title() + " " +self.first_name.title())
        print("Have a pleasant stay today.")


goran = User('goran','andersson','root','unethical hacker')

goran.greet_user()

goran.describe_user()
