#Anagrams are a words or phrases made by transposing the letters of another word or phrase

def is_anagram(word1, word2):
    """
    function to check if two words are anagram or not.
    """
    if sorted(word1) == sorted(word2): #Checking if the words are anagram
        print('The given two words are Anagram') #printing if its anagram
        
    else:
        print('The given two words are not Anagram') #printing if its not anagram


if __name__ == "__main__":
    word1 = input("Please enter the first word: ")
    word2 = input("Please enter the second word: ")
    is_anagram(word1,word2)