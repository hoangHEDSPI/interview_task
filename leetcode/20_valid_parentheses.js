/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function(s) {
    if (s.length % 2 != 0) return false;
    if (s.length == 0) return true;

    var parentheses_stack = [];

    var close_sign = [')', ']', '}'];
    var paren_dict = {'(' : ')', '[' : ']', '{' : '}'};

    for (let i = 0 ; i < s.length; i++) {
        if (i == 0) {
            parentheses_stack.push(s[i]);
        }
        else {
            // the next element of s is a close sign
            if (close_sign.indexOf((s[i])) != -1) {
                console.log("i == " + i);
                if (paren_dict[parentheses_stack[parentheses_stack.length-1]] != s[i]) return false;
                else {
                    parentheses_stack.pop();
                }
            }
            // the next element of s is an open sign
            else if (close_sign.indexOf(s[i]) == -1) {
                    parentheses_stack.push(s[i]);
                }
        }
        console.log("stack = " + parentheses_stack);
            
    }
    
    if (parentheses_stack.length == 0) return true;
    else return false;
};

s = "()[]{}";
s1 = "[][]{]";
console.log(isValid(s));
// console.log(isValid(s1));
