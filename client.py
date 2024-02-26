#!/usr/bin/env python



from websockets.sync.client import connect

def hello():
    message = input("What's your message? ")
    responce= input("would you like to send this message to the server?  y/n ")

    if responce == "y" or responce == "Y":
        with connect("ws://localhost:8765") as websocket:
            websocket.send(message)


            message = websocket.recv()
            print(f"Received: {message}")


    else:
        print("ok, have a nice day")



hello()





