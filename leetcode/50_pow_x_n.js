/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    // x : float
    // n : integer

    if (n == 0) return 1;
    if (n < 0) {
        x = 1/x;
        return (n%2 == 0) ? myPow(x*x, (Math.floor(-n/2))) : x*myPow(x*x, (Math.floor(-n/2)));
    }
    return (n%2 == 0) ? myPow(x*x, Math.floor(n/2)) : x*myPow(x*x, Math.floor(n/2));
};


// Maximmun call stack size exceeded Error

// Make sure that my recursive calling has a terminated point
console.log(myPow(2, 100000000));