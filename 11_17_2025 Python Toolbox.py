team_arrow = zip(code_names, characters_names)

cnames, names = zip(*team_arrow)

print(names)


-----------------------------------------------------------------

# Generator function that loads data in chunks
def read_large_file(file_object):
  """A generator function to read a large file lazily."""
  while True:
    data = file_object.readline()
    
    if not data:
      break
    yield data


-----------------------------------------------------------------

matrix = [[col for col in range(1, 4)] for row in range(3)]

print(matrix)


-----------------------------------------------------------------

def to_upper(heroes):
  for i in heroes:
    yield i.upper()

print(list(to_upper(superhero_list)))


-----------------------------------------------------------------

capitals = {'australia':'canberra', 'belgium':'brussels'}

for key, value in capitals.items():

  print(key, value)
