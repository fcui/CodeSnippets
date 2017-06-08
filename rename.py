import os

path = os.getcwd()

f = os.listdir(path)
for i in f:
    if 'mp3' in i:
        oldname = os.path.join(path, i)
        newname = os.path.join(path,
                               '4-' + i[-6:-4].replace(' ', '0') + '.mp3')
        os.rename(oldname, newname)
        print(newname)
