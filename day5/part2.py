import re

# Linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __len__(self) -> int:
        node = self.head
        cnt = 0
        while node is not None:
            cnt += 1
            node = node.next
        return cnt
    
    def append_node(self, child:'Node'):
        if self.head is None:
            self.head = child
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = child

    def append_element(self, element):
        if self.head is not None:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(element)
        else:
            self.head = Node(element)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


with open("input.txt", "r", encoding="ascii") as f:
    cargo:list[list[str]] = []
    matched:bool = False
    stacks:list = []
    for line in f.readlines():
        if not matched:
            if re.match(r"^( \d  ?)+$", line):
                matched = True

                # Transpose by 90°                    
                cargo = list(map(list, zip(*cargo)))
                for row in cargo:
                    row.reverse()
                    t = LinkedList()
                    t.head = Node("Start")
                    stacks.append(t)
                    for el in row:
                        if el != ' ': 
                            stacks[-1].append_element(element=el)

                #print("Beginning:")                
                #for stack in stacks:
                #    print(stack, len(stack))
                #print("\n\n")
                #continue
            else:
                tmp = re.findall(r"((?:\[\w\])|(?:\s{3}))\s?", line)
                cargo.append([x[1] for x in tmp])
        else:
            instr = re.findall(r"^move (\d+) from (\d+) to (\d+)$", line)
            if len(instr) != 1: 
                continue

            quant, stFrom, stTo = map(int,instr[0])

            cr = len(stacks[stFrom-1])-quant-1
            nd = stacks[stFrom-1].head
            while cr > 0:
                cr -= 1
                nd = nd.next

            stacks[stTo-1].append_node(nd.next)
            nd.next = None

            #print(f"After moving {quant} from {stFrom} to {stTo}:")
            #for stack in stacks:
            #    print(stack)
            #print("\n")
    out = ""
    for stack in stacks:
        nd = stack.head
        while nd.next is not None:
            nd = nd.next
        out += nd.data

    print(*out, sep="")