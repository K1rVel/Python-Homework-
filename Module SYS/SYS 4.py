import os
import sys

path = sys.argv[1]
folder_name = sys.argv[2]

os.makedirs(os.path.join(path, folder_name))