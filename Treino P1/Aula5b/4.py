#O Método de Hondt permite fazer a distribuição de deputados eleitos para uma assembleia de
# forma proporcional aos votos de cada partido. Considerando que V_i é o número de votos obtidos pelo partido i, o método
#  determina o número N_i de lugares a atribuir a esse partido.

#O método começa com N_i = 0 para todos os partidos e depois:

#Calcula os quocientes Q_i = \frac{V_i}{N_i+1}.
#Encontra o partido com o maior quociente e atribui-lhe um deputado (aumenta o N_i correspondente).
#Se vários partidos tiverem quocientes iguais, atribui o deputado ao partido com menos votos.
#Repete estes passos até todos os lugares estarem atribuídos.
#Por exemplo, para distribuir 6 lugares por quatro partidos que tiveram as votações V = [15300, 12000, 6600, 5100] o
# processo deve seguir os passos abaixo.

#Q: [15300, 12000, 6600, 5100] => +1 for party 0 => N: [1, 0, 0, 0]
#Q: [ 7650, 12000, 6600, 5100] => +1 for party 1 => N: [1, 1, 0, 0]
#Q: [ 7650,  6000, 6600, 5100] => +1 for party 0 => N: [2, 1, 0, 0]
#Q: [ 5100,  6000, 6600, 5100] => +1 for party 2 => N: [2, 1, 1, 0]
#Q: [ 5100,  6000, 3300, 5100] => +1 for party 1 => N: [2, 2, 1, 0]
#Q: [ 5100,  4000, 3300, 5100] => +1 for party 3 => N: [2, 2, 1, 1]
#Note que o 1º deputado vai para o partido 0, porque tem o quociente mais alto. Depois atualiza-se Q e r
# epete-se. No último passo há dois partidos com Q máximo, por isso atribui-se o lugar ao partido menos votado.

#Implemente uma função hondt(votes, numseats) que, dada uma lista com os números de votos em cada um
# partidos e dado o número de lugares disponíveis, calcule e devolva uma lista com a distribuição de deputados para
# cada partido. Por exemplo, hondt([15300, 12000, 6600, 5100], 6) deve devolver [2, 2, 1, 1].

def hondt(votes, numseats):
    Ni = [0]*len(votes)
    Qi = []
    for a in range(numseats):
        for i in range(len(votes)):
            q = votes[i]/(Ni[i]+1)
            Qi.append(q)


        V = max(Qi)
        Vp = Qi.index(V)

        Ni[Vp] +=1
        Qi=[]

    return Ni