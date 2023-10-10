#Procura por um curso pelo seu id
def select(id, courses):
    for course in courses:
        if course[0] == id:
            return course
    return None

#Exibe todos os cursos e suas disciplinas
def selectAll(courses, disciplines ):
    print("Teste")
    for course in courses: 
        print(f"ID do curso: {course[0]}")
        print(f"Nome do curso: {course[1]}")
        print(f"Duração do curso: {course[2]}")
        for discipline in disciplines:
            if discipline[2] == course[0]:
                print(f"Nome da disciplina: {discipline[1]}")

#Adiciona um aluno caso não exista outro com o mesmo ra
def include(course, courses):
    result = select(course[0],courses)
    if result == None:
        courses.append(course)
    return result

def update(course, courses):
    pass
