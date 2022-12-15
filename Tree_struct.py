class TreeNode(dict):
    def __init__(self, name, children=None):
        super().__init__()
        self.__dict__ = self
        self.name = name
        self.children = list(children) if children is not None else []
    def from_dict(dict_):
        node = TreeNode(dict_['name'], dict_['children'])
        node.children = list(map(TreeNode.from_dict, node.children))
        return node
    def getchild(this,i):
        return this.children[i]
    def howmanychild(this):
        return len(this.children)
    def addtwochild(this,children1,children2):
        this.children.append(children1)
        this.children.append(children2)