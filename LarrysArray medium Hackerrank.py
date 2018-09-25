####  Hankerrank documentation for Larry's Array ##########################################################
#
# Larry has been given a permutation of a sequence of natural numbers incrementing from 1 as an array. 
# He must determine whether the array can be sorted using the following operation any number of times:
#
# Choose any 3 consecutive indices and rotate their elements in such a way that ABC -> BCA -> CAB -> ABC.
#
# For example, if A = {1,6,5,2,4,3}:
#
# A              rotate 
# [1,6,5,2,4,3]  [6,5,2]
# [1,5,2,6,4,3]  [5,2,6]
# [1,2,6,5,4,3]  [5,4,3]
# [1,2,6,3,5,4]  [6,3,5]
# [1,2,3,5,6,4]  [5,6,4]
# [1,2,3,4,5,6]
#
# YES
#
#####  Continued Hackerrank documentaion  #################################################################
#
# On a new line for each test case, print YES if A array can be fully sorted. Otherwise, print NO.
#
# Function Description
#
# Complete the larrysArray function. It must return a string, either YES or NO.
#
# larrysArray has the following parameter(s):
# A: an array of integers
#
# Input Format
# - The first line contains an integer 't', the number of test cases.
# - The next 't' pairs of lines are as follows:
# - The first line contains an integer 'n', the length of 'A'.
# - The next line contains 'n' space-separated integers A[i].
#
# Constraints
# 1 <= 't' <= 10
# 3 <= 'n' <= 1000
# 1 <= A[i] <= 'n'
# A'sorted' = integers that increment by 1 from 1 to 'n'
#
# Output Format
# For each test case, print YES if 'A' can be fully sorted. Otherwise, print NO
#
#####  Continued Hackerrank documentaion  #################################################################
#
# Sample Input
# 3
# 3
# 3 1 2
# 4
# 1 3 4 2
# 5
# 1 2 3 5 4
#
# Sample Output
# YES
# YES
# NO
#
# Explanation
# In the explanation below, the subscript of 'A' denotes the number of operations performed.
#
# Test Case 0:
# A0 = {3,1,2} -> rotate(3,1,2) -> A1 = {1,2,3}
# 'A' is now sorted, so print YES on a new line.
#
# Test Case 1:
# A0 = {1,3,4,2} -> rotate(3,4,2) -> A1 = {1,4,2,3}
# A1 = {1,4,2,3} -> rotate(4,2,3) -> A1 = {1,2,3,4}
# 'A' is now sorted, so print YES on a new line.
#
# Test Case 2:
# No sequence of rotations will result in a sorted 'A'. Thus, we print NO on a new line.
#
# **** End of Hackerrank documentation ****
#
###########################################################################################################
#
# **** Formula for determining solvability ****
#
# There is a method to check whether any given array is solvable. Consider the following array:
# [12, 1, 2, 10, 7, 11, 4, 14, 5, 9, 15, 8, 13, 6, 3] length of array is 15
#
# An inversion is when an index value "precedes and is greater than" other index value(s). 
# i.e. A sorted array has zero inversions. 
#
# For example, in the above array, number 12 is index 0, then there will be 11 inversions from this index, 
# as numbers 1-11 come after it. To explain it another way, an inversion is a pair of indeces (a,b) such that 
# 'a' appears before 'b', but a>b. 
#
# Count the number of inversions in the array. For example, on the above array:
# the 12 gives us 11 inversions
# the  1 gives us  0 inversions
# the 10 gives us  8 inversions
# the  2 gives us  0 inversions
# the  7 gives us  4 inversions
# the 11 gives us  6 inversions
# the  4 gives us  1 inversion
# the 14 gives us  6 inversions
# the  5 gives us  1 inversion
# the  9 gives us  3 inversions
# the 15 gives us  4 inversions
# the  8 gives us  2 inversions
# the 13 gives us  2 inversions
# the  6 gives us  1 inversion
# ------------------------------
#                 49 inversions
#
# The formula (considering specified operations in Larry's Array doc):
#   a. if #inversions is even the array CAN    be sorted.
#   b. if #inversions is odd  the array CANNOT be sorted.
#
# That gives us this formula for determining solvability:
# number_of_inversions % 2 == 0
#
###########################################################################################################

def createSortedArray(A):

    # return a sorted array with the same items of A array
    B = list(map(int, A))
    B.sort()
    return B

def countInversions(num, B):

    # B array is sorted.
    # Count the number of inversions for num against array B.
    # An inversion is when num is greater than a number(s) in array B. 
    count = 0
    i = 0
    while i < len(B) and num > B[i]:
        count += 1
        i += 1

    return count

def isSortable(num):

    # if value of num is an even number return "YES"
    # else return "NO"
    if num % 2 == 0:
        return "YES"
    else:
        return "NO"

def larrysArray(A):

    # check if A array already sorted.
    B = createSortedArray(A)  # returns a sorted array with the same items of A array
    if A == B:
        return("YES")

    N = len(A)
    inversions = 0     # keep count of total number of inversions.

    for i in range(N-1):
        B = createSortedArray(A[i+1:])          # returns sorted array.
        inversions += countInversions(A[i], B)  # returns number of inversions.

    return(isSortable(inversions))  # returns "YES" or "NO"

def main():
    T = int(input("Enter number of Test Cases:  "))

    for _ in range(T):
        A = list(map(int, input("Enter string of integers  ").split()))
        result = larrysArray(A)
        print(result)

if __name__  == '__main__':
    main()