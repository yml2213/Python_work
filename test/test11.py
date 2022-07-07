fruits = ["apple", "banana", "cherry"]
ckArr = ['13754650804&tpy123456', '15339956683&123456']
for ck in ckArr:
    # print(ck)
    ck = ck.split("&")
    print(ck[0])
    print(ck[1])
    start()
