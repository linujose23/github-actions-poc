from flask import Flask
app = Flask('hello-world')
@app.route('/')
def hello():
 return "This is simple push to repo poc repo !!!\n"
if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 8080)
