public class Solution {
    /**
     * @param nums: An integer array
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        // write your code here
        int len, n1, n2;

        len = sizeof(nums) / sizeof(*nums);

        n1 = std::max(nums[0], nums[1]);
        
        for (i = 2; i < len; i ++ ){
            if (nums[i] < n2) {
                
            } else if (nums[i] > n1) {
            } else {
            }
        }
    }
}
