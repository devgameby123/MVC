#เรียกใช้งาน view model
from view import MainWindow
from model import MOMLModel

class Controller:
    #สร้าง Constructor รับ model view เข้ามาทำงาน
    def __init__(self,model,view):
        self.model = model
        self.view = view
        #เชื่อมการกดของปุ่ม
        self.view.bttag1.clicked.connect(self.ClickedOnTag1)
        self.view.bttag2.clicked.connect(self.ClickedOnTag2)
    #เรียกใช้งานเมื่อคลิกปุ่ม
    def ClickedOnTag1(self):
        self.view.textout1.clear()
        textInput = self.view.textinput.toPlainText()
        self.view.textout1.append(self.model.parse_text1(textInput))
    def ClickedOnTag2(self):
        self.view.textout2.clear()
        textInput = self.view.textinput.toPlainText()
        self.view.textout2.append(self.model.parse_text2(textInput))
        
#