from pynput import keyboard  # Importo modulo per tastiera

letters = "abcdefghijklmnopqrstuvwxyz"

def pressure(key):
        if key.char in letters:
            print(f"E stato premutp il tasto: {key.char}")

# Crea un listener che chiama la funzione pressure ogni volta che un tasto viene premuto
with keyboard.Listener(on_press=pressure) as listener:
    listener.join()  # Mantiene il programma in esecuzione finché il listener è attivo

