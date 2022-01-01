def parse_real_name(name):
  stripped_name = name.strip()
  name_list = stripped_name.split(" ")
  if len(name_list) == 1:
    return name_list.insert(1, '')
  if len(name_list) == 2:
    return name_list
  return [name_list[0], name_list[-1]]

def parse_nickname(nickname):
  print("in parser")
  print(nickname)
  stripped_nickname = nickname.strip()
  return stripped_nickname


