from utils.app import Bot
import getpass


def run():
    
    email = input('Enter your email/number: ')
    password = getpass.getpass(prompt='Enter your password: ')
    if email and password:
        send_to = input('Enter your friends id: ')
        # no need of unnecessary driver args
        # we only use chromium now
        b = Bot(email, password)
        b.login()
        b.message_to(send_to)


if __name__ == "__main__":
    run()
