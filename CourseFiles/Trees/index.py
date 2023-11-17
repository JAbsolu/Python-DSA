class BinaryTree:
  def __init__(self, root):
    self.key = root
    self.left = None
    self.right = None
  '''
    Get the valur of the node
  '''
  def get_key(self):
    return self.key
  '''
    Insert a left child
  '''
  def insert_left_child(self, new_node):
    if self.left == None:
      self.left = BinaryTree(new_node)
    else:
      new_child = BinaryTree(new_node)
      new_child.left = self.left
      self.left = new_child
  '''
    Insert a right child
  '''
  def insert_right_child(self, new_node):
    if self.right == None:
      self.right = BinaryTree(new_node)
    else:
      new_child = BinaryTree(new_node)
      new_child.right = self.right
      self.right = new_child
  '''
    Get the left child
  '''
  def get_left_child(self):
    return self.left
  '''
    get the right child
  '''
  def get_right_child(self):
    return self.right

  '''
    Print the tree in the terminal
  '''
  def to_string(self):
    stack = [self]
    index = 0
    while len(stack) > 0:
      node = stack.pop()
      index += 1
      
      print(f"Node {index}'s Value: {node.get_key()}")
      
      if node.get_left_child() and node.get_right_child():
        print(f"Node {index}'s left: {node.get_left_child().get_key()}")

      if node.get_right_child():
        print(f"Node {index}'s right: {node.get_right_child().get_key()}")
      
      if node.right:
        stack.append(node.get_right_child())
      if node.left:
        stack.append(node.get_left_child())

'''
  Building the tree from a list
'''

my_list = ['Louis', 'Brian', 'Peter', 'George', 'Amy', 'Hannah', 'Sarah', 'Mike', 'David']

def BuildTree(nums):
  my_tree = BinaryTree(nums[0])
  
  for i in range(1, len(nums) - 1):
    my_tree.insert_left_child(nums[i])
    my_tree.insert_right_child(nums[i+1])
    
  return my_tree.to_string()
  
BuildTree(my_list)