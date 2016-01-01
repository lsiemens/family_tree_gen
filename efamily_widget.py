import widget_framework as framework
import efamily
from IPython.html import widgets
from IPython.display import display, clear_output
import shutil
import os

add_family_item = "Add new family"

def start_efamily_widget(dir="./"):
    frame = framework.framework()
    frame.set_default_display_style(padding= "0.25em",background_color="white", border_color="#D3D3D3", border_radius="0.5em")
    frame.set_default_io_style(padding="0.25em", margin="0.25em", border_color="#D3D3D3", border_radius="0.5em")

    group_style = {"border_style":"none", "border_radius":"0em", "width":"100%"}
    text_box_style = {"width":"10em"}
    button_style = {"font_size":"1.25em", "font_weight":"bold"}
    first_tab_style = {"border_radius":"0em 0.5em 0.5em 0.5em"}

    states = ["data_loaded"]

    frame.add_state(states)
    frame.set_state_data("dir", os.path.abspath(dir))
    frame.set_state_data("data", efamily.interpreter())

    def update_dir_bar_list():
        dir = frame.get_state_data("dir")
        dirs = [".", ".."] + os.listdir(dir)
        
        frame.set_state_attribute("address_bar", value=dir)
        frame.set_state_attribute("directory_list", options=dirs)

    def add_pblocks(strings):
        strings = strings.split("\n")
        data = ""
        for string in strings:
            string = string.strip()
            if string != "":
                data = data + "<p>" + string + "</p>"
        return data

    def remove_pblocks(string):
        string = string.replace("<p>", "")
        string = string.replace("</p>", "\n\n")
        string = string.strip()
        return string

    def clear_efamily_fields():
        frame.set_attributes("select_family", value=add_family_item)
        frame.set_attributes("husband", value="")
        frame.set_attributes("wife", value="")
        frame.set_attributes("hfather", value="")
        frame.set_attributes("wfather", value="")
        frame.set_attributes("hmother", value="")
        frame.set_attributes("wmother", value="")
        frame.set_attributes("hbirth", value="")
        frame.set_attributes("wbirth", value="")
        frame.set_attributes("hdeath", value="")
        frame.set_attributes("wdeath", value="")
        frame.set_attributes("marriage", value="")
        frame.set_attributes("children", value="")
        frame.set_attributes("pictures", value="")
        frame.set_attributes("notes", value="")
        
    def update_efamily_fields(name=add_family_item):
        id = name.replace("and ", "").replace(" ", "_")
        data = frame.get_state_data("data")
        selection = [add_family_item]
        selected_family = None
        for family in data.families:
            title = ""
            if family.husband != "":
                title = family.husband

            if family.wife != "":
                if title != "":
                    title = title + " and "

                title = title + family.wife
            
            selection.append(title)
            if family.id == id:
                selected_family = family

        family = selected_family
        frame.set_attributes("select_family", options=selection)

        if name == add_family_item:
            clear_efamily_fields()
            return

        if family == None:
            raise ValueError("No family with id " + id + " found.")

        frame.set_attributes("husband", value=family.husband)
        frame.set_attributes("wife", value=family.wife)
        frame.set_attributes("hfather", value=family.hfather)
        frame.set_attributes("wfather", value=family.wfather)
        frame.set_attributes("hmother", value=family.hmother)
        frame.set_attributes("wmother", value=family.wmother)
        frame.set_attributes("hbirth", value=family.hbirth)
        frame.set_attributes("wbirth", value=family.wbirth)
        frame.set_attributes("hdeath", value=family.hdeath)
        frame.set_attributes("wdeath", value=family.wdeath)
        frame.set_attributes("marriage", value=remove_pblocks(family.marriage))
        frame.set_attributes("children", value=remove_pblocks(family.children))
        frame.set_attributes("pictures", value=family.pictures)
        frame.set_attributes("notes", value=remove_pblocks(family.notes))

    frame.add_display_object("window")
    frame.add_io_object("Title") 
    frame.add_display_object("widget")

    ###Data page###
    frame.add_display_object("page_data")
    frame.add_io_object("address_bar")
    frame.add_io_object("directory_list")
    frame.add_display_object("load_save_group")
    frame.add_io_object("load_files")
    frame.add_io_object("save_files")
    frame.add_io_object("new_files")
    
    ###Edit page###
    frame.add_display_object("page_edit")
    frame.add_display_object("select_family_delete_group")
    frame.add_io_object("select_family")
    frame.add_io_object("delete_selection")
    frame.add_display_object("husband_wife_group")
    frame.add_io_object("husband")
    frame.add_io_object("wife")
    frame.add_display_object("father_group")
    frame.add_io_object("hfather")
    frame.add_io_object("wfather")
    frame.add_display_object("mother_group")
    frame.add_io_object("hmother")
    frame.add_io_object("wmother")
    frame.add_display_object("birth_group")
    frame.add_io_object("hbirth")
    frame.add_io_object("wbirth")
    frame.add_display_object("death_group")
    frame.add_io_object("hdeath")
    frame.add_io_object("wdeath")
    frame.add_io_object("marriage")
    frame.add_io_object("children")
    frame.add_io_object("pictures")
    frame.add_io_object("notes")
    frame.add_io_object("apply_change")
    frame.add_io_object("download_link")
    
    ###Generate page###
    frame.add_display_object("page_generate")
    frame.add_io_object("generate_tree")

    frame.set_state_children("window", ["Title", "widget"])
    frame.set_state_children("widget", ["page_data", "page_edit", "page_generate"], titles=["Load data", "Edit data", "Generate family tree"])
    frame.set_state_children("page_data", ["address_bar", "directory_list", "load_save_group"])
    frame.set_state_children("load_save_group", ["load_files", "save_files", "new_files"])
    
    frame.set_state_children("page_edit", ["select_family_delete_group", "husband_wife_group", "father_group", "mother_group", "birth_group", "death_group", "marriage", "children", "pictures", "notes", "apply_change"])
    frame.set_state_children("select_family_delete_group", ["select_family", "delete_selection"])
    frame.set_state_children("husband_wife_group", ["husband", "wife"])
    frame.set_state_children("father_group", ["hfather", "wfather"])
    frame.set_state_children("mother_group", ["hmother", "wmother"])
    frame.set_state_children("birth_group", ["hbirth", "wbirth"])
    frame.set_state_children("death_group", ["hdeath", "wdeath"])

    frame.set_state_children("page_generate", ["address_bar", "directory_list", "generate_tree", "download_link"])

    frame.set_state_attribute('window', visible=True, **group_style)
    frame.set_state_attribute('Title', visible=True, value = "<center><h1>Efamily widget</h1></center><p><center>Create electronic family tree.</center></p>")
    frame.set_state_attribute('widget', visible=True, **group_style)

    frame.set_state_attribute("page_data", visible=True, **first_tab_style)
    frame.set_state_attribute("address_bar", visible=True)
    frame.set_state_attribute("directory_list", visible=True)
    frame.set_state_attribute("load_save_group", visible=True, **group_style)
    frame.set_state_attribute("load_files", visible=True, description="Load data", **button_style)
    frame.set_state_attribute("save_files", visible=True, description="Save data", disabled=True, **button_style)
    frame.set_state_attribute("save_files", "data_loaded", disabled=False)
    frame.set_state_attribute("new_files", visible=True, description="New data", **button_style)

    def address_bar_handler(widget):
        dir = frame.get_attribute("address_bar", "value")
        if os.path.isdir(dir):
            dir = os.path.abspath(dir)
            frame.set_state_data("dir", dir)
            update_dir_bar_list()
            frame.update()
            frame.set_attributes("address_bar", value=dir)
            frame.set_attributes("directory_list", value=".", selected_label=u".")
        else:
            dir = os.path.abspath(dir)
            frame.set_state_data("dir", dir)
            frame.update()
            frame.set_attributes("address_bar", value=dir)

    def directory_list_handler(name, value):
        dir = frame.get_state_data("dir")
        dir = dir + "/" + frame.get_attribute("directory_list", "value")
        if os.path.isdir(dir):
            dir = os.path.abspath(dir)
            frame.set_state_data("dir", dir)
            update_dir_bar_list()
            frame.update()
            frame.set_attributes("address_bar", value=dir)
            frame.set_attributes("directory_list", value=".", selected_label=u".")
        else:
            dir = os.path.abspath(dir)
            frame.update()
            frame.set_attributes("address_bar", value=dir)

    def load_files_handler(widget):
        file = frame.get_attribute("address_bar", "value")
        data = frame.get_state_data("data")
        data.families = data.read_file(file)

        frame.set_state_data("data", data)
        frame.set_state("data_loaded")
        frame.set_attributes("address_bar", value=file)
        update_efamily_fields(add_family_item)

    def save_files_handler(widget):
        file = frame.get_attribute("address_bar", "value")
        data = frame.get_state_data("data")
        data.write_file(file)
        
    def new_files_handler(widget):
        data = frame.get_state_data("data")
        data.families = []

        frame.set_state_data("data", data)
        frame.set_state("data_loaded")
        update_efamily_fields(add_family_item)
            
    frame.set_state_callbacks("address_bar", address_bar_handler, attribute=None, type="on_submit")
    frame.set_state_callbacks("directory_list", directory_list_handler)
    frame.set_state_callbacks("load_files", load_files_handler, attribute=None, type="on_click")
    frame.set_state_callbacks("save_files", save_files_handler, attribute=None, type="on_click")
    frame.set_state_callbacks("new_files", new_files_handler, attribute=None, type="on_click")

    frame.set_object("window", widgets.Box())
    frame.set_object("Title", widgets.HTML())
    frame.set_object("widget", widgets.Tab())
    frame.set_object("page_data", widgets.VBox())
    frame.set_object("address_bar", widgets.Text())
    frame.set_object("directory_list", widgets.Select())
    frame.set_object("load_save_group", widgets.HBox())
    frame.set_object("load_files", widgets.Button())
    frame.set_object("save_files", widgets.Button())
    frame.set_object("new_files", widgets.Button())

    frame.set_state_attribute("page_edit", visible=True, **group_style)
    frame.set_state_attribute("select_family_delete_group", visible=True, **group_style)
    frame.set_state_attribute("select_family", visible=True, disabled=True, description="Select family")
    frame.set_state_attribute("select_family", "data_loaded", disabled=False)
    frame.set_state_attribute("delete_selection", visible=True, disabled=True, description="Delete entry", **button_style)
    frame.set_state_attribute("delete_selection", "data_loaded", disabled=False)
    frame.set_state_attribute("husband_wife_group", visible=True, **group_style)
    frame.set_state_attribute("husband", visible=True, disabled=True, description="Husband")
    frame.set_state_attribute("husband", "data_loaded", disabled=False)
    frame.set_state_attribute("wife", visible=True, disabled=True, description="wife")
    frame.set_state_attribute("wife", "data_loaded", disabled=False)
    frame.set_state_attribute("father_group", visible=True, **group_style)
    frame.set_state_attribute("hfather", visible=True, disabled=True, description="father")
    frame.set_state_attribute("hfather", "data_loaded", disabled=False)
    frame.set_state_attribute("wfather", visible=True, disabled=True, description="father")
    frame.set_state_attribute("wfather", "data_loaded", disabled=False)
    frame.set_state_attribute("mother_group", visible=True, **group_style)
    frame.set_state_attribute("hmother", visible=True, disabled=True, description="mother")
    frame.set_state_attribute("hmother", "data_loaded", disabled=False)
    frame.set_state_attribute("wmother", visible=True, disabled=True, description="mother")
    frame.set_state_attribute("wmother", "data_loaded", disabled=False)
    frame.set_state_attribute("birth_group", visible=True, **group_style)
    frame.set_state_attribute("hbirth", visible=True, disabled=True, description="birth")
    frame.set_state_attribute("hbirth", "data_loaded", disabled=False)
    frame.set_state_attribute("wbirth", visible=True, disabled=True, description="birth")
    frame.set_state_attribute("wbirth", "data_loaded", disabled=False)
    frame.set_state_attribute("death_group", visible=True, **group_style)
    frame.set_state_attribute("hdeath", visible=True, disabled=True, description="death")
    frame.set_state_attribute("hdeath", "data_loaded", disabled=False)
    frame.set_state_attribute("wdeath", visible=True, disabled=True, description="death")
    frame.set_state_attribute("wdeath", "data_loaded", disabled=False)
    frame.set_state_attribute("marriage", visible=True, disabled=True, description="marriage")
    frame.set_state_attribute("marriage", "data_loaded", disabled=False)
    frame.set_state_attribute("children", visible=True, disabled=True, description="children")
    frame.set_state_attribute("children", "data_loaded", disabled=False)
    frame.set_state_attribute("pictures", visible=True, disabled=True, description="pictures")
    frame.set_state_attribute("pictures", "data_loaded", disabled=False)
    frame.set_state_attribute("notes", visible=True, disabled=True, description="notes")
    frame.set_state_attribute("notes", "data_loaded", disabled=False)
    frame.set_state_attribute("apply_change", visible=True, disabled=True, description="Apply Changes")
    frame.set_state_attribute("apply_change", "data_loaded", disabled=False)

    def delete_selection_handler(widget):
        data = frame.get_state_data("data")
        husband = frame.get_attribute("husband", "value")
        wife = frame.get_attribute("wife", "value")
        id = ""
        if husband != "":
            id = husband
        
        if wife != "":
            if id != "":
                id = id + " "
            id = id + wife
        
        id = id.replace(" ", "_")
        family_id = None
        for i, family in enumerate(data.families):
            if id == family.id:
                family_id = i
                break
        
        if family_id != None:
            del data.families[i]
        frame.set_state_data("data", data)
        clear_efamily_fields()

    def select_family_handler(name, value):
        update_efamily_fields(value)
        
    def apply_change_handler(widget):
        data = frame.get_state_data("data")
        husband = frame.get_attribute("husband", "value")
        wife = frame.get_attribute("wife", "value")
        hfather = frame.get_attribute("hfather", "value")
        wfather = frame.get_attribute("wfather", "value")
        hmother = frame.get_attribute("hmother", "value")
        wmother = frame.get_attribute("wmother", "value")
        hbirth = frame.get_attribute("hbirth", "value")
        wbirth = frame.get_attribute("wbirth", "value")
        hdeath = frame.get_attribute("hdeath", "value")
        wdeath = frame.get_attribute("wdeath", "value")
        marriage = add_pblocks(frame.get_attribute("marriage", "value"))
        children = add_pblocks(frame.get_attribute("children", "value"))
        pictures = frame.get_attribute("pictures", "value")
        notes = add_pblocks(frame.get_attribute("notes", "value"))
        id = ""
        if husband != "":
            id = husband
        
        if wife != "":
            if id != "":
                id = id + " "
            id = id + wife
        
        id = id.replace(" ", "_")
        exists = False
        new_family = None
        for family in data.families:
            if id == family.id:
                exists = True
                new_family = family
                break
        
        if not exists:
            new_family = efamily.data_family()
        
        family = new_family
        family.id = id
        family.husband = husband
        family.wife = wife
        family.hfather = hfather
        family.wfather = wfather
        family.hmother = hmother
        family.wmother = wmother
        family.hbirth = hbirth
        family.wbirth = wbirth
        family.hdeath = hdeath
        family.wdeath = wdeath
        family.marriage = marriage
        family.children = children
        family.pictures = pictures
        family.notes = notes
        
        if not exists:
            data.families.append(family)

        update_efamily_fields()

            
    frame.set_state_callbacks("delete_selection", delete_selection_handler, attribute=None, type="on_click")
    frame.set_state_callbacks("select_family", select_family_handler)
    frame.set_state_callbacks("apply_change", apply_change_handler, attribute=None, type="on_click")

    frame.set_object("page_edit", widgets.VBox())
    frame.set_object("select_family_delete_group", widgets.HBox())
    frame.set_object("select_family", widgets.Dropdown())
    frame.set_object("delete_selection", widgets.Button())
    frame.set_object("husband_wife_group", widgets.HBox())
    frame.set_object("husband", widgets.Text())
    frame.set_object("wife", widgets.Text())
    frame.set_object("father_group", widgets.HBox())
    frame.set_object("hfather", widgets.Text())
    frame.set_object("wfather", widgets.Text())
    frame.set_object("mother_group", widgets.HBox())
    frame.set_object("hmother", widgets.Text())
    frame.set_object("wmother", widgets.Text())
    frame.set_object("birth_group", widgets.HBox())
    frame.set_object("hbirth", widgets.Text())
    frame.set_object("wbirth", widgets.Text())
    frame.set_object("death_group", widgets.HBox())
    frame.set_object("hdeath", widgets.Text())
    frame.set_object("wdeath", widgets.Text())
    frame.set_object("marriage", widgets.Textarea())
    frame.set_object("children", widgets.Textarea())
    frame.set_object("pictures", widgets.Textarea())
    frame.set_object("notes", widgets.Textarea())
    frame.set_object("apply_change", widgets.Button())

    frame.set_state_attribute("page_generate", visible=True, **group_style)
    frame.set_state_attribute("generate_tree", "data_loaded", visible=True, description="Generate tree", **button_style)
    frame.set_state_attribute("download_link", visible=True, value = "No Link: Tree not generated", **group_style)

    def generate_tree_handler(widget):
        dir = frame.get_state_data("dir")
        output = "./../notebook/files/"
        shutil.rmtree(output, True)
        os.mkdir(output)
        if os.path.isdir(dir):
            data = efamily.interpreter()
            data.process("./../data/", output, "./../template/")
            print("Generated " + str(len(data.families)) + " file(s).")
        
        fname = ""
        for filename in os.listdir(output):
            if ".html" in filename:
                fname = filename
                break
        
        shutil.make_archive("./../notebook/files", "zip", output)
        frame.set_attributes("download_link", value= "<a href=\"files.zip\" download=\"family_tree.zip\">Family Tree Download</a>, <a href=\"files/" + filename + "\" target=\"_blank\">Family Tree View</a>")
            
    frame.set_state_callbacks("generate_tree", generate_tree_handler, attribute=None, type="on_click")

    frame.set_object("page_generate", widgets.VBox())
    frame.set_object("generate_tree", widgets.Button())
    frame.set_object("download_link", widgets.HTML())

    update_dir_bar_list()
    frame.display_object("window")
