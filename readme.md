---- Running the application ----
1. In constants.py you can choose the port you want to listen on
2. In client.py line 9 you can input the server machine name or ip to connect to
3. Open a terminal
4. Run the server_program.py file with the server directory of your choice e.g: "python3 /Users/janannibalaskandan/Documents/Projects/DropboxApp/server_program.py /Users/janannibalaskandan/Documents/Projects/DropboxApp/Server_directory"
5. Open a second terminal
6. Run the client_program.py file with the client directory of your choice e.g. "python3 /Users/janannibalaskandan/Documents/Projects/DropboxApp/client_program.py /Users/janannibalaskandan/Documents/Projects/DropboxApp/Client_directory"
7. Add a file to the Client directory 
8. There should be a copy in the server directory
9. Delete the file in the client directory
10. It should be deleted in the server directory

---- Requirements ----
1. Python 3.10
2. Non standard libraries:
   1. tqdm (pip3 install tqdm)
3. This program was developed on macOS 10.13.6

---- Shortcomings and Improvements ----
1. No proper protocol for receiving a file. I wanted to send the filesize to the server so that when that many bytes was received by the server it would finish receiving the file, and continue.
2. Doesn't handle loads larger than 1 file. Can use a queue which is sent to the server and consumed on the server side. The queue can be received by the server and consumed by the server asynchronously.


