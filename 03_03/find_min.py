def find_min(xs):
    min_index = 0
    for i in range(len(xs)):
        if xs[i] < xs[min_index]:
            min_index = i
    return xs[min_index]


xs = [3, 2, 1, 5, 4]
min_value = find_min(xs)
print(f"The minimum value is {min_value}.")



def find_theMin(the_array):
    minimum_index = 0
    for i in range(len(the_array)):
        if the_array[i] < the_array[minimum_index]:
            minimum_index = i
    return the_array[minimum_index]
        
        
the_array = [-1,14,14,29,37,5]
minimum_value = find_theMin(the_array)
print(f"The second minimum value is {minimum_value}.")