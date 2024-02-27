let input = require('fs').readFileSync('/dev/stdin').toString().trim().split("\n")
const [X, Y] = input[0].split(' ').map(v => +v);
const arr = []
for (let i=1; i<X+1; i++) {
    arr.push(input[i].split(" ").map(v => +v))
}
const dir = [[0,1],[1,0],[0,-1],[-1,0]]
const visited = Array.from(Array(X), () => Array(Y).fill(false))

let mmax = 0
function dfs(x,y,depth,ssum) {
    if (depth===4) {
        mmax = Math.max(mmax,ssum)
        return
    }
    for (let k=0; k<4; k++) {
        let nx = x+dir[k][0]
        let ny = y+dir[k][1]
        if (nx>=0 && nx<X && ny>=0 && ny<Y) {
            if (!visited[nx][ny]) {
                visited[nx][ny] = true
                dfs(nx,ny,depth+1,ssum+arr[nx][ny])
                visited[nx][ny] = false
            }
        }
    }
}

function mount(x,y,ssum) {
    const tmp = ssum
    for (let n=0; n<4; n++) {
        let ssum = tmp
        for (let k=0; k<3; k++) {
            const t = (n+k) % 4
            let nx = x + dir[t][0]
            let ny = y + dir[t][1]
            if (nx>=0 && nx<X && ny>=0 && ny<Y) {
                ssum += arr[nx][ny]
            }
        }
        mmax = Math.max(mmax,ssum)
    }
}

for (let i=0; i<X; i++) {
    for (let j=0; j<Y; j++) {
        visited[i][j] = true
        dfs(i,j,1,arr[i][j])
        visited[i][j] = false
        mount(i,j,arr[i][j])
    }
}

console.log(mmax)

