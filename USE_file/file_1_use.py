# # write - replace
# with open("file_1.txt", "w") as file_1: # or [ file_1 = open("file.txt", "w") ]
#                 # \t == tab
#     file_1.write("\tHELLO PROGRAMER\t !")

# ----------------------------------------

# read
# with open("file_1.txt", "r") as file_1:
#     for line in file_1.readlines():
#         print(line.strip()) # HELLO PROGRAMER

# ----------------------------------------

# # append
# with open("file_1.txt", "a") as file_1:
#                 # \n == Next_line
#     file_1.write("\n USE_FILE")

# ----------------------------------------

# # clear
# with open("file_1.txt", "w") as file_1:
#     file.write("")

# ----------------------------------------

# delet
# import os
# os.remove("/tmp/<file_name>.txt")
