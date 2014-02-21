# murfie class test
import Murfie

murfie = Murfie.API('jason@murfie.com', 'password')

collection = murfie.Collection()

disc = murfie.Disc(collection[0]['disc']['id'])

track = murfie.Track(disc['id'], disc['tracks'][0]['id'])

print track
