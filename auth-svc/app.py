from bottle import Bottle, route, run, get, template, post, request
import pymysql


def createUser(user, password):
	

	mysql_config = {
		'host':'localhost',
		'db':'users',
		'user': 'root',
		'password': 'root'
	}
	cnx = None
	try:
	    	cnx = pymysql.connect(**mysql_config)
		
		insertStr = "INSERT INTO credentials (username, password) VALUES (%s, %s)" 
		cursor = cnx.cursor()
		data = (username, password)
		cursor.execute(insertStr, data)
		cnx.commit
		cursor.close()
	
	    	cnx.close()
	except pymysql.err as err:
	    	print "Failed to connect: {0}".format(err)
	return 1
     


app = Bottle()

users = [{"username": "pepe", "password": "pepe123"},\
	 {"username": "diego", "password": "diego123"}]

@app.route('/hello', method="GET")
def hello():
	return "hello world!"

@app.get('/')
@app.get('/hello/<name>', method="GET")
def greet(name='Stranger'):
	return template('hello {{name}}', name=name)

@app.post('/param')
def hello_json():
	data = request.json
	param = data['param']
	ret = {"status": "OK", "param": param}
	return ret

@app.post('/login')
def login_json():
	data = request.json
	if data in users:
		return {"status": "OK", "descripcion": "Bienvenido"}	
	return {"status login": "error...", "Descripcion": "se ingreso mal el usuario"}

@app.post('/register')	
def register_json():
	data = request.json
	#users.append(data)
	a = createUser(data["username"], data["password"])
	if a:
		return {"status": "OK"}
	else:	
		return {"status": "ERROR"}

run(app, host='127.0.0.1', port=8081)
 
