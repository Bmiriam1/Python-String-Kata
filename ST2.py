def Add(num):
    if not num:
        return 0
    
    if num.startswith("//"):
        delimeter, num = num[2:].split("\n", 1)
        num = num.replace(delimeter, ",")
        
    if "," not in num:
        return int(num)
    total = sum(int(num) for num in num.replace("\n", ",").split(",") if num)
    
    numbers = [int(n) for n in num.replace("\n", ",").split(",") if n]
    negatives = [ n for n in numbers if n < 0]
     
    if negatives:
      raise ValueError(f"Negatives not allowed:{", ".join(map(str, negatives))}")
    return sum(numbers)


try:
    Add("1,-2,3,-4")
    print("Failed")
except ValueError as e:
    print(e)

if Add("//;\n1;2") == 3:
    print("Test 6 passed")
else:
    print("Failed")

if Add("1\n2,3") == 6:
    print("Test 5 passed")
else:
    print("Failed")

if Add("1,2,3,4") == 10:
    print("Test 4 passed")
else:
    print("Failed")

if Add("1,2") == 3:
    print("Test 3 passed")
else:
    print("Failed")

if Add("1") == 1:
    print("Test 2 passed")
else:
    print("Failed")

if Add("") == 0:
    print("Test 1 passed")
else:
    print("Failed")