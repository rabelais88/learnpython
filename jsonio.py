import json

data = {
  "var1":32949,
  "var2":[34,2,3],
  "var3":"djfkldfjkdlflfd"
}

filename = "test.json"
with open(filename, "w") as fp:
  json.dump(data,fp)

with open(filename, "r") as fp:
  r = json.load(fp)
  for key, value in r.items():  # iterate through dictionary !! must remember this
    print(" - {0} : {1}".format(key,value))