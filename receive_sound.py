import os

os.system("pip install sounddevice")
os.system("pip install numpy")

import sounddevice as sd
import socket
import numpy as np

# Set up the client (phone)
server_ip = "your_laptop_ip"  # Replace with your laptop's IP address
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Set up the audio stream
sample_rate = 44100
block_size = 1024


def callback(outdata, frames, time, status):
    if status:
        print(status, flush=True)
    data = client_socket.recv(4096)
    outdata[:] = np.frombuffer(data, dtype=np.int16).reshape((frames, 2))


with sd.OutputStream(
    callback=callback,
    channels=2,
    dtype=np.int16,
    samplerate=sample_rate,
    blocksize=block_size,
):
    print("Receiving audio... Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing connection...")
        client_socket.close()
