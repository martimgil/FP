import bisect

with open("wordlist.txt") as f:
    words = f.read().splitlines()

def count_words_with_prefix(prefix, words):
    start = bisect.bisect_left(words, prefix)
    end = bisect.bisect_left(words, prefix[:-1] + chr(ord(prefix[-1]) + 1))
    return end - start

def first_letter_after(prefix, char, words):
    start = bisect.bisect_left(words, prefix)
    for word in words[start:]:
        if len(word) > len(prefix) and word[len(prefix)] > char:
            return word[len(prefix)]
    return None

def possible_next_letters(prefix, words):
    start = bisect.bisect_left(words, prefix)
    end = bisect.bisect_right(words, prefix + chr(255))
    next_letters = set()
    for word in words[start:end]:
        if len(word) > len(prefix):
            next_letters.add(word[len(prefix)])
    return sorted(next_letters)

# Example usage
prefix_ea = "ea"
prefix_truo = "truo"
prefix_tru = "tru"

print(f"Number of words starting with '{prefix_ea}': {count_words_with_prefix(prefix_ea, words)}")
print(f"Number of words starting with '{prefix_truo}': {count_words_with_prefix(prefix_truo, words)}")
print(f"First letter after '{prefix_tru}' greater than 'o': {first_letter_after(prefix_tru, 'o', words)}")

prefix = "pre"
print(f"Possible next letters after '{prefix}': {possible_next_letters(prefix, words)}")