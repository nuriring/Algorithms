let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
const arr = [];
for (let i = 1; i < N + 1; i++) {
  arr.push(input[i].trim().split(" "));
}

// const fs = require("fs");
// const stdin = fs.readFileSync("test.txt").toString().trim();

// -------------
// 입력
// -------------
// const input = stdin.split("\n").map((item) => item.trim().split(" "));
// const [[N], ...arr] = input;

function dfs(x, y, N, res, op) {
  if (x === N - 1 && y === N - 1) {
    if (mmax <= res) {
      mmax = res;
    }
    if (mmin > res) {
      mmin = res;
    }
  } else {
    const dir = [
      [0, 1],
      [1, 0],
    ];
    for (let i = 0; i < 2; i++) {
      let nx = x + dir[i][0];
      let ny = y + dir[i][1];
      if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
        if (operator.includes(arr[nx][ny])) {
          dfs(nx, ny, N, res, arr[nx][ny]);
        } else {
          if (op === "+") {
            dfs(nx, ny, N, res + parseInt(arr[nx][ny]), op);
          }
          if (op === "-") {
            dfs(nx, ny, N, res - parseInt(arr[nx][ny]), op);
          }
          if (op === "*") {
            dfs(nx, ny, N, res * parseInt(arr[nx][ny]), op);
          }
        }
      }
    }
  }
}

let mmax = -11111111;
let mmin = 111111111;
const operator = ["+", "-", "*"];
const op = "";
dfs(0, 0, N, parseInt(arr[0][0]), op);
console.log(`${mmax} ${mmin}`);
