# Challenge 3: Implement the Complete Student Class
class school:

    school_name = "Edyoda_Institution"  

    def __init__(self,rno,name):
        self.rno = rno
        self.name = name

    def display(self):
        print(f"Roll No. : {self.rno} \nName : {self.name} \nSchool Name : {school.school_name}")

    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
    @classmethod
    def set_school_name(cls,s_name):
        cls.school_name = s_name

obj = school(1, "Hari")
obj.display()
obj = school(2, "Melvin")
obj.display()
obj = school(3, "Karthik")
obj.display()


