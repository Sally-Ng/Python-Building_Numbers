# I acknowledge the assitance of Marc Mares

# open and read the file, then store in a dictionary
def read_buildings_from_file(f):
  building_dict = {}
  file = open(f) 
  for line in file:
    line_S = line.split()
    name = line_S[0]
    building_dict[name] = int(line_S[1])
  file.close()
  return building_dict

building = read_buildings_from_file("buildings.txt")

# add a new name and building number
building["Satish"] = 6

# change Maya's building number
building["Maya"] = 11
print building

# update the file
def write_buildings_to_file(dict, f):
  file = open(f, "w")
  for key in dict:
    file.write(key + " " + str(dict[key]) + "\n")
  file.close

write_buildings_to_file(building, "buildings.txt")
