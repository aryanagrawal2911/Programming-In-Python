ori_price = [4.95, 9.95, 14.95, 19.95, 24.95]

dis_price = []

for i in ori_price:

    dis_price.append("{:.2f}".format(0.4 * i))

for i in range(len(ori_price)):

    print(f"Original Price : {ori_price[i]}\tDiscounted Price : {dis_price[i]}")