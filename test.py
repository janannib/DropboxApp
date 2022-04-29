# DropBox App
# author: Jananni Balaskandan

import unittest
import shutil
import threading
import os
import time
from watcher import Watcher
from handler import Handler
from server import Server


def server():
    server_directory = os.path.join(os.getcwd(), "Server_directory")
    server = Server(server_directory)

    try:
        while True:
            server.receive_data()

    except KeyboardInterrupt:
        pass

    finally:
        server.connection.close()
        server.socket.close()

def client():
    directory = os.path.join(os.getcwd(), "Client_directory")
    handler = Handler()
    watcher = Watcher(directory, handler)
    watcher.run()

class MyTestCase(unittest.TestCase):
    def test(self):
        dir = os.getcwd()
        # --------------------- Start server ------------------------------------------
        t1 = threading.Thread(target=server)
        t1.daemon = True

        t1.start()

        # ---------------------- Start client ------------------------------------------
        t2 = threading.Thread(target=client)
        t2.daemon = True

        t2.start()

        # --------------------- Send file to client directory ---------------------
        test_file = os.path.join(dir, 'Test_file', 'doc_file.docx')
        shutil.move(test_file, os.path.join(dir, 'Client_directory'))
        # --------------------- Check file in server directory --------------------
        destination_file = os.path.join(dir, 'Server_directory', 'doc_file.docx')
        actual = False
        wait = 20
        while wait > 0:
            time.sleep(1)
            if os.path.isfile(destination_file):
                actual = True
                break
            wait -= 1
        # --------------------- Assertion -----------------------------------------
        expected = True

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
