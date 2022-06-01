from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest_self(root: TreeNode, k: int) -> int:
    val = []

    def traverse_tree(node: TreeNode):
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            val.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    traverse_tree(root)
    val = quick_sort(val)
    return val[-k]


def kthSmallest_recursive(root: TreeNode, k: int) -> int:
    def inorder_traverse(node: TreeNode, val=[]):
        if not node:
            return val

        inorder_traverse(node.left)
        val.append(node.val)
        inorder_traverse(node.right)

        return val

    val = inorder_traverse(root)
    return val[k - 1]


def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    visit_counter = 0
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        visit_counter += 1
        if visit_counter == k:
            return curr.val
        curr = curr.right


def test1():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    res = kthSmallest(root, 1)
    print(res)


def test2():
    root = TreeNode(5)
    root.right = TreeNode(6)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)

    res = kthSmallest(root, 3)
    print(res)


def print_bfs(root: TreeNode):
    res = []
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if node and node.left:
            queue.append(node.left)
        if node and node.right:
            queue.append(node.right)
        res.append(node.val if node else node)

    print(res)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
