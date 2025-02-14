# 32B	Borze using python by Ashar Islam

# s = list(input())
# k = []
# final = []
#
# while s:
#     if s[0] == ".":
#         m = s.pop(0)
#         k.append(m)
#     elif s[0] == "-":
#         if len(s) >= 1:
#             p = s.pop(0)
#             q = s.pop(0)
#             n = p + q
#             k.append(n)
#         else:
#             k.append(s.pop(0))
#
# for i in k:
#     if i == ".":
#         final.append("0")
#     elif i == "-.":
#         final.append("1")
#     else:
#         final.append("2")
# print("".join(final))


s = list(input())
final = []
i = 0

while i < len(s):
    if s[i] == ".":
        final.append("0")
        i += 1
    elif s[i] == "-":
        if i + 1 < len(s) and s[i + 1] == ".":
            final.append("1")
            i += 2
        elif i + 1 < len(s) and s[i + 1] == "-":
            final.append("2")
            i += 2
        else:
            # Handle invalid input (e.g., a single "-" at the end)
            final.append("2")
            i += 1

print("".join(final))
