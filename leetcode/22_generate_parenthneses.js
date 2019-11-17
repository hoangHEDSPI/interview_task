/**
 * @param {number} n
 * @return {string[]}
 */

function backtracking(results, str, num_open, num_close, half_length) {
    if (str.length == half_length*2) {
        results.push(str);
        return;
    }
    if (num_open < half_length) backtracking(results, str + "(", num_open+1, num_close, half_length);
    if (num_close < num_open) backtracking(results, str + ")", num_open, num_close+1, half_length);
    return results;
};


var generateParenthesis = function(n) {
    let results = [];
    backtracking(results, "", 0, 0, n);
    return results;
};


let n = 3;
console.log(generateParenthesis(n));