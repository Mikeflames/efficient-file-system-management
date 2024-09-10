import os
import shutil

def create_file(filename, size_mb):
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

def delete_file(filename):
    os.remove(filename)

def move_file(src, dst):
    shutil.move(src, dst)

def list_files(directory):
    return os.listdir(directory)

if __name__ == "__main__":
    create_file("test_file.txt", 10)
    print("File created")
    print("Files in current directory:", list_files("."))
    move_file("test_file.txt", "test_file_moved.txt")
    print("File moved")
    print("Files in current directory:", list_files("."))
    delete_file("test_file_moved.txt")
    print("File deleted")
    print("Files in current directory:", list_files("."))
