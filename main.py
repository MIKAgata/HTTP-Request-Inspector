import socket

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Listening on {PORT}...")

while True:
    client, addr = server.accept()
    print(f"\nConnection from {addr}")

    request = client.recv(4096).decode()

    print("----- RAW REQUEST -----")
    print(request)

    lines = request.split("\r\n")

    request_line = lines[0]
    method, path, version = request_line.split()

    print("\n----- PARSED DATA -----")
    print("Method:", method)
    print("Path:", path)
    print("HTTP Version:", version)

    print("\nHeaders:")
    for line in lines[1:]:
        if line == "":
            break
        print(line)

    response = """HTTP/1.1 200 OK
Content-Type: text/plain

Request received
"""

    client.send(response.encode())
    client.close()