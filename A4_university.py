class student:
    def __init__(self):
        self._student_id=None
        self._age=None
        self._marks=None

    def setter(self,i,a,m):
        self._student_id=i
        self._age=a
        self._marks=m

    def getter(self):
        return self._student_id,self._age,self._marks

    def validate_marks(self):
        if self._marks>=0 and self._marks<=100:
            return True
        else:
            return False

    def validate_age(self):
        if self._age>20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self._marks>=65:
                return True
            else:
                return False
        else:
            return False

for i in range(3):
    print("\nStudent ",i+1,":")
    sid=input("Enter Student ID: ")
    age=int(input("Enter age: "))
    marks=float(input("Enter marks: "))
    ob=student()
    ob.setter(sid,age,marks)
    print("Qualified: ",ob.check_qualification())
    print("ID: %s\nAge: %s\nMarks: %s"%ob.getter())
    
