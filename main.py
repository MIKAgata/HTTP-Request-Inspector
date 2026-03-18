import socket
from core.display import main, get_clear

# Definisi Warna (ANSI Escape Codes)
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

get_clear()
main()

HOST = "127.0.0.1"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"{GREEN}{BOLD}Listening on http://{HOST}:{PORT} ...{RESET}")

while True:
    client, addr = server.accept()
    try:
        data = client.recv(4096)
        if not data:
            client.close()
            continue

        request = data.decode('utf-8')
        
        # Header Log Koneksi
        print(f"\n{BLUE}{'='*40}{RESET}")
        print(f"{CYAN}Connection from:{RESET} {YELLOW}{addr}{RESET}")
        print(f"{BLUE}{'='*40}{RESET}")

        lines = request.split("\r\n")
        if len(lines) > 0:
            request_line = lines[0]
            parts = request_line.split()
            
            if len(parts) == 3:
                method, path, version = parts
                
                print(f"{BOLD}----- PARSED DATA -----{RESET}")
                print(f"{CYAN}Method      :{RESET} {GREEN}{method}{RESET}")
                print(f"{CYAN}Path        :{RESET} {YELLOW}{path}{RESET}")
                print(f"{CYAN}HTTP Version:{RESET} {version}")

                print(f"\n{BOLD}Headers:{RESET}")
                for line in lines[1:]:
                    if line == "":
                        break
                    # Memberi warna berbeda untuk Key: Value pada Header
                    if ": " in line:
                        key, val = line.split(": ", 1)
                        print(f"  {BLUE}{key}{RESET}: {val}")
                    else:
                        print(f"  {line}")

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Connection: close\r\n"
            "\r\n"
            "Request received successfully!"
        )

        client.sendall(response.encode('utf-8'))
        print(f"\n{GREEN}✔ Response sent successfully!{RESET}")

    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")
    finally:
        client.close()