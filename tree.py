from collections import deque

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order(self):
        ans: list[list[int]] = []
        q: deque[Tree] = deque()
        q.append(self)
        q.append(None)
        cur: list[int] = []
        while q:
            node = q.popleft()
            if node == None:
                ans.append(cur)
                cur = []
                if q:
                    q.append(None)
                continue
            else:
                cur.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return ans


t = Tree(0)
t.left = Tree(5)
t.right = Tree(9)
t.right.left = Tree(1)
t.right.right = Tree(3)
t.right.left.left = Tree(4)
t.right.left.right = Tree(2)
print(t.level_order())
