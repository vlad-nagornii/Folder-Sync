import datetime
import config

log_path = config.get_config_value('log_path')

# gets the current time formated to yyyy-mm-dd hh-mm-ss
def get_time():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# creates a log file and writes the time of creation
def create_log(log_path):
    with open(log_path, 'a') as log:
        current_time = get_time()
        log.write(f"{current_time}: started copying\n")
        print(f"{current_time}: started copying")

# updates a file and writes the path and time in the log and terminal
def update_file(file_path):
      print(log_path)
      with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: file updated in {file_path}\n")
            print(f"{current_time}: file updated in {file_path}")

# updates a directory and writes the path and time in the log and terminal
def update_directory(directory_path):
      with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: direcotry updated in {directory_path}\n")
            print(f"{current_time}: directory updated in {directory_path}")

# writes the path of a created file and the time of creation in the log and terminal
def create_file(file_path):
    with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: file created in {file_path}\n")
            print(f"{current_time}: file created in {file_path}")

# writes the path of a created directory and the time of creation in the log and terminal      
def create_directory(directory_path):
      with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: directory created in {directory_path}\n")
            print(f"{current_time}: directory created in {directory_path}")

# writes the path of a removed file and the time of removal in the log and terminal             
def remove_file(file_path):
    with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: file removed in {file_path}\n")
            print(f"{current_time}: file removed in {file_path}")

# writes the path of a removed directory and the time of removal in the log and terminal      
def remove_directory(directory_path):
     with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: directory removed in {directory_path}\n")
            print(f"{current_time}: directory removed in {directory_path}")

# writes in the log the time when the user interrupted the copying
def user_interrupt():
        with open(log_path, 'a') as log:
            current_time = get_time()
            log.write(f"{current_time}: copying interrupted\n")
            print(f"\n{current_time}: copying interrupted")
        