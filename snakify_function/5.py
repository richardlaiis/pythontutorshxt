def reverse_seq():
    num = int(input())
    if num == 0:
        print(num)
    else:    
        reverse_seq()
        print(num)

reverse_seq()
