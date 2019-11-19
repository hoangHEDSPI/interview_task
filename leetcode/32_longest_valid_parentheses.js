/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let stack = [];
    let longest_length = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(') stack.push(i);
        else {
            if (stack.length > 0) {
                if (s[stack[stack.length-1]] == '(') stack.pop();
                else stack.push(i);
            }
            else stack.push(i);
        }
    }

    if (stack.length == 0) return s.length;
    longest_length = Math.max(stack[0], s.length - stack[stack.length-1]-1);
    for (let i = 0; i < stack.length-1; i++) {
        if (stack[i+1]-stack[i]-1 > longest_length) longest_length = stack[i+1] - stack[i]-1;
    }
    return longest_length;

};

s = ")()())";

console.log(longestValidParentheses(s));