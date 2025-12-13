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



  
  
# -------------------- Task 9: Sub-Parts 'text' and 'lang' --------------------------

df = pd.DataFrame(tweets_data,
                  columns=['lang'])
print(df.head())






# ------------------- Task 10: Retrieve Director's Name ------------------------------

with open("another.json") as json_file:
  
  json_data = json.load(json_file)
  print(json_data["Director"])





# ------------------- Task 11: Parse and Extract -------------------------------------

url = 'https://www.python.org/~guido/'
r = requests.get(url)

html_doc = r.text

s = BeautifulSoup(html_doc)
print(s.title)






# -------------------- Task 12: Web Scraping Hyperlinks -------------------------------

for link in a_tags:
  print(link.get('href'))

# Assignment of Tags
a_tags = soup.find_all('a')





# ------------------- Task 13: Output Desired Number of Hyperlinks -------------------

for link in s.find_all("a")[:3]:
  
  print(link.get('href'))





# ------------------ Task 14: Web Scraping & API Keys --------------------------------

url = ('http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network')
r = requests.get(url)

json_data = r.json()

print(json_data['Awards'])





# ------------------ Task 15: Flat File Printing -------------------------------------

urlretrieve(url,'winequality-red.csv')
df = pd.read_csv('winequality-red.csv',
                 sep=';')

print(df[['alcohol','quality']].head()


      



# --------------------------------------------------------------------------



      

      
      
      

      
      


      

      

      

      

      



      
      


      

      


      


      


      

      
      
      
      

      
