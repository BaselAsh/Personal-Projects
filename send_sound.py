import sounddevice as sd
import socket
import numpy as np

# Set up the server (laptop)
server_ip = "0.0.0.0"  # Use 0.0.0.0 to bind to all available interfaces
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Listening on {server_ip}:{server_port}")

# Accept a connection from the phone
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Set up the audio stream
sample_rate = 44100
block_size = 1024


def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    client_socket.sendall(indata.tobytes())


with sd.InputStream(
    callback=callback,
    channels=2,
    dtype=np.int16,
    samplerate=sample_rate,
    blocksize=block_size,
):
    print("Streaming audio... Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing connection...")
        client_socket.close()
        server_socket.close()
