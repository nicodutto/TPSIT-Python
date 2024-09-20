import socket

# Definisce l'indirizzo IP e la porta del server
server_ip = "192.168.141.150"
server_port = 12345
buffer_size = 1024
server_address = (server_ip, server_port)   # Tupla con: IPCLIENT, PORTA


# Crea un socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM = socket UDP

# Associa l'indirizzo e la porta al socket
udp_server_socket.bind(server_address)

# Dico che il server è in ascolto
print(f"Server in ascolto su {server_ip}:{server_port}...")

# Ricezione del messaggio dal client
data, client_address = udp_server_socket.recvfrom(buffer_size) #bloccante ||  quando un client invia dati si memorizano in data, l'indirizzo in address
print(f"Messaggio ricevuto: {data.decode()} da {client_address}")   # Decode: converte in UTF-8 

# Risposta del server al client
response = "Messaggio ricevuto"
udp_server_socket.sendto(response.encode(), client_address)

# Chiudo il server
udp_server_socket.close()   # Da togliere while true se si vuole chiudere il server dopo la prima risposta











