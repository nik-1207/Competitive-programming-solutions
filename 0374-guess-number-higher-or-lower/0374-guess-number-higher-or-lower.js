/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function (n) {
    let num = n;
    while (guess(num) !== 0) {
        if (guess(num) === -1) {
            num--;
        } else {
            num++
        }
    }
    return num
};