file_reader = open("list.txt","r")
#create a new file object for file writing
file_writer = open("list.txt","w")
file_writer2 = open("list.txt","w")

print(file_reader.read())

for each_line in file_reader:
    #splitting the data by comma
    datum = each_line.split(",") #datum[0]=john, datum[1]= 20
    print("{:s}\t:{:s}".format(datum[0],datum[1]))
    #print the formatted data to the file which is pointed by file_writer
    print("{:s}\t:{:s}".format(datum[0],datum[1]), file=file_writer)
    #Second way of writing text to file
    file_writer2.write("{:s}\t:{:s}".format(datum[0],datum[1]))
    #print(each_line)

file_reader.close()
file_writer.close()
file_writer2.close()