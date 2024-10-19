balance = 1000
for i in range(0,5):
    balance *= 1.05 
print(balance)

balance_true = (1000.00 * 1.05 * 1.05 * 1.05
                   * 1.05 * 1.05)
print(balance_true)