class Person:
  def __init__(self,*pros,**attrs):
    self.name = "jeff"
    self.pros = pros
    for (key,value) in attrs.items():
      stm = "self.%s = /"%s/""% (key,value)
      exec(stm)
  if __name__ == "__main__":
    jeff = Person(1,2,3,sex="boy")
    print jeff.pros
    print jeff.sex
