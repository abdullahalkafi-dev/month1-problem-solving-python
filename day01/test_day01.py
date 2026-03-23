def fizzbuzz_value(n:int):
    if not (isinstance(n, int)):
        raise TypeError(f"Expected int")

    if n < 0:
        raise Exception("Value must be larger  than 0")
    if n >100:
        raise Exception("Number can not be larger than 100")
    
    print(n)


fizzbuzz_value("22")
