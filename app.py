from flask import Flask
app = Flask('hello-world')
@app.route('/')
def hello():
 return "Iam LinuJose returning this from github actions merged from PR branch final test!!!\n"
if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 8080)
