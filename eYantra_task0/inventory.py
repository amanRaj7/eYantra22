for _ in range(int(input())):
    item = {}
    for __ in range(int(input())):
        item_name, item_quant = list(input().split())
        item_quant = int(item_quant)
        item[item_name] = item_quant
    for ___ in range(int(input())):
        key, item_name, item_quant = list(input().split())
        item_quant = int(item_quant)
        if (key == "ADD"):
            if(item_name in item):
                item[item_name] = item[item_name]+item_quant
                print("UPDATED Item {}".format(item_name))
            else:
                item[item_name] = item_quant
                print("ADDED Item {}".format(item_name))
        elif (key == "DELETE"):
            if (item_name in item) and (item_quant<=item[item_name]):
                item[item_name] = item[item_name] - item_quant
                print("DELETED Item {}".format(item_name))
            elif (item_name in item):
                print("Item {} could not be DELETED".format(item_name))
            else:
                print("Item {} does not exist".format(item_name))
            
    print("Total Items in Inventory: {}".format(sum(item.values())))