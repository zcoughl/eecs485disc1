from flask import Flask
from flask.ext.mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'

mysql.init_app(app)

@app.route("/helloworld")
def hello():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM test.testdata''')
	messages = cur.fetchall()
	return str(messages)

if __name__ == "__main__":
	app.run()