#!/usr/bin/env python3

import argparse
import json
import sys
from subprocess import PIPE, Popen


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description='List disks behind a MegaRAID controller')
        parser.add_argument('-debugfile', dest='infile', help='Use this file as input instead of executing storcli')
        parser.add_argument('-sudo', dest='sudo', help='Use sudo to execute storcli')
        parser.add_argument('-storcli', dest='storcli', help='Path to storcli')
        parser.add_argument('-intf', dest='intf', help='Which kind of disks to list')
        parser.add_argument('-verbose', dest='verbose', help='Don\'t swallow errors')
        parser.set_defaults(infile='')
        parser.set_defaults(sudo=False)
        parser.set_defaults(storcli="storcli")
        parser.set_defaults(intf="SAS")
        parser.set_defaults(verbose=False)
        self.args = parser.parse_args()

    def load(self):
        if self.args.infile != '':
            f = open(self.args.infile, 'r')
            self.val = f.read()
            f.close()
        else:
            if self.args.sudo:
                args = ['sudo']
            else:
                args = []
            args.extend([self.args.storcli, "/call/eall/sall", "show", "J"])
            cliproc = Popen(args, stdout=PIPE, bufsize=8192)
            cliproc.wait()
            (indata, _) = cliproc.communicate()
            self.val = indata.decode('UTF-8')

        if self.args.verbose:
            print (self.val)
        self.val = json.loads(self.val)

    def decode_and_print(self):
        for item in self.val["Controllers"]:
            for disk in item["Response Data"]["Drive Information"]:
                if disk['Intf'] == self.args.intf:
                    print ("megaraid,{}".format(disk["DID"]))

    def run(self):
        try:
            self.load()
            self.decode_and_print()
        except:
            if (self.args.verbose):
                print ("Unexpected error:", sys.exc_info()[0])
                raise
            return


obj = Main()
obj.run()
