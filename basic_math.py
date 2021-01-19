#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""

def get_greatest(number_list):
    greatest_number = number_list[0]
    for x in number_list:
        if x > greatest_number:
            greatest_number = x
        
    return greatest_number


def get_smallest(number_list):
    smallest_number = number_list[0]
    for x in number_list:
        if x < smallest_number:
            smallest_number = x
        
    return smallest_number


def get_mean(number_list):
    sum = 0
    for x in number_list:
        sum += x
    
    mean = sum/len(number_list)
    return mean


def get_median(number_list):
    median = -1
    number_list.sort()
    length = len(number_list)
    if length % 2 ==0:
        mid1 = number_list[int(length/2)-1]
        mid2 = number_list[int(length/2)]
        median = (mid1+mid2)/2
    else:
        median = number_list[int(length/2)]

    return median

