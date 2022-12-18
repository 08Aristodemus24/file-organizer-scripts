import os
import shutil

def checkAndMove():
    # provide directory that will be checked
    # if length is 1 or more then move all files
    # with a loop based on the length
    # if 0 do nothing
    DOWNLOADS_PATH='C:/Users/Cueva/Downloads'
    DEST_PATH='C:/Users/Cueva/Documents'

    # when script is ran it should move all files
    # in the specific source
    files=os.listdir(DOWNLOADS_PATH)
    # 
    for file in files:
        if '.exe' in file:
            source_path=DOWNLOADS_PATH+'/'+file

            # define the new path of the file
            new_dest_path=DEST_PATH+'/Downloaded Exe Files/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.png' in file or '.jpg' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Images/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.pdf' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded PDF Files/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.c' in file or '.py' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Scripts/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.docx' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Word Files/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.pptx' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded PPT Files/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.mp3' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Audio/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.mp4' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Videos/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        elif '.zip' in file:
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Zip Files/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

        else:
            # put in miscellaneous folder
            source_path=DOWNLOADS_PATH+'/'+file
            new_dest_path=DEST_PATH+'/Downloaded Miscellaneous/'+file
            shutil.move(source_path,new_dest_path)
            print('files moved')

    print('OPERATION COMPLETE')
        


if __name__ == "__main__":
    checkAndMove()