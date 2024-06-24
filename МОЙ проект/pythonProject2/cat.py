class Cat:
  def __init__(self, name, gender, age):
      self.name = name
      self.gender = gender
      self.age = age


  def get_name(self):
      return self.name

  def get_gender(self):
      return self.gender

  def get_age(self):
      return self.age


cat_1 = Cat("Baron", "boy", 2)
cat_2 = Cat("Sam", "boy", 2)

print(cat_1.get_name(), cat_1.get_gender(), cat_1.get_age())
print(cat_2.get_name(), cat_2.get_gender(), cat_2.get_age())