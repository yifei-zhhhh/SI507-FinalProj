I create a tree structure for the data for this project and store the data as a json file.<br/>
The basic structure for a single node in the tree is name and children. For the leaf node, the name is the list of indexes that represents movies, and the children is a null list.
For the parent node, the children of it are two nodes, the name of the two nodes are indexes that are classified by the given question. I construct the tree recursively. Detailed 
construction detail can be seen in data_to_tree.py.<br/>
