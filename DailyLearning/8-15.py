#construte a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):                    # 注意这里是一个public方法（我知道我傻逼了）
        current = root                #建立一个指针指向root节点
        stack = []                      #这里创建一个stack（注意这只是一个list，逻辑上我们把他当作一个stack）

        while True:
            if current is not None:             #首先遍历整个左子节点，如果左子节点存在就吧它们入stack，直到最左下的节点被找到
                stack.append(current)
                current = current.left
            elif(stack):                        # 
                current = stack.pop()
                print(current.data, end = " ")
                current = current.right
            else:
                break
        print() 


# Driver program to test above function
  
"""
Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   
"""
  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  
inOrder(root)