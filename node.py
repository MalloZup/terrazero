#! /usr/bin/python

import time
import zmq
import subprocess
 

def main():
    port= "5556"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind ("tcp://*:%s" % port)

    while True:
        message = socket.recv()
        try:
           out = subprocess.check_output(message, shell=True)
        except:
           out = "error when running command {0}".format(message)
        time.sleep (1)
        socket.send(out)

if __name__ == "__main__":
    main()
