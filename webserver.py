import socket
# import mysql.connector
#
# # Test to connect to MySQL db
# config = {
#   'user': 'scott',
#   'password': 'tiger',
#   'host': '127.0.0.1',
#   'database': 'employees',
#   'raise_on_warnings': True,
# }
#
# cnx = mysql.connector.connect(**config)
#
# cnx.close()

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
    HTTP/1.1 200 OK

    Hello, world!
    """

    client_connection.sendall(http_response)
    client_connection.close()
