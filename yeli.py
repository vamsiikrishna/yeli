from subprocess import call
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/pull', methods=['POST'])
def pull():
	github_ips = ['207.97.227.253', '50.57.128.197', '108.171.174.178']
	req_ip = request.remote_addr
	if req_ip in github_ips:
		call(['git pull'], shell=True)

@app.route('/')
def oh_hai():
	req_ip = request.remote_addr
	return "Hello "+req_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0')