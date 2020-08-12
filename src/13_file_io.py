"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt') as foo:
    print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# note. /n makes a new line

bar = open("bar.txt", "w")
bar.write("hi this is 1st line.\n")
bar.write("hello first line, i'm 2nd line\n")
bar.write("hi 2nd line, i'm dad")
bar.close()
print(bar.closed)
with open("bar.txt") as bar:
  print("\n" + bar.read())
print(bar.closed)
