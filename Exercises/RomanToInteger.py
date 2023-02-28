class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Note, there are 6 instances where the "subtraction principle" is applied:
        I can be placed before V and X (s.t. IV == 4; IX == 9)
        X can be placed before L and C (s.t. XL == 40; XC == 90)
        C can be placed before D and M (s.t. CD == 400; CM == 900)

        :param s: string of uppercase letters, corresponding to Roman Numeral input.
        recall I == 1; V == 5; X == 10; L == 50; C == 100; D == 500; M == 1000.
        :return: an integer, indicating the value of the Roman Numeral parameter.
        '''
        # Attempt 1: apply a number of conditionals
        counter = 0
        special_cases = ["IV", "IX", "XL", "XC", "CD", "CM"]
        for i in range(len(s) - 1):
            if str(s[i] + s[i + 1]) in special_cases:
                print("special case")

        for i in range(len(s) - 1):
            if str(s[i] + s[i + 1]) not in special_cases:
                if s[i] == "I":
                    counter += 1
                elif i == "V":
                    counter += 5
                elif i == "X":
                    counter += 10
                elif i == "L":
                    counter += 50
                elif i == "C":
                    counter += 100
                elif i == "D":
                    counter += 500
                elif i == "M":
                    counter += 1000

        return counter


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("XL"))