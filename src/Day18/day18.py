import re


class Node:
    def __init__(self, left=None, right=None):
        self.parent = None
        self.left = left
        if isnode(left):
            left.parent = self
        self.right = right
        if isnode(right):
            right.parent = self

    def __str__(self):
        if isinstance(self, int):
            return self
        else:
            return "({},{})".format(str(self.left), str(self.right))


    def find_explode(self, depth=0):
        # it is assumed that 4 is the max depth, otherwise it returns a node of nodes
        if depth == 4:
            return self
        if isnode(self.left):
            return self.left.find_explode(depth + 1)
        elif isnode(self.right):
            return self.right.find_explode(depth + 1)
        return None


    def explode(self):
        explode_node = self.find_explode()
        print("Explode", explode_node)


    def flatten(self):
        left = self.left
        right = self.right
        left_series = left.flatten() if isnode(left) else [left]
        right_series = right.flatten() if isnode(right) else [right]
        return left_series + right_series


    def flatten2(self):
        left = self.left
        right = self.right
        left_series = left.flatten2() if isnode(left) else [NodeValue(self, True)]
        right_series = right.flatten2() if isnode(right) else [NodeValue(self, False)]
        return left_series + right_series


class NodeValue:
    def __init__(self, node: Node, value: bool):
        self.node = node
        self.value = value  # True means left and false means right


    def __str__(self):
        return str(self.node.left if self.value else self.node.right)


def isnode(n):
    return isinstance(n, Node)


def parse(node_str):
    # This is cheating :-)
    return eval(node_str.replace("[","Node(").replace("]",")"))


def parse2(node_str):
    if re.match("\d", node_str):
        return int(node_str)
    left_br = 0  # count number of left brackets
    right_br = 0  # count number of right brackets
    i = 0
    for i in range(len(node_str)):
        s = node_str[i]
        match s:
            case '[':
                left_br += 1
            case ']':
                right_br += 1
            case ",":
                if left_br - right_br == 1:
                    break
    left = node_str[1:i]
    right = node_str[i+1:len(node_str)-1]
    return Node(parse2(left), parse2(right))


nodes = []
with open('day18.txt', 'r') as f:
    for line in f:
        nodes.append(parse2(line.rstrip()))

for node in nodes:
    print(node)
    print("E", node.find_explode())
    print("F",node.flatten())
    print("F2",[int(str(nv)) for nv in node.flatten2()])
    # node.explode()

