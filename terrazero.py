#! /usr/bin/python

import zmq
import sys
import argparse

DESCRIPTION= """Terrazero CLI
status: underdevel"""


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-c", "--command", default="", help="command to execute on nodes")

    args = parser.parse_args()
    return parser, args


# todo: get all ips from terraform output

port = "5556"
target_host = "tcp://localhost:%s" % port
def main():
    # parse arguments and validation
    parser, args = parse_arguments()
    if args.command == "":
        print("Please provide command -c to run on nodes")
        exit(1)

    # create socket for sending messages
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect (target_host)

    socket.send (args.command)
    message = socket.recv()
    print("Command output: {0}".format(message))

if __name__ == "__main__":
    main()
