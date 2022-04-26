# import math
# filepath='sampleTrace.txt'
# global number_of_set,number_of_ways,cache_line_size,byte_offset,index,tag,  type_and_addr, tag_in_binary, index_in_binary
# global number_of_cache_reads, number_of_cache_writes,set_and_way,hit,miss,evict,writeback,access_type 

# def get_input():
#     print("CACHE PARAMETERS")
#     number_of_set=int(input("Number of sets :"))
#     number_of_ways=int(input("Number of ways (max=8) :"))
#     cache_line_size=int(input("Cache line size (32 bytes to 128 bytes):"))
#     return number_of_set,number_of_ways,cache_line_size

# def get_bits():
#     byte_offset= int(math.log2(cache_line_size))
#     index=int(math.log2(number_of_set))
#     tag=int(32-(index+byte_offset))
#     return byte_offset,index,tag

# def set_and_ways():
#     set_and_way=[]
#     for sets in range(number_of_set):
#         a=[]
#         ways=[[0 for j in range(4)]for i in range(number_of_ways)]
#         a.append(ways)
#         set_and_way.append(a)
#     return set_and_way

# def get_type_and_addr():
#      with open(filepath) as f:
#                     lines = f.read().splitlines()
#                     #lines = [line.rstrip('/n') for line in open(filepath)]
#                     type_and_addr=[]
#                     tag_in_binary=[]
#                     index_in_binary=[]
#                     access_type=[]
#                     i=0
#                     for line in lines:
#                          type_and_addr.append(line.split(" "))                              
#                          if(len(type_and_addr[i][1])<9):                                 
#                              access_type.append(type_and_addr[i][0])
#                              type_and_addr[i][1]= int(type_and_addr[i][1],16)                     
#                              addr_in_binary = f'{type_and_addr[i][1]:0>32b}'                         
#                              type_and_addr[i][1]= addr_in_binary
#                              tag_in_binary.append((int(addr_in_binary,2) >>(index+byte_offset)))
#                              addr_in_binary= addr_in_binary[tag : tag+index] 
#                              index_in_binary.append((int(addr_in_binary,2)))
#                          i+=1
#      f.close()
#      print("\n###################required output###############\n")
#      print("\n")
#      print(type_and_addr)
#      print("\n")
#      print(index_in_binary)
#      print("\n")
#      print(tag_in_binary)
#      print("\n")
#      print(access_type)
#      print("\n")
#      return index_in_binary,tag_in_binary, access_type

# def check_hit_or_miss():
#     i=0
#     hit=0
#     miss=0
#     evict=0
#     writeback=0
#     number_of_cache_reads=0
#     number_of_cache_writes=0
#     for index in index_in_binary:
#         if int(access_type[i])== 0:
#             number_of_cache_reads+=1
#         else:
#             number_of_cache_writes+=1
#         for k in set_and_way[index]:
#             for j in k:
#                 if j[0]==0:                         # slot is empty
#                     j[0]=1                          # valid bit 1
#                     if int(access_type[i])== 1:   # Read or write
#                         j[1]=1                      # if write then dirty bit 1
#                     j[2]=1                          # LRU bit 1
#                     j[3]=tag_in_binary[i]           # write tagbit
#                     miss+=1                            #  miss count
#                     break
#                 elif j[0]==1:                  # slot is occupied
#                     if j[3]==tag_in_binary[i]:          # check tagbit
#                         if int(access_type[i])== 1:   # Read or write
#                             j[1]=1                      # if write then dirty bit 1
#                         j[2]=1                          # LRU bit 1
#                         hit+=1                             # hit count
#                         break
#             else:                # loop fell through without finding any empty or valid match slot 
#                 for k in set_and_way[index]:
#                     for j in k:
#                         if j[2]==0:                    # check LRU bit=0 for line evict
#                             if j[1]==1:                # check for dirty bit
#                                 writeback+=1               # dirty bit=1 so writeback
#                             j[2]=1                     # Set LRU bit 1
#                             j[3]=tag_in_binary[i]      # write tagbit
#                             if int(access_type[i])== 1:   # Read or write
#                                 j[1]=1                 # if write then dirty bit 1
#                             else:
#                                 j[1]=0                 # if read then dirty bit 0
#                             miss+=1                       # miss count
#                             evict+=1                      # evict count
#                             break
#                     else:                               # loop fell through without finding any LRU bit 0
#                         x=0
#                         for k in set_and_way[index]:
#                             for j in k:
#                                 j[2]=0                          # rest all LRU to 0                     
#                                 if x==0:
#                                     j[2]=1                     # LRU bit 1 for pos 1st 
#                                     if j[1]==1:                # check for dirty bit
#                                         writeback+=1               # dirty bit=1 so writeback
#                                     j[3]=tag_in_binary[i]
#                                     if int(access_type[i])== 1:   # Read or write
#                                         j[1]=1                 # if write then dirty bit 1
#                                     else:
#                                         j[1]=0                 # if read then dirty bit 0
#                                     miss+=1                                     # miss count
#                                     evict+=1                                    # evict count
#                                 x+=1
#         i+=1
#     return hit,miss,evict,writeback,number_of_cache_reads,number_of_cache_writes

# def output():
#     print('\nCACHE STATISTICS')
#     print('Total number of cache accesses :',number_of_cache_reads+number_of_cache_writes)
#     print('Number of cache reads :',number_of_cache_reads)
#     print('Number of cache writes :',number_of_cache_writes)
#     print('Number of cache hits :',hit)
#     print('Number of cache misses :',miss)
#     print('Cache hit ratio :',(hit/(number_of_cache_reads+number_of_cache_writes))*100,'%')
#     print('Cache miss ratio :',(miss/(number_of_cache_reads+number_of_cache_writes))*100,'%')
#     print('Number of evictions :',evict)
#     print('Number of writebacks :',writeback)

# number_of_set,number_of_ways,cache_line_size=get_input()
# set_and_way=set_and_ways()
# byte_offset,index,tag = get_bits()
# index_in_binary,tag_in_binary,access_type= get_type_and_addr()
# hit,miss,evict,writeback,number_of_cache_reads,number_of_cache_writes=check_hit_or_miss()
# print("\n required data array\n")
# print(set_and_way)
# output()
