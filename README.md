Larrys_Array_Hackerrank - Can an array of numbers be sorted rotating 3 consecutive indeces

**** Formula for determining solvability ****

There is a method to check whether any given array is solvable. Consider the following array:
[12, 1, 2, 10, 7, 11, 4, 14, 5, 9, 15, 8, 13, 6, 3] length of array is 15

An inversion is when an index value "precedes and is greater than" other index value(s). 
i.e. A sorted array has zero inversions. 

For example, in the above array, number 12 is index 0, then there will be 11 inversions from this index, 
as numbers 1-11 come after it. To explain it another way, an inversion is a pair of indeces (a,b) such that 
'a' appears before 'b', but a>b. 

Count the number of inversions in the array. For example, on the above array:
the 12 gives us 11 inversions
the  1 gives us  0 inversions
the 10 gives us  8 inversions
the  2 gives us  0 inversions
the  7 gives us  4 inversions
the 11 gives us  6 inversions
the  4 gives us  1 inversion
the 14 gives us  6 inversions
the  5 gives us  1 inversion
the  9 gives us  3 inversions
the 15 gives us  4 inversions
the  8 gives us  2 inversions
the 13 gives us  2 inversions
the  6 gives us  1 inversion
------------------------------
                49 inversions

The formula (considering specified operations in Larry's Array doc):
  a. if #inversions is even the array CAN    be sorted.
  b. if #inversions is odd  the array CANNOT be sorted.

That gives us this formula for determining solvability:
number_of_inversions % 2 == 0
