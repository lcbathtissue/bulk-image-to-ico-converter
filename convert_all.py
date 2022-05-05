import os
from PIL import Image
from os import walk

main_dir = os.getcwd()

f = []
for (dirpath, dirnames, filenames) in walk(f"{main_dir}/to_be_converted"):
    f.extend(filenames)
    break

if len(filenames) == 0:
    print("\nNo files were found to be converted in the 'to_be_converted' folder..")
    print("Exiting Program..")

print()

for file in filenames:
    img = Image.open(f"{main_dir}/to_be_converted/{file}")
    print_out = file
    file = file[:file.find(".")]
    img.save(f"{main_dir}/converted/{file}.ico")
    print_out = print_out + " --> " + f"{file}.ico"
    print(print_out)