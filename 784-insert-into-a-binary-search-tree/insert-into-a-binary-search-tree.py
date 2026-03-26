class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        current = root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
        
        return root
        