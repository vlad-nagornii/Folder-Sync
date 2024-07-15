# Folder Synchronization

This program synchronizes two folders: source and replica. The program ensures that the replica folder maintains an exact copy of the source folder and updates it periodically.

## Usage

To run the program use the following command:
```bash
python runner.py <sync_interval> <source_folder_path> <replica_folder_path> <log_file_path>
```

Example:
```bash
python runner.py 10 /Users/vladnagornii/Desktop/Veeam/test /Users/vladnagornii/Desktop/Veeam/test/ /Users/vladnagornii/Desktop/Veeam/test/
```

## How to use it

When the program is executed, it will store the arguments provided by the user (sync_interval, source_folder_path, replica_folder_path, log_file_path) in a JSON file, and if necessary create the source and replica folders, and the log file.

After that the user can type in the terminal any of the following commands:

create_file <path>: Creates a new file at the specified path.

create_directory <path>: Creates a new directory at the specified path.

remove_file <path>: Removes the file at the specified path.

remove_directory <path>: Removes the directory at the specified path.


NOTE: 
When the user writes a path to use any of the four commands above, it should be considered that the program will execute the command inside the source folder. 

For example:
If you want to create a file in /Users/vladnagornii/Desktop/Veeam/test/source/ called 'file.txt'
you should just type at the terminal:

```bash
create_file /file.txt
```
All the commands above only perform actions on the source folder.
The program assumes that all the paths given by the user are valid


sync: Triggers the synchronization process. To end the synchronization, the user interrupts the program (CTRL + C), and the program will go back to prompting the user for any of the commands above.

q (quit): Exits the program.

## Author

Vladislav Nagornii