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
            n = self.left.find_explode(depth + 1)
            if n:
                return n
        if isnode(self.right):
            n = self.right.find_explode(depth + 1)
            if n:
                return n
        return None

    def explode(self):
        explode_node = self.find_explode()
        flat = self.flatten2()
        for exp_index in range(len(flat)):
            if flat[exp_index].node == explode_node:
                break
        if exp_index > 0:  # set value to the left
            flat[exp_index - 1].set(flat[exp_index - 1].get() + flat[exp_index].get())
        if exp_index < len(flat) - 2:  # set value to the right
            flat[exp_index + 2].set(flat[exp_index + 2].get() + flat[exp_index + 1].get())
        parent = flat[exp_index].node.parent
        if parent.left == explode_node:
            parent.left = 0
        else:
            parent.right = 0

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
        return str(self.get())

    def get(self):
        return self.node.left if self.value else self.node.right

    def set(self, set_value):
        if self.value:
            self.node.left = set_value
        else:
            self.node.right = set_value


def isnode(n):
    return isinstance(n, Node)


def parse_str(node_str):
    # This is cheating :-)

    return eval(node_str.replace("[", "Node(").replace("]", ")"))


def parse(node_str):
    if re.match("[0-9]", node_str):
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
    right = node_str[i + 1:len(node_str) - 1]
    return Node(parse(left), parse(right))


nodes = []
with open('day18.txt', 'r') as f:
    for line in f:
        nodes.append(parse(line.rstrip()))

for node in nodes:
    print(node)
    node.explode()
    print("Exploded:", node)
