'''
Softsytems Ltd is a private firm that provides software solutions to its customers.
The management wants to calculate salary for the employees. There are two types of 
employees namely graduates who are in probation period and laterals who are experienced 
joiners in the company. 
Write a python program based on the class diagram given below.

RULES TO FOLLOW
===================
Class Description:

Employee class:
validate_basic_salary(): Basic salary of an employee is always more than 3000 
    If basic salary is valid, return true. Else return false
validate_qualification(): Employee should posses either a "Bachelors" or "Masters" degree
    If qualification is valid, return true. Else return false

Graduate class:
validate_job_band(): Graduates can be in "A", "B" or "C" job band
    If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary Validate basic salary, qualification 
and job band If valid,
Compute gross salary as basic salary + PF+ TPI amount + incentive
    PF is 12% of basic salary
    Identify TPI amount based on cgpa
    Identify incentive based on job band. 
    Incentive should be applied on basic salary (Refer tables given)
Return gross salary
Else return -1
Job Band	A	B	C	D	E	F
Incentive %	4	6	10	13	16	20

CGPA	4 to 4.25	4.26 to 4.5	 4.51 to 4.75	4.76 to 5
TPI Amount	1000	    1700	         3200	          5000

Lateral class:
validate_job_band(): Laterals can be in "D", "E" or "F" job band
If job band is valid, return true. Else return false
calculate_gross_salary(): Calculate gross salary
Validate basic salary, qualification and job band
If valid,
Compute gross salary as basic salary + PF + SME bonus + incentive
    PF is 12% of basic salary
    Identify SME bonus based on skill set
    Identify incentive based on job band. Incentive should be applied on basic salary (Refer
    tables given)
Return gross salary
Skill Set	SME Bonus
AGP	        6500
AGPT	    8200
AGDEV	    11500
Else return -1
Perform case sensitive string comparison.
For testing:
Create objects of Graduate and Lateral classes
Invoke calculate_gross_salary() on Graduate and Lateral objects
Display the details
'''
class Employee:
    def __init__(s,name,salary,qualification) -> None:
        s.__salary=salary
        s.__name=name
        s.__qualification=qualification
    def validate_basic_salary(s):
        if(s.__salary>3000):
            return True
        return False
    def validate_qualification(s):
        if(s.__qualification in ["Bachelors","Masters"]):
            return True
        return False
    def get_basic_salary(s):
        return s.__salary
    def get_incentive(s,job_brand):
        d={'A':0.04,'B':0.06,'C':0.10,'D':0.13,'E':0.16,'F':0.20}
        return s.__salary*d[job_brand]
    def get_name(s):
        return s.__name
    def get_qualification(s):
        return s.__qualification
    
class Graduate(Employee):
    def __init__(s, name, salary, qualification,cgpa,job_brand) -> None:
        super().__init__(name, salary, qualification)
        s.__job_brand=job_brand
        s.__gross_salary=None
        s.__cgpa=cgpa
    def validate_job_band(s):
        if s.__job_brand in ["A","B","C"]:
            return True
        return False
    def calculate_gross_salary(s):
        if(super().validate_basic_salary() and super().validate_qualification() and s.validate_job_band()):
            # basic salary + PF+ TPI amount + incentive
            PF=0.12*super().get_basic_salary()
            TPI=0
            if(s.__cgpa>=4 and s.__cgpa<=4.25):
                TPI=1000
            elif(s.__cgpa>=4.26 and s.__cgpa<=4.5):
                TPI=1700
            elif(s.__cgpa>=4.51 and s.__cgpa<=4.75):
                TPI=3200
            elif(s.__cgpa>=4.76 and s.__cgpa<=5):
                TPI=5000
            incentive=super().get_incentive(s.__job_brand)
            s.__gross_salary=super().get_basic_salary()+PF+TPI+incentive
        else:
            s.__gross_salary=-1
    def get_gross_salary(s):
        return s.__gross_salary
    def get_job_brand(s):
        return s.__job_brand
    def get_cgpa(s):
        return s.__cgpa
    def display(s):
        print()
        print("Employee Details:\n")
        print("Name: ",super().get_name())
        print("Qualification: ",super().get_qualification())
        print("Job Brand: ",s.__job_brand)
        print("CGPA: ",s.__cgpa)
        print("Gross Salary: ",s.__gross_salary)
        print()

class Lateral(Employee):
    def __init__(s, name, salary, qualification,skill_set,job_brand) -> None:
        super().__init__(name, salary, qualification)
        s.__job_brand=job_brand
        s.__skill_set=skill_set
        s.__gross_salary=None
    def validate_job_band(s):
        if(s.__job_brand in ["D","E","F"]):
            return True
        return False
    def calculate_gross_salary(s):
        if(super().validate_basic_salary() and super().validate_qualification() and s.validate_job_band()):
            PF=0.12*super().get_basic_salary()
            skill={'AGP':6500,'AGPT':8200,'AGDEV':11500}
            SME=skill[s.__skill_set]
            incentive=super().get_incentive(s.__job_brand)
            s.__gross_salary=super().get_basic_salary()+PF+SME+incentive
        else:
            s.__gross_salary=-1
    def get_gross_salary(s):
        return s.__gross_salary
    def get_job_brand(s):
        return s.__job_brand
    def get_skill_set(s):
        return s.__skill_set
    def display(s):
        print()
        print("Employee Details:\n")
        print("Name: ",super().get_name())
        print("Qualification: ",super().get_qualification())
        print("Job Brand: ",s.__job_brand)
        print("Skill set: ",s.__skill_set)
        print("Gross Salary: ",s.__gross_salary)
        print()
    
G=Graduate('Kiran',4000,'Bachelors',4.6,'A')
G.calculate_gross_salary()
G.display()

L=Lateral('Sipu',5000,'Masters','AGDEV','E')
L.calculate_gross_salary()
L.display()