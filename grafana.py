from subprocess import call
import os
import sys
call(["echo","Kundjanasith Thonglek"])

file = open(sys.argv[1], "r") 

lines = []
for line in file:
    lines.append(line)

blockManagerInfo_list = []
memoryStore_list = []

for line in lines:
    l = line.split(" ")
    if l[3]=="MemoryStore:":
        memoryStore_list.append(l)
    if l[3]=="BlockManagerInfo:":
        blockManagerInfo_list.append(l)

def MB2KB(x):
    res = 0
    if x[-2:]=="MB":
        res = float(x[:-2])*1000
    if x[-2:]=="KB":
        res = float(x[:-2])
    return res

file_b = open(sys.argv[2],"w")
file_b.write("USED,FREE\n")
for b in blockManagerInfo_list:
    if b[4]=="Added": 
        print("Added")
        storage = b[7]
        print("STORAGE : "+storage)
        size = (b[11]+b[12])[:-1]
        print("SIZE : "+size)
        free = (b[14]+b[15])[:-2]
        print("FREE : "+free)
        sql_used = "'insert b_used value="+str(MB2KB(size))+"'"
        sql_free = "'insert b_free value="+str(MB2KB(free))+"'"
        print(sql_used)
        print(sql_free)
	file_b.write(str(MB2KB(size))+","+str(MB2KB(free))+"\n")
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_used)
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_free)
    elif b[4]=="Removed":
        print("Removed")
        storage = b[9]
        print("STORAGE : "+storage)
        if storage == "disk":
            size = (b[11]+b[12])[:-2]
            print("SIZE : "+size)
            sql_used = "'insert b_used value="+str(MB2KB(size))+"'"
            sql_free = "'insert b_free value="+str(MB2KB(free))+"'"
            print(sql_used)
            print(sql_free)
            file_b.write(str(MB2KB(size))+","+str(MB2KB(free))+"\n")
            os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_used)
            os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_free)
        if storage ==  "memory":
            size = (b[11]+b[12])[:-1]
            print("SIZE : "+size)
            free = (b[14]+b[15])[:-2]
            print("FREE : "+free)
            sql_used = "'insert b_used value="+str(MB2KB(size))+"'"
            sql_free = "'insert b_free value="+str(MB2KB(free))+"'"
            print(sql_used)
            print(sql_free)
            file_b.write(str(MB2KB(size))+","+str(MB2KB(free))+"\n")
            os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_used)
            os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_free)
    elif b[4]=="Updated":
        print("Updated")
        storage = b[7]
        print("STORAGE : "+storage)
        current = (b[12]+b[13])[:-1]
        print("CURRENT : "+current)
        original = (b[16]+b[17])[:-2]
        print("ORIGINAL : "+original)
        sql_used = "'insert b_used value="+str(MB2KB(size))+"'"
        sql_free = "'insert b_free value="+str(MB2KB(free))+"'"
        print(sql_used)
        print(sql_free)
        file_b.write(str(MB2KB(size))+","+str(MB2KB(free))+"\n")
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_used)
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_free)
    else:
        print("ERROR")

file_m = open(sys.argv[3],"w")
file_m.write("USED,FREE\n")
for m in memoryStore_list:
    if m[4]=="Block":
        print("Block") 
        size = (m[13]+m[14])[:-1]
        print("SIZE : "+size)
        free = (m[16]+m[17])[:-2]
        print("FREE : "+free)
        sql_used = "'insert m_used value="+str(MB2KB(size))+"'"
        sql_free = "'insert m_free value="+str(MB2KB(free))+"'"
        print(sql_used)
        print(sql_free)
        file_m.write(str(MB2KB(size))+","+str(MB2KB(free))+"\n")
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_used)
        os.system("influx -host 203.185.71.2 -database sparkmon -execute "+sql_free)
    elif m[4]=="MemoryStore":
        print("MemoryStore")
    else:
        print("ERROR")


