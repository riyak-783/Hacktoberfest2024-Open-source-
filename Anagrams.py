from collections import defaultdict

def find_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        # Sort the characters of the word and use it as the key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())

# Example usage
words = ["listen", "silent", "enlist", "rat", "tar", "god", "dog"]
print(find_anagrams(words))  
