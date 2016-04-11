from flask import Flask
app = Flask(__name__)
print ("about to start")

@app.route ("/")
def hello():
    # test comment
    print ("Request received")
    return ("Hello World")
    
if __name__ == "__main__":
    print ("Here we go")
    app.run()    
    