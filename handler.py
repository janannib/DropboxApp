# DropBox App
# author: Jananni Balaskandan

import os
from watchdog.events import FileSystemEventHandler
from client import Client
import constants


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        try:
            self.client = Client()
            self.client.create_socket()

            self.client.connect_to_server()

            path = event.src_path
            file_size = os.path.getsize(path)
            file_name = os.path.basename(path)

            self.client.socket.send(f"{file_size}{constants.SEPARATOR}{file_name}".encode('utf-8'))

            with open(path, "rb") as file:
                reading = True
                while reading:
                    bytes = file.read(constants.BUFFERSIZE)
                    if not bytes:
                        reading = False
                    self.client.socket.sendall(bytes)

            self.client.socket.close()
        finally:
            self.client.socket.close()

    def on_deleted(self, event):
        try:
            self.client = Client()
            self.client.create_socket()

            self.client.connect_to_server()

            path = event.src_path
            file_size = 0
            file_name = os.path.basename(path)
            self.client.socket.send(f"{file_size}{constants.SEPARATOR}{file_name}".encode())

            self.client.socket.close()
        finally:
            self.client.socket.close()

    def on_modified(self, event):
        # TODO: partial transfer of files
        pass