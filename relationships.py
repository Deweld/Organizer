import os
import shutil


class Relationship():
    def __init__(self, name):
        pass



class Item():
    def __init__(self, name, catagory):
        pass




class Catagory():
    def __init__(self, name):
        self.name = name

    def print_relationships(self, catagory=None):
        if catagory == None:
            # print all
            pass
        else:
            # print selected
            pass

    def add_parent(self):
        pass

    def add_paring(self):
        pass

    def add_child(self):
        pass

    def remove_parent(self):
        pass

    def remove_paring(self):
        pass

    def remove_child(self):
        pass
        



class System():
    def __init__(self, name, foldername):
        self.name = name
        self.folder = foldername + "/" + self.name
        self.catagory_folder = self.folder + "/Catagory"

        # key == name
        # value = [catagory class, list of items currently in that Catagory]
        self.catagories = {}

        self.import_file()

    def import_file(self):
        try:
            print("Known File")
            with open(self.folder + "/catagories", "r") as catagories:
                # import relations
                pass
        except:
            os.mkdir(self.folder)
            os.mkdir(self.catagory_folder)
            print("Unknown File")
            open(self.folder + "/catagories", "w")

    def init_catagories(self):
        print("\n-------")
        print("Please enter the names of catagories you want to be in your system.  More catagories can be added later, and these catagories can be modified later as well.")
        print("-------")
        print("get current Catagories : current")
        print("add new Catagory       : new <name>")
        print("remove Catagory        : remove <name>")
        print("finish initialization  : done")
        print("-------\n")
        while True:
            user_input = input()
            if user_input == "done":
                print("Finished initial catagories:")
                for key in self.catagories:
                    print(key)
                break
            elif user_input == "help":
                print("\n-------")
                print("get current catagories : current")
                print("add new Catagory       : new <name>")
                print("remove Catagory        : remove <name>")
                print("-------\n")
            elif user_input == "current":
                print("Current catagories:")
                for key in self.catagories:
                    print(key)
                print("\n")
            elif len(user_input) > 3:
                info = user_input.split(" ")
                if info[0] == "new":
                    if len(info) < 2:
                        print("add new Catagory       : new <name>")
                        continue
                    else:
                        name = user_input[3:].strip()
                        self.add_catagory(name)
                elif info[0] == "remove":
                    if len(info) < 2:
                        print("remove Catagory        : remove <name>")
                        continue
                    else:
                        name = user_input[3:]
                        self.remove_catagroy(name)
                        
    def define_catagories(self):
        print("\n-------")
        print("Add relations between different catagories to the selected Catagory.  Added relationships will have their relationship mirrored onto the selected catagory.  Parent relationships will be items that can have this catagory as a member.  Child relationships will be items that can be members of this catagory.  Pairing relationships will be items come together as set, but are not parents or childen of each other.")
        print("-------")
        print("get catagories list      : catagories")
        print("get current properties   : current")
        print("change selected Catagory : modify <catagory>")
        print("add parent relationship  : add parent")
        print("remove parent            : remove parent")
        print("add pairing relationship : add pairing")
        print("remove pairing           : remove pairing")
        print("add child relationship   : add child")
        print("remove child             : remove child")
        print("add Catagory             : add catagory <name>")
        print("remove Catagory          : remove catagory <name>")
        print("finish relationships     : done")
        print("-------\n")

        selected_catagory = self.catagories.keys()[0]
        print("Modifying Catagory: {}".format(selected_catagory))
        while True:
            user_input = input()
            if user_input == "done":
                print("Finished catagories properties:")
                print("-------")
                for key in self.catagories:
                    self.catagories[key][0].print_relationships()
                print("-------\n")
                break
            elif user_input == "help":
                print("\n-------")
                print("get catagories list      : catagories")
                print("get current properties   : current")
                print("change selected Catagory : modify <catagory>")
                print("add parent relationship  : parent")
                print("remove parent            : remove parent")
                print("add pairing relationship : pairing")
                print("remove pairing           : remove pairing")
                print("add child relationship   : child")
                print("remove parent            : remove parent")
                print("finish relationships     : done")
                print("-------\n")
            elif user_input == "catagories":
                print("\n-------")
                print("Current catagories:")
                for key in self.catagories:
                    print(key)
                print("-------\n")
            elif user_input == "current":
                print("\n-------")
                print("Modifying Catagory: {}".format(selected_catagory))
                self.catagories[selected_catagory][0].print_relationships()
                print("-------\n")
            elif len(user_input) > 3:
                info = user_input.split(" ")
                if info[0] == "add":
                    if len(info) == 2:
                        if info[1] == "parent":
                            self.catagories[selected_catagory][0].add_parent()
                        elif info[1] == "pairing":
                            self.catagories[selected_catagory][0].add_pairing()
                        elif info[1] == "child":
                            self.catagories[selected_catagory][0].add_child()
                    elif len(info) > 2:
                        if info[1] == "catagory":
                            self.add_catagory(info[12].strip())
                elif info[0] == "remove":
                    if len(info) == 2:
                        if info[1] == "parent":
                            self.catagories[selected_catagory][0].remove_parent()
                        elif info[1] == "pairing":
                            self.catagories[selected_catagory][0].remove_pairing()
                        elif info[1] == "child":
                            self.catagories[selected_catagory][0].remove_child()
                    elif len(info) > 2:
                        if info[1] == "catagory":
                            self.remove_catagory(info[15].strip())
                elif info[0] == "modify":
                    if len(info) == 2:
                        name = user_input[6].strip()
                        new_selection = self.catagories.get(name, False)

                        if new_selection:
                            print("Now Modifying Catagory: {}".format(selected_catagory))
                            selected_catagory = new_selection
                        else:
                            print("Failed to find catagory: {}".format(name))

    def add_catagory(self, name):
        new_name = True
        for key in self.catagories:
            if key == name:
                new_name = False
        
        if not new_name:
            print("Duplicate Catagory: {}".format(name))
        else:
            print("New Catagory made: {} ".format(name))
            new_catagory = Catagory(name)
            self.catagories[name] = [new_catagory, []]

    def remove_catagory(self, name):
        removed_name = self.catagories.pop(name, False)

        if removed_name:
            print("Catagory removed: {}".format(name))
            shutil.rmtree(self.catagory_folder + name)
        else:
            print("Failed to find catagory: {}".format(name))

    def write_catagories(self):
        catagory_names = self.catagories.keys()

        with open(self.folder + "/catagories", "w") as catagories:
            for catagory in catagory_names:
                catagories.write(catagory)

        for catagory in catagory_names:
            # write specific file stuff
            with open(self.catagory_folder + "/" + catagory, "w") as catagories:
                properties = self.catagories[catagory]
                # Catagory
                pass






