# DropBox App
# author: Jananni Balaskandan

import os
import sys
from watcher import Watcher
from handler import Handler

if __name__ == "__main__":

    #directory = os.path.join(os.getcwd(), "Client_directory")
    directory = sys.argv[1]


    handler = Handler()
    watcher = Watcher(directory, handler)

    watcher.run()



