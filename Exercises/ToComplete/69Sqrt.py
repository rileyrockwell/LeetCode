# Collaborators: Peter

class Solution:
    def mySqrt(self, x: int) -> int:
        guess = 1
        while True:
            y = (guess + x / guess) / 2.0
            if y == guess:
                break
            guess = y

        return y

if __name__ == "__main__":
    print(Solution().mySqrt(16))