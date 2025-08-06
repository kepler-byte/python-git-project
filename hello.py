import config

def say_hello(name):
    now = datetime.datetime.now()
    print(f"Hello, {name}! from {config.APP_NAME}")
    print(f"Today is {now.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    say_hello("hello")