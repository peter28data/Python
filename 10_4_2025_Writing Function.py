# ---------------------- Task 1: Nested Function -------------------------------------

def nth_rot(n):
  def actual_root(x):
    root = x ** (1/n)
    return root 
  return actual_root
print(nth_root(3)(27))


# ---------------------- Task 2: Return Largest from List --------------------------

def sorted_elements(x, desc=True, n=2):
  new_x = sorted(x, reverse=desc)[0:n]
  return new_x

# ---------------------- Task 3: Return Positive Numbers ----------------------------

filter_positives = filter(lambda n: n > 0, x)
print(list(filter_positives))

# --------------------------------------------------------------------------

