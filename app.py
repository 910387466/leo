from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def is_login(func):
    def wrapper():
        print "IS LOGIN"
        func()
    return wrapper;

@is_login
@app.route('/<name>', methods=['POST', 'GET'])
def index(name=None):
    if name == None:
        name = ''
	return render_template('index.html', name=name)

@is_login
@app.route('/admin', methods=['POST', 'GET'])
def admin(name=None):
    resp = make_response(render_template('admin.html'))
    resp.headers['X-Powered-By'] = 'Leo'
    resp.headers['X-Used-By'] = 'YANG'
    resp.set_cookie('SESSION_ID', 'DU998IU')
    return resp

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    return resp

if __name__ == "__main__":
	app.run(debug=True)
