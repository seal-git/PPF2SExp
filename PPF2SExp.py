
class Node:
    def __init__(self):
        self.parent = -1
        self.value = ""
        self.children = []

def join_node(text):
    pass

def convert(text, tree):
    word_list = text.split()
    tree = tree.split("|")
    # print(text, tree)
    node_list = []
    node_list.append(Node())
    for i, word in enumerate(word_list):
        node = Node()
        node.value = word
        node_list.append(node)
    for node in node_list:
        print(node.value)

    return text