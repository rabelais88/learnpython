txt = """
I don't wanna waste my time if I can't be by your side
You really shouldn't think about God if she can't see where you hide
We don't gotta talk about nothing nice if you wanna come down
But she don't gotta know 'bout nothing
But she don't gotta know...

Chorus
And if the stars collide, will she relieve my soul?
And when we feel alive I know she'll let me go
When you read my lips, I know you feel all cold
But I promise you my heart is made of gold

Verse 2
I don't wanna waste my time if I can't make you decide
You're only on my mind when I need you
I don't need to know about what you do when the sun goes down
Cause I don't gotta know about nothing
Cause I don't gotta know...

Chorus
And if the stars collide, will she relieve my soul?
When we feel alive I know she'll let me go
When you read my lips, I know you feel my cold
But I promise you my heart is made of gold
"""
txt.lower()
txt = txt.replace(";","").replace(",","").replace(".","").split()

counter = {}
for w in txt:
  if w in counter:
    counter[w] += 1
  else:
    counter[w] = 1

for k,v in sorted(counter.items()):
  if v >= 3:
    print(k,v)
