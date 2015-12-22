#handle the template html file and html file generation.

import os

html_header = "efamily-template"

class efamily_html:
    def __init__(self, dir="./"):
        self.file = None
        self.data = None
        self.tags = {}
        
        for item in os.listdir(dir):
            if os.path.isfile(dir + item):
                with open(dir + item, "r") as fin:
                    line = fin.readline()
                    if (line[:len(html_header)] == html_header):
                        self.file = dir + item
                        break
        
        with open(self.file, "r") as fin:
            self.data = fin.readlines()[1:]
            self.data =  "".join(self.data)
        
        index = 0
        tag_previous = 0
        EOF = len(self.data)
        
        result = ""
        while (index <= EOF):
            tag_start = self.data.find("[", index)
            if tag_start == -1:
                break
            index = tag_start

            tag_end = self.data.find("]", index) + 1
            index = tag_end

            tag = self.data[tag_start:tag_end]
            if tag[1] == "/":
                raise ValueError("Unmatched closing tag found.")
        
            close_tag_start = self.data.find("[", index)
            close_tag_end = close_tag_start + len("[/" + tag[1:])
            index = close_tag_end
        
            if self.data[close_tag_start:close_tag_end] != "[/" + tag[1:]:
                raise ValueError("No Closing tag found. Nested tags are not alowed.")

            self.tags[tag[1:-1]] = self.data[tag_end:close_tag_start]
            result = result + self.data[tag_previous:tag_end]
            tag_previous = close_tag_end
        result = result + self.data[tag_previous:]
        self.data = result

    def save_file(self, file, **kwargs):
        output = self.data
        for key in self.tags:
            if key in kwargs:
                output = output.replace("[" + key + "]", self.tags[key].replace("{" + key + "}", str(kwargs[key])))
            else:
                output = output.replace("[" + key + "]", "")
        with open(file, "w") as fout:
            fout.write(output)
