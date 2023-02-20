class Solution:
    def monkeyMove(self, n: int) -> int:
        '''
        param n: 3 <= n <= 10**9
        return: the number of ways the monkeys can move so that at least one collision happens. since the answer
        may be very large, return it modulo 10**9 + 7

        thought: is there not always a collision unless all monkeys move in either the clockwise or counterclockwise
        direction at the same time? i.e., if ALL monkeys move SIMULTANEOUSLY there is n - 2 ways that the monkeys
        CAN move in order to result in a collision?

        '''

        answer = int()





        return answer % 10**9 + 7

if __name__ == "__main__":
    print(Solution().monkeyMove())