class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVLTree:

    def __init__(self):
        self.root = None

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key, value):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases

        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, root, key):

        if not root:
            return root

        elif root.key == key:
            return root.value

        elif root.key > key:
            return self.search(root.left, key)

        else:
            return self.search(root.right, key)


    def remove(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.remove(root.left, key)

        elif key > root.key:
            root.right = self.remove(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        # If the tree has only one node, simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases

        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def deep(self, curr_node):
        if curr_node is None or (curr_node.left is None and curr_node.right is None):
            return 0

        else:
            if self.deep(curr_node.left) > self.deep(curr_node.right):
                return 1 + self.deep(curr_node.left)

            else:
                return 1 + self.deep(curr_node.right)

    def numberOfNodes(self, root):
        if root is None:
            return 0

        return 1 + self.numberOfNodes(root.left) + self.numberOfNodes(root.right)

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print(f'{root.key}', end='\n')
        self.inOrder(root.right)

    def searchByYear(self, root, year):

        global res

        if not root:
            return

        self.searchByYear(root.left, year)
        if root.value.year == year:
            res.append(root.key)
        self.searchByYear(root.right, year)

        return res

res = []
