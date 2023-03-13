"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object): # Approach 1: Recursive
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return 
        # the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this 
        # would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the 
        # next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


class Solution(object): # Approach 2: Iterative with O(N)O(N) Space
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" 
        # and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary          
            if node in self.visited:
                # If its in the visited dictionary then return the new node 
                # reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the 
                # visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head == None:
            return head

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


class Solution(object):# Approach 3: Iterative with O(1) Space
    def copyRandomList(self, head):
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be 
            # A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random 
        # pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and 
        # the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Check the difference between defaultdict and method get()
        # https://stackoverflow.com/questions/6130768/return-none-if-dictionary-key-is-not-available
        dummy = node = Node(0)
        h = head
        nodemap = dict()
        while h: # The final None will not be in nodemap
            node.next = Node(h.val)
            nodemap[h] = node.next
            node = node.next
            h = h.next
        while head:
            rh = head.random
            nodemap[head].random = nodemap.get(rh, None)
            head = head.next
        return dummy.next

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #copy the linked list without random
        #Using a dict to store coresoponding node
        if not head:
            return None
        node_map = collections.defaultdict(lambda: None)#The only difference
        curr = head
        while curr:
            node_map[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next]#Difference
            node_map[curr].random = node_map[curr.random]#Difference
            curr = curr.next
        return node_map[head]

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #copy the linked list without random
        #Using a dict to store coresoponding node
        if not head:
            return None
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map.get(curr.random, None)
            curr = curr.next
        return node_map[head]
