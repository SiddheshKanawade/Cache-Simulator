import tagarray
import dataarray

tagarrayObj = tagarray.TagArray
dataarrayObj = dataarray.DataArray

class HitMiss:
    @staticmethod
    def lru(tagAddrarr, readwritearr, indexarr, offsetarr, ways, sets, n_block, fileaddr):
        # n_block size is 2**n
        conflict_miss = 0
        compulsory_miss = 0
        capacity_miss = 0
        read_miss = 0
        write_miss = 0
        dirty_blocks_evicted = 0
        unique_tags=[]
        uniqueaddr = []
        tagStore = tagarrayObj.tagArray(sets)
        dataStore = dataarrayObj.dataarray(sets, ways, n_block)


        # iterate over tagStore
        i = 0
        
        for checkIndex in indexarr:
            tagllist = tagStore[checkIndex]
            datalist = dataStore[checkIndex]
            searchArr = tagllist.search(tagAddrarr[i])
            offset = offsetarr[i]
            flag = 0

            if fileaddr[i] not in uniqueaddr:
                compulsory_miss += 1
                if(readwritearr[i] == 0):
                    read_miss += 1
                else:
                    write_miss += 1

                flag = 1
                uniqueaddr.append(fileaddr[i])
            
            # not found the tagAddr
            if(searchArr[1] == -1):
                
                # capacity not full
                if(tagllist.maxCapacity() < ways):
                    
                    tagllist.push(tagAddrarr[i])
                    datalist.head.data[offset] = 1
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
                    # reach to specific tag in datalist
                
                # capacity is full
                else:
                    if(flag == 0):
                        # not a compulsory miss
                        capacity_miss += 1
                        if(readwritearr[i] == 0):
                            read_miss += 1
                        else:
                            write_miss += 1
                    tagllist.pop()
                    tagllist.push(tagAddrarr[i])
                    pusharr = [0]*n_block
                    pusharr[offset] = 1
                    datalist.pop()
                    datalist.push(pusharr)
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
            
            else:
                # found the tagAddr
                # print("tagadd not present : ", searchArr[1])
                tagllist.replaceNode(searchArr)
                datalist.replaceNode(searchArr)

                # 
                if(datalist.head.data[offset] == 0):
                    if(flag == 0):
                    # not a compulsory miss)
                        conflict_miss += 1
                        if(readwritearr[i] == 0):
                                read_miss += 1
                        else:
                            write_miss += 1
                        
                    datalist.head.data[offset] = 1
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
    
            i = i + 1
            
        cache_miss = compulsory_miss + capacity_miss + conflict_miss
        return [cache_miss, compulsory_miss, capacity_miss, conflict_miss, read_miss, write_miss, dirty_blocks_evicted]

# tagaddr checkindex i

    @staticmethod
    def fifo(tagAddrarr, readwritearr, indexarr, offsetarr, ways, sets, n_block, fileaddr):
        # n_block size is 2**n
        conflict_miss = 0
        compulsory_miss = 0
        capacity_miss = 0
        read_miss = 0
        write_miss = 0
        dirty_blocks_evicted = 0
        unique_tags=[]
        uniqueaddr = []
        tagStore = tagarrayObj.tagArray(sets)
        dataStore = dataarrayObj.dataarray(sets, ways, n_block)


        # iterate over tagStore
        i = 0
        
        for checkIndex in indexarr:
            tagllist = tagStore[checkIndex]
            datalist = dataStore[checkIndex]
            searchArr = tagllist.search(tagAddrarr[i])
            offset = offsetarr[i]
            flag = 0

            if fileaddr[i] not in uniqueaddr:
                compulsory_miss += 1
                if(readwritearr[i] == 0):
                    read_miss += 1
                else:
                    write_miss += 1

                flag = 1
                uniqueaddr.append(fileaddr[i])
            
            # not found the tagAddr
            if(searchArr[1] == -1):
                
                # capacity not full
                if(tagllist.maxCapacity() < ways):
                    
                    tagllist.push(tagAddrarr[i])
                    datalist.head.data[offset] = 1
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
                    # reach to specific tag in datalist
                
                # capacity is full
                else:
                    if(flag == 0):
                        # not a compulsory miss
                        capacity_miss += 1
                        if(readwritearr[i] == 0):
                            read_miss += 1
                        else:
                            write_miss += 1
                    tagllist.pop()
                    tagllist.push(tagAddrarr[i])
                    pusharr = [0]*n_block
                    pusharr[offset] = 1
                    datalist.pop()
                    datalist.push(pusharr)
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
            
            else:
                if(datalist.head.data[offset] == 0):
                    if(flag == 0):
                    # not a compulsory miss)
                        conflict_miss += 1
                        if(readwritearr[i] == 0):
                                read_miss += 1
                        else:
                            write_miss += 1
                        
                    datalist.head.data[offset] = 1
                    if(readwritearr[i]==1 and tagAddrarr[i] not in unique_tags):
                        dirty_blocks_evicted+=1
                        unique_tags.append(tagAddrarr[i])
    
            i = i + 1
            
        cache_miss = compulsory_miss + capacity_miss + conflict_miss
        return [cache_miss, compulsory_miss, capacity_miss, conflict_miss, read_miss, write_miss, dirty_blocks_evicted]