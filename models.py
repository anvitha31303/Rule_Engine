class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        # Convert the Node and its children into a dictionary
        node_dict = {
            "type": self.type,
            "value": self.value
        }
        if self.left:
            node_dict["left"] = self.left.to_dict()  # Recursively call to_dict on the left node
        if self.right:
            node_dict["right"] = self.right.to_dict()  # Recursively call to_dict on the right node
        return node_dict
