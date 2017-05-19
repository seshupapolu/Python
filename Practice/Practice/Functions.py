students=[]

def get_students_titlecase():
    students_titles=[]
    for stundent in students:
        students_titles.append(stundent.title())
    return  students_titles;


def add_student(name):
    students.append(name)

def print_students():
    list=get_students_titlecase()
    for stu in list:
        print(stu)

add_student("seshu")
add_student("papolu")

print_students()

