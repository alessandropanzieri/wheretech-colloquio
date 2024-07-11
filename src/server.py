from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    pass # da implementare

if __name__ == "__main__": app.run()