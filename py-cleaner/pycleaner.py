import os
import shutil

temp_folder = '/Windows/Temp/'
second_temp_folder = '/Users/loqqty/AppData/Local/Temp/'
prefetch_folder = '/Windows/Prefetch/'

def delete_files(folder_name):
    files = 0
    folders = 0
    for file_name in os.listdir(folder_name):
        file_to_delete = os.path.join(folder_name, file_name)
        if os.path.isfile(file_to_delete):
            try:
                os.remove(file_to_delete)
                files += 1
            except PermissionError:
                print(f'{file_name}, file being used by another process') 
        else:
            try:
                shutil.rmtree(file_to_delete)
                folders += 1
            except PermissionError:
                print(f'{file_name}, file being used by another process') 
        print(file_name, ' removed.')
    print(f'Removed a total of {files} files and {folders} folders.')


delete_files(temp_folder)
delete_files(second_temp_folder)
delete_files(prefetch_folder)