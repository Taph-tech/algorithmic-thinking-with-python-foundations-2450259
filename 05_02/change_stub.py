def make_change(target_amount):
    pass  # Write your solution here. 
    coin_denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    coin_count = 0  
    values = []
    remaining_amount = target_amount
    for coin in coin_denominations:
        while remaining_amount >= coin:
            remaining_amount -= coin
            values.append(coin)
            coin_count += 1
    return f'Number of coins are {coin_count}, Amount is {target_amount} pence, {values}.'



print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
print(make_change(28)) # 4: 20p + 5p + 2p + 1p
print(make_change(99)) # 6: 50p + 20p + 20p + 5p + 2p + 2p + 1p
