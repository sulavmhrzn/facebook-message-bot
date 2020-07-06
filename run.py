from utils.app import Bot
import getpass

email = input('Enter your email/number: ')
password = getpass.getpass(prompt='Enter your password: ')

if email and password:
    send_to = input('Enter your friends id: ')
    b = Bot(email, password)
    b.login()
    b.message_to(send_to)
