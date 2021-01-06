#What are lists and tuples?
# What is the key difference between the two?
#The key difference between the two is that while lists are mutable,
# tuples on the other hand are immutable objects.
# This means that lists can be modified, appended or sliced on-the-go
# but tuples remain constant and cannot be modified in any manner.
# You can run the following example on Python IDLE to confirm the difference

my_tuple = ('sara', 6, 5, 0.97)
my_list = ['sara', 6, 5, 0.97]

print(my_tuple[0])     # output => 'sara'
print(my_list[0])     # output => 'sara'

my_tuple[0] = 'ansh'    # modifying tuple => throws an error
my_list[0] = 'ansh'    # modifying list => list modified

print(my_tuple[0])     # output => 'sara'
print(my_list[0])     # output => 'ansh'