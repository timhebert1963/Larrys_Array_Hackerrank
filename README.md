Larrys_Array_Hackerrank - Can an array of numbers be sorted rotating 3 consecutive indeces

**** Formula for determining solvability ****

There is a method to check whether any given array is solvable. Consider the following array:
[12, 1, 2, 10, 7, 11, 4, 14, 5, 9, 15, 8, 13, 6, 3] length of array is 15

An inversion is when an index value "precedes and is greater than" other index value(s). 
i.e. A sorted array has zero inversions. 

For example, in the above array, number 12 is index 0, then there will be 11 inversions from this index, 
as numbers 1-11 come after it. To explain it another way, an inversion is a pair of indeces (a,b) such that 
'a' appears before 'b', but a>b. 

