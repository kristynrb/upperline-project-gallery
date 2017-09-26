from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MyNewPass'
app.config['MYSQL_DATABASE_DB'] = 'ProjectGallery'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

api = Api(app)
mysql.init_app(app)

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')

            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            # connect to database
            conn = mysql.connect()
            # MySQL cursor to interact with database
            cursor = conn.cursor()
            # Calling the stored procedure
            cursor.callproc('spCreateUser',(_userEmail,_userPassword))
            data = cursor.fetchall()

            # Returning successful creation message or error
            if len(data) is 0:
               conn.commit()
               return {'StatusCode':'200','Message': 'User creation success'}
            else:
               return {'StatusCode':'1000','Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    app.run(debug=True)

# User API Tutorial: http://codehandbook.org/flask-restful-api-using-python-mysql/
