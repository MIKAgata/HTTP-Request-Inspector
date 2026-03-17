import socket
from core.display import main, get_clear

# Initialize display
get_clear()
main()

HOST = "127.0.0.1"
PORT = 9999

# Create and bind the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow immediate reuse of the port after stopping the script
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"Listening on http://{HOST}:{PORT} ...")

while True:
    client, addr = server.accept()
    try:
        # Receive the request
        data = client.recv(4096)
        if not data:
            client.close()
            continue

        request = data.decode('utf-8')
        print(f"\nConnection from {addr}")
        print("----- RAW REQUEST -----")
        print(request)

        lines = request.split("\r\n")
        if len(lines) > 0:
            request_line = lines[0]
            parts = request_line.split()
            
            # Ensure the request line is valid (Method Path Version)
            if len(parts) == 3:
                method, path, version = parts
                print("\n----- PARSED DATA -----")
                print(f"Method: {method}")
                print(f"Path: {path}")
                print(f"HTTP Version: {version}")

                print("\nHeaders:")
                for line in lines[1:]:
                    if line == "":
                        break
                    print(line)

        # Standard HTTP response with \r\n line endings
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Connection: close\r\n"
            "\r\n"
            "Request received successfully!"
        )

        client.sendall(response.encode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()