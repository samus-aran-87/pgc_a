import os
import time

DAYS = 5                                # Maximal age of file to stay, older will be deleted
FOLDERS = [
    "~/Desktop",
    "~/Downloads",                      # or /Users/alexander/Downloads
]

TOTAL_DELETED_SIZE = 0                  # Total deleted size of all files in bytes
TOTAL_DELETED_FILE = 0                  # Total deleted files
TOTAL_DELETED_DIRS = 0                  # Total deleted empty folders

nowTime = time.time()                   # Get current file in seconds
ageTime = nowTime - 60*60*24*DAYS       # Minus days in seconds


def delete_old_files(folder):
    # global TOTAL_DELETED_FILE
    # global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for f in files:
            fileName = os.path.join(path, f)                # Get full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile              # Count sum of all free space
                TOTAL_DELETED_FILE += 1                     # Count number of deleted files
                print("Deleting file: " + str(fileName))     
                os.remove(fileName)                         # Delete files


def delete_empty_dir(folder):
    # global TOTAL_DELETED_DIRS
    empty_folders_it_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_it_this_run += 1
            print("Deleting empty path: " + str(path))
            os.rmdir(path)
        if empty_folders_it_this_run > 0:
            delete_empty_dir(folder)


start_time = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)            # Delete old files
    delete_empty_dir(folder)            # Delete empty folders

finish_time = time.asctime()

print("-------------------------------------------")
print("Start time: {}".format(start_time))
print("Total deleted size: {} Mb".format((TOTAL_DELETED_SIZE/1024)/1024))
print("Total deleted files: {}".format(TOTAL_DELETED_FILE)
print("Total deleted empty folders: {}".format(TOTAL_DELETED_DIRS)
print("Finish time: {}".format(finish_time))
print("--------------------EOF--------------------")
