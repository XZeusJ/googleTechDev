/*
1. brute force
for each number, we compute its span
and compare to find the max span.
*/

public int maxSpan(int[] nums) {
  int maxSpan = 0;
  int span;

  for (int i=0; i< nums.length; i++) {
    for (int j = nums.length-1; j >= 0; j--) {
    	if (nums[i] == nums[j]) {
    		span = j - i + 1;
    		if (span > maxSpan) maxSpan = span;
    		break;
    	}
    }
  }
  return maxSpan;
}

/*
2. 滑窗
for each number, we store the max span window, and move the window  
*/
