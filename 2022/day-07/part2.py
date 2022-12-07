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

    def get_dir(self, dir_name):
        for d in self.dirs:
            if d.name == dir_name:
                return d

    def has_child(self):
        return len(val) != 0

    def compute_size(self):
        self.size = sum()

def read_dir(node, lines, sizes):
    #entering a new dir via cd
    #ignore next line as it is ls
    next(lines)

    for line in lines:
        line = line.strip()

        if line == '$ cd ..':
            sizes.append(node.size)
            return

        elif line[0:5] == '$ cd ':
            dir_name = line[5:]
            dir_node = Node(dir_name, 0)
            read_dir(dir_node, lines, sizes)
            node.add_dir(dir_node)

        # dir definition ignore it for now
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

sizes = []
read_dir(root, lines, sizes)
sizes.append(root.size)

total_size = root.size
disk_size = 70000000
left = disk_size - total_size
needed = 30000000 - left

for t in sorted(sizes):
    if t >= needed:
        print(t)
        break