import math
from geopy.distance import geodesic

city_bank_locations = [
    {"name": 'Uttara Branch', "lat": 23.8728568, "long": 90.3984184},
    {"name": 'City Bank Airport', "lat": 23.8513998, "long": 90.3944536},
    {"name": 'City Bank Nikunja', "lat": 23.8330429, "long": 90.4092871},
    {"name": 'City Bank Beside Uttara Diagnostic', "lat": 23.8679743, "long": 90.3840879},
    {"name": 'City Bank Mirpur 12', "lat": 23.8248293, "long": 90.3551134},
    {"name": 'City Bank Le Meridien', "lat": 23.8271499, "long": 90.4106238},
    {"name": 'City Bank Shaheed Sarani', "lat": 23.8629078, "long": 90.3816318},
    {"name": 'City Bank Narayanganj', "lat": 23.8673789, "long": 90.429412},
    {"name": 'City Bank Pallabi', "lat": 23.8248938, "long": 90.3549467},
    {"name": 'City Bank JFP', "lat": 23.8133169, "long": 90.4147498}
]


def get_second_highest_distance(unsorted_list, sorted_list, current_branch, sorted_name, counter=1):
    index = unsorted_list.index(sorted_list[counter])
    if branch_list[index] not in sorted_name and current_branch != branch_list[index]:
        sorted_name.append(branch_list[index])
        return current_branch, branch_list[index], sorted_name, sorted_list[counter]
    else:
        if (counter + 1) < (len(sorted_list) - 1):
            # -1 for getting last index number
            counter += 1
            return get_second_highest_distance(unsorted_list, sorted_list, current_branch, sorted_name, counter)
        else:
            counter += 1
            index = unsorted_list.index(sorted_list[counter])
            sorted_name.append(branch_list[index])
            return current_branch, branch_list[index], sorted_name, sorted_list[counter]


def calculate_sort_distance(branch_list, distance_metrix):
    current_branch = branch_list[0]
    sorted_name = [branch_list[0]]
    for _ in range(0, len(branch_list) - 1):
        # 2 for two branch in pair, so slast branch can not be count.
        sorted_list = distance_metrix[current_branch].copy()
        sorted_list.sort()
        current, next, sorted_name, meter = get_second_highest_distance(distance_metrix[current_branch], sorted_list,
                                                                        current_branch, sorted_name)
        current_branch = next
        print(f"Form {current} branch to next branch ({next}) branch distance {round(meter / 1000, 3)} km")
    return sorted_name


distance_metrix = {}
branch_list = [item["name"] for item in city_bank_locations]
for branch_data in city_bank_locations:
    distance = 0
    distance_metrix[branch_data["name"]] = []
    data = {}
    data_distance = []
    for path in city_bank_locations:
        distance = geodesic(
            (branch_data["lat"], branch_data["long"]),
            (path["lat"], path["long"])
        ).meters
        data_distance.append(distance)
        distance_metrix[branch_data["name"]].append(distance)
sorted_path = calculate_sort_distance(branch_list, distance_metrix)

print(distance_metrix)
for branch_name in sorted_path:
    print(branch_name, " >> ", end=" ")
print("Uttara Branch")
print(f"distance between Uttara and {sorted_path[-1]} is {round(distance_metrix[sorted_path[-1]][0] / 1000, 3)} Km")

distance = geodesic(
    (city_bank_locations[0]["lat"], city_bank_locations[0]["long"]),
    (city_bank_locations[7]["lat"], city_bank_locations[7]["long"])
).kilometers
print(distance)
