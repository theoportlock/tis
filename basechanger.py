def convert_to_base(decimal_number, base):
    remainder_stack = []
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(2**remainder_stack.pop())

    return new_digits

a = 2152183459839873
print(a)
print(bin(a))
#print([bin(i) for i in convert_to_base(a, 66)])

new = []
count = 0
out = 0
for j in convert_to_base(a, 66):
    count += 1 
    out += j
    if count => 3:
        new.append(out)
        count = 0

print(new)
