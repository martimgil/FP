h_sair = 6
m_sair = 52
m_saida = h_sair*60 + m_sair

v1 = 10
v2 = 6 

tempo_total = 1 * v1 + 3*v2 + 4 * v1
m_chegada = m_saida + tempo_total

h_casa = m_chegada//60
m_casa = m_chegada%60

print(h_casa, m_casa)
