/*
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.


canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
*/

public boolean canBalance(int[] nums) {
  int mid = nums.length / 2;
  
  // compute left sum and right sum
  int leftSum = 0, rightSum = 0;
  for (int i= 0; i < nums.length; i++) {
    if (i < mid) leftSum += nums[i];
    else rightSum += nums[i];
  }
  
  // start from the mid point, judge diff to reach the final result
  int diff = Math.abs(leftSum - rightSum);
  while (diff >= 0) {
    if (diff == 0) return true;
    if (leftSum > rightSum) diff -= nums[mid--] * 2;
    else diff -= nums[mid++] * 2;
  }
  return false;
  
}