from collections import Counter

word1 = "silent"
word2 = "listen"

word1 = sorted(word1)
print(word1)                          

word2 = sorted(word2)
print(word2)                            

word1_counter = Counter(word1)        
print(word1_counter)                    
word2_counter = Counter(word2) 
print(word2_counter)
