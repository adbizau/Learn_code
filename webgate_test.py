class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score
    print(self.score)
  
  def is_passing(self):
    if self.score > Grade.minimum_passing:
      print("Passing")
    else:
      print("Not passing")
  

x = Grade(88)
x.is_passing()

