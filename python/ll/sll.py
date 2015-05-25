class node():
    '''A typical node of the 'singly linked list'. '''

    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.next = nextNode

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

class sll(node):
    ''' A singly linked list. '''

    def __init__(self):
        self.head = node(None)
        self.length = 0

    def display(self):
        current,l = self.head,[]

        while current!= None:
            l.append(current.getData())
            current = current.getNext()
        return l

    def insertAtBeginning(self,data):
        newNode = node(data)

        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1

    def insertAtEnd(self,data):
        newNode = node(data)

        current = self.head
        while current.getNext() !=  None:
            current = current.getNext()

        current.setNext(newNode)
        self.length += 1

    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos ==0:
                self.insertAtBeginning(data)
            else:
                newNode, count = node(data), 0
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1 
                
