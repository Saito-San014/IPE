import registrations
exit = True
students = []
disciplines = []
courses = []
discipline = [1, "Introdução a logica Estruturada", 1]
registrations.include(discipline, disciplines)
discipline = [213, "Logica de Programação  e Algoritomo", 1]
registrations.include(discipline, disciplines)
discipline = [3355, "Noções de Direiro", 2]
registrations.include(discipline, disciplines)
student = ["123", "Gabriel", "12345", 1]
registrations.include(student, students)
student = ["1234", "Deborah", "123456", 2]
registrations.include(student, students)
course = [1, "Ciencia da Computação", 4]
registrations.include(course, courses)
course = [2, "Psicologia", 5]
registrations.include(course, courses)
subTextStudentRegistration = """1. Cadastro de Alunos    
    a. Incluir
    b. Alterar (buscar pelo RA que deve ser alterado)
    c. Consultar pelo RA (exibir dados do aluno, curso e disciplinas)
    d. Relatório completo (exibir dados de todos os alunos, seu curso e suas disciplinas)
    e. Excluir (buscar pelo RA que deve ser excluído)"""
subTextCourseRegistration = """2. Cadastro de Cursos
    a. Incluir
    b. Alterar (buscar pelo ID que deve ser alterado)
    c. Consultar pelo ID (exibir dados do curso e suas disciplinas)
    d. Relatório completo (exibir dados de todos os cursos e suas respectivas disciplinas)
    e. Excluir (buscar pelo ID que deve ser excluído)"""    
subTextDisciplineRegistration = """3. Cadastro de Disciplinas
    a. Incluir
    b. Alterar (buscar pelo ID que deve ser alterado)
    c. Consultar pelo ID
    d. Relatório completo, com todas as disciplinas
    e. Excluir (buscar pelo ID que deve ser excluído)"""
subTextBack = """
    f. Voltar"""
text = f"""
{subTextStudentRegistration}
{subTextCourseRegistration}
{subTextDisciplineRegistration}
4. Sair
Escolha uma opção: """
entry = ""
def endAction(preText):
    if preText == "":
        input("Continuar.")
        pass
    else:
        input(f"{preText} \n Continuar.")
    global entry 
    entry = ""
while(exit): 
    if entry == "":
        entry = input(text)
    match(entry):
        case "1":  #Sub-menu aluno
            entry = input(subTextStudentRegistration + subTextBack + "\n Escolha uma opção: ")
            match entry:
                case "a":
                    entry = "1a"
                case "b":
                    entry = "1b"
                case "c":
                    entry = "1c"
                case "d":
                    entry = "1d"
                case "e":
                    entry = "1e"
                case "f":
                    entry = ""
                case _:
                    entry = "1"
                    print("Opção invalida")
        case "1a": #Cadastra aluno
            ra = input("RA do aluno: ")
            name = input("Nome do aluno: ")
            cpf = input("CPF: ")
            validCourse = None
            while(validCourse == None):
                print("Cursos")
                registrations.selectAllCoursesSimple(courses)
                idCurso = int(input("Digite o id do curso: "))
                validCourse = registrations.select(idCurso, courses)
                if validCourse == None:
                    print("Curso invalido")
            result = registrations.include([ra, name, cpf, idCurso], students)
            if (result == None):
                endAction("Aluno incluido.")
            else:
                endAction("Este Aluno já foi cadastrado.")
        case "1b": #Altera aluno
            student = None
            update = "s"
            while(student == None and update == "s"):
                registrations.selectAllStudentSimple(students)
                idCurso = input("RA do aluno: ")
                student = registrations.select(idCurso, students)
                if(student == None):
                    print("Aluno não encontrado")
                else:
                    name = input(f"Nome do aluno<{student[1]}>: ")
                    if name == "":
                        name = student[1]
                    cpf = input(f"CPF<{student[2]}>: ")
                    if cpf == "":
                        cpf = student[2]
                    studentCourse = registrations.select(student[3], courses)
                    print(f"Curso do aluno: {studentCourse[1]}")
                    updateCourse = input("Alterar curso <s/n>: ")
                    if updateCourse == "s":
                        validCourse = None
                        while(validCourse == None):
                            registrations.selectAllCoursesSimple(courses)
                            idCurso = int(input("Digite o id do curso: "))
                            validCourse = registrations.select(idCurso, courses)
                            if validCourse == None:
                                    print("Curso invalido")
                            else:
                                student[3] = idCurso
                    update = input("Salvar alterações <s/n>: ")
                    if update == "s":
                        students[students.index(student)] = [student[0], name, cpf, student[3]] 
                        endAction("Alteração feita com sucesso.")
                    else:
                        update = "s"
                        endAction("Alteração cancelada.")
        case "1c": #Busca aluno
            registrations.selectAllStudentSimple(students)
            ra = input("RA do aluno: ")
            student = registrations.select(ra, students)
            if(student == None):
                print("Aluno não encontrado")
            else:
                registrations.selectAllStudents([student], courses, disciplines)
                endAction("")  
        case "1d": #Relatorio de alunos
            registrations.selectAllStudents(students, courses, disciplines)    
            endAction("")
        case "1e": #Exclui aluno
            registrations.selectAllStudentSimple(students)
            ra = input("RA do aluno: ")
            student = registrations.select(ra, students)
            if(student == None):
                print("Aluno não encontrado")
            else:
                deletar = input(f"Deletar aluno {student[1]} <s/n>: ")
                if deletar == "s":
                    students.remove(student)
                    endAction("Apagado com sucesso.")
        case "2":  #Sub-menu curso
            entry = input(subTextCourseRegistration + subTextBack + "\n Escolha uma opção: ")
            match entry:
                case "a":
                    entry = "2a"
                case "b":
                    entry = "2b"
                case "c":
                    entry = "2c"
                case "d":
                    entry = "2d"
                case "e":
                    entry = "2e"
                case "f":
                    entry = ""
                case _:
                    entry = "2"
                    print("Opção invalida")
        case "2a": #Cadastra curso
            idCurso = int(input("Digite o id do curso: "))
            name = input("Nome do curso: ")
            duration = int(input("Duração do curso: "))
            result = registrations.include([idCurso, name, duration], courses)
            if(result == None):
                endAction("Curso cadastrado com sucesso")
            else:
                endAction("Curso já existente")
        case "2b": #Altera curso
            course = None
            update = "s"
            while(course == None and update == "s"):
                registrations.selectAllCoursesSimple(courses)
                idCurso = int(input("ID do curso: "))
                course = registrations.select(idCurso, courses)
                if(course == None):
                    print("Curso não encontrado")
                else:
                    name = input(f"Nome do curso<{course[1]}>: ")
                    duration = int(input(f"Duração<{course[2]}>: "))
                    update = input("Salvar alterção <s/n>: ")
                    if update == "s":
                        courses[courses.index(course)] = [course[0], name, duration] 
                        endAction("Alteração feita com sucesso.")
        case "2c": #Busca Curso
            Course = None
            while(Course == None):
                print("Cursos")
                registrations.selectAllCoursesSimple(courses)
                idCurso = int(input("Digite o id do curso: "))
                Course = registrations.select(idCurso, courses)
                if Course == None:
                    print("Curso invalido")
                else:
                    registrations.selectAllCourses([Course], disciplines)
            endAction("")
        case "2d": #Relatorio de cursos
            registrations.selectAllCourses(courses, disciplines)
            endAction("")
        case "2e": #Exclui curso
            registrations.selectAllCoursesSimple(courses)
            idCurso = int(input("Digite o id do curso: "))
            course = registrations.select(idCurso, courses)
            if(course == None):
                print("Curso invalido")
            else:
                deletar = input(f"Deletar curso {course[1]} <s/n>: ")
                if deletar == "s":
                    courses.remove(course)
                    endAction("Curso apagado com sucesso.")
        case "3":  #Sub-menu disciplinas
            entry = input(subTextCourseRegistration + subTextBack + "\n Escolha uma opção: ")
            match entry:
                case "a":
                    entry = "3a"
                case "b":
                    entry = "3b"
                case "c":
                    entry = "3c"
                case "d":
                    entry = "3d"
                case "e":
                    entry = "3e"
                case "f":
                    entry = ""
                case _:
                    entry = "3"
                    print("Opção invalida")
        case "3a": #Cadastra disciplinas
            idDiscipline = int(input("Digite o id da disciplina: "))
            name = input("Nome da disciplina: ")
            validCourse = None
            while(validCourse == None):
                print("Cursos")
                registrations.selectAllCoursesSimple(courses)
                idCurso = int(input("Digite o id do curso: "))
                validCourse = registrations.select(idCurso, courses)
                if validCourse == None:
                    print("Curso invalido")
            result = registrations.include([idDiscipline, name,idCurso], disciplines)
            if (result == None):
                endAction("Discipina cadastrada.")
            else:
                endAction("Disciplina já existente.")
            pass
        case "3b": #Altera disciplina
            discipline = None
            update = "s"
            while(discipline == None and update == "s"):
                registrations.selectAllDisciplinesSimple(disciplines)                
                idCurso = int(input("ID da disciplina: "))
                discipline = registrations.select(idCurso, disciplines)
                if(discipline == None):
                    print("Disciplina não encontrada")
                else:
                    name = input(f"Nome da disciplina<{discipline[1]}>: ")
                    if name == "":
                        name = discipline[1]
                    disciplineCourse = registrations.select(discipline[2], courses)
                    print(f"Disciplina do curso: {disciplineCourse[1]}")
                    updateCourse = input("Alterar curso <s/n>: ")
                    if updateCourse == "s":
                        validCourse = None
                        while(validCourse == None):
                            registrations.selectAllCoursesSimple(courses)                
                            idCurso = int(input("Digite o id do curso: "))
                            validCourse = registrations.select(idCurso, courses)
                            if validCourse == None:
                                    print("Curso invalido")
                            else:
                                discipline[2] = idCurso
                    update = input("Salvar alterção <s/n>: ")
                    if update == "s":
                        disciplines[disciplines.index(discipline)] = [discipline[0], name, discipline[2]] 
                        endAction("Alteração feita com sucesso.")
        case "3c": #Busca disciplina
            idDiscipline = int(input("Digite o id da disciplina: "))
            discipline = registrations.select(idDiscipline, disciplines)
            if(discipline == None):
                print("Disciplina invalida")
            else:
                registrations.selectAllDisciplines([discipline], courses)
            endAction("")
        case "3d": #Relatoiro de disciplinas
            registrations.selectAllDisciplines(disciplines, courses)
            endAction("")
        case "3e": #Exclui disciplina
            registrations.selectAllDisciplinesSimple(disciplines)
            idDiscipline = int(input("Digite o id da disciplina: "))
            discipline = registrations.select(idDiscipline, disciplines)
            if(discipline == None):
                print("Disciplina invalida")
            else:
                deletar = input(f"Deletar a disciplina {discipline[1]} <s/n>: ")
                if deletar == "s":
                    disciplines.remove(discipline)
                    endAction("Disciplina excluida com sucesso.")
                else:
                    endAction("Exclusão cancelada.")
        case "4":  #Sair do menu
            exit = False
        case _:    #Opção invalida
            endAction("Opção invalida")