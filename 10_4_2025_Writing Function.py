# ---------------------- Task 1: Nested Function -------------------------------------

def nth_rot(n):
  # Function within a Function
  def actual_root(x):
    # Nested function raises x to the inverse of n to be square root, cube root, etc.
    root = x ** (1/n)
    
    return root 
  return actual_root
print(nth_root(3)(27))





# ---------------------- Task 2: Return Largest from List --------------------------

def sorted_elements(x, desc=True, n=2):
  # '[0:n]' will return a subset of specified indexes
  new_x = sorted(x, reverse=desc)[0:n]
  return new_x





# ---------------------- Task 3: Return Positive Numbers ----------------------------

filter_positives = filter(lambda n: n > 0, x)
print(list(filter_positives))





# ----------------------- Task 4: Return Area & Perimeter ---------------------------------------------------

def square(s):
  """Returns area & perimeter of a square."""
  try:
    a = s * s
    p = 4 * s
    return a, p
    expect TypeError:
      print('s can not be a string')
square('5')



# --------------------- Task 5 : Convert Yards to Feet if feet is True -----------------------------------------------------

def conver_yards(y, feet=True):
  if feet is True:
    new_y = y * 3
  else:
    new_y = y * 36
  return new_y





# --------------------------------------------------------------------------















