import mysql.connector
from connection import connection
from Student import Student
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self,Id):
        query = "Select * from student where Id = %s"
        value = (Id,)
        self.cursor.execute(query,value)
        
        try:
            obj = self.cursor.fetchone()            
            return Student.createStudent(obj)
        except mysql.connector.errors as err:
            print('Hata: ',err)
    
    def getStudentsByClassId(self,classId):
        query = "Select * from student where classId = %s"
        value = (classId,)
        self.cursor.execute(query,value)
        
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except mysql.connector.errors as err:
            print('Hata: ',err)
    
    def getClasses(self):
        query = "Select * from Class"
        self.cursor.execute(query)
        
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except mysql.connector.errors as err:
            print('Hata: ',err)

    def addStudent(self,student:Student):
        query = "INSERT INTO STUDENT(studentNumber,firstName,lastName,birthdate,gender,classId) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (student.studentNumber,student.firstName,student.lastName,student.birthdate,student.gender,student.classId)
        self.cursor.execute(query,values)
        
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt eklendi')
        except mysql.connector.errors as err:
            print('Hata: ',err)
    
    def editStudent(self,student:Student):
        query = "Update Student Set studentNumber=%s,firstName=%s,lastName=%s,birthdate=%s,gender=%s,classId=%s where Id=%s"
        values = (student.studentNumber,student.firstName,student.lastName,student.birthdate,student.gender,student.classId,student.Id)
        self.cursor.execute(query,values)
        
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt güncellendi')
        except mysql.connector.errors as err:
            print('Hata: ',err)
    
    def deleteStudent(self,studentId):
        query = "Delete from student where Id = %s"
        value = (studentId,)
        self.cursor.execute(query,value)
        
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt silindi')
        except mysql.connector.errors as err:
            print('Hata: ',err)
    def getStudentsCountByClassId(self,classId):
        query = "Select Count(*) from Student where ClassId=%s"
        value = (classId,)
        self.cursor.execute(query,value)
        
        try:
            obj = self.cursor.fetchone()
            # return obj            #dersen tuple döner yani (6,) yazar 
            if obj:
                return obj[0]           #dersem tuple dönmez artık 6 yazar ve stringe çevrilir
        except mysql.connector.errors as err:
            print('Hata: ',err)
            
    def __del__(self):
        self.connection.close()
        print('db silindi')










