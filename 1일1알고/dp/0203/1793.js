// let input = require("fs")
//   .readFileSync("1793.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .map(Number)
// console.log(input)

// const newInput = input.map(Number)
// console.log(newInput)

// function tiling(n) {
//     const dp = Array(n+1).fill(null)
//     dp[0] = 1
//     dp[1] = 2
//     for (let i=2; i<n; i++) {
//         dp[i] = dp[i-1] + dp[i-2]
//     }
//     console.log(dp)
//     return dp[n-1].toFixed().toString()
// }

// newInput.map((item,idx) => {

//     console.log(tiling2(item))
// })

// // console.log(tiling(9))

// function tiling2(n) {
//     const dp = Array(n+1).fill(null)
//     dp[0] = 1
//     dp[1] = 3
//     for (let i=2; i<n; i++) {
//         dp[i] = dp[i-1] + 2*dp[i-2]
//     }
//     // console.log(dp)
//     return dp[n-1].toFixed().toString()
// }

// console.log(tiling2(8))

// function solution(n) {
//     if (n === 1 || n === 2)
//         return n;
//     const dp = Array(n+1).fill(0);
//     const mod = 1000000007;
//     dp[0] = 1;
//     dp[1] = 2;
//     for (let i = 2; i < n; i++)
//         dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
//     return dp[n + 1];
// }

// console.log(solution(2))




let input = require('fs').readFileSync('1793.txt').toString().trim().split('\n');
let N = 1;
// 넘버링
input.forEach((n, i) => {
    input[i] = +n;
    N = Math.max(+n, N);
    // console.log(N, '이게대체무슨')
});
// console.log(input,'input')

// let dp = new Array(N+1).fill(0n);
// console.log(dp,'dp')
// dp[0] = 1n
// dp[1] = 1n
// for (let n = 2; n <= N; ++n) dp[n] = dp[n-2] * 2n + dp[n-1];

// console.log(dp,'dp')
// let output = new Array(input.length);
// for (let i = 0 ; i < input.length; ++i) output[i] = dp[input[i]];
// console.log(output.join('\n'));



let dp = new Array(N+1).fill(0n);
dp[0] = 1n
dp[1] = 1n
// console.log(dp,'dp')
for (let n = 2; n <= N; ++n) dp[n] = dp[n-2] * 2n + dp[n-1];
// console.log(dp,'결과dp')
let output = new Array(input.length);
for (let i = 0 ; i < input.length; ++i) output[i] = dp[input[i]];
console.log(output.join('\n'))


let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let N = 1;
input.forEach((n, i) => {
    input[i] = +n;
    N = Math.max(+n, N);
});

let dp = new Array(N+1).fill(0n);
dp[0] = 1n
dp[1] = 1n
for (let n = 2; n <= N; ++n) dp[n] = dp[n-2] * 2n + dp[n-1];

let output = new Array(input.length);
for (let i = 0 ; i < input.length; ++i) output[i] = dp[input[i]];
console.log(output.join('\n'));