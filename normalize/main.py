def normalize(vet):
  new_vet = []
  vet_max = my_max(vet)
  vet_min = my_min(vet)
  if(vet_max - vet_min) == 0:
    for n in range(len(vet)):
      new_vet.append(100)
    return new_vet

  for n in range(len(vet)):
    a = vet[n] - vet_min
    b = vet_max - vet_min
    new_vet.append(a/b*100)

  return new_vet
 
def my_max(vet):
  return max(vet)

def my_min(vet):
  return min(vet)