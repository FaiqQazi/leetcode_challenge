import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j = 0, k = 0;
        if (n == 0) {
            return; // No need to perform merge operation, nums1 remains unchanged
        }

        if (m - n < 0) {
            if (m == 0) {
                System.arraycopy(nums2, 0, nums1, 0, n); // nums1 is empty, copy nums2 into nums1
            } else {
                int[] result = Arrays.copyOf(nums1, m); // Create a copy of nums1 with only m elements
                for (int i = 0; i < m + n; i++) {
                    if (j < m && k < n) {
                        if (result[j] <= nums2[k]) {
                            nums1[i] = result[j];
                            j++;
                        } else {
                            nums1[i] = nums2[k];
                            k++;
                        }
                    } else if (j < m) {
                        nums1[i] = result[j];
                        j++;
                    } else if (k < n) {
                        nums1[i] = nums2[k];
                        k++;
                    }
                }
            }
        } else {
            int[] result = Arrays.copyOf(nums1, m); // Create a copy of nums1 with only m elements
            for (int i = 0; i < m + n; i++) {
                if (j < m && k < n) {
                    if (result[j] <= nums2[k]) {
                        nums1[i] = result[j];
                        j++;
                    } else {
                        nums1[i] = nums2[k];
                        k++;
                    }
                } else if (j < m) {
                    nums1[i] = result[j];
                    j++;
                } else if (k < n) {
                    nums1[i] = nums2[k];
                    k++;
                }
            }
        }
    }
}
