class Lesson:
    def __init__(self,Id,lessonName):
        if Id is None:
            self.Id=0
        else:
            self.Id = Id
        self.lessonName = lessonName
    