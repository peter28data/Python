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

