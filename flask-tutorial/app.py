# app.py
from flask import Flask  

app = Flask(__name__) # name for the Flask app (refer to output)

@app.route('/')
def helloWorld():
    return 'Hello World!'


@app.route('/sec')
def second():
    return 'second page'



# running the server
if __name__ == "__main__":
    app.run(debug = True) # to allow for debugging and auto-reload