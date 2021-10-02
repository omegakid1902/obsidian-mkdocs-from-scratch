import os
import re
import frontmatter
from shutil import *
import json

base_docs_url = "./docs/Zet"


# For Regex, match groups are:
#       0: Whole markdown link e.g. [Alt-text](url)
#       1: Alt text
#       2: Full URL e.g. url + hash anchor
#       3: Filename e.g. filename.md
#       4: File extension e.g. .md, .png, etc.
#       5. hash anchor e.g. #my-sub-heading-link
AUTOLINK_RE = r'\[([^\]]+)\]\((([^)/]+\.(md|png|jpg))(#.*)*)\)'

# For Regex, match groups are:
#       0: Whole roamlike link e.g. [[filename#title|alias]]
#       1: Whole roamlike link e.g. filename#title|alias
#       2: filename
#       3: #title
#       4: |alias
ROAMLINK_RE = r'\[\[(([^\]#\|]*)(#[^\|\]]+)*(\|[^\]]*)*)\]\]'



'''
{
   "nodes": [

      {
         "name": "title 1"
         "id":"0",
         "backlinks": []
      },

      {
         "name": "title 2"
         "id":"1",
         "backlinks": [1]
      }
   ],
}

{"file": "mkdow.md", 
"backlink": [1, 3]
}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
'''

nodes = {}
'''
node_init = {
    "name": {"id": nodes_id, "outgoing_links" : [], "backlinks" : []}
}
'''
nodes_id = 0

class AutoLinkDetect:
    def __init__(self, base_docs_url, page_url):
        self.base_docs_url = base_docs_url
        self.page_url = page_url

    def __call__(self, match):
        # Name of the markdown file
        filename = match.group(3).strip()

        # Absolute URL of the linker
        abs_linker_url = os.path.dirname(
            os.path.join(self.base_docs_url, self.page_url))

        # Find directory URL to target link
        rel_link_url = ''
        # Walk through all files in docs directory to find a matching file
        for root, dirs, files in os.walk(self.base_docs_url):
            for name in files:
                # If we have a match, create the relative path from linker to the link
                if name == filename:
                    # Absolute path to the file we want to link to
                    abs_link_url = os.path.dirname(os.path.join(root, name))
                    # Constructing relative path from the linker to the link
                    rel_link_url = os.path.join(
                        os.path.relpath(abs_link_url, abs_linker_url),
                        filename)
        if rel_link_url == '':
            print('WARNING: AutoLinksPlugin unable to find ' + filename +
                  ' in directory ' + self.base_docs_url)
            return match.group(0)

        # Construct the return link by replacing the filename with the relative path to the file
        if (match.group(5) == None):
            link = match.group(0).replace(match.group(2), rel_link_url)
        else:
            link = match.group(0).replace(match.group(2),
                                          rel_link_url + match.group(5))

        return link


class RoamLinkDetect:
    def __init__(self, base_docs_url, page_url):
        self.base_docs_url = base_docs_url
        self.page_url = page_url
        self.file_name = os.path.basename(page_url).replace(".md", "")
        if self.file_name not in nodes.keys():
            global nodes_id
            nodes[self.file_name] = {"id": nodes_id, "outgoing_links" : [], "backlinks" : []}
            nodes_id += 1

    def simplify(self, filename):
        """ ignore - _ and space different, replace .md to '' so it will match .md file,
        if you want to link to png, make sure you filename contain suffix .png, same for other files
        but if you want to link to markdown, you don't need suffix .md """
        return re.sub(r"[\-_ ]", "", filename.lower()).replace(".md", "")

    def gfm_anchor(self, title):
        """Convert to gfw title / anchor 
        see: https://gist.github.com/asabaylus/3071099#gistcomment-1593627"""
        if title:
            title = title.strip().lower()
            title = re.sub(r'[^\w\u4e00-\u9fff\- ]', "", title)
            title = re.sub(r' +', "-", title)
            return title
        else:
            return ""

    def __call__(self, match):
        # Name of the markdown file
        whole_link = match.group(0)
        filename = match.group(2).strip() if match.group(2) else ""
        title = match.group(3).strip() if match.group(3) else ""
        format_title = self.gfm_anchor(title)
        alias = match.group(4).strip('|') if match.group(4) else ""
        #print(f'    --debug: link: {whole_link}, filename:{filename}, title: {title}, format_title: {format_title} alias:{alias}  ')
        
        # Absolute URL of the linker
        abs_linker_url = os.path.dirname(
            os.path.join(self.base_docs_url, self.page_url))

        # Find directory URL to target link
        rel_link_url = ''
        # Walk through all files in docs directory to find a matching file
        if filename:
            for root, dirs, files in os.walk(self.base_docs_url):
                for name in files:
                    # If we have a match, create the relative path from linker to the link
                    if self.simplify(name) == self.simplify(filename):
                        # if name == filename:
                        # Absolute path to the file we want to link to
                        abs_link_url = os.path.dirname(os.path.join(
                            root, name))
                        # Constructing relative path from the linker to the link
                        rel_link_url = os.path.join(
                                os.path.relpath(abs_link_url, abs_linker_url), name)
                        if title:
                            rel_link_url = rel_link_url + '#' + format_title

            if rel_link_url == '':
                #print('WARNING: RoamLinksPlugin unable to find ' + filename + 'in directory ' + self.base_docs_url)
                return whole_link
            else:
                #print('RoamLinksPlugin  ' + filename + ' in directory ' + self.base_docs_url)
                pass
        else:
            rel_link_url = '#' + format_title

        # ignore picture
        if not filename.endswith(".jpg") and not filename.endswith(".png"):
            nodes[self.file_name]['outgoing_links'].append(filename)
        
        return filename

'''
class RoamLinksPlugin(BasePlugin):
    def on_page_markdown(self,
                         markdown,
                         page,
                         config,
                         site_navigation=None,
                         **kwargs):

        # Getting the root location of markdown source files
        base_docs_url = config["docs_dir"]

        # Getting the page url that we are linking from
        page_url = page.file.src_path

        # Look for matches and replace
        markdown = re.sub(AUTOLINK_RE,
                          AutoLinkReplacer(base_docs_url, page_url), markdown)
        markdown = re.sub(ROAMLINK_RE,
                          RoamLinkReplacer(base_docs_url, page_url), markdown)

        return markdown
'''

for root, dirs, files in os.walk(base_docs_url):
    for file in files:
        if file.endswith(".md"):
            page_url = os.path.join(root, file)
            #print(f'--debug: Scan File: {page_url}')
            with open(os.path.join(root, file), encoding="utf-8") as f:
                markdown = f.read()
                markdown = re.sub(ROAMLINK_RE,
                          RoamLinkDetect(base_docs_url, page_url), markdown)


'''
node_init = {
    "name": {"id": nodes_id, "outgoing_links" : [], "backlinks" : []}
}
'''

''' Convert back/forward link to id of node
for node in nodes:
    for outgoing_idx in range(len(nodes[node]["outgoing_links"])):

        target_node_name = nodes[node]['outgoing_links'][outgoing_idx]
        nodes[target_node_name]['backlinks'].append(nodes[node]["id"])
        nodes[node]['outgoing_links'][outgoing_idx] = nodes[target_node_name]["id"]
'''

for node in nodes:
    if node in nodes[node]["outgoing_links"]:
        nodes[node]["outgoing_links"].remove(node)

    nodes[node]["outgoing_links"] = list(dict.fromkeys(nodes[node]["outgoing_links"]))

    for outgoing_idx in range(len(nodes[node]["outgoing_links"])):

        target_node_name = nodes[node]['outgoing_links'][outgoing_idx]
        nodes[target_node_name]['backlinks'].append(node)

for root, dirs, files in os.walk(base_docs_url):
    for file in files:
        if file.endswith(".md"):
            file_name_strip = os.path.basename(file).replace(".md", "")
            with open(os.path.join(root, file), 'a', encoding="utf-8") as f:
                if len(nodes[file_name_strip]["backlinks"]):
                    f.write("\n## Backlinks:\n")
                    for backlink in nodes[file_name_strip]["backlinks"]:
                        f.write("- [["+backlink+"]]\n")

# write json with unicode utf8 character encoding="utf-8", ensure_ascii=False
with open('docs/backlink.json', 'w', encoding="utf-8") as outfile:
    json.dump(nodes, outfile, indent=4, ensure_ascii=False)

graph_nodes = {"nodes" : [], "links": []}
for node in nodes:
    node_url = "https://omegakid1902.github.io/Zet/" + node
    graph_node = { "id": node, "group": 1, "url": node_url}
    # graph_node["id"] = node
    # graph_node["group"] = 1
    graph_nodes["nodes"].append(graph_node)
    link_info = { "source": "", "target": "", "value": 1 }
    for outgoing in nodes[node]["outgoing_links"]:
        
        if node == outgoing:
            continue

        link_info["source"] = node
        link_info["target"] = outgoing
        link_info["value"] = 1
        graph_nodes["links"].append(link_info)

with open('docs/d3graph/graph_nodes.json', 'w', encoding="utf-8") as outfile:
    json.dump(graph_nodes, outfile, indent=4, ensure_ascii=False)
