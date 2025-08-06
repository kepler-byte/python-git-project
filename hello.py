import config
import datetime

def say_hello(name):
    now = datetime.datetime.now()
<<<<<<< HEAD
    print(f"Hello again, {name}! from {config.APP_NAME}")
=======
    print(f"Goodbye, {name}! from {config.APP_NAME}")
>>>>>>> feature-farewell
    print(f"Today is {now.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    say_hello("hello")