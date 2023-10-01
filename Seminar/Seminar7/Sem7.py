# transformation = lambda x: x
#
# values =[1, 23, 42, "adsf"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print ("ok")
# else:
#     print ("fall")

# def find_fartherst_orbits(orbits):
#     condition = lambda data: (data[0] != data[1]) * data[0] * data[1]
#     square_orbits = list(map(condition, orbits))
#     return orbits[square_orbits.index(max(square_orbits))]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
# find_fartherst_orbits(orbits)
# print(find_fartherst_orbits(orbits))


# # Task 51
#
# values = [0, 2, 10, 6]
# def same_by(characteristics,objects ):
#     return len(set(map(characteristics, objects))) in (0,1)
#
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")


