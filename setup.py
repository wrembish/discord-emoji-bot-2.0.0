def build_conversion_map():
  f = open("letter_to_emoji.txt")
  line = f.read()
  f.close()

  isKey = True
  key = 'a'
  value = ""
  values = []
  conversion_map = {}
  for c in line:
    if isKey:
      key = c
      isKey = False
    elif (c == '\r') or (c == '='):
      isKey = False
    elif c == '\n':
      values.append(value)
      conversion_map[key] = values

      value = ""
      values = []
      isKey = True
    elif c == ' ':
      if value != "" and value != " ":
        values.append(value)
      value = ""
    else:
      value = value + c
  
  values.append(value)
  conversion_map[key]=values

  return conversion_map

def get_guild_ids():
  ids = []
  returnids = []
  f = open("guildids.txt")
  line = f.read()
  f.close()
  ids = line.split(",")
  for s in ids:
    if(s != ""):
      returnids.append(int(s))

  return returnids

def addguildid(id):
  f = open("guildids.txt","a")
  f.write(str(id)+",")
  f.close()

def get_built_in_messages():
  f = open("built_in_messages.txt", "r")
  line = f.read()
  key = ""
  value = ""
  output = {}
  isKey = True

  for c in line:
    if c == '"':
      isKey = False
    elif isKey:
      key = key + c
    elif c == '\r':
      True
    elif c == '\n':
      output[key] = value
      key = ""
      value = ""
      isKey = True
    else:
      value = value + c
  output[key] = value
  return output