let input = require("fs")
  .readFileSync("2468.txt")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
const arr = [];
for (let i = 1; i < N + 1; i++) {
  arr.push(input[i].trim().split(" ").map(Number));
}



const findMax = (N) => {
    let mmax = 0
    for (let i=0; i<N; i++) {
        for (let j=0; j<N; j++) {
            if (mmax < arr[i][j]) {
                mmax = arr[i][j]
            }
        }
    }
    return mmax
}

// const bfs = (graph, start, visited) => {
//     const q = [];
//     q.push(start);
//     visited[start] = true;
  
//     while (q.length !== 0) {
//       const v = q.shift();
//       console.log(v);
      
//       for(const cur of graph[v]){
//         if(!visited[cur]){
//           q.push(cur);
//           visited[cur] = true;
//         }
//       }
//     }
//   }
const bfs = (i,j,visited, height) => {
  const q = []
  q.push([i,j])
  visited[i][j] = true;
  const dir = [[0,1],[1,0],[0,-1],[-1,0]]

  while ( q.length !== 0 ) {
    const [i,j] = q.shift()
    for (let k=0; k<4; k++) {
      let ni = i+dir[k][0]
      let nj = j+dir[k][1]
      if (ni>=0 && ni<N && nj>=0 && nj<N && arr[ni][nj] > height && visited[ni][nj] === false) {
        visited[ni][nj] = true
        q.push([ni,nj])
      } 
    }
  }
}

const maxHeight = findMax(N)

let max_ans = 0

for (let height=0; height<maxHeight+1; height++) {
  let visited = Array.from(Array(N), ()=> Array(N).fill(false))
  let cnt = 0
  for (let i=0;i<N;i++) {
    for (let j=0;j<N;j++) {
      if ( arr[i][j] > height && visited[i][j] === false ) {
        bfs(i,j,visited,height)
        cnt += 1
      }
    }
  }
  if (max_ans<=cnt) {
    max_ans=cnt
  }
}


console.log(max_ans)
