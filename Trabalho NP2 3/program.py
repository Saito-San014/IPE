import studentRegistration
import courseRegistration
exit = True
students = []
disciplines = []
courses = []
discipline = [1, "Introdução a logica Estruturada", 1]
disciplines.append(discipline)
course = ["123", "Gabriel", "123", 1]
studentRegistration.include(course, students)
course = [1, "Ciencia da Computação", 4]
courseRegistration.include(course, courses)
course = [2, "Psicologia", 5]
courseRegistration.include(course, courses)
subTextStudentRegistration = """    
    a. Incluir
    b. Alterar (buscar pelo RA que deve ser alterado)
    c. Consultar pelo RA (exibir dados do aluno, curso e 
    disciplinas)
    d. Relatório completo (exibir dados de todos os alunos, 
    seu curso e suas disciplinas)
    e. Excluir (buscar pelo RA que deve ser excluído)"""
subTextCourseRegistration = """
    a. Incluir
    b. Alterar (buscar pelo ID que deve ser alterado)
    c. Consultar pelo ID (exibir dados do curso e suas 
    disciplinas)
    d. Relatório completo (exibir dados de todos os cursos 
    e suas respectivas disciplinas)
    e. Excluir (buscar pelo ID que deve ser excluído)"""    
text = f"""
1. Cadastro de Alunos{subTextStudentRegistration}
2. Cadastro de Cursos{subTextCourseRegistration}
    
3. Cadastro de Disciplinas
    a. Incluir
    b. Alterar (buscar pelo ID que deve ser alterado)
    c. Consultar pelo ID
    d. Relatório completo, com todas as disciplinas
    e. Excluir (buscar pelo ID que deve ser excluído)
4. Sair
Escolha uma opção: """
entry = ""
def endAction(preText):
    if preText == "":
        input("Continuar.")
    else:
        input(f"{preText} \n Continuar.")
    global entry 
    entry = ""
while(exit): 
    if entry == "":
        entry = input(text)
    match(entry):
        case "1":
            entry = input(subTextStudentRegistration)
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
                case _:
                    print("Opção invalida")
        case "1a":
            id = input("RA do aluno: ")
            name = input("Nome do aluno: ")
            duration = input("CPF: ")
            validCourse = None
            while(validCourse == None):
                print("Cursos")
                for course in courses:
                    print(f"{course[0]} - {course[1]}")
                idCurso = int(input("Digite o id do curso: "))
                validCourse = courseRegistration.select(idCurso, courses)
                if validCourse == None:
                    print("Curso invalido")
            result = studentRegistration.include([id, name, duration,idCurso], students)
            if (result == None):
                print("Aluno incluido.")
            else:
                print("Aluno já existe.")
            endAction("")
        case "1b":
            course = None
            update = "s"
            while(course == None and update == "s"):
                id = input("RA do aluno: ")
                course = studentRegistration.select(id, students)
                if(course == None):
                    print("Aluno não encontrado")
                else:
                    name = input(f"Nome do aluno<{course[1]}>: ")
                    duration = input(f"CPF<{course[2]}>: ")
                    updateCourse = input("Alterar curso <s/n>: ")
                    if updateCourse == "s":
                        course = courseRegistration.select(course[3], courses)
                        print(f"Curso do aluno: {course[1]}")
                        validCourse = None
                        while(validCourse == None):
                            print("Cursos")
                            for course in courses:
                                print(f"{course[0]} - {course[1]}")
                            idCurso = int(input("Digite o id do curso: "))
                            validCourse = courseRegistration.select(idCurso, courses)
                            if validCourse == None:
                                    print("Curso invalido")
                            else:
                                course[3] = idCurso
                    update = input("Alterar <s/n>: ")
                    if update == "s":
                        students[students.index(course)] = [course[0], name, duration, course[3]] 
                        endAction("Alteração feita com sucesso.")
        case "1c":
            id = input("RA do aluno: ")
            course = studentRegistration.select(id, students)
            if(course == None):
                print("Aluno não encontrado")
            else:
                print(f"RA do aluno: {course[0]}")
                print(f"Nome do aluno: {course[1]}")
                print(f"CPF do aluno: {course[2]}")
                course = courseRegistration.select(course[3], courses)
                print(f"Curso do aluno: {course[1]}")
                endAction("")  
        case "1d":
            for course in students:
                print(f"RA do aluno: {course[0]}")
                print(f"Nome do aluno: {course[1]}")
                print(f"CPF do aluno: {course[2]}")
                course = courseRegistration.select(course[3], courses)
                print(f"Curso do aluno: {course[1]}")
                
            endAction("")
        case "1e":
            id = input("RA do aluno: ")
            course = studentRegistration.select(id, students)
            if(course == None):
                print("Aluno não encontrado")
            else:
                deletar = input(f"Deletar aluno {course[1]} <s/n>: ")
                if deletar == "s":
                    students.remove(course)
                    endAction("Apagado com sucesso.")
        case "2":
            pass
        case "2a":
            id = int(input("Digite o id do curso: "))
            name = input("Nome do curso: ")
            duration = int(input("Duração do curso"))
            result = courseRegistration.include([id, name, duration])
            if result:
                print("Curso cadastrado com sucesso")
            else:
                print("Curso já existente")
            endAction("")
        case "2b":
            course = None
            update = "s"
            while(course == None and update == "s"):
                for course in courses:
                    print(f"{course[0]} - {course[1]}")
                id = int(input("ID do curso: "))
                course = courseRegistration.select(id, courses)
                if(course == None):
                    print("Curso não encontrado")
                else:
                    name = input(f"Nome do curso<{course[1]}>: ")
                    duration = int(input(f"Duração<{course[2]}>: "))
                    update = input("Salvar <s/n>: ")
                    if update == "s":
                        courses[courses.index(course)] = [course[0], name, duration] 
                        endAction("Alteração feita com sucesso.")
        case "2c":
            endAction("")
            pass
        case "2d":
            courseRegistration.selectAll(courses, disciplines)
            endAction("")
        case "2e":
            endAction("")
            pass
        case "3":
            endAction("")
            pass
        case "3a":
            endAction("")
            pass
        case "3b":
            endAction("")
            pass
        case "3c":
            endAction("")
            pass
        case "3d":
            endAction("")
            pass
        case "3e":
            endAction("")
            pass
        case "4":
            exit = False
        case _: 
            endAction("Opção invalida")