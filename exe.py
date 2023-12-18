import json
import os

class ExeItem:
    def __init__(self, line) -> None:
        self.__name = line["name"]
        self.__path = line["path"]
        self.__file = line["file"]
        
    def name(self):
        return self.__name
    
    def path(self):
        return self.__path
    
    def exe(self):
        return self.path() + '/' + self.__file
    
    def raw(self):
        return {"name": self.name(), "path": self.path(), "file": self.__file}
    
        
        
class Exe:
    def __init__(self, data) -> None:
        self.__items = []
        for line in data:
            self.__items.append(ExeItem(line))
            
    def add(self, line):
        self.__items.append(ExeItem(line))
        
    def raw(self):
        ret = []
        for item in self.__items:
            ret.append(item.raw())
        return ret
    
    def execute(self):
        for item in self.__items:
            print("------------execute {}-------------".format(item.name()))
            os.chdir(item.path())
            os.system("python {}".format(item.exe()))

def getExe():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return Exe(list(data))
    
def addExe(name, path, file):
    data = getExe()
    data.add({"name": name, "path": path, "file": file})
    dumpExe(data)
        
def dumpExe(data):
    with open('data.json', 'w') as file:
        json.dump(data.raw(), file)
        
def execute():
    data = getExe()
    data.execute()