from random import choices
from typing import Tuple, List

NUMBERS = "1234567890"
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
SPECIALS = "!@#$%¨&*()-_=+[]~^{};,.<>:/?\\|"


class Account:
    def __init__(self, user: str, email: str, password: str, service: str | None = None) -> None:
        self.service = service
        self.user = user
        self.email = email
        self.password = password

    def __eq__(self, __o: object) -> bool:
        if __o.email == self.email and __o.password == self.password:
            return True
        return False

    def get_service(self):
        return self.service

    def no_service(self):
        return False if self.service else True

    def get_account(self):
        return f"\n{self.user}'s email: {self.email}\n{self.user}'s password: {self.password}"


class PWManager:
    def __init__(self, master_login: Account):
        self.master_login = master_login
        self.__accounts: List[Account] = []

    def add_account(self, master_login, new_account: Account):
        if master_login == self.master_login:
            if new_account.no_service():
                raise Exception("No service found")
            self.__accounts.append(new_account)

    def get_account(self, master_login, account_service):
        if master_login == self.master_login:
            for _account in self.__accounts:
                if _account.get_service() == account_service:
                    return _account.get_account()
                raise Exception('Account not found')

    @staticmethod
    def pw_generator(length=12, password_number=1):
        def new_pass(): return "".join(choices(NUMBERS+CHARS+SPECIALS, k=length))

        if password_number > 1:
            passwords = []
            for _ in range(password_number):
                passwords.append(new_pass())
            return passwords
        return "".join(choices(NUMBERS+CHARS+SPECIALS, k=length))


class LoginSystem:
    def __init__(self):
        self.accounts = dict()

    def registe(self, user, password):
        self.accounts.update({user: password})

    def login(self, user, password):
        if not user in self.accounts.keys():
            print("User doesn't exists")
        elif self.accounts[user] == password:
            print(f"Hello {user}, welcome!")
        else:
            print("password is wrong")


if __name__ == "__main__":
    master = Account("Master", "masterdev@gmail.com", "badpass")
    manager = PWManager(master)
    manager.add_account(master, Account(
        "D'eu", "masterdev@gmail.com", "70-uW8vdBR_462NU", "Google"))
    manager.add_account(master, Account(
        "D'eu", "masterdev@gmail.com", "uQd8vfdR_NU", "Discord"))

    print(manager.pw_generator())
    print(manager.get_account(master, "Google"))

    registed_passwords = {
        "Banana": "banana",
        "Caramaneiro": "dK4Nls_13",
        "D'eu": "70-uW8vdBR_462NU"
    }
    system = LoginSystem()
    for user, password in registed_passwords.items():
        system.registe(user, password)

    system.login("D'eu", "70-uW8vdBR_462NU")
