/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {

    // make sure that n always greater or equal than m
    let tmp;
    if (nums1.length > nums2.length) {
        tmp = nums1;
        nums1 = nums2;
        nums2 = tmp;
    }
    let m = nums1.length;
    let n = nums2.length;
    let imin = 0;
    let imax = m;
    let haft_length = Math.floor((m+n+1)/2);
    let max_of_left = 0;
    let min_of_right = 0;

    while (imin <= imax) {
        let i = Math.floor((imin+imax)/2);
        j = haft_length - i;
        if (i < m && nums2[j-1] > nums1[i]) imin = i+1;
        else if (i > 0 && nums1[i-1] > nums2[j]) imax = i-1;
        else {
            if (i === 0) max_of_left = nums2[j-1];
            else if (j === 0) max_of_left = nums1[i-1];
            else max_of_left = Math.max(nums1[i-1], nums2[j-1]);
            if ((m+n) % 2 == 1) {
                return max_of_left;
            }
            if (i == m) {
                min_of_right = nums2[j];
            }
            else if (j == n) {
                min_of_right = nums1[i];
            }
            else {
                min_of_right = Math.min(nums1[i], nums2[j]);
            }

         
            return (max_of_left+min_of_right)/2;
        }
    }
};


A = [1,2];
B = [3,4];
console.log(findMedianSortedArrays(A, B));