# DropBox App
# author: Jananni Balaskandan

import os
import sys
from server import Server


if __name__ == "__main__":

    #server_directory = os.path.join(os.getcwd(), "Server_directory")
    server_directory = sys.argv[1]

    server = Server(server_directory)

    try:
        while True:
            server.receive_data()

    except KeyboardInterrupt:
        pass

    finally:
        server.socket.close()
