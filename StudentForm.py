import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow,QInputDialog,QLineEdit,QMessageBox,QListWidget,QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from ui_studentForm import Ui_MainWindow
from Student import Student
from DbManager import DbManager
import datetime

class MyApp(QMainWindow):
    class CustomQListWidgetItem(QListWidgetItem):
        def __init__(self, text, classId):
            super().__init__(text)
            self.classId = classId 
            
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DbManager()   
        self.currentClassId = None
        self.currentStudentId = None
        self.setWindowTitle('My first Application')
        self.setWindowIcon(QIcon('student.png'))
    
        self.ui.btnShowStudents.clicked.connect(self.displayClasses) 
        self.ui.btnAddStudent.clicked.connect(self.addStudent)
        self.ui.btnEditStudent.clicked.connect(self.updateStudent)
        self.ui.btnDeleteStudent.clicked.connect(self.removeStudent)
        self.ui.btnExit.clicked.connect(self.closeApp)
        self.ui.btnBack.clicked.connect(self.backForm)
        self.ui.btnForward.clicked.connect(self.forwardForm)
        
        #Load Classes
        self.displayClasses()
        
        self.ui.lstStudents.itemClicked.connect(self.onItemClicked)   

    
    def getStudentFormById(self):
        currentIndex = self.ui.lstStudents.currentRow()
        item = self.ui.lstStudents.item(currentIndex)        
        self.currentStudentId = item.text().split('-')[0]
        student = self.db.getStudentById(self.currentStudentId)
        return (student,item)
        
        
    def displayClasses(self):        
        classes = self.db.getClasses()  
        if classes:       #None, False, boş bir liste, sözlük veya demet olmaması durumunda if bloğunu çalıştıracaktır.
            self.ui.lstStudents.clear()
            for c in classes:
                count = self.db.getStudentsCountByClassId(c.Id)                
                item = self.CustomQListWidgetItem(f"{c.Id}-{c.className}         Öğrneci Sayısı: {count}",c.Id)             
                self.ui.lstStudents.addItem(item)
                  
    
    def displayStudents(self,classId):  
        self.currentClassId = classId      
        students = self.db.getStudentsByClassId(self.currentClassId)        
        if students:
            self.ui.lstStudents.clear()            
            for s in students:
                self.ui.lstStudents.addItem(f'{s.Id}-    {s.studentNumber}  {s.firstName} {s.lastName}  {s.birthdate}  {s.gender}')
        
    def onItemClicked(self,item): 
        try:       
            self.displayStudents(item.classId)   
            classId = item.classId
            self.currentClassId = classId
            # print(self.currentClassId)         
        except AttributeError:
            pass  

    def addStudent(self):       
        currentIndex = self.ui.lstStudents.currentRow()  
        studentNumber,ok = QInputDialog.getText(self,"Yeni Öğrenci","Öğrenci No:")        
        if studentNumber and ok:
            firstName, ok = QInputDialog.getText(self,"Yeni Öğrenci","Öğrenci Adı:")
            if firstName and ok:
                lastName, ok = QInputDialog.getText(self,"Yeni Öğrenci","Öğrenci Soyadı:")
                if lastName and ok:
                    birthdate, ok = QInputDialog.getText(self,"Yeni Öğrenci","Öğrenci Doğum Yılı (yyyy.mm.gg):")
                    if birthdate and ok:
                        gender, ok = QInputDialog.getText(self,"Yeni Öğrenci","Öğrenci Cinsiyeti (E/K):")
                        if gender and ok:
                            
                            student = Student(None,studentNumber,firstName,lastName,birthdate,gender,self.currentClassId)
                            self.db.addStudent(student)
                            self.ui.lstStudents.insertItem(currentIndex+1,f"{student.firstName} {student.lastName}")
        return self.displayStudents(self.currentClassId)

    def updateStudent(self): 
        student,item = self.getStudentFormById()        
        if student:
            print(student[0].firstName)
            if item is not None:
                student[0].studentNumber=str(student[0].studentNumber)
                student[0].studentNumber , ok = QInputDialog.getText(self,"Öğrenci Güncelle","Öğrenci No:", QLineEdit.EchoMode.Normal,student[0].studentNumber)
                student[0].firstName , ok = QInputDialog.getText(self,"Öğrenci Güncelle","Öğrenci Adı:", QLineEdit.EchoMode.Normal,student[0].firstName)
                student[0].lastName , ok = QInputDialog.getText(self,"Öğrenci Güncelle","Öğrenci Soyadı:", QLineEdit.EchoMode.Normal,student[0].lastName)
                student[0].gender , ok = QInputDialog.getText(self,"Öğrenci Güncelle","Öğrenci Cinsiyeti:", QLineEdit.EchoMode.Normal,student[0].gender)                
                
                student[0].studentNumber = int(student[0].studentNumber)                
                msg = QMessageBox.question(
                    self,
                    'Güncelleme',
                    'Güncelleme yapmak istediğinize emin misiniz?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No 
                )
                if msg == QMessageBox.StandardButton.Yes:
                    self.db.editStudent(student[0])
                    self.displayStudents(self.currentClassId)
    
    def removeStudent(self):
        studentId,item = self.getStudentFormById()        
        if item is None:
            return        
        msg = QMessageBox()
        msg.setWindowTitle("Silme İşlemi")
        msg.setText("Öğrenciyi silmek istediğinize emin misiniz?")   
        msg.setIcon(QMessageBox.Icon.Warning)  
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) 
        retval = msg.exec()
        if retval == QMessageBox.StandardButton.Yes:            
            self.db.deleteStudent(self.currentStudentId)
        return self.displayStudents(self.currentClassId)
    
    def closeApp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Uygulamadan Çıkış")
        msg.setText("Uygulamadan çıkmak istediğinize emin misiniz?")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()
        if retval == QMessageBox.StandardButton.Yes:
            self.close()
    
    def backForm(self):
        self.displayClasses()
    def forwardForm(self):
        if self.currentClassId:
            self.displayStudents(self.currentClassId)
            
    def keyPressEvent(self,event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

def myapp():
    myapp = QApplication(sys.argv)
    win = MyApp()
    win.show()
    myapp.installEventFilter(win)
    myapp.exec()

myapp()