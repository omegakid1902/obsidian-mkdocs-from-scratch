import os
import frontmatter
from shutil import *

target = "./docs/"
date_path = "./docs/dates"
if os.path.exists(date_path):
    os.rmdir(date_path)

os.mkdir(date_path)

def month_str_num(month):
    switcher = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(month, "nothing")

total_date_file = []

for root, dirs, files in os.walk(target):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), 'a', encoding="utf-8") as f:

                content = f.read()
                try:
                    metadata, content = frontmatter.parse(content)
                except:
                    print("YAML ERORR in file:", file.encode("utf-8"))
                    continue

                if 'tags' in metadata.keys():
                    for tag in metadata['tags']:
                        if 'created' in tag:
                            # print("-----------------file:", file.encode("utf-8"))
                            # print("   - tags file:", tag.encode("utf-8"))
                            date = tag.strip('created/').strip('#created/').split('/')
                            date[1] = month_str_num(date[1])
                            date_file = '-'.join(date)

                            if date_file not in total_date_file:
                                total_date_file.append(date_file)
                            
                            f.write("\n[[" + date_file + "]]\n")
                            
                            # if not os.path.isfile(date_file):
                            with open(date_path + "/" + date_file + ".md", 'a', encoding="utf-8") as d_f:
                                d_f.write("- [[" + file.replace('.md', '') + "]]\n")
                                
total_date_file.sort(reverse=True)
month = "0000-00"
with open(date_path + "/date_list" + ".md", 'a', encoding="utf-8") as f:
    for file in total_date_file:
        num_lines = sum(1 for line in open(date_path + '/' + file + '.md', encoding="utf-8"))
        if month not in file:
            month = file.strip('[[').strip(']]')[:7]
            f.write("## " + month + "\n")
        f.write("- [[" + file + "]] (" + str(num_lines) + " notes)\n")
        
