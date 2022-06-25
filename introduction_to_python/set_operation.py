friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends = abroad.difference(friends)
print(local_friends)

# Unite 2 sets -> gabungin 2 set jadi 1
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)


# Exercise
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

just_art = art.difference(science)
print(just_art)

just_science = science.difference(art)
print(just_science)

both = art.intersection(science)
print(both)