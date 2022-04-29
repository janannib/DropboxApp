# DropBox App
# author: Jananni Balaskandan

import socket
import constants
import os
import tqdm

class Server:
    def __init__(self, server_directory):
        #self.ip = socket.gethostname()
        self.ip = ""  # Listen for any machine

        #port = self.get_free_port()
        port = constants.PORT
        self.address = (self.ip, port)

        if socket.has_dualstack_ipv6():
            self.socket = socket.socket(family=socket.AF_INET6,
                                        type=socket.SOCK_STREAM,
                                        proto=0)

        else:
            self.socket = socket.socket(family=socket.AF_INET,
                                        type=socket.SOCK_STREAM,
                                        proto=0)

        self.socket.bind(self.address)
        self.socket.listen(1)

        self.connection = None
        self.client_address = None

        self.server_directory = server_directory

        self.path = None

    def receive_data(self):
        if self.path is None:
            self.connection, self.client_address = self.socket.accept()
            data = self.connection.recv(constants.BUFFERSIZE)
            if data == b'':  # Client data transfer finished
                return
            try:
                file_size, file_name = data.decode('utf-8').split(constants.SEPARATOR)
            except UnicodeError:
                return
            file_size = int(file_size)
            self.path = os.path.join(self.server_directory, file_name)

        if self.path is not None:
            # ------------------ Create file ---------------------------
            if not os.path.isfile(self.path):
                progress = tqdm.tqdm(range(file_size),
                                     "INFO : Writing file",
                                     unit="B",
                                     unit_scale=True,
                                     unit_divisor=constants.BUFFERSIZE)

                with open(self.path, 'wb') as file:
                    while True:
                        bytes_received = self.connection.recv(constants.BUFFERSIZE)
                        if bytes_received == b'':  # Client data transfer finished
                            break
                        file.write(bytes_received)
                        progress.update(len(bytes_received))

            # ----------------- Delete file -----------------------------
            else:
                print("INFO : Deleting file")
                os.remove(self.path)

            self.path = None
            self.connection.close()

    def get_free_port(self):
        test_socket = socket.socket()
        test_socket.bind((self.ip, 0))
        free_port = test_socket.getsockname()[1]
        print(f"INFO : Server listening on '{free_port}'")
        return free_port



