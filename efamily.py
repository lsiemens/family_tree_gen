#generate family tree webpage from text file.

import os, sys
import efamily_html

data_header = "efamily-data"

class data_family:
    def __init__(self):
        self.id = None
        self.husband = None
        self.hfather = None
        self.hmother = None
        self.hbirth = None
        self.hdeath = None
        self.wife = None
        self.wfather = None
        self.wmother = None
        self.wbirth = None
        self.wdeath = None
        self.marriage = None
        self.children = None
        self.pictures = None
        self.notes = None

        self.hflink = False
        self.hmlink = False
        self.wflink = False
        self.wmlink = False
        
        self.children_link = {}
        
    def __str__(self):
        data = ""
        data = data + self.write_entry("husband", self.husband)
        data = data + self.write_entry("father", self.hfather)
        data = data + self.write_entry("mother", self.hmother)
        data = data + self.write_entry("birth", self.hbirth)
        data = data + self.write_entry("death", self.hdeath)
        data = data + self.write_entry("wife", self.wife)
        data = data + self.write_entry("father", self.wfather)
        data = data + self.write_entry("mother", self.wmother)
        data = data + self.write_entry("birth", self.wbirth)
        data = data + self.write_entry("death", self.wdeath)
        data = data + self.write_entry("marriage", self.marriage)
        data = data + self.write_entry("children", self.children)
        data = data + self.write_entry("pictures", self.pictures)
        data = data + self.write_entry("notes", self.notes)
        data = data + "\n"
        return data
        
    def write_entry(self, id, data):
        if data != str.strip(data):
            print(repr(data), repr(str.strip(data)))
        if str.strip(data) != "":
            return id + " " + str.strip(data) + "\n"
        else:
            return id + " None\n"

class interpreter:
    def __init__(self):
        self.families = []
        self.files = []
        self.ids = {}
        
    def process(self, dir_input="./", dir_output="./", dir_template="./"):
        for item in os.listdir(dir_input):
            if os.path.isfile(dir_input + item):
                with open(dir_input + item, "r") as fin:
                    line = fin.readline()
                    if (line[:len(data_header)] == data_header):
                        self.files.append(dir_input + item)
        
        self.read_files()
        
        for family in self.families:
            id = family.husband + " " + family.wife
            id = id.replace(" ", "_")
            self.ids[id] = family
            family.id = id
        
        for family in self.families:
            hpid = family.hfather + " " + family.hmother
            hpid = hpid.replace(" ", "_")

            wpid = family.wfather + " " + family.wmother
            wpid = wpid.replace(" ", "_")
            
            if hpid in self.ids:
                hpfamily = self.ids[hpid]
                hpfamily.children_link[family.husband.split(" ")[0]] = family.id
                if family.hfather != "":
                    family.hflink = True

                if family.hmother != "":
                    family.hmlink = True

            if wpid in self.ids:
                wpfamily = self.ids[wpid]
                wpfamily.children_link[family.wife.split(" ")[0]] = family.id
                if family.wfather != "":
                    family.wflink = True

                if family.wmother != "":
                    family.wmlink = True
        
        for family in self.families:
            title = ""
            if family.husband != "":
                title = family.husband
                
            if family.wife != "":
                if title != "":
                    title = title + " and "
                title = title + family.wife

            hpid = family.hfather + " " + family.hmother
            hpid = hpid.replace(" ", "_")

            wpid = family.wfather + " " + family.wmother
            wpid = wpid.replace(" ", "_")
            
            if family.hflink:
                hfather = "<a href=\"" + hpid + ".html\">" + family.hfather + "</a>"
            else:
                hfather = family.hfather

            if family.hmlink:
                hmother = "<a href=\"" + hpid + ".html\">" + family.hmother + "</a>"
            else:
                hmother = family.hmother
            
            if family.wflink:
                wfather = "<a href=\"" + wpid + ".html\">" + family.wfather + "</a>"
            else:
                wfather = family.wfather

            if family.wmlink:
                wmother = "<a href=\"" + wpid + ".html\">" + family.wmother + "</a>"
            else:
                wmother = family.wmother
            
            children = family.children
            for child in family.children_link:
                children = children.replace(child, "<a href=\"" + family.children_link[child] + ".html\">" + child + "</a>", 1)
                

            html_writer = efamily_html.efamily_html(dir_template)
            html_writer.save_file(dir_output + family.id + ".html", title=title, husband=family.husband, hfather=hfather, hmother=hmother, hbirth=family.hbirth, hdeath=family.hdeath, wife=family.wife, wfather=wfather, wmother=wmother, wbirth=family.wbirth, wdeath=family.wdeath, marriage=family.marriage, children=children, notes=family.notes)

    def read_files(self):
        families = []
        for file in self.files:
             families += self.read_file(file)
        self.families = families
        
    def read_file(self, file):
        families = []
        if not os.path.isfile(file):
            raise IOError("item " + file + " not found or is not a file.")
        data = []

        with open(file, "r") as fin:
            data = fin.readlines()
        
        if not data_header in data[0]:
            raise IOError("file " + file + " is not a valid efamily data file.")
        
        data = data[1:]
        while len(data) != 0:
            family, success, data = self.load_family(data)
            if success:
                families.append(family)
            else:
                break
        return families

    def write_file(self, file):
        data = data_header + "\n\n"
        for family in self.families:
            data = data + str(family)
        with open(file, "w") as fout:
            fout.write(data)
        
    def load_family(self, data):
        family = data_family()
        
        if len(data) == 0:
            return family, False, []
        
        while data[0].strip() == "":
            data = data[1:]
            if len(data) == 0:
                 return family, False, []
        
        family.husband, data = get_item("husband", data)
        family.hfather, data = get_item("father", data)
        family.hmother, data = get_item("mother", data)
        family.hbirth, data = get_item("birth", data)
        family.hdeath, data = get_item("death", data)

        family.wife, data = get_item("wife", data)
        family.wfather, data = get_item("father", data)
        family.wmother, data = get_item("mother", data)
        family.wbirth, data = get_item("birth", data)
        family.wdeath, data = get_item("death", data)

        family.marriage, data = get_item("marriage", data)
        family.children, data = get_item("children", data)
        family.pictures, data = get_item("pictures", data)
        family.notes, data = get_item("notes", data)
        
        title = ""
        if family.husband != "":
            title = family.husband

        if family.wife != "":
            if title != "":
                title = title + " "
            title = title + family.wife

        family.id = title.replace(" ", "_")

        return family, True, data

def get_item(id, data):
    try:
        
        temp = data[0].split(maxsplit=1)
        data_id = temp[0].strip()
        if len(temp) > 1: 
            info = temp[1].strip()
            if info.lower() == "none":
                info = ""
        else:
            raise ValueError("empty attribute, expected none.")

        if data_id != id:
            raise ValueError("incorrect id, expected: " + id + " got: " + data_id)

        data = data[1:]
        return info, data
    except IndexError:
        print("File ERROR:  missing id: " + id + "\n")
        sys.exit(1)
    
#program = interpreter()
#program.process("./", "./test")
