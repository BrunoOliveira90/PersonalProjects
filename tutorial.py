from flask import Flask

app = Flask(__main__)

def home():
    return ""


if __name__ == "__main__":
    app.run()

print("New Version 1.01")