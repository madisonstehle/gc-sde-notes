class DrawingProgramIterator():
  """
  class that provides the ability to iterate across
  the collection of shapes in DrawingProgram using a for loop

  assuming drawing_program = DrawingProgram(), the following code should work
    for shape in drawing_program:
      print(shape)
  """
  #resource used: https://python-patterns.guide/gang-of-four/iterator/,
  #https://sourcemaking.com/design_patterns/iterator/python/1,

  def __init__(self, List):
    self.tracker=0 #keeps track of index
    self.list_of_shapes = List

  def __next__(self):
    if self.tracker < len(self.List): #if list > counter
      the_shape = self.List[self.tracker] #tracker point in List is stored as the_shape
      self.tracker +=1
      return the_shape
    else:
      raise StopIteration #built in stop iterations breaks/stops iteration

  def __iter__(self):
    return self