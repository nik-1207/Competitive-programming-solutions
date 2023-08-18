// Problem https://leetcode.com/problems/fizz-buzz/

// solution
function fizzBuzz(n: number): string[] {
    const arr = new Array(n).fill(0).map((_, i) => {
        let num = i + 1;
        switch (true) {
            case num % 3 === 0 && num % 5 === 0:
                return "FizzBuzz";
            case num % 3 === 0:
                return "Fizz";
            case num % 5 === 0:
                return "Buzz";
            default:
                return num.toString();
        }
    });
    return arr
};