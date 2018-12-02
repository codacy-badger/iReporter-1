import datetime


class BaseUser:

    user_id = 0

    def __init__(self, firstname, lastname, othernames, phoneNumber):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.phoneNumber = phoneNumber
        self.registered = datetime.datetime.now()
        self.id = BaseUser.user_id
        BaseUser.user_id += 1


class User:

    def __init__(self, base, username, email, password):
        self.base = base
        self.username = username
        self.email = email
        self.password = password
        self.isAdmin = False

    def validate_input(self):
        if not self.username or self.username.isspace():
            return "Username field cannot be left empty."
        elif not self.email or self.email.isspace():
            return "Email field cannot be left empty."
        elif not self.password or self.password.isspace():
            return "Password field cannot be left empty."
 
    def to_json(self):
        return {
            "id": self.base.user_id,
            "firstname": self.base.firstname,
            "lastname": self.base.lastname,
            "othernames": self.base.othernames,
            "username": self.username,
            "registered": self.base.registered,
            "admin": self.isAdmin,
            "email": self.email,
            "password": self.password, 
            "phoneNumber": self.base.phoneNumber
        }
   