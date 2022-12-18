# flaws:
# when download is initialized in the downloads folder it is directly moved

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CurrentDirHandler(FileSystemEventHandler):
    # define source and destination path 
    # for each and every object
    def __init__(self,downloads_path,dest_path):
        self.DOWNLOADS_PATH=downloads_path
        self.DEST_PATH=dest_path

    # override method from parent class
    def on_modified(self,event):
        # create an array of all files in the directory given
        files=os.listdir(self.DOWNLOADS_PATH)

        for file in files:
            if '.exe' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file

                # define the new path of the file
                new_dest_path=self.DEST_PATH+'/Downloaded Exe Files/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.png' in file or '.jpg' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Images/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.pdf' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded PDF Files/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.c' in file or '.py' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Scripts/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.docx' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Word Files/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.pptx' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded PPT Files/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.mp3' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Audio/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.mp4' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Videos/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            elif '.zip' in file:
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Zip Files/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')

            else:
                # put in miscellaneous folder
                source_path=self.DOWNLOADS_PATH+'/'+file
                new_dest_path=self.DEST_PATH+'/Downloaded Miscellaneous/'+file
                shutil.move(source_path,new_dest_path)
                print('files moved')
                

if __name__ == "__main__":    
    downloads_path='C:/Users/Cueva/Downloads'
    dest_path='C:/Users/Cueva/Documents'

    event_handler=CurrentDirHandler(downloads_path,dest_path)
    observer=Observer()
    observer.schedule(event_handler,downloads_path,recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



    
