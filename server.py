from flask import Flask  
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<string:name>') 
def hi(name):
    print(name)
    return "Hello, " + name

@app.route('/repeat/<int:num>/<string:name>') 
def hello(num, name):
    return f"{name * num}"

# @app.route('/ ')
# def try_again():
#     return f"Sorry! No response. Try again."

if __name__=="__main__":    
    # app.run(debug=True)
    app.run(debug=True, host="localhost", port=8000)