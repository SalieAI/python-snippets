'''
Simple Flask code to get ip back
'''

from flask import Flask, request

app = Flask(__name__)

@app.route("/ip", methods=["GET"])
def ip():
  '''
  will return IP
  '''
  return request.headers.get('X-Forwarded-For', request.remote_addr), 200
  
if __name__ == "__main__":
    app.run()
