def getItemLook(body, num, name, addr):
    item_container = body.container()
    col1, col2 = item_container.columns([1,9])
    col1.write(num)
    row1 = col2.container()
    row2 = col2.container()
    row1.write(name)
    row2.write(addr)

    return item_container

