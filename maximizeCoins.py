def maximizeCoins(coins, i = 0, j = 0, count = 0):
	for cell in coins:
		if cell == [i,j]:
			count += 1
	if len(coins) == 1:
		return count

	sums = [0]*len(coins)
	for ii in range(len(coins)):
		for elem in coins:
			if coins[ii][0] <= elem[0] and coins[ii][1] <= elem[1]:
				sums[ii] += 1
	if [i, j] in coins:
		next_cell = coins[sums.index(sorted(sums)[-2])]
	else:
		next_cell = coins[sums.index(sorted(sums)[-1])]
	next_cell_coins = []

	for cell in coins:
		if cell[0] >= next_cell[0] and cell[1] >= next_cell[1]:
			next_cell_coins.append(cell)


	count = maximizeCoins(next_cell_coins, i = next_cell[0], j = next_cell[1], count = count)

	return count

coins = [[8,3], 
 [6,7], 
 [1,5], 
 [10,4], 
 [6,2], 
 [5,1], 
 [8,0], 
 [10,7], 
 [8,6], 
 [0,10]]
print maximizeCoins(coins)

# import numpy as np
# a = np.zeros((11, 11))
# for i in coins:
# 	a[i[0], i[1]] += 1
# print a