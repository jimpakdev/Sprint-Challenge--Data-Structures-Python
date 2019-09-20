class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  # adds elements to the buffer
  def append(self, item):
    self.storage[self.current] = item
    if self.current >= len(self.storage)-1:
      self.current = 0
    else:
      self.current += 1

  # returns list of all elements in the buffer in given order
  def get(self):
    return [i for i in self.storage if i is not None]
    