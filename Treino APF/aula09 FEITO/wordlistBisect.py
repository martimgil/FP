import bisect

with open ("wordlist.txt","r", encoding = "utf-8") as f:
    words = [line.strip() for line in f]

def count_words_with_prefic(prefix):
    start_index = bisect.bisect_left(words,prefix)
    end_index = bisect.bisect_right(words, prefix[:-1])
    return end_index - start_index

count_ea = count_words_with_prefic("ea")
print(f"Número de palavras que começam com 'ea': {count_ea}")

count_truo = count_words_with_prefic("truo")
print(f"Número de palavras que começam com 'truo: {count_truo}'")

index_tru = bisect.bisect_left(words, "tru")
for word in words[index_tru]:
    if len(word)>3 and word[3] > 'o':
        print(f"A primeira letra maior do que 'o' após 'tru' é: {word[3]}")
        break

def possible_next_letters(prefix):
    start_index = bisect.bisect_left(words, prefix)
    end_index = bisect.bisect_left(words, prefix[:-1] + chr(ord(prefix[-1]) + 1))
    next_letters = set()

    for word in words[start_index:end_index]:
        if len(word) > len(prefix):
            next_letters.add(word[len(prefix)])

    return sorted(next_letters)