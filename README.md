# Description

This is a client-server CLI model that sends and receives data by using UDP. Object Oriented Programming is used to create server and client objects. Client just sends simple text messages to the server with the back-off strategy based on the scenario.

# Scenario

Between 12:00 and 17:00 the maximum wait time must be 2 seconds and the exponential backoff must be increased by 2 in each iteration.

Between 17:00 and 23:59 the maximum wait time must be 4 seconds and the exponential backoff must be increased by 3 in each iteration.

Between 23:59 and 12::00 of the next day the maximum wait time must be 1 second and the exponential backoff must be increased by 2 in each iteration.

## Installation

## Usage

Firstly, two terminals are opened, one for the server and one for the client. After writing 'python3' and specifying the name of the file, the role must be shown - either client or server. The next thing is to type the hostname of the machine or the word 'localhost'. Another thing that is necessary for this program is the port number. However, in the code, the default port number is selected and it is not required to write. But if you want to use any particular port, you can write it by typing '-p' before this port number.  Here is an example:
```
python3 spotify_udp.py server localhost -p 4337

python3 spotify_udp.py client localhost
```


Client side terminates after receiving the message from the server, however, you should stop server by pressing Ctrl + C. As long as the server is running, it can make a connection with different clients. 

