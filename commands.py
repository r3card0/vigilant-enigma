import pandas as pd

def description():
    program_description= """
    This program shows the list of some scripting
    commands
    """
    return program_description

def command_dict():
    commands = {
        "module": ["sys","sys","os"],
        "command": ["sys.argv","sys.version","os.path"],
        "use" : ["shows the current file location","shows the version of . .","implements some useful functions on pathnames"],
        "module example": ["import sys","import sys","import os"],
        "more": [" "," ","www.docs.python.org/3/library/os.path.html"],
    }

    return commands

def table_command():
    df = pd.DataFrame(command_dict())
    return df

def run():
    print(table_command())

if __name__ == "__main__":
    run()