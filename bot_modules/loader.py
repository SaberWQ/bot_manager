import os 
from aiogram.types.input_file import FSInputFile

def loader_file(file_name: str | None = None) -> FSInputFile:

    # path_to_loader_file = __file__ # за допомогою магічної змінної __file__ отримуємо абсолютний шлях до її місця розташування
    # 
    # path_to_folder_bot_modules = os.path.abspath(path_to_loader_file + "/..")
    # print('\npath_to_folder_bot_modules = ' + path_to_folder_bot_modules + '\n')
    # 
    # path_to_folder_final_bot = os.path.abspath(path_to_folder_bot_modules + "/..") 
    # print(f"path_to_folder_final_bot = {path_to_folder_final_bot}\n")
    # 
    # path_to_folder_images = os.path.abspath(path_to_folder_final_bot + "/images")
    # print(f"path_to_folder_images = {path_to_folder_images}\n")
    # 
    # path_to_file_in_images = os.path.abspath(path_to_folder_images + f"/{file_name}")
    # print(f"path_to_file_in_images = {path_to_file_in_images}\n")
    # 
    # image_file = FSInputFile(path= path_to_file_in_images)
    # return image_file
    return FSInputFile(path= os.path.abspath(__file__ + f'/../../images/{file_name}'))
    
    
