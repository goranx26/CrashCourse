    
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


class Privileges():
    def __init__(self):
        self.privileges=['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print("Your  admin privileges: ")
        i=1
        for priv in self.privileges:
            print(str(i),".",priv)
            i+=1

class Admin(User):
    def __init__(self,first_name,last_name,login_name,title):
        super().__init__(first_name,last_name,login_name,title)
    
        self.privileges=Privileges()

#add a user and test its methods
yngve_stoor = User('yngve', 'stoor', 'yngve.stoor', 'IT-miffo')
yngve_stoor.greet_user()
yngve_stoor.describe_user()

#add an admin and test the methods
goran = Admin('goran','andersson','root','unethical hacker')
goran.greet_user()
goran.describe_user()
goran.privileges.show_privileges()

i=1
while i<10:
    goran.increment_login_attempts()
    print("Login attempts: " + str(goran.login_attempts))
    i += 1

goran.reset_login_attempts()
print("RESET, login attempts now: " + str(goran.login_attempts))
