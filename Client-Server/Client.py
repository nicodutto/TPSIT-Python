import socket

# Definisce l'indirizzo IP e la porta del server a cui connettersi
server_ip = "192.168.141.164"
server_port = 12345
buffer_size = 1024  # Quando ricevo dei dati dichiaro quanti bit utilizzare, se i dati sono > di 4092 messaggio spezzettato ed error
server_address = (server_ip, server_port)   # Tupla con: IPSERVER, PORTA


# Crea un socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Tirato su il server web:  AF_INET:    SOCK_DGRAM: socket UDP


# Messaggio da inviare al server
message = "Ciao server, questo è un messaggio UDP!".encode()


try:
    # Invio del messaggio
    udp_client_socket.sendto(message, server_address)
    # Ricezione del messaggio del server
    data, address = udp_client_socket.recvfrom(buffer_size)
    print(f"Risposta dal server: {data.decode()}")

except OSError as e:
    print(e)





udp_client_socket.close()
