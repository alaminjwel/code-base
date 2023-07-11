# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
# Examples
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love

def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    nw=nw.split()
    curr=""
    for i in range(len(nw)):
      if len(nw[i])>len(curr):
        curr=nw[i]
    return curr

# keep this function call here 
print(LongestWord(input()))