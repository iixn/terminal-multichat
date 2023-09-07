import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 8000)
client_socket.connect(server_address)

print("\033[1;33mConectado al servidor : {}".format(server_address))

my_name = input("\033[1;36mEscribe tu nombre: ")

while my_name == "":

    print("\033[1;31mNo es un nombre valido")
    my_name = input("\033[1;36mEscribe tu nombre: ")

client_socket.send(my_name.encode())

try:
    while True:

        message = input("\033[1;36mEscribe tu mensaje: ")

        if message == "":
            continue
        else: 
            client_socket.send(message.encode())

except KeyboardInterrupt:

    print("\033[1;31mCliente detenido por el usuario.")

finally:

    client_socket.close()