# ------------------------ Task 1: Same outputs to retrieve with Query -------------

# 1: Traditional way
with engine.connect() as con:
  rs = con.execute("SELECT * FROM Album")
  df = pd.DataFrame(rs.fetchall())
  df.columns=rs.keys()

# 2: Modern way
df = pd.read_sql_query("SELECT * FROM Album", engine)


# ------------------------ Task 2: Retrieve first 4 Elements -----------------------

engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()
print(table_names[0:4])

# ----------------------- Task 3: Read part of CSV ---------------------------------

titanic_data = pd.read_csv('titanic.csv', nrows=2, header=0)
print(titanic_data)

# ----------------------- Task 4: Read Second Excel Sheet, first 4 rows ------------

df = data.parse(1, parse_cols=[0],
                skiprows="0",
                names=['Country'])
print(df.head())

# ---------------------- Task 5: Return Data Type ---------------------------------

import scipy.io
filename = 'file.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))


# ---------------------- Task 6: Import File ---------------------------------------

seaslugs = np.loadtxt(file,
                      delimiter= "/t",
                      skiprows=1)
print(seaslugs[0:3])


# --------------------------------------------------------------------------

# keys are equivalent to MATLAB variable names
# values are equivalent to objects assigned to variables

# --------------------- Task 7: Equivalent Code ------------------------------

# 1
np.recfromcsv(filename)

# 2
np.genfromtxt(filename,
              delimiter=',',
              dtype=None,
              names=True)

# -------------------- Task 8: Equivalent Code -----------------------------------

# 1
file = open('filename.txt', mode='r')
file.close()

# 2
with open('filename.txt','r') as file:

# --------------------------------------------------------------------------







