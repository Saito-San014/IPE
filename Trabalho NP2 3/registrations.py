#Procurar por um elemento pelo seu identificador
def select(id, registrations):
    for register in registrations:
        if register[0] == id:
            return register
    return None

#Adiciona um curso caso não exista outro com o mesmo id
def include(course, courses):
    result = select(course[0],courses)
    if result == None:
        courses.append(course)
    return result

#Exibe todas as disciplinas
def selectAllDisciplines(disciplines, courses):
    labelId = f"{' '*3}ID{' '*3}" 
    labelName = f"{' '*20}Nome da disciplina{' '*20}"
    labelCourse = f"{' '*20}Curso{' '*20}"
    title = f"|{labelId}|{labelName}|{labelCourse}|"
    print("-" * len(title)) 
    print(title)
    print("-" * len(title)) 
    for discipline in disciplines:
        idSpace = len(labelId) - len(str(discipline[0]))
        nameSpace = len(labelName) - len(discipline[1])
        id = (" " * int(idSpace/2))+str(discipline[0])+(" " * (idSpace - int(idSpace/2)))
        name = (" " * int(nameSpace/2))+discipline[1]+(" " * (nameSpace - int(nameSpace/2)))
        for course in courses:
            if discipline[2] == course[0]:
                courseSpace = len(labelCourse) - len(course[1])
                Course = (" " * int(courseSpace/2))+course[1]+(" " * (courseSpace - int(courseSpace/2)))
        print(f"|{id}|{name}|{Course}|")
        print("-" * len(title)) 
#Exibe todas as disciplinas com uma tabulação mais simples
def selectAllDisciplinesSimple(disciplines):
    labelId = f"{' '*3}ID{' '*3}" 
    labelNome = f"{' '*20}Nome da disciplina{' '*20}" 
    title = f"|{labelId}|{labelNome}|"
    print("-" * len(title)) 
    print(title)
    print("-" * len(title)) 
    for discipline in disciplines:
        idSpace = len(labelId) - len(str(discipline[0]))
        nameSpace = len(labelNome) - len(discipline[1])
        id = (" " * int(idSpace/2))+str(discipline[0])+(" " * (idSpace - int(idSpace/2)))
        name = (" " * int(nameSpace/2))+discipline[1]+(" " * (nameSpace - int(nameSpace/2)))
        print(f"|{id}|{name}|")
        print("-" * len(title)) 

#Exibe todos os cursos com uma tabulação mais simples
def selectAllCoursesSimple(courses):
    labelId = f"{' '*3}ID{' '*3}" 
    labelNome = f"{' '*20}Nome da curso{' '*20}" 
    title = f"|{labelId}|{labelNome}|"
    print("-" * len(title)) 
    print(title)
    print("-" * len(title)) 
    for course in courses:
        idSpace = len(labelId) - len(str(course[0]))
        nameSpace = len(labelNome) - len(course[1])
        id = (" " * int(idSpace/2))+str(course[0])+(" " * (idSpace - int(idSpace/2)))
        name = (" " * int(nameSpace/2))+course[1]+(" " * (nameSpace - int(nameSpace/2)))
        print(f"|{id}|{name}|")
        print("-" * len(title)) 
#Exibe todos os cursos e suas disciplinas
def selectAllCourses(courses, disciplines ):
    labelId = f"{' '*3}ID{' '*3}" 
    labelName = f"{' '*20}Nome do curso{' '*20}" 
    labelDuration = f"{' '*3}Duração do curso{' '*3}" 
    title = f"|{labelId}|{labelName}|{labelDuration}|"
    for course in courses: 
        print("-" * len(title)) 
        print(title)
        print("-" * len(title))
        idSpace = len(labelId) - len(str(course[0]))
        nameSpace = len(labelName) - len(course[1])
        durationSpace = len(labelDuration) - len(str(course[2]))
        id = (" " * int(idSpace/2))+str(course[0])+(" " * (idSpace - int(idSpace/2)))
        name = (" " * int(nameSpace/2))+course[1]+(" " * (nameSpace - int(nameSpace/2)))
        duration = (" " * int(durationSpace/2))+str(course[2])+(" " * (durationSpace - int(durationSpace/2)))
        print(f"|{id}|{name}|{duration}|")
        print("-" * len(title)) 
        courseDisciplines = []
        for discipline in disciplines:
            if discipline[2] == course[0]:
                courseDisciplines.append(discipline)
        selectAllDisciplinesSimple(courseDisciplines)
#Exibe todos os alunos e seus cursos e disciplinas
def selectAllStudents(students, courses, disciplines):
    labelRA = f"{' '*9}RA{' '*9}" 
    labelName = f"{' '*20}Nome do aluno{' '*20}" 
    labelCPF = f"{' '*13}CPF{' '*13}" 
    labelCourse = f"{' '*20}Curso{' '*20}" 
    title = f"|{labelRA}|{labelName}|{labelCPF}|{labelCourse}|"
    for student in students:
        print("-" * len(title)) 
        print(title)
        print("-" * len(title))
        raSpace = len(labelRA) - len(str(student[0]))
        nameSpace = len(labelName) - len(student[1])
        cpfSpace = len(labelCPF) - len(student[2])
        id = (" " * int(raSpace/2))+str(student[0])+(" " * (raSpace - int(raSpace/2)))
        name = (" " * int(nameSpace/2))+student[1]+(" " * (nameSpace - int(nameSpace/2)))
        cpf = (" " * int(cpfSpace/2))+student[2]+(" " * (cpfSpace - int(cpfSpace/2)))
        for course in courses:
            if student[3] == course[0]:
                courseSpace = len(labelCourse) - len(course[1])
                Course = (" " * int(courseSpace/2))+course[1]+(" " * (courseSpace - int(courseSpace/2)))

        print(f"|{id}|{name}|{cpf}|{Course}|")
        print("-" * len(title)) 
        courseDisciplines = []
        for discipline in disciplines:
            if discipline[2] == student[3]:
                courseDisciplines.append(discipline)
        selectAllDisciplinesSimple(courseDisciplines)

#Exibe todas as disciplinas com uma tabulação mais simples
def selectAllStudentSimple(students):
    labelId = f"{' '*3}ID{' '*3}" 
    labelNome = f"{' '*20}Nome do aluno{' '*20}" 
    title = f"|{labelId}|{labelNome}|"
    print("-" * len(title)) 
    print(title)
    print("-" * len(title)) 
    for student in students:
        idSpace = len(labelId) - len(str(student[0]))
        nameSpace = len(labelNome) - len(student[1])
        id = (" " * int(idSpace/2))+str(student[0])+(" " * (idSpace - int(idSpace/2)))
        name = (" " * int(nameSpace/2))+student[1]+(" " * (nameSpace - int(nameSpace/2)))
        print(f"|{id}|{name}|")
        print("-" * len(title)) 
