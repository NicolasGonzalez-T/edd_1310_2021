class Nodo:
    def __init__( self, value, siguiente = None):
        self.data = value           #falta encapsulamiento
        self.next = siguiente       #falta encapsulamiento


class LinkedList:
    def __init__( self ):
        self.__head = None

    def is_empty( self ):
        return self.__head == None

    def append( self, value ):
        new = Nodo( value )
        if self.__head == None:     #self.is_empty()
            self.__head = new

        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"{ curr_node.data } ----> ", end = "")
            curr_node = curr_node.next
        print("")


    def remove( self, value ):
        curr_node = self.__head
        while curr_node.data != value and curr_node.siguiente != None:
            curr_node = curr_node.siguiente

        if curr_node.data == value:
