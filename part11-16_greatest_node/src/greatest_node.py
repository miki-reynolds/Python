class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):
    node_max = root.value

    if root.left_child is not None and node_max < greatest_node(root.left_child):
        node_max = greatest_node(root.left_child)

    if root.right_child is not None and node_max < greatest_node(root.right_child):
        node_max = greatest_node(root.right_child)

    return node_max








