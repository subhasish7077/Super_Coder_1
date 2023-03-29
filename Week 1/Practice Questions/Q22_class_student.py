#  Addmission Process of University

class Student:
    __student_id=None
    __marks=None
    __age=None
    course_dir={1001:25575,1002:15500}
    __course=None
    __feese=None
    __discount=None
    def __init__(s,id,marks,age,course) -> None:
        s.__student_id=id
        s.__marks=int(marks)
        s.__age=int(age)
        s.__course=course
        s.__feese=s.course_dir[course]
    def validation_marks(s):
        if(s.__marks>=0 and s.__marks<=100):
            return True
        else:
            return False
    def validate_age(s):
        if(s.__age>=20):
            return True
        else:
            return False
    def check_qualification(s):
        if(s.validate_age() and s.validation_marks() and s.__marks>=65):
            s.check_dicount()
            return True
        else:
            return False
    def check_dicount(s):
        if(s.__marks>85):
            s.__discount=25
            s.__feese=s.__feese-(s.__feese*0.25)
            
    def set_id(s,id):
        s.__student_id=id
    def set_marks(s,marks):
        s.__marks=marks
    def set_age(s,age):
        s.__age=age
    def set_course(s,course):
        s.__feese=s.course_dir[course]
        s.__course=course

    def get_id(s):
        return s.__student_id
    def get_marks(s):
        return s.__marks
    def get_age(s):
        return s.__age
    def get_course(s):
        return s.__course
    def get_feese(s):
        return s.__feese
    def get_discount(s):
        return s.__discount
    
    def display(s):
        print()
        print("Id: ",s.__student_id)
        print("Mark: ",s.__marks)
        print("Age: ",s.__age)
        if(s.check_qualification()):
            print("You are Eligible for Addmission")
            print("Course: ",s.__course)
            print("Discount: ",s.__discount,"%")
            print("Feese: ",s.__feese)
        else:
            print("You are not Eligible for Addmission")

# id,marks,age,course
s1=Student(101,67,22,1001)
s2=Student(202,87,21,1002)
s3=Student(303,37,25,1001)

s1.display()
s2.display()
s3.display()