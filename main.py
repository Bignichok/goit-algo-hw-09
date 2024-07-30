coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(coins, sum):
    result = {}
    for coin in coins:
        if sum >= coin:
            coins_amount = sum // coin
            result[coin] = coins_amount
            sum = sum - coin * coins_amount

    return result

def find_min_coins(coins, sum):
    result = {}
    min_coins_needed = [float('inf')] * (sum + 1)
    min_coins_needed[0] = 0
    coin_used = [-1] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin >= 0 and min_coins_needed[i-coin] + 1 < min_coins_needed[i]:
                min_coins_needed[i] = min_coins_needed[i - coin] + 1
                coin_used[i] = coin

    if min_coins_needed[sum] == float('inf'):
        return result
    
    while sum > 0:
        coin = coin_used[sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        sum -= coin

    return result


print(find_coins_greedy(coins, 113))
print(find_min_coins(coins,1765123)) 
