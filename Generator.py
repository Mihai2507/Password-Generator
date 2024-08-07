import random


def generate_password(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    password = ''.join(random.choice(chars) for i in range(length))
    print(password)
