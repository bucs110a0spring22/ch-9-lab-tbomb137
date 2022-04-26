class Rectangle:
  def __init__(self,x,y,h,w):
    self.height = max(0,h)
    self.width = max(0,w)
    self.x = max(0,x)
    self.y = max(0,y)

  def __str__(self):
    str = "(x:[], y:[]) width:[], height:[]"
    return str.format(self.x, self.y, self.width, self.height)
