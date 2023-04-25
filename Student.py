class Student:
    def __init__(self,Id,studentNumber,firstName,lastName,birthdate,gender,classId):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.studentNumber = studentNumber
        self.firstName = firstName
        self.lastName = lastName
        self.birthdate = birthdate
        self.gender = gender
        self.classId = classId
    
    @staticmethod
    def createStudent(obj):
        list = []
        if isinstance(obj,tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list
    