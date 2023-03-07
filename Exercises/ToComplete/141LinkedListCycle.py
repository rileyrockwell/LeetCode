class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        return True

if __name__ == "__main__":
    print(Solution().hasCycle(ListNode(1)))