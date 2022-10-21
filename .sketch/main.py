from random import randrange


# create password
def new_password() -> str:
    """ creates a password like: 00-aa0aaa_000aa, 70-uW8vdBR_462NU, ..."""
    # NLLNLLLL_NN
    password_head = f'{_new_number(2)}-'
    body = f'{_new_letter(2)}{_new_number()}{_new_letter(4)}'
    tail = f'_{_new_number(3)}{_new_letter(2).upper()}'
    return password_head+body+tail


def _new_number(digits=1) -> str:
    number = str(randrange(0, 9))
    if digits == 1:
        return number
    return number + _new_number(digits-1)


def _new_letter(digits=1) -> str:
    illegal_range = [i for i in range(91, 97)]
    letter = chr(new if not (new := randrange(65, 122)) in illegal_range
                 else randrange(97, 122))
    if digits == 1:
        return letter
    return letter + _new_letter(digits-1)


# validate password
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
    registed_passwords = {
        "Banana": "banana",
        "Caramaneiro": "dK4Nls_13",
        "D'eu": "70-uW8vdBR_462NU"
    }

    system = LoginSystem()
    for user, password in registed_passwords.items():
        system.registe(user, password)

    system.login("d'eu", "70-uW8vdBR_462NU")

    # while True:
    #     cmd = input(">")
