class Node:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.files = []
        self.dirs = []

    def add_file(self, child):
        self.files.append(child)
        self.size += child.size

    def add_dir(self, child):
        self.dirs.append(child)
        self.size += child.size

def read_dir(node, lines, res):
    #entering a new dir via cd
    #ignore next line as it is ls
    next(lines)

    for line in lines:
        line = line.strip()

        # Going back to parent dir
        if line == '$ cd ..':
            if node.size <= 100000:
                res.append(node.size)
            return

        # Entering and parsing a new dir
        elif line[0:5] == '$ cd ':
            dir_name = line[5:]
            dir_node = Node(dir_name, 0)
            read_dir(dir_node, lines, res)
            node.add_dir(dir_node)

        # dir definition can be ignored
        # since we'll cd into it later
        elif line[0:3] == 'dir': 
            continue
        
        # file definition
        else: 
            size, name = line.split(' ')
            size = int(size)
            node.add_file(Node(name, size))


root = Node('/',0)
res = []
lines = open('input.txt')
next(lines)

read_dir(root, lines, res)

if(root.size <= 100000):
    res.append(root.size)

print(sum(res))