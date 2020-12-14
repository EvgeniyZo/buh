
import itertools,csv

#86849,855,86,22262,98565,3290,946,36948,6148,18510
#7936,23600,4024,105812,28872,84
d = [86849,16135,88565,3290,567,48000,10000,36948]#
c = [27936,2460,7417,149176,28872,4359,6148,684,13000]#


#28042,10600,10153,30,557,4359,30737
other = [68000,63200,607,6600,4153,595,34737]#

other2 = d + c + other
print(len(other2))

#print(len(other2)**2)


def find_equal_sums(d,c,other):
    solved_list = []
    ds = sum(d)
    cs = sum(c)
    a = itertools.product([0,1],repeat=len(other))
    for i in a:
        ds2=ds
        cs2=cs
        for n,j in enumerate(i):
            if j ==0:
                ds2+=other[n]
            else:
                cs2+=other[n]
        if ds2 == cs2:
            solved_list.append(list(i))
    
    return solved_list

test_d = [1337,451]
test_c = [472,3754]
test_other = [212,214,60,2500,3000,500,2000,250,200,50,]

print(find_equal_sums(d,c,other))

print('-'*50)

arr = []

ad = open('ass_data','r')

for i in ad.readlines():
    arr.append(int(i.strip('\n')))
print(arr)
print()
def list_to_file(list,file):
    writer = csv.writer(file, delimiter=',', quotechar='|')
    for row in list:
        writer.writerow(row)

fes = find_equal_sums([],[],arr)
list_to_file(fes,open('belevich','w'))

