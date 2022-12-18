import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



# inherit the events received by the FileSystemEventHandler
class CurrentDirHandler(FileSystemEventHandler):
    def __init__(self,source,destination):
        self.source=source
        self.destination=destination

    # this must be the same name as the functions
    # in the inhreitance of FileSystemEventHandler
    # because we will be overriding the current functions
    # of the 
    def on_modified(self,event):
        for file in os.listdir(self.source):
            
            # this variable will keep track of the
            # old folder 
            source=self.source+'/'+file
            destination=self.destination+'/'+file
            shutil.move(source,destination)
            print('file moved')


folder_destination='C:/Users/Cueva/Desktop/Moved Files'
folder_to_track='C:/Users/Cueva/Desktop/Drag here to move files'
event_handler=CurrentDirHandler(folder_to_track,folder_destination)
observer=Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()    

try:
    # this will keep running forever
    # until system detects that user has pressed
    # ctrl + c which is a KeyboardInterrupt error
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
