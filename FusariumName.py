import os

path = os.chdir("C:\\Users\\khush\\OneDrive\\Documents\\ScienceFair2022\\LeafDatabase\\Fusarium")

i = 0
for file in os.listdir(path):

    new_file_name = "fusarium{}.jpg".format(i)
    os.rename(file, new_file_name)

    i = i + 1
