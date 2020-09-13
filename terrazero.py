#! /usr/bin/python

import zmq
import sys
import argparse
import os
import shlex
import subprocess
import json

DESCRIPTION= """Terrazero CLI
status: underdevel"""



def get_terraform_output():
    """
    Get terraform output data. Assume this on same level as main.tf on your X provider
    """
    current_path = os.path.dirname(os.path.realpath(__file__))
    # get workspace of terraform
    out = subprocess.check_output("terraform workspace show", shell=True)
    workspace = out.strip()
    if workspace == "default":
        state_path = "./terraform.tfstate"
    else:
        state_path = "./terraform.tfstate.d/{}/terraform.tfstate".format(workspace)

    cmd = "terraform output -state={} -no-color -json".format(state_path)
    proc = subprocess.Popen(shlex.split(cmd), cwd=current_path,
        stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    out_json = json.loads(out.decode())
    return out_json


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
    json = get_terraform_output()
    print(json)
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
