import random
import string


class RandomPasswordGenerator:
    def __init__(self, pass_length):
        self.pass_length = pass_length

    def generate_numbers(self):
        res = ''.join(random.choices(string.digits, k=self.pass_length))
        return res

    def generate_letters(self):
        res = ''.join(random.choices(string.ascii_letters, k=self.pass_length))
        return res

    def generate_mixed(self):
        mixed_values = string.ascii_letters + string.digits + string.punctuation
        res = ''.join(random.choices(mixed_values, k=self.pass_length))
        return res


password_type = input('Enter password type (numbers, letters, mixed): ')
password_length = int(input('Enter password length: '))
password_quantity = int(input('Enter password quantity: '))
r = RandomPasswordGenerator(password_length)

for i in range(1, password_quantity+1):
    if password_type == 'numbers':
        print(r.generate_numbers())
    if password_type == 'letters':
        print(r.generate_letters())
    if password_type == 'mixed':
        print(r.generate_mixed())


