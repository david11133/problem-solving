class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None
  
def main():
    # Creating a simple binary search tree
    #         6
    #        / \
    #       2   8
    #      / \ / \
    #     0  4 7  9
    #       / \
    #      3   5
  
    root = TreeNode(6)
    node2 = TreeNode(2)
    node8 = TreeNode(8)
    node0 = TreeNode(0)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
  
    root.left = node2
    root.right = node8
    node2.left = node0
    node2.right = node4
    node8.left = node7
    node8.right = node9
    node4.left = node3
    node4.right = node5
  
    # Nodes to find LCA for
    p = node2  # Node with value 2
    q = node8  # Node with value 8
  
    lca = lowestCommonAncestor(root, p, q)
    if lca:
        print(f'The LCA of {p.val} and {q.val} is {lca.val}.')
    else:
        print('LCA not found.')
  
if __name__ == "__main__":
    main()
