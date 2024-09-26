import socket
import threading as tr

# Imposta l'IP del server (può essere 0.0.0.0 per ascoltare su tutte le interfacce)
server_ip = "192.168.1.93"
server_port = 12345
buffer_size = 1024

# Crea un socket UDP e lo binda all'indirizzo e alla porta specificati
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((server_ip, server_port))

print(f"Server in ascolto su {server_ip}:{server_port}...")

# Memorizza l'indirizzo del client per inviare messaggi
client_address = None

# Funzione per ricevere messaggi dai client
def receive_messages():
    global client_address
    while True:
        try:
            # Riceve il messaggio dal client
            data, client_address = udp_server_socket.recvfrom(buffer_size)
            print(f"Messaggio ricevuto da {client_address}: {data.decode()}")
        except OSError:
            print("Chiusura del server")
            break

# Funzione per inviare messaggi ai client
def send_messages():
    global client_address
    while True:
        if client_address:  # Verifica se c'è un client connesso
            message = input("Server: ").encode()
            if message.decode() == 'exit':
                print("Chiusura del server.")
                udp_server_socket.close()
                break
            # Invia il messaggio al client
            udp_server_socket.sendto(message, client_address)

# Crea i thread per inviare e ricevere messaggi
thread_receiver = tr.Thread(target=receive_messages)
thread_sender = tr.Thread(target=send_messages)

# Avvia i thread
thread_receiver.start()
thread_sender.start()

# Sincronizzazione per la terminazione dei thread
thread_receiver.join()
thread_sender.join()
