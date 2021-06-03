import os
import shutil

folder_root = os.path.abspath('my_project')

for root, dirs, files in os.walk(folder_root):
    for file in files:
        if file.endswith('html'):
            name_dir = os.path.join('templates', os.path.basename(root))
            if not os.path.exists(name_dir):
                os.makedirs(name_dir)
            shutil.copy(os.path.join(root, file), os.path.join(name_dir,file))