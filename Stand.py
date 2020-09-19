from array import *

class Stand:
  def __init__(self,_id):
      self.id = _id
      self.name=None
      self.loc = {'x': 0,'y': 0}
      self.requests = [0] * 8 #Array of size 8 per stand

  def add_destination(self, dest): #############add to avoid duplicates
      self.requests[dest] += 1
      
      