#importing multiline inputs without lagging out python and being intuitive
#turned out to be much more annoying than expected
import re

print("starting")

output = open("tf2_inv_output.txt","w")
output.close()
with open('inventory markdown.txt','r') as file:content = file.read()

invlist = content.splitlines()
groupedlist = []
count = 0

for invstring in invlist: #parse

    count += 1
    if count % 50 == 0:print(".",end = "")

    item = re.findall(r"^.*?(?=\s\()",  invstring) #before " ("
    item = item[0] if item else invstring

    context = (re.findall(r"\((.*?)\)", invstring)) #between parentheses
    context = context[0].replace("â€“","-") if context else ""

    cost_unit = re.findall(r"(key|\$|ref)", context)
    cost_unit = cost_unit[0] if cost_unit else ""

    cost_list = re.findall(r"[0-9\.]+", context)
    if cost_list:
        cost_min, cost_max = cost_list[0],cost_list[-1]
    else:
        cost_min, cost_max = "",""

    warpaint_wear = re.findall(r"(Factory New|Minimal Wear|Field-Tested|Well-Worn|Battle-Scarred)", context)
    warpaint_wear = warpaint_wear[0] if warpaint_wear else""


    for group in groupedlist: #group
        if group[0]:
            if item == group[0]:
                group[1] += 1
                break
    else:
        groupedlist += [[item, 1, cost_unit, cost_min, cost_max, warpaint_wear]]

    item = ['']
    cost_unit = ['']
    cost_min = ['']
    cost_max = ['']
    warpaint_wear = ['']


#sort by item name
groupedlist.sort(key = lambda sublist: sublist[0])

#sort by count
groupedlist.sort(reverse = True, key = lambda sublist: sublist[1])

#sort by cost_min
groupedlist.sort(reverse = True, key = lambda sublist: (float(sublist[3]))if sublist[3] else 0 )

#sort by cost_unit
groupedlist.sort(key = lambda sublist: sublist[2])

output = open("tf2_inv_output.txt","a")
for group in groupedlist:

    
    output.write(group[3].ljust(7))#cost_min
    output.write(group[2].ljust(5))#cost_unit

    output.write("x   ")

    output.write(str(group[1]).ljust(6))#count
    output.write(group[0].ljust(30))#item

    output.write("\n")
    
output.close()
print("\ndone")
print("sanity check, total inventory slots used:", count)
