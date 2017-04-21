from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
	return 'Flask is running!'

@app.route('/data')
def names():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)

@app.route('/mem')
def mem():
	get_hits = int(os.popen("echo 'stats' | nc 127.0.0.1 11211 | grep get_hits | awk {'print $3'}").read())
	cmd_get = int(os.popen("echo 'stats' | nc 127.0.0.1 11211 | grep cmd_get | awk {'print $3'}").read())
	if get_hits != 0 and cmd_get != 0:
		output = "get_hits is %d\ncmd_get is %d\nGet Percentage is %d"%(get_hits,cmd_get,(get_hits/cmd_get*100))
		return output
	else:
		output = "Gets or Total hits is 0, Quiting..."
		return output

@app.route('/stats')
def stats():
	output = os.popen("echo 'stats' | nc 127.0.0.1 11211").read()
	return output

if __name__ == '__main__':
	app.run()