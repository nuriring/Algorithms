//한줄입력
// const fs = require("fs");
// // let input = fs.readFileSync("/dev/stdin").toString().split("\n"); 백준용
// let input = fs.readFileSync("10807.txt").toString().trim().split(/\s/);
// // let input = fs.readFileSync("10807.txt").toString().split(/\s/);

// // console.log(input);
// const n = input[0];
// // console.log(n); //정수갯수

// // const n_arr = input.slice(2, Number(n) + 2);
// // console.log(n_arr); //정수리스트

// let n_arr = input.slice(2, Number(n) + 2).map(Number);
// // console.log(n_arr);

// const v = input[input.length - 1];
// // console.log(v); //찾아야하는 수
// // console.log(typeof v);

// var i = 0;
// n_arr.map((item, idx) => {
//   // console.log(item);
//   if (item === Number(v)) {
//     i += 1;
//   }
// });

// console.log(i);

// const fs = require("fs");
// // const np = fs.readFileSync("./dev/stdin").toString().split("\n");
// const np = fs.readFileSync("10807.txt").toString().split("\n");

// let intArr = np[1].split(" ").map(Number);
// let v = +np[2];
// let cnt = 0;
// console.log(intArr);
// console.log(v);
// console.log(cnt);
// intArr.forEach((el) => check(el));
// function check(a) {
//   if (a === v) {
//     cnt++;
//   }
// }
// console.log(cnt);

//한줄입력
const fs = require("fs");
// // let input = fs.readFileSync("/dev/stdin").toString().split("\n"); 백준용
// // let input = fs.readFileSync("./dev/stdin").toString().trim().split(/\s/);
// let input = fs.readFileSync("10807.txt").toString().split(/\s/);

// const np = fs.readFileSync("./dev/stdin").toString().split("\n");
const np = fs.readFileSync("10807.txt").toString().split("\n");
// console.log(np);
//https://velog.io/@grap3fruit/%EA%B5%AC%EB%A6%84goorm-%EC%BD%94%ED%85%8C-javascript-%EB%A1%9C-%EC%9E%85%EB%A0%A5%EA%B0%92-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95
let intArr = np[1].split(" ").map(Number);
let v = +np[2];
let vv = np[2];
// 이 두개는 무슨 차이지
// console.log(v, vv);
// // console.log(input);
// let n = input[0];
// // console.log(n); //정수갯수

// let n_arr = input.slice(2, Number(n) + 2);
// // console.log(n_arr); //정수리스트

// let v = input[input.length - 1];
// console.log(v); //찾아야하는 수

var i = 0;
intArr.map((item, idx) => {
  // console.log(item);
  if (item === v) {
    i += 1;
  }
});

console.log(i);
