import pyexcel as p
from YKWIM.Enumerations import Enumerations
from YKWIM.associations import Associations
from YKWIM.attributes import Attributes
from YKWIM.classes import Classes

class Template:
    
    def __init__(self, file) -> None:
        self.file=file
        self.classes=Classes()
        self.attributes=Attributes()
        self.associations=Associations()
        self.enumerations=Enumerations()
    
    def openTemplate(self):
        file= p.get_book(file_name=self.file)
        return file

    def saveTemplate(self):
        pass