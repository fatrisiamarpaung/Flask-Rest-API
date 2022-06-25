l = ["Eta", "Fatri", "Sia"]
t = ("Eta", "Fatri", "Sia") # Gabisa diubah
s = {"Eta", "Fatri", "Sia"} # Gabole ada duplicate value

# This is how to access list and tuple
print(l[0]) #print value index 0

# Change value in list
l[0] = "Smith"
print(l)

# Add an element to a list
l.append("Marpaung")
print(l)

#remove element from a list
l.remove("Smith")
print(l)

# Add an element to a set
s.add("Marpaung")
print(s)