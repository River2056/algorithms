class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree_self(preorder: list[int], inorder: list[int]) -> TreeNode:
    if len(inorder) <= 0:
        return
    if len(preorder) > 0:
        node_elem = preorder.pop(0)

        idx = inorder.index(node_elem)
        root = TreeNode(node_elem)
        root.left = buildTree_self(preorder, inorder[0:idx])
        root.right = buildTree_self(preorder, inorder[idx + 1 :])

    return root


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1 : mid + 1], inorder[0:mid])
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

    return root


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


def test_case(preorder: list[int], inorder: list[int]):
    res = buildTree_self(preorder, inorder)
    print_bfs(res)


def main():
    test_case([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])  # [3, 9, 20, null, null, 15, 7]
    test_case([-1], [-1])  # [-1]
    test_case([1, 2], [1, 2])


if __name__ == "__main__":
    main()
