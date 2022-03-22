# import os

# path = '/Users/drpoojayadav/Downloads/class 99/test/'
# root_ext = os.path.splitext(path)

# print(root_ext)


# # 2

# import os
# import shutil

# path = '/Users/drpoojayadav/Desktop/Books'
# print("before moving file ")
# print(os.listdir(path))

# src_file = '/Users/drpoojayadav/Desktop/Books/hi.pdf'
# dst_file = '/Users/drpoojayadav/Downloads/class 99/test2'

# dst = shutil.move(src_file, dst_file)
# print("After Copying file")
# print(os.listdir(path))


# 3
# program to organise files by extension in a folder

# import os
# import shutil

# path = input("Enter your directory name to be organised ")
# list_of_files = os.listdir(path)

# for file in list_of_files:
#     name, ext = os.path.splitext(file)
#     # print("Name = ", name, "\n Extension = ", ext)

#     if( ext == '' ):
#         continue
#     if( os.path.exists(path + '/' + ext) ):
#         shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
#     else:
#         os.mkdir(path + '/' + ext)
#         shutil.move(path + '/' + file, path + '/' + ext + '/' + file)


# program to reverse the above

# import os 
# import shutil

# path = input("Enter the root file name the files of which you sorted ")
# list_of_folders = os.listdir(path)

# for folder in list_of_folders:
#     if( folder == '.DS_Store' ):
#         continue
#     else:
#         name, ext = os.path.splitext(folder)
#         list_of_files = os.listdir(path + '/' + folder)
        
#         for file in list_of_files:
#             shutil.move(path + '/' + folder + '/' + file, path)

#         os.rmdir(path + '/' + folder)


# 4
# program which backs up any folder given to it as input. It should copy all the content inside the folder to the destination folder

# import os
# import shutil

# source = input("Enter the source directory name ")
# destination = input("Enter the destination folder name ")

# print("Source = ", os.listdir(source))

# list_of_files = os.listdir(source)

# for file in list_of_files:
#     shutil.copy(source + '/' + file, destination)