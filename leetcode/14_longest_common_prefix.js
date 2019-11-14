/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {

    if (strs.length == 0) return "";
    if (strs.length == 1) return strs[0];

    let longest_prefix = "";
    let letter = "";
    let j = 0;
    let i = 0;

    while (j < strs[0].length) {
        i = 1;
        letter = strs[0][j];
        while (i < strs.length) {
            if (strs[i][j] == letter) i += 1;
            else break;
        }
        if (i == strs.length) {
            longest_prefix += letter;
            j += 1;
        }
        else break;
    }

    return longest_prefix;
};

strs = ["flower","flow","flight"];

console.log(longestCommonPrefix(strs));

strs_1 = ["dog","racecar","car"];

console.log(longestCommonPrefix(strs_1));