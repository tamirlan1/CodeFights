def swapLexOrder(string, pairs):
    elems = list(string)
    connected = []
    for pair in pairs:
        current_con_ind = -1
        to_delete_ind = []
        for j in range(len(connected)):
            if pair[0] in connected[j] or pair[1] in connected[j]:
                if current_con_ind == -1:
                    connected[j].extend(pair)
                    connected[j] = sorted(list(set(connected[j])))
                    current_con_ind = j
                else:
                    connected[current_con_ind].extend(connected[j])
                    to_delete_ind.append(j)
                    connected[current_con_ind].extend(pair)
                    connected[current_con_ind] = sorted(list(set(connected[current_con_ind])))

        for d in to_delete_ind:
        	del connected[d]

        if current_con_ind == -1:
            connected.append(sorted(pair))
    print connected

    for indeces in connected:
        substring = []
        for index in indeces:
            substring.append(string[index-1])
        substring = sorted(substring, reverse=True)
        for i in range(len(indeces)):
            elems[indeces[i]-1] = substring[i]
    return ''.join(elems)



# string = "abdc"
# pairs = [[1, 4], [3, 4]]
# string = 'acxrabdz'
# pairs = [[1,3], 
#  [6,8], 
#  [3,8], 
#  [2,7]]
# string = 'dznsxamwoj'
# pairs = [[1,2], 
#  [3,4], 
#  [6,5], 
#  [8,10]]
# string = 'lvvyfrbhgiyexoirhunnuejzhesylojwbyatfkrv'
# pairs = [[13,23], 
#  [13,28], 
#  [15,20], 
#  [24,29], 
#  [6,7], 
#  [3,4], 
#  [21,30], 
#  [2,13], 
#  [12,15], 
#  [19,23], 
#  [10,19], 
#  [13,14], 
#  [6,16], 
#  [17,25], 
#  [6,21], 
#  [17,26], 
#  [5,6], 
#  [12,24]]
string = 'fixmfbhyutghwbyezkveyameoamqoi'
pairs = [[8,5], 
 [10,8], 
 [4,18], 
 [20,12], 
 [5,2], 
 [17,2], 
 [13,25], 
 [29,12], 
 [22,2], 
 [17,11]]
# string = ''
# pairs = 
print swapLexOrder(string, pairs)# = "dbca"
# fzxmybhtuigOwbyefkvHyameoamqei
