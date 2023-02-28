class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        Use a hashmap to determine if the given sentence is a pangram or not. Return True
        if it is a pangram, False otherwise.
        :param sentence: string (all lowercase letters, including spaces)
        :return: boolean
        '''
        return "tesitng"


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().checkIfPangram(sentence))

sentence = "leetcode"
print(Solution().checkIfPangram(sentence))