# DropBox App
# author: Jananni Balaskandan

import socket
import constants

class Client:
    def __init__(self):
        self.ip = socket.gethostname()  # Input server machine name or ip

        self.port = constants.PORT

    def create_socket(self):
        self.socket = socket.socket(family=socket.AF_INET,
                                    type=socket.SOCK_STREAM,
                                    proto=0,
                                    fileno=None)

    def connect_to_server(self):
        server_address = (self.ip, self.port)
        self.socket.connect(server_address)


