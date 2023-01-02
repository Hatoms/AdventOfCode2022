import re

with open('input.txt') as f:
    input = f.readlines()

input = [c.strip() for c in input]


class Node(object):

    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.nodes_child = []

    def create_node_child(self, name):
        child = Node(name, self)
        self.nodes_child.append(child)
    
    def find_child(self, name):
        for child in self.nodes_child:
            if child.name == name:
                return child

    def add_size(self, size):
        self.size += size
        if self.parent :
            self.parent.add_size(size)



### Construct tree

current_node = None

index_input = 0

parent_node = Node('root', None)
parent_node.create_node_child('/')
current_node = parent_node

command = input[0]

while index_input < len(input)-1: 
    command = input[index_input]

    if command[:4] == "$ cd" and command[5:] != '..':
        try:
            current_node = current_node.find_child(command[5:])
        except:
            import pdb; pdb.set_trace()

        index_input += 1 # ls always following a cd dir
        
        while index_input < len(input)-1:
            index_input += 1
            command = input[index_input]
            if command[0] == '$':
                break
            if command[:3] == 'dir':
                current_node.create_node_child(command[4:])
            else :
                size = re.findall(r'\d+', command)[0]
                current_node.add_size(int(size))
    else :
        current_node = current_node.parent
        index_input += 1


### Display Tree and size



#lvl 1

# light_folders = []
# def print_node(node, depth):
#     print('  '*depth + '-' + node.name + ' : ' + str(node.size))
#     if node.size <= 100000 :
#         light_folders.append(node.size)

#     for node_child in node.nodes_child :
#         print_node(node_child, depth+1)

# print_node(parent_node, 0)

#print(sum(light_folders))

# lvl 2

TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000
free_space = TOTAL_SPACE - parent_node.size
space_to_del = SPACE_NEEDED - free_space

node_min_size = parent_node.size

def find_node_to_del(node):
    global node_min_size

    if node.size < space_to_del :
        return
    if node.size <= node_min_size :
        node_min_size = node.size
        print(node.name + ' : ' + str(node_min_size))
        
    for node_child in node.nodes_child :
        find_node_to_del(node_child)


find_node_to_del(parent_node)

