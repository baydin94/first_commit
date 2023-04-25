from DbManager import DbManager
import datetime
from Student import Student

class App:
    def __init__(self):
        self.db = DbManager()        
    
    def initApp(self):   
        msg = "***\n1-Öğrencileri Listele\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Çıkış (E/Ç)" 
        while True:
            print(msg)
            process = input("Yapmak istediğiniz işlem: ")
            if process == "1":
                self.displayStudents()
            elif process == "2":
                self.addStudentByClassId()
            elif process == "3":
                self.editStudent()
            elif process == "4":
                self.deleteStudent()
            elif process == "E" or "Ç":
                break
    
    def displayClasses(self):
        classes = self.db.getClasses() 
        if classes:       #None, False, boş bir liste, sözlük veya demet olmaması durumunda if bloğunu çalıştıracaktır.
            for c in classes:
                print(f'{c.Id} - {c.className}')
        
    def displayStudents(self):
        self.displayClasses()
        classId = int(input("Hangi Sınıf: "))
        
        students = self.db.getStudentsByClassId(classId)
        print("Öğrenci Listesi")
        if students:
            for s in students:
                print(f'{s.Id}  {s.studentNumber}-{s.firstName} {s.lastName}')
            return classId
    
    def addStudentByClassId(self):
        self.displayClasses()
        classId = int(input('Eklemek istediğiniz sınıf: '))
        self.db.getStudentsByClassId(classId)
        studentNumber = input("Öğrenci Numarası: ")
        firstName = input("Öğrenci Adı: ")
        lastName = input("Öğrenci Soyadı: ")
        gender = input("Öğrenci Cinsiyet (E/K): ")        
        while True:
            date_str= input("Lütfen doğum tarihini yyyy.mm.dd formatında giriniz: ")
            try:
                birthdate = datetime.datetime.strptime(date_str,"%Y.%m.%d")
                break
            except ValueError:
                print("Hatalı tarih formati girdiniz lütfen yyyy.aa.gg şeklinde giriniz: ")
        student = Student(None,studentNumber,firstName,lastName,birthdate,gender,classId)
        self.db.addStudent(student)
    
    def editStudent(self):        
        classId = self.displayStudents()
        studentId = int(input("Öğrenci Id: "))
        
        student = self.db.getStudentById(studentId)
        if student:
            print(student[0].firstName)
            student[0].studentNumber = input("Numara: ") or student[0].studentNumber
            student[0].firstName = input("İsim: ") or student[0].firstName
            student[0].lastName = input("Soyad: ") or student[0].lastName
            student[0].birthdate = datetime.datetime.strptime(input("Doğum Tarihi (yyyy.aa.gg): "),"%Y.%m.%d") or student[0].birthdate
            student[0].gender = input("Cinsiyet (E/K): ") or student[0].gender
            self.db.editStudent(student[0])
    
    def deleteStudent(self):
        classId = self.displayStudents()
        studentId = int(input("Silmek istediğiniz Id: "))
        self.db.deleteStudent(studentId)

app = App()
app.initApp()