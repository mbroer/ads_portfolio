file1 = open('desc.txt', 'r')
Lines = file1.readlines()

x = list()

for line in Lines:
    t = line.split(' ', 1);
    x.append( f'{{"{t[0]}": "{t[1].rstrip()}" }},\n'  )
    #print( f'{{"{t[0]}": "{t[1]}" }},' )

file1 = open('myfile.txt', 'w')
file1.writelines(x)
file1.close()