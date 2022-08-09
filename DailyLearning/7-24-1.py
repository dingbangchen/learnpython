#inorder of python binary tree
# we have a pointer that search from the left, and we also have a stack that stores all the numbers(FILO)
# 1. we search from the left, if there is a left child then we add the node to the stack
# 2. if we couldn't find a left child in the node, we pop out the last node that we just pushed in the stack
# 3. After we pop out the node we search at the right node, if there is no right node then we just pop out the upper node again 
# 4. If the right child does exist, we push that right child into the stack .
# 5. Then we check the right child see if it has any left child.
# ...
# 6. when our pointer is null and our stack is empty, we have no nodes left