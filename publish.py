import os
import frontmatter
from shutil import *

zet_folder = "../zettelkasten/"
target = "./docs/"

if os.path.exists('./docs'):
    rmtree('./docs')

os.mkdir('./docs')

for file in os.listdir(zet_folder):
    if file.endswith(".md"):
        with open(os.path.join(zet_folder, file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys():
                print("Copy publish files from zettelkasten to docs/")
                copy(os.path.join(zet_folder, file), './docs/')
            else:
                pass

release_folders = ["../zettelkasten/Zet"]
for folder in release_folders:
    copytree(folder, './docs/Zet')

for root, dirs, files in os.walk(target):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys() and metadata['publish'] == True:
                    print("Publish file:", os.path.join(root, file))
                    publish = True
                else:
                    os.remove(os.path.join(root, file))
                    publish = False
            if publish:
                with open("yourfile.txt", "r") as f:
                    lines = f.readlines()
                with open(os.path.join(root, file), 'w', encoding="utf8") as newf:
                    print("Remove title file:", os.path.join(root, file))
                    for line in content:
                        if not line.startswith("# "):
                            newf.write(line)

folder = "../zettelkasten/Spaces/Projects"
copytree(folder, './docs/Projects')
