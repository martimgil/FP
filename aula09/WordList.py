import bisect

with open("wordlist.txt") as f:
    words = f.read().splitlines()

def count_words(prefix, words):
    start = bisect.bisect_left(words, prefix)
    end = bisect.bisect_right(words, prefix + 'z')
    return end - start, start, end

# Contar palavras que começam com "ea"
ea_count, ea_start, ea_end = count_words("ea", words)
print(f"Palavras que começam com 'ea': {ea_count}")

# Contar palavras que começam com "truo"
truo_count, truo_start, truo_end = count_words("truo", words)
print(f"Palavras que começam com 'truo': {truo_count}")

# Encontrar a primeira letra maior do que 'o' após "tru"
tru_start = bisect.bisect_right(words, "tru")
if tru_start < len(words):
    next_word = words[tru_start]
    for char in next_word:
        if char > 'o':
            print(f"A primeira letra maior do que 'o' após 'tru' é: {char}")
            break
else:
    print("Não há palavras após 'tru'")