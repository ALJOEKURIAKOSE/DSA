stokckprice = {}
with open("stockprice.csv","r") as file:
    for line in file:
        tokens = line.split(',')
        date = tokens[0]
        price = tokens[1]
        stokckprice[date] = price
    print(stokckprice['mar 2'])