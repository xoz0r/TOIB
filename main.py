import string
import itertools
import time

password_real = "rtpa"
start_time = time.time()

guess_password_set = string.digits + string.ascii_letters + string.punctuation
guess_password_length = 1


def string_iter(string, length):
    yield from itertools.product(string, repeat=length)


while True:
    for password_set in string_iter(guess_password_set, guess_password_length):
        password_string = ''.join(password_set)
        if password_string == password_real:
            end_time = time.time()
            exec_time = end_time - start_time
            print("Пароль был подобран за {} секунд. Пароль: {}".format(exec_time, password_string))
            exit()
    guess_password_length += 1