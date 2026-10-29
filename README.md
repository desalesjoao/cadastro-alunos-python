Sistema de Cadastro de Alunos (CRUD) com Tuplas e Dicionarios em Python

Projeto desenvolvido como parte da disciplina de Algoritmos e Programacao I (APR1) do Instituto Federal de Sao Paulo (IFSP), Campus Sao Carlos.

O objetivo desta atividade e reescrever um sistema de gerenciamento de alunos utilizando estruturas de dados compostas e imutaveis/mutaveis do Python (dicionarios e tuplas) em substitucion ao uso exclusivo de listas.

Estrutura de Dados

O sistema utiliza dicionarios onde as chaves sao compostas por tuplas e os valores armazenam dados estruturados.

Dicionario de Disciplinas (disciplina)

Chave: Sigla da disciplina (string).
Valor: Lista com nome da disciplina (string) e carga horaria (int).

disciplina = {
    'APR1': ["ALGORITMOS E PROGRAMACAO 1", 140],
    'CAL1': ["CALCULO 1", 90]
}

Dicionario de Alunos (dic_alunos)

Chave: Tupla contendo (RA/RM, Nome).
Valor: Tupla contendo (Data de Nascimento, [Emails], [[Disciplina, Nota], ...]).

dic_alunos = {
    ("2026001", "Ana Silva"): (
        "15/05/2004",
        ["ana.silva@email.com"],
        [["APR1", 8.5], ["CAL1", 7.0]]
    )
}

Funcionalidades

O sistema oferece um menu interativo via terminal com as seguintes operacoes:

Adicionar Aluno: Cadastra um novo aluno no sistema utilizando uma chave tupla (RM, Nome).

Alterar Aluno: Atualiza os dados de identificacao e contato do aluno.

Remover Aluno: Exclui o registro de um aluno do dicionario.

Consultar Aluno pela Chave Completa: Busca os dados completos de um aluno informando RM e Nome.

Mostrar Todos os Alunos: Lista o nome de todos os alunos cadastrados.

Adicionar Disciplinas e Notas: Associa uma disciplina cadastrada e uma nota ao historico do aluno.

Fim: Encerra a execucao do programa.

Estruturas de Dados: Dicionarios (dict), Tuplas (tuple) e Listas (list)
