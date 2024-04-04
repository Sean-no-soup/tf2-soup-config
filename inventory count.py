#importing multiline inputs without lagging out python and being intuitive
#turned out to be much more annoying than expected

with open('inventory markdown.txt','r') as file:content = file.read()
itemlist = content.splitlines()
groupedlist = []

#I coud do this with a class but lazy. might have to if I want to do more with this info like graphs. could extract a bunch of data directly from backpack with the other markdown options
for item in itemlist:
    for index in range(len(groupedlist)):
        group = groupedlist[index][0]
        if group == item:
            groupedlist[index][1] += 1
            break
    else:
        groupedlist += [[item,1]]

#sort by number cuz eyelanders
groupedlist.sort(reverse = True, key = lambda sublist: sublist[1])
total = 0
for group,count in groupedlist:
    total += count
    print(group,count)
    
print('sanity check, total inventory slots used:',total)
