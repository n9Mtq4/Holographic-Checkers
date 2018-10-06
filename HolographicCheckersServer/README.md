# Websocket
--------
This is the websocket library for the checker game in processing.


#### Usage

In processing:
```python
from com.n9mtq4.checker import CheckerWebsocketServer

port = 8881  # the port of the server

def player1(msg):
    """ This is called every time player 1 send a message to the server"""
    print("player1: " + msg)
    # you can send messages back
    server.sendToPlayer1("sending a message to player 1")
    server.broadcast("message to all players")

def player2(msg):
    """ This is called every time player 2 send a message to the server"""
    print("player2: " + msg)
    server.sendToPlayer2("sending a message to player 2")

def setup():
    global server
    server = CheckerWebsocketServer(port, player1, player2)
    server.start()  # might need to do this in a thread

```

To build this library:
1. Install gradle
2. run `gradle shadowJar` on this project
3. The jar is located at `./build/libs/HolographicCheckersServer-1.0-SNAPSHOT-all.jar`

To actually run, export your processing application:
1. File > Export Application
2. In the exported directory, find the directory `./lib/jycessing`. For the raspberry pi, this will be `./application.linux32/lib/jycessing/`
3. Put the built jar of this library in the directory from step 3

