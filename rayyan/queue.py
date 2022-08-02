class queue:
  def __init__(self):
    self.items=[]
  def isempty(self):
      return self.items==[]
  def enqueue(self,item):
      self.items.append(item)
  def dequeue(self):
      return self.items.pop(0)
  def front(self):
    return self.items[len(self.items)-1]
  def size(self):
          return len(self.items)
q=queue()
print("Queue operation Exampoles")
print(q. isempty())
q.enqueue("python")
q.enqueue(5)
print(q.front())
q.enqueue(True)
print(q.size())
print(q.isempty())
q.enqueue(11.5)
print(q.dequeue())
print(q.dequeue())
print(q.size())