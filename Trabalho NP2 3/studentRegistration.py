#Procura por um aluno pelo ra
def select(ra, students):
    for student in students:
        if student[0] == ra:
            return student
    return None
#Adiciona um aluno caso não exista outro com o mesmo ra
def include(student, students):
    result = select(student[0],students)
    if result == None:
        students.append(student)
    return result
    

def update(student, index, students):
    students[index] = student

    