def sum_even(num_list:list[int])->int:
    """This take an """
    total =0
    for i in num_list:
        
        if not isinstance(i,int):
            raise TypeError("Only int array allowed")
        if i%2==0:
            total = total +i
        
    return total
        

if __name__== "__main__":
    print(sum_even([2,3,4,5]))