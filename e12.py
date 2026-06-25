import random
stud=["Pepe","Carlos","Juan","Tito","Ignacio"]
x=[]
for i in range(len(stud)):
  n=random.randint(0,len(stud)-1)
  x.append(stud[n])
  del(stud[n])
print(f"The winner is: {x}")