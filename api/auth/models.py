import re
import datetime
from passlib.apps import custom_app_context as pwd_context


class BaseUser:
    """
    A class used to represent user base data.

    ...

    Attributes
    ----------
    firstname : str
        the first name of the user
    lastname : str
        the last name of the user
    othernames : str
        the other names of the user
    phoneNumber : str
        the phone number of the user
    registered : str
        the date and time when the user is created
    id : int
        the user id
    """

    user_id = 1

    def __init__(self, firstname, lastname, othernames, phoneNumber):
        """
        initialize user base attributes
        """
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.phoneNumber = phoneNumber
        self.registered = datetime.datetime.now()
        self.id = BaseUser.user_id
        BaseUser.user_id += 1  
         

class User:
    """
    A class used to represent a User.

    ...

    Attributes
    ----------
    base : class
        inherits class BaseUser attributes
    username : str
        the username of a user
    email : str
        the email of the user
    password : str
        the hashed password of the user
    isAdmin : boolean
        the role of the user (default = False)

    Methods
    -------
    hash_password(password)
        takes in a plain password and stores the hash of it with the user
    validate_user_input
        validates user input (username, email, password)
    validate_base_input
        validates base user input (firstname, lastname, othernames, phone number)
    to_json
        returns user data in json serializable format
    """

    def __init__(self, base, username, email, password):
        """
        initialize user attributes
        """
        self.base = base
        self.username = username
        self.email = email
        self.password = password
        self.isAdmin = False

    def hash_password(self, password):
        """
        takes in a plain password and stores 
        the hash of it with the user
        """
        self.password_hash = pwd_context.encrypt(password)

    def validate_user_input(self):
        """
        validates user input
        returns: error message
        """
        if not self.username or self.username.isspace():
            return "Username field cannot be left empty."
        elif not self.email or self.email.isspace():
            return "Email field cannot be left empty."
        elif not self.password or self.password.isspace():
            return "Password field cannot be left empty."
        elif len(self.password) < 6:
            return "Password too short, must be atleast 6 characters or more."
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return "Enter a valid email address."

    def validate_base_input(self):
        """
        validates user base input
        returns: error message
        """
        if not self.base.firstname or self.base.firstname.isspace():
            return "Firstname field cannot be left empty."
        elif not self.base.lastname or self.base.lastname.isspace():
            return "Lastname field cannot be left empty."
        elif not self.base.othernames or self.base.othernames.isspace():
            return "Othernames field cannot be left empty."
        elif not self.base.phoneNumber or self.base.phoneNumber.isspace():
            return "Phone number field cannot be left empty." 

    @property
    def to_json(self):
        """
        returns user data in json serializable format
        """
        return {
            "id": self.base.id,
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