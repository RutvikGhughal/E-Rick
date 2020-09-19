class Rickshaw:
  def __init__(self,_id):
    self.id = _id
    self.driverName = ''
    self.loc = {'x':0,'y':0}
    self.passengers = 0
    self.active = False
    self.des=[]

  def isfull(self):
      if self.passengers == 4:
          return True
      else:
          return False

  def add_passenger(self):
      self.passengers+=1
      
  def remove_passenger(self):
      self.passengers-=1
      
  def deactivate(self):
      self.active = False
      
  def distance(self,_loc):
      x1 = self.loc['x']
      x2 = _loc['x']
      y1 = self.loc['y']
      y2 = _loc['y']