def adionarAluno(rm, nome, data_nascimento, email):
    if (rm, nome) in dic_alunos:
        return('Aluno ja cadastrado')
    else:
        dic_alunos.update({(rm, nome) : (data_nascimento, email, []) })
        return('aluno cadastrado com sucesso')

def alterarAluno (rm, nome,novo_rm, novo_nome, data_nascimento, email):   
    if (rm, nome) in dic_alunos:
        dic_alunos.update({(novo_rm, novo_nome) : (data_nascimento, email, [])})
        del dic_alunos[(rm, nome)]
        return('Aluno alterado!!!')  
    else:
        return('Aluno não encontrado')
def deletarAluno(rm, nome):
    if (rm, nome) in dic_alunos:
        del dic_alunos[(rm, nome)]
        return("Aluno Deletado")
    else:
        return("Aluno não encontrado, digite o rm ou nome válido.")

def consultarAluno(rm, nome):
    if(rm, nome) in dic_alunos:
        return(dic_alunos[rm, nome])
    else:
        return("Aluno não encontrado, digite o rm ou nome válido.")   

def ConsultarAlunos():
    alunos = []        
    for aluno in dic_alunos:
        alunos.append(aluno[1])
    return(alunos)    

def adicionarNota(rm, nome, materia, nota):
    materia_nota = [materia, nota]
    if (rm, nome) in dic_alunos and materia in disciplina:
        dic_alunos[(rm, nome)][2].append(materia_nota)
        return(f'A Disiplina e nota foi adicionada')
    else:
        return("Aluno não encontrado, digite o rm ou nome válido.")
        
disciplina = {
    'APR1': ["ALGORITMOS E PROGRAMAÇÃO 1", 140],
    'CAL1': ["CÁLCULO 1", 90],
    'ALGA': ["ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA", 60],
    'FYS1': ["FÍSICA 1", 90],
    'EST1': ["ESTRUTURAS DE DADOS", 120],
    'BDADOS': ["BANCO DE DADOS", 80],
    'SOPE': ["SISTEMAS OPERACIONAIS", 80],
    'REDES': ["REDES DE COMPUTADORES", 80],
    'ENGSO': ["ENGENHARIA DE SOFTWARE", 90],
    'IAVANC': ["INTELIGÊNCIA ARTIFICIAL", 60]
}

dic_alunos = {
    ("2026001", "Ana Silva"): (
        "15/05/2004",
        ["ana.silva@email.com", "ana.academico@email.com"],
        [["APR1", 8.5], ["CAL1", 7.0], ["EST1", 9.2]]
    ),
    ("2026002", "Bruno Souza"): (
        "22/10/2003",
        ["bruno.souza@email.com"],
        [["APR1", 6.0], ["ALGA", 5.5], ["FYS1", 7.8]]
    ),
    ("2026003", "Carla Dias"): (
        "03/12/2005",
        ["carla.dias@email.com", "carla.uni@email.com"],
        [["EST1", 9.5], ["BDADOS", 8.5], ["SOPE", 9.0]]
    ),
    ("2026004", "Daniel Lima"): (
        "11/01/2004",
        ["daniel.lima@email.com"],
        [["REDES", 6.5], ["ENGSO", 7.0], ["IAVANC", 8.0]]
    ),
    ("2026005", "Elena Rocha"): (
        "29/07/2004",
        ["elena.rocha@email.com", "elena.pessoal@email.com"],
        [["CAL1", 9.0], ["ALGA", 8.5], ["ENGSO", 9.5]]
    )
}

print('MENU:')
print('1-Adicionar Aluno')
print('2-Alterar Aluno')
print('3-Remover Aluno')
print('4-Consultar um Aluno pela chave completa')
print('5-Mostrar todos os alunos')
print('6-Adicionar disciplinas e notas ao Aluno')
print('7-Fim')


op = int(input('qual o número da sua opção:'))

while op != 7:
    
    if op == 1:
        rm = input('RM do aluno:')
        nome = input('aluno:')
        data_nascimento = input('Data de nascimento(xx/xx/xxxx):')
        email = input('emial:')
        mensagem = adionarAluno(rm, nome, data_nascimento, email)
        print(mensagem)
        
    if op == 2:
        rm = input('RM do aluno:')
        nome = input('aluno:')
        novo_rm = input('Novo RM:')
        novo_nome = input('Novo Nome:')
        data_nascimento = input('Nova data de nascimento(xx/xx/xxxx):')
        email = input('Novo emial:')
        mensagem = alterarAluno (rm, nome,novo_rm, novo_nome, data_nascimento, email)
        print(mensagem) 

    if op == 3:
        rm = input('RM do aluno:')
        nome = input('aluno:')
        mensagem = deletarAluno(rm, nome)
        print(mensagem)
        
    if op == 4:
        rm = input('RM do aluno:')
        nome = input('aluno:')
        mensagem = consultarAluno(rm, nome)
        print(mensagem)
        
    if op == 5:
        mensagem = ConsultarAlunos()
        print(mensagem)
        
    if op == 6:
        rm = input('RM do aluno:')
        nome = input('aluno:')
        materia = input('Qual disiplina deseja adicionar(sigla):')
        nota = float(input('Nota do aluno:'))
        mensagem = adicionarNota(rm, nome, materia, nota)
        print(mensagem)
        print(dic_alunos)
        
    op = int(input('qual o número da sua opção:'))
    

if op == 7:
    print('Secção Finalizada')