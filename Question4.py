import queue
class Huffmancode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     
    def children(self):
        return((self.left, self.right))
prob = [
    (0.167, 'a'), (0.492, 'b'), (0.782, 'c'), (0.253, 'd'),
    (0.702, 'e'),(0.228, 'f'), (0.015, 'g'), (0.094, 'h'),
    (0.966, 'i'), (0.153, 'j'), (0.747, 'k'), (0.025, 'l'),
    (0.406, 'm'), (0.749, 'n'), (0.507, 'o'), (0.929, 'p'), 
    (0.095, 'q'), (0.987, 'r'), (0.327, 's'), (0.056, 't'), 
    (0.758, 'u'), (0.037, 'v'), (0.365, 'w'), (0.150, 'x'),
    (0.974, 'y'), (0.074, 'z') ]
def create_tree(prob):
    p = queue.PriorityQueue()
    for value in prob:    
        p.put(value)             
    while p.qsize() > 1:         
        l, r = p.get(), p.get()  
        node = Huffmancode(l, r) 
        p.put((l[0]+r[0], node)) 
    return p.get()               
node = create_tree(prob)
print(node)
def build_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], Huffmancode):
        build_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],Huffmancode):
        build_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)

code = build_tree(node)
for i in sorted(prob, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
