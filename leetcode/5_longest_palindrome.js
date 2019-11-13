/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
    if (s.length <= 1) return s;

    let F = Array(s.length).fill().map(() => Array(s.length));
    let max_palin = "";
    let max_length = 1;
    let start_index = 0;

    // check for less or equal 1-character given string

    for (let i = 0; i < s.length; i++) {
        F[i][i] = true;
    }

    // check for 2-character substring

    for (let i = 0; i < s.length-1; i++) {
        if (s[i] === s[i+1]) {
            F[i][i+1] = true;
            max_length = 2;
            start_index = i;
        } 
    }

    // check for greater or equal 3-character substring
    for (let k = 3; k  <= s.length; k++) { 
        for (let i = 0; i < s.length-k+1; i++) {
            let j = i+k-1;
            
            if (F[i+1][j-1] == true && s[i] === s[j]) {
                F[i][j] = true;
                if (k > max_length) {
                    max_length = k;
                    start_index = i;
                }
            }
        }
    }

    max_palin = s.substring(start_index, start_index+max_length);

    return max_palin;
};


s = "babad";

console.log(longestPalindrome(s))