class Class:
    def __init__(self,Id,className,teacherId):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.className = className
        self.teacherId = teacherId
    
    @staticmethod
    def createClass(obj):
        list = []
        for i in obj:
            list.append(Class(i[0],i[1],i[2]))
        return list
            
        