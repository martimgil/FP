def maior_capicua(s):
	n = len(s)
	max_len = 1

	for i in range(n):
		for j in range(i, n):
			substr = s[i:j+1]
			if substr == substr[::-1]:
				max_len = max(max_len, j-i+1)

	return max_len

# Exemplos de uso
print(maior_capicua("1"))      # 1
print(maior_capicua("12"))     # 1
print(maior_capicua("323"))    # 3
print(maior_capicua("74989"))  # 3
print(maior_capicua("11"))     # 2
		