class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

def loop_size(node):
    arr = []
    while not node in arr:
        arr.append(node)
        node = node.next
    return len(arr) - arr.index(node)

def main():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    
    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = node11
    node11.next = node12
    node12.next = node1

    l_size = loop_size(nodeA)
    print('loop size: ', l_size)
    assert l_size == 12, f'should be 12, got {l_size} instead'

if __name__ == '__main__':
    main()
