import socket
import sys
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # The server will respond with a 200 HTTP status code and a message
        self.response_body = "It's all working!!"
        self.response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(self.response_body)}\r\n\r\n{self.response_body}".encode('utf-8')

        # Establishing IPv4 and TCP protocols for the server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allowing the server to use the same address when needed
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):
        # Passing IP and port configurations
        self.sock.bind((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Closes server
        self.sock.close()

    def handle_client(self, conn):
        """Handle communication with the client."""
        with conn:
            request = conn.recv(1024).decode()
            print(f"Received request:\n{request}")

            # Send the HTTP response
            conn.sendall(self.response)

    def start(self):
        # Starts listening
        self.sock.listen()
        print(f"Serving on {self.host}:{self.port}...")
        while True:
            try:
                # Accepts client connection creating another socket entity for the communication
                conn, _ = self.sock.accept()
                threading.Thread(target=self.handle_client, args=(conn,)).start()  # Handle client in a new thread
            except Exception as err:
                print(f"Error: {err}")
                sys.exit(1)


def main():
    # Default HTTP-Proxy interface
    HOST, PORT = "127.0.0.1", 8080
    with Server(HOST, PORT) as server:
        server.start()


if __name__ == "__main__":
    main()
