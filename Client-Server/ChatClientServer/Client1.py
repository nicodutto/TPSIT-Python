import socket
import threading as tr

# Definisce l'indirizzo IP e la porta del server a cui connettersi
server_ip = "192.168.1.93"  # Cambia con l'IP corretto del server
server_port = 12345
buffer_size = 1024  # Buffer per la ricezione dei dati
server_address = (server_ip, server_port)

# Crea un socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Funzione per inviare messaggi al server
def send_message():
    while True:
        message = input("Tu: ").encode()
        if message.decode() == 'exit':
            print("Chiusura connessione.")
            udp_client_socket.close()
            break
        # Invia il messaggio al server
        udp_client_socket.sendto(message, server_address)

# Funzione per ricevere messaggi dal server
def receive_message():
    while True:
        try:
            # Riceve il messaggio dal client
            data, _ = udp_client_socket.recvfrom(buffer_size)
            print(f"Messaggio ricevuto da {server_address}: {data.decode()}")
        except OSError:
            break

# Crea i thread per inviare e ricevere messaggi
thread_sender = tr.Thread(target=send_message)
thread_receiver = tr.Thread(target=receive_message)

# Avvia i thread
thread_sender.start()
thread_receiver.start()

# Sincronizzazione per la terminazione dei thread
thread_sender.join()
thread_receiver.join()
