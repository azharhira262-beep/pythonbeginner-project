class students:
    schoolname ="abcd"
    campus= "gujrat"
    def  dispaly (self):
        print(self.NAME,self.ROLLNO)
         

student1 = students()
student1.NAME = "HIRA"
student1.ROLLNO = "23"
student1.GRADE = "A"

student2= students()
student2.NAME= "anaya"
student2.ROLLNO= "45"
student2.GRADE = "B"

print("the data is here:",student1.ROLLNO)
print("second std data is here:", student2.NAME) 
print("here it is:",student1.NAME)
print("school is:",student1.schoolname)
 
 
student1.dispaly()

 