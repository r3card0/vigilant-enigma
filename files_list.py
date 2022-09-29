import os

def list_directory_content():
    choosed_directory= str(input('Enter the name of the directory: '))
    root = os.path.join('..', choosed_directory)
    for directory, subdir_list, file_list in os.walk(root):
        print('Directory:', directory)
        for name in subdir_list:
            print('Subdirectory:', name)
        for name in file_list:
            print('File:', name)
        print()

def run():
    list_directory_content()

if __name__ == "__main__":
    run()