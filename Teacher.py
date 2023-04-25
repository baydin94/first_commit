class Teacher:
    def __init__(self,Id,firstName,lastName,branch,gender):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.firstName = firstName
        self.lastName = lastName
        self.brach = branch
        self.gender = gender