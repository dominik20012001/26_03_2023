# import json


# def niepar() -> dict:
#     wsad = []
#     for i in range(21):
#         wsad.append(i)
#     print(wsad)

#     nieparzyte = []
#     parzyste = []
#     for x in wsad:
#         if x % 2 != 0:
#             nieparzyste.append(x)
#         else:
#             parzyste.append(x)
#     slownik = {
#         'nieparzyste': nieparzyste,
#         'parzyste': parzyste
#     }
#     return slownik


# def wielkie_litery(text):
#     return (lambda x: x.upper())(text)
# print(wielkie_litery("polska gurom"))

def dodaj(a, b):
    return (lambda x, y: x + y)(a, b)

print(dodaj(2, 3))
