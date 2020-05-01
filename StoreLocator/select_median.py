import time
def median(lst):
    if len(lst) == 1:
        return lst[0]

    if len(lst) % 2 == 1:
        return quick_select(lst, len(lst) // 2)
    else:
        index_1 = len(lst) // 2
        index_2 = index_1 - 1
        return (quick_select(lst, index_1) + quick_select(lst, index_2)) / 2

def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n

def quick_select( aList, k):
    if len(aList) > 0:
        pivot = aList[len(aList) // 2]
        smaller_list = []
        larger_list = []
        count = 0
        for element in aList:
            if element < pivot:
                smaller_list.append(element)
            elif element > pivot:
                larger_list.append(element)
            else:
                count += 1
        m = len(smaller_list)
        if k >= m and k < (m + count):
            return pivot
        if m > k:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)

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
    (location_names, locations) = get_values_from_file(filename) #Reads the file
    start_time = time.time()

    optimum_store_location = median(locations)
    distance_sum = sum_distances(locations)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Optimum store location:", optimum_store_location) #Prints the location
    print("Sum of distances to new store:", distance_sum)
    print("elapsed time:", elapsed_time)