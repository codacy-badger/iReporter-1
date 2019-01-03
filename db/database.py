class UsersDb:

    def __init__(self):
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)

    def get_all_users(self):
        return self.users_list

    def find_user_by_username(self, username):
        for user in self.users_list:
            if user.username == username:
                return user
        return None

    def check_user(self, username, password):
        for user in self.users_list:
            if username == user.username and password == user.password:
                return user
            return None


class RedflagsDb:

    def __init__(self):
        self.redflags_list = []

    def add_redflag(self, redflag):
        self.redflags_list.append(redflag)

    def get_all_redflags(self):
        return self.redflags_list