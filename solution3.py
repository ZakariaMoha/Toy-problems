def solve(word):
    vowels = 'aeiou'
    max_value = 0
    consonants = [ord(letter) - ord('a') + 1 for letter in word if letter not in vowels]
    i = 0
    while i < len(consonants):
        j = i
        current_value = 0
        while j < len(consonants) and consonants[j] > 0:
            current_value += consonants[j]
            j += 1
        max_value = max(max_value, current_value)
        i = j + 1
    print(max_value)
solve(' qwerty')
