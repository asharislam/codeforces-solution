# 785A - Anton and Polyhedrons using python by Ashar Islam

n = int(input())
total = 0
dictio ={
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}
for _ in range(n):
    x = input()
    if x in dictio:
        total +=dictio[x]
print(total)



# Another way
# n = int(input())
# total = 0
#
# for _ in range(n):
#     x = input()
#     if x == "Tetrahedron":
#         total += 4
#     elif x == "Cube":
#         total += 6
#     elif x == "Octahedron":
#         total += 8
#     elif x == "Dodecahedron":
#         total += 12
#     elif x == "Icosahedron":
#         total += 20
#
# print(total)



# Another way
# n = int(input())
# total = 0
#
# shapes = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
# faces = [4, 6, 8, 12, 20]
#
# for _ in range(n):
#     x = input()
#     if x in shapes:
#         total += faces[shapes.index(x)]
#
# print(total)
