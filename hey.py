# a=int(input())
# b=set(map(int,input().split()))
# n=int (input())
# for i in range(n):
#     operation=input().split()
#     cmd_type=operation[0]
#     if cmd_type=="pop":
#         if b:
#             b.pop()
#     elif cmd_type=="remove":
#         ele=int(operation[1])
#         if ele in b:
#             b.remove(ele)
#     elif cmd_type=="discard":
#         ele=int(operation[1])
#         b.discard(ele)

# print(sum(b),b)


b = "appple"
z = ""
skip = False

for i in range(len(b)):
    if skip:
        # Skip the current character if flagged
        skip = False
        continue
    
    # Check if the next character is the same as the current
    if i < len(b) - 1 and b[i] == b[i + 1] :
        # Skip both current and next character
        skip = True
    else:
        # Add non-repeated character to the result
        z += b[i]

print(z)
