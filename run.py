from utils.app import Bot
import getpass


def run():
    driver = input(
        'Enter driver name (Firefox | default: Chrome) : ').capitalize()
    email = input('Enter your email/number: ')
    password = getpass.getpass(prompt='Enter your password: ')
    if email and password:
        send_to = input('Enter your friends id: ')
        if driver:
            b = Bot(email, password, webd=driver)
            b.login()
            b.message_to(send_to)
        else:
            b = Bot(email, password)
            b.login()
            b.message_to(send_to)


if __name__ == "__main__":
    run()
