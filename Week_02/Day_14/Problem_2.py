def palindrome(word):
    word = word.strip().lower()
    j = len(word) - 1
    for i in range(len(word)):
        if (i in range(len(word)//2))  and (word[i] == word[j]):
            return "The string is palindrome"
        else:
            return "The string is not palindrome"
    
word1 = "Kabir"
word2 = "ABCCBA"
print(palindrome(word1))
print(palindrome(word2))
