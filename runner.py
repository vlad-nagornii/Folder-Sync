import sys
import time
import os
import log
import hashlib
import config

def copy_directory(source_directory, replica_directory):
    # creates new replica directory if necessary
    if not os.path.isdir(replica_directory):
        os.makedirs(replica_directory)
        log.update_directory(source_directory)
    
    source_list = os.listdir(source_directory)

    # updates every item in the directory
    for item in source_list:
        source_path = os.path.join(source_directory, item)
        replica_path = os.path.join(replica_directory, item)

        # updates a file if any changes were made
        if os.path.isfile(source_path):
            if not equal_files(source_path, replica_path):
                update_file(source_path, replica_path)
                log.update_file(source_path)
        
        # calls itself recursively in the sub-directory
        if os.path.isdir(source_path):
            copy_directory(source_path, replica_path)
            
# syncs the source and replica folder periodicaly
def sync_loop(source_directory, replica_directory, sync_interval):
    try:
        while True:
            copy_directory(source_directory, replica_directory)
            time.sleep(sync_interval)
    except KeyboardInterrupt:
        log.user_interrupt()

# returns 1 if the files are equal
def equal_files(path1, path2):
    if not os.path.isfile(path1) or not os.path.isfile(path2):
        return 0 
        
    hash1 = md5_hash(path1)
    hash2 = md5_hash(path2)

    return hash1 == hash2

# returns the md5 hash of a file
def md5_hash(path):
    hash_md5 = hashlib.md5()

    with open(path, "rb") as file:
            content = file.read()
            hash_md5.update(content)
    return hash_md5.hexdigest()


# copies the content of the source file to the replica
def update_file(source_path, replica_path):
    with open(source_path, 'r') as source:
        with open(replica_path, 'w') as replica:
            content = source.read()
            replica.write(content)

# creates a file in the given path   
def create_file(source_directory, item):
    source_path = source_directory + item

    if os.path.isfile(source_path):
        print("File already exists!")
        return
    
    with open(source_path, 'w'):
        log.create_file(source_path)

# creates a directory in the given path
def create_directory(source_directory, item):
    source_path = source_directory + item

    try:
        os.makedirs(source_path)
        log.create_directory(source_path)
    except:
        print("Directory already exists!")

# removes a file in the given path
def remove_file(source_directory, replica_directory, item):
    source_path = source_directory + item
    replica_path = replica_directory + item
    try:
        os.remove(source_path)
        os.remove(replica_path)
        log.remove_file(source_path)
    except:
        pass

# removes a directory in the given path
def remove_directory(source_directory, replica_directory, item):
    source_path = source_directory + item
    replica_path = replica_directory + item
    try:
        os.rmdir(source_path)
        os.rmdir(replica_path)
        log.remove_directory(source_path)
    except:
        pass

def main():
    # gets the user arguments
    sync_interval = int(sys.argv[1])
    source_directory = sys.argv[2] + "/source"
    replica_directory = sys.argv[3] + "/replica"
    log_path = sys.argv[4] + "/log.txt"

    # stores the user arguments in the json file
    config.set_config_value('sync_interval', sync_interval)
    config.set_config_value('source_path', source_directory)
    config.set_config_value('replica_path', replica_directory)
    config.set_config_value('log_path',log_path)
    
    print(log_path)

    log.create_log(log_path)

    try:
        os.makedirs(source_directory)
        os.makedirs(replica_directory)
    except:
        pass

    # gets user input to execute diffent commands
    while True:
        user_input = input("Enter a command or 'q' to quit): ")
        
        if user_input == 'q':
            print("Exiting the program.")
            quit()

        elif user_input == 'sync':
            sync_loop(source_directory, replica_directory, sync_interval)

        elif user_input.startswith('create_file'):
            args = user_input.split()
            item = args[1]
            create_file(source_directory, item)

        elif user_input.startswith('create_directory'):
            args = user_input.split()
            item = args[1]
            create_directory(source_directory, item)

        elif user_input.startswith('remove_file'):
            args = user_input.split()
            item = args[1]
            remove_file(source_directory, replica_directory, item)

        elif user_input.startswith('remove_directory'):
            args = user_input.split()
            item = args[1]
            remove_directory(source_directory, replica_directory, item)

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
