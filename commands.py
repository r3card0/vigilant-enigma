import pandas as pd

def description():
    program_description= """
    This program shows the list of some scripting
    commands
    """
    return program_description

def command_dict():
    commands = {
        "module": ["sys","sys","os","os","os"],
        "command": ["sys.argv","sys.version","os.path","os.getcwd()","os.chdir()"],
        "use" : ["shows the current file location","shows the version of . .","implements some useful functions on pathnames","returns current working directory of a process","changes the current directory to the given path. It returns None in all the cases"],
        "module example": ["import sys","import sys","import os","import os","import os"],
        "more": [" "," ","www.docs.python.org/3/library/os.path.html","https://www.tutorialspoint.com/python/os_getcwd.html","https://www.tutorialspoint.com/python/os_chdir.htm"],
    }

    return commands

def table_command():
    df = pd.DataFrame(command_dict())
    return df

def run():
    print(table_command())

if __name__ == "__main__":
    run()