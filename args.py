# contains the command line arguments passed to a script

import sys

def clargs():
    comlargs = sys.argv
    return comlargs

def run():
    print(clargs())


if __name__ == "__main__":
    run()