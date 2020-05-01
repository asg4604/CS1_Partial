import quick_sort
import time

def sort_list(lst):
    return quick_sort.quick_sort(lst)

def median(lst):
    lst = sort_list(lst)
    if len(lst) == 1:
        return lst[0]

    if len(lst) % 2 == 1:
        return lst[(len(lst)) // 2]
    else:
        index_1 = len(lst) // 2
        index_2 = index_1 - 1
        return (lst[index_1] + lst[index_2]) / 2

def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n

def sum_distances(location_list):
    new_store_location = median(location_list)
    acc = 0
    for location in location_list:
        acc += absolute_value(location - new_store_location)

    return acc

def get_values_from_file(filename):
    location_names = []
    locations = []
    for line in open(filename):
        line = line.strip()
        line_pieces = line.split(" ")
        location_names.append(line_pieces[0])
        locations.append(int(line_pieces[1]))
    return (location_names, locations)

def main():
    start_time, end_time = 0
    filename = input("Enter data file: ")
    (location_names, locations) = get_values_from_file(filename)  # Reads the file
    start_time = time.time()

    optimum_store_location = median(locations)
    distance_sum = sum_distances(locations)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Optimum store location:", optimum_store_location)  # Prints the location
    print("Sum of distances to new store:", distance_sum)
    print("elapsed time:", elapsed_time)
