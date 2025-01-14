import os

# Caminho completo do arquivo Python em execução
file_path = os.path.abspath(__file__)

# Diretório onde o arquivo está localizado
directory = os.path.dirname(file_path)

print("Caminho completo do ficheiro:", file_path)
print("Diretório do ficheiro:", directory)
