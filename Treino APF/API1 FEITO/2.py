#Implemente uma função que verifica a validade de um endereço de e-mail com base nas seguintes regras:

#Um endereço de e-mail deve conter exatamente um símbolo @.

#A parte anterior ao @ (nome do utilizador):
#Deve ter pelo menos 3 caracteres.
#Não pode conter a sequência ...
#Só pode conter letras, números e pontos (.).

#A parte após o @ (domínio):
#Deve ter pelo menos 3 caracteres.
#Não pode conter a sequência ...
#Só pode conter letras, números e pontos (.).

#A função deve retornar:
#"ErrorF" se o formato geral (número de @) estiver incorreto.
#"ErrorU" se houver um problema no nome do utilizador.
#"ErrorD" se houver um problema no domínio.
#"Valid" se o e-mail for válido.
 #   Escreva a função e teste-a com diferentes exemplos de e-mails para garantir que ela funciona corretamente em todos os casos possíveis.



def validate(s):
    s.split("@")
    if s.count("@")!=1:
        return "ErroF"
    if s[0]<3 or ".." in s[0]:
        return "ErroU"

    for letter in s[0]:
        if (letter.isalnum() == False) and letter != ".":
             return "ErrorU"

    if s[1]<3 or "" in s[1]:
        return "ErrorD"

    for letter in s[1]:
        if (letter.isalnum() == False) and letter != ".":
            return "ErrorD"

    return "Valid"