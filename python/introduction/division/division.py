if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    div_integer = a // b
    div_float = float(a) // float(b)
    
    print(div_integer, div_float, sep='\n')