import sys


def system_version():
    sv = sys.version
    return sv

def run():
    print(system_version())


if __name__ == "__main__":
    run()

#print(sys.version)

print(sys.argv)