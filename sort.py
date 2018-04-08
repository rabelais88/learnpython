#array with tuple inside in each element
lstAnimal = [
  ("lion",53),
  ("cheetah",110),
  ("zebra",60),
  ("reindeer",80)
]

#this also works with this dictionary structure below
'''
lstAnimal = {
  "lion":53,
  "cheetah":110,
  "zebra":60,
  "reindeer":80
}
'''

lstFaster = sorted(
  lstAnimal,
  key = lambda x: x[1], #use second element of tuple as a sort hint
  reverse=True
)

print(lstAnimal)
print(lstFaster)