class Node:
    def __init__(self,cargo = None,next = None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self) -> str:
        return str(self.cargo)
print(Node("text"))