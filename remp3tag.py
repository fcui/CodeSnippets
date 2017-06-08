import eyed3
import os

path = os.getcwd()

f = os.listdir(path)
for i in f:
    if 'mp3' in i:
        oldname = os.path.join(path, i)
        audiofile = eyed3.load(oldname)
        audiofile.tag.artist = 'Letterland'
        audiofile.tag.album = 'CD4'
        newname = '4-' + i[-6:-4].replace(' ', '0')
        audiofile.tag.title = newname
        # audiofile.tag.track_num =
        newnamemp3 = os.path.join(path, newname + '.mp3')
        # os.rename(oldname, newname)
        audiofile.tag.save()
        print(newname)
