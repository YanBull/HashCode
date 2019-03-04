### we could only sort out the horizonatal and vertical photos from each other,
### and group random two vertical photos in one slide, and also created an array of all the slides,
### without any sorting

f=open('e_shiny_selfies.txt')
file = f.readline()
print(file)
length=int(file)

a=[]

### file reading routine
for k in range(length):
    a.append([])
    i=0
    file=f.readline()
    while i<len(file):
        if file[i]!=' ' and file[i]!='\n':
            a[k].append(file[i])
            i+=1
            while file[i]!=' ' and file[i]!='\n':
                #print(file[i])
                a[k][len(a[k])-1]+=file[i]
                #print(A[k])
                i+=1
            else:
                i=i+1
        else:
            i=i+1
    print(a[k])

### function to collide two lists with no repeatings in it
def collision(a=[], b=[]):
    l = len(a)
    i = 0
    while (i < l):
        word = a[i]
        if word in b:
            i += 1
        else:
            a.append(word)
            i += 1

    return a


tags_only_in_first = 0
tags_only_in_second=0
common_tags=0
vertical_photos = []
horizontal_photos = []

for i in range(len(a)): ## sorting out vertical and horizontal photos
    for j in range(len(a[i])):
        if a[i][j] == "H":
            horizontal_photos.append(a[i])
        if a[i][j] == "V":
            vertical_photos.append(a[i])

print(vertical_photos)

vertical_slides =[]
### making a slide from two vertical photos
for i in range(1,len(vertical_photos)):
    if (i-1) % 2 == 0:
        vertical_slides.append(collision(vertical_photos[i], vertical_photos[i-1]))


print(vertical_slides)
### making a list of slides from vertical and horizontal ones
slides = collision(vertical_slides , horizontal_photos)
print(slides)