import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames

listfilename = glob.glob(pattern)

print(listfilename)

# TODO: use os.path.getsize to find each file's size

print("The size of each file is: ")
for filename in listfilename:
    sizefilename = os.path.getsize(filename)
    print(filename, ":", sizefilename, "bytes")

# TODO: Add a test to only display files that are not zero length

print("The files of non-zero length are: ")
for filename in listfilename:
    sizefilename = os.path.getsize(filename)
    if sizefilename == 0:
        pass
    else: print(filename)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

print("Removing the leading directory name gives: ")
for filename in listfilename:
    shortfilename = os.path.basename(filename)
    print(shortfilename)

