product = []
while True:
    name = input('請輸入商品名稱：')
    if name =='q':
        break
    price = input('請輸入價格：')
    if price =='q':
        break
    p = []
    p.append(name) #將名字加入小清單
    p.append(price) #將價格加入小清單
    #上述三行可改成 p = [name, price]
    product.append(p) #將名字及價格的小清單加入大清單
    #上述四行可以改成product.append([name, price]) 
print(product)

for p in product: #把清單中的東西一個一個拿出來
    print(p)
    print(p[0],'的價格是', p[1])