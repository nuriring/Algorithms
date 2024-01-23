let input = require('fs').readFileSync('1987.txt').toString().trim().split("\n")

const [X, Y] = input[0].split(' ').map(v => +v);

const arr = []
for (let i=1; i<X+1; i++) {
    arr.push(input[i].split(""))
}
const index = []
const dir = [[0,1],[1,0],[0,-1],[-1,0]]
let visited = new Array(26).fill(false);


let mmax = 0
function dfs(x,y,depth) {
    mmax = Math.max(mmax,depth)
    // 출발지 설정
    let start = arr[x][y]
    visited[start.charCodeAt()-65] = true

   
    for (let i=0; i<4; i++) {
        let nx = x + dir[i][0]
        let ny = y + dir[i][1]
        if (nx>=0 && nx<X && ny>=0 && ny<Y) {
            let next = arr[nx][ny]
            if (!visited[next.charCodeAt()-65]) {
                dfs(nx,ny,depth+1)
                visited[next.charCodeAt()-65] = false
            }
        }
    }
}

dfs(0,0,1,arr[0][0])
console.log(mmax)

