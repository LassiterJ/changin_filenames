import os
input_dir = "/home/lassiter/Programming/UdacityIPND/ChangingFileNames/prank"
def rename_files():
    # 1: get file names from a folder
    file_list = os.listdir(input_dir)
    print file_list
    # 2: for each file, rename filename
    saved_path = os.getcwd()
    print ("Current Working Directory is " + saved_path)
    os.chdir(input_dir)
    for file_name in file_list:
      new_file_name = file_name.translate( None, "0123456789")
      os.rename(file_name, new_file_name)
    os.chdir(saved_path)
    
    
rename_files()
