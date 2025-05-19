llist = [1, 2, 3, 4]


class Node:
    def __init__(self, data, next, prev):

        self.data = data
        self.next = next
        self.prev = prev

def reverse(llist):

    llist2 = []

    for no in range(len(llist)):

        if no == 0:
            llist2.append(Node(llist[no], llist[no + 1], None))
            continue
        if llist[no] == llist[-1]:
            llist2.append(Node(llist[no], None, llist[no - 1]))
            break
        llist2.append(Node(data=llist[no], next=llist[no + 1], prev=llist[no - 1]))
    ans = [i.data for i in reversed(llist2)]
    #for i in reversed(llist2):
    #    print(i.data)

    return ans

print(reverse(llist))

print("TEM QUE RETORNAR O PONTEIRO PARA O NÓ CABEÇA DA NOVA LISTA")