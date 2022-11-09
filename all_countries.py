def allcountries():
  df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')
  
  year = df["YEAR"]
  spain = df[" SP"]
  turkey = df[" TK"]
  poland = df[" PL"]
  
  plt.style.use('seaborn')
  fig, ax = plt.subplots()
  ax.plot(year, spain, c='yellow')
  ax.plot(year, turkey, c='red')
  ax.plot(year, poland, c='pink')
  
  
  ax.set_title("Tourism in last decade, 2010-2020", fontsize=24)
  ax.set_xlabel('', fontsize=16) 
  ax.set_ylabel("?", fontsize=16)
  ax.tick_params(axis='both', which='major', labelsize=16)
  
  plt.show()
