import numpy as np
from numpy import pi

distance = [10,15,17,26]
time = [0.3, 0.47, 0.55, 1.20]

np_distance = np.array(distance)
np_time = np.array(time)

np_speed = np_distance/np_time
print(np_speed)


# Classes and attributes of ndarray
# Shape, size, ndim, and dtype are attributes of ndarray
np_city = np.array(["NYC", "LA", "MIami", "Houstan"])
print(np_city.ndim)   # ndim is used to check the dimenision of array
print(np_city.shape)

print("--------------------------")
np_city_with_states = np.array([["NYC", "LA", "MIami", "Houstan"], ["NY", "CA", "USA", "AZ"]])
print(np_city_with_states.ndim)
print(np_city_with_states.shape)
print(np_city_with_states.dtype)


print("--------------------------")
# Basic operation on an array
first_trail_cyclist = [10, 15, 17, 26]
second_trail_cyclist = [12, 11, 21, 24]

np_first_trail_cyclist = np.array(first_trail_cyclist)
np_second_trail_cyclist = np.array(second_trail_cyclist)

total_distance = np_first_trail_cyclist + np_second_trail_cyclist
print(total_distance)


print("--------------------------")
# Access the array elements 
cyclist_trails = np.array([[10, 15, 17, 26], [12, 11, 21, 24]])
first_trial = cyclist_trails[0][0::2]
print(first_trial)
second_trial = cyclist_trails[1]
print(second_trial)

first_cyclist_all_trials = cyclist_trails[:,0] 
print(first_cyclist_all_trials)
print(cyclist_trails.shape)

two_cyclist_trials_data = cyclist_trails[:,1:3]        # [row, column]
print(two_cyclist_trials_data)


print("--------------------------")
# Accessing array elements: iterations 
for i in cyclist_trails:
    print(i)

for j in two_cyclist_trials_data:
    print(j)


print("--------------------------")
# Indexing with boolean arrays
test_score = np.array([[83,71,57,63], [54,68,81,45]])
pass_score = test_score > 60
print(pass_score)
print(test_score[pass_score])

print(pass_score & ~pass_score)


print("--------------------------")
# Copy and views
print(np_city)
new_np_city = np_city        # Assigned data
print(new_np_city)
print(new_np_city is np_city)

print("--------------------------")
# view or shallow copy
view_np_city = new_np_city.view()    
print(view_np_city)
print(len(view_np_city))
view_np_city[3] = "LPU"
print(view_np_city)
print(new_np_city)
print(view_np_city is new_np_city)

print("--------------------------")
# Deep copy
copy_np_city = new_np_city.copy() 
print(copy_np_city)
print(copy_np_city is new_np_city)
copy_np_city[2] = "CU"
print(copy_np_city)
print(new_np_city)


print("--------------------------")
# Universal function
# sqrt, cos, floor, exp
print(np_distance)
np_sqrt = np.sqrt(np_distance)
print(np_sqrt)

print(np.cos(0))
print(np.sin(np.pi/2))
print(np.sin(pi/2))
print(np.cos(pi))
print(np.floor([1.5,2.6,3.6]))
print(np.exp([0,1,5]))


print("--------------------------")
# Shape Manipulation 
# ravel, split, flatten, resize, reshape, stack

print(cyclist_trails)
new_oneD_array = cyclist_trails.ravel()    # ravel,flatten -> both will creates 1D array and ravel changes original array but flatten creates only copy of original array
print(new_oneD_array)
print(new_oneD_array.ndim)

print(new_oneD_array.reshape(4,2))    # array reshape
print(np.hsplit(new_oneD_array, 4))   # array split

print(np.hstack((new_oneD_array, new_oneD_array)))   # array stack -> combine two array

