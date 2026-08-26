import math

hospitals = [
    ["Hospital A", 1, 2],
    ["Hospital B", 10, 12],
    ["Hospital C", 3, 4],
    ["Hospital D", 20, 25],
    ["Hospital E", 5, 6]
]

min_distance = float("inf")
hospital1 = ""
hospital2 = ""


for i in range(len(hospitals)):

    for j in range(i + 1, len(hospitals)):

        x1 = hospitals[i][1]
        y1 = hospitals[i][2]

        x2 = hospitals[j][1]
        y2 = hospitals[j][2]

        distance = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        if distance < min_distance:
            min_distance = distance

            hospital1 = hospitals[i][0]
            hospital2 = hospitals[j][0]


print("Closest Hospitals:")
print(hospital1)
print(hospital2)

print("Distance:", min_distance)