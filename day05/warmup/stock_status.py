def stock_status(qty:int)->str:
    if not isinstance(qty, int):
        raise TypeError("qty data type not allowed")
    if qty < 0:
        raise ValueError("qty must be grater than 0")
    if qty == 0:
        return "OUT_OF_STOCK"
    if qty < 10:
        return "LOW_STOCK"
    return "IN_STOCK"
    
    
if __name__ == "__main__":
    print(stock_status(0))
    print(stock_status(5))
    print(stock_status(10))
    print(stock_status(-1))
    print(stock_status("20"))