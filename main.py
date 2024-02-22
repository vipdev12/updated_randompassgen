import random
import string


class RandomPasswordGenerator:
    def __init__(self, pass_length):
        self.pass_length = pass_length

    def generate_password(self):
        pass


class RandomLetterPasswordGenerator(RandomPasswordGenerator):

    def generate_password(self):
        res = ''.join(random.choices(string.ascii_letters, k=self.pass_length))
        return res


class RandomMixedPasswordGenerator(RandomPasswordGenerator):
    def generate_password(self):
        mixed_values = string.ascii_letters + string.digits + string.punctuation
        res = ''.join(random.choices(mixed_values, k=self.pass_length))
        return res


class RandomNumberPasswordGenerator(RandomPasswordGenerator):
    def generate_password(self):
        res = ''.join(random.choices(string.digits, k=self.pass_length))
        return res


password_type = input('Enter password type (numbers, letters, mixed): ')
password_length = int(input('Enter password length: '))
password_quantity = int(input('Enter password quantity: '))

for i in range(1, password_quantity+1):
    if password_type == 'numbers':
        print(RandomNumberPasswordGenerator(password_length).generate_password())
    if password_type == 'letters':
        print(RandomLetterPasswordGenerator(password_length).generate_password())
    if password_type == 'mixed':
        print(RandomMixedPasswordGenerator(password_length).generate_password())


