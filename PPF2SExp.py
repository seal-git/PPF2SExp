
class Node:
    def __init__(self):
        self.parent = -1
        self.value = ""
        self.children = [] # 子要素のインデックス
        self.min_child = 100000 # 子孫の中で一番小さいインデックス

def convert(text, tree):
    """
    各単語(leaf)とそれをつなげたフレーズ(node)を木構造で表す。
    それぞれのnodeがS式のフレーズ情報を持つ。rootが求めたいS式になる。
    :param text: スペース区切りのテキスト
    :param tree: parent pointer formatの数字列(|区切り)
    :return: nltk.Treeで読める形のS式
    """
    word_list = text.split("|")
    tree = tree.split("|")
    # print(text, tree)
    node_list = []
    node_list.append(Node())
    for i, parent in enumerate(tree):
        node = Node()
        node.parent = int(parent)
        node_list.append(node)

    for i, word in enumerate(word_list):
        # leafを入れていく
        node_list[i+1].value = f"({word})"
        node_list[i+1].min_child = i
        parent = node_list[i+1].parent
        node_list[parent].children.append(i+1)

    for i in range(len(word_list)+1, len(node_list)):
        # nodeを入れていく
        # min_childでchildren_nodeをソートして、語順が正しくなるようにする
        children = [node_list[idx] for idx in node_list[i].children]
        children.sort(key=lambda x: x.min_child)
        min_child = children[0].min_child
        children = [c.value for c in children]
        value = f"({''.join(children)})"
        node_list[i].value = value
        node_list[i].min_child = min_child
        # parentに自身を登録する
        parent = node_list[i].parent
        node_list[parent].children.append(i)
        # print(i,
        #       node_list[i].value,
        #       node_list[i].parent,
        #       node_list[i].children,
        #       node_list[i].min_child)

    # root直下のnodeが求めたいS式になる
    text = node_list[node_list[0].children[0]].value
    text = text[0] + 'S ' + text[1:]
    return text