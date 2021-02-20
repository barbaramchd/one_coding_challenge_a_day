"""
819. Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph_new = paragraph.replace(",", "")
        print(paragraph_new)
        list_words = paragraph_new.split(" ")
        repeated_words = 0
        current_max_repeated_word = []
        for element in range(len(list_words)):
            for element2 in range(len(list_words)):
                if element != element2:
                    if list_words[element] not in banned:
                        repeated_words += 1
                        current_max_repeated_word.append(list_words[element])
                        if list_words[element] == list_words[element2]:
                            repeated_words = 0
                            current_max_repeated_word = []
                            repeated_words += 1
                            current_max_repeated_word.append(list_words[element])

        return current_max_repeated_word[0]