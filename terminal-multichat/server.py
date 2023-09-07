import socket, threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 8000)
server_socket.bind(server_address)
server_socket.listen(1)

print("\033[1;33mServidor escuchando en : {}".format(server_address))

def handle_client(client_socket):

    while True:

        name_received = client_socket.recv(1024).decode()
        
        print(f"\033[1;32mCliente {client_address} se conectó con el nombre: {name_received}")
            
        while True:
                
            data = client_socket.recv(1024)
            
            if data:
                print(f"\033[1;36m[{name_received}]: {data.decode()}")

while True:
          
    client_socket, client_address = server_socket.accept()
    print(f"\033[1;32mConexión establecida con {client_address}")

    client_handler_thread = threading.Thread(
        target=handle_client, args=(client_socket,))
    client_handler_thread.start()