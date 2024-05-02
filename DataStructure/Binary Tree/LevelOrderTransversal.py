from CreateBinaryTree import CreateTree


def levelOrder(root, result = "", begin = True):
    if begin:
        result += root.value.__str__() + " "

    if root is None:
        return result
    
    if root.left is not None:
        result += root.left.value.__str__() + " "
    if root.right is not None:
        result += root.right.value.__str__() + " "
    result = levelOrder(root.left, result, False)
    result = levelOrder(root.right, result, False)
    return result


my_tree = CreateTree()
level = levelOrder(my_tree).split(" ")[:-1]
print( f"Level order traversal: {level}")