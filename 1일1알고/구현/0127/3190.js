const input = require('fs').readFileSync('3190.txt').toString().trim().split("\n")
const N = +input[0] //보드 크기
const appleCnt = +input[1]
const moveCnt = +input[appleCnt+2]
const appleLocations = input.slice(2,appleCnt+2)
const moveInfos = input.slice(appleCnt+3,appleCnt+3+moveCnt)
const moveInfoDict = {}
moveInfos.map((item) => {
    const time = Number(item.split(' ')[0])
    const dir = item.split(' ')[1].trim()
    moveInfoDict[time] = dir
})
const board = Array.from(Array(N), () => Array(N).fill(0))
appleLocations.forEach((item)=>{
    const [x,y] = item.split(' ').map((str)=>Number(str))
    board[x][y] = 'A'
})

function findDirIdx(nowDir) {
    if (nowDir==='r' || nowDir==='l') {
        return {'L':[-1,0], 'D': [1,0]}
    } else {
        return {'L':[0,1], 'D':[0,-1]}
    }
}

const fourWay = ['r','d','l','u']
function turnDir(nowDir, turnIdx) {
    if (turnIdx === 'L') {
        const leftRotateIdx = nowDir==='r' ? 3 : fourWay.indexOf(nowDir) % 4 - 1
        return fourWay[leftRotateIdx]
    } else {
        const rightRotateIdx = nowDir==='u' ? 0 : fourWay.indexOf(nowDir) % 4 + 1
        return fourWay[rightRotateIdx]
    }
}
let dir = 'r'
let cnt = -1 //경과시간
const snake = [[0,0]]
let [x,y] = [0,0]
board[x][y] = 1
const goIdx = [[0,1],[1,0],[0,-1],[-1,0]]

while (true) {
    cnt += 1
    console.log(snake,'snake')
    if (cnt in moveInfoDict) {
        const turnIdx = moveInfoDict[cnt]
        const dirIdx = findDirIdx(dir)
        x = x + dirIdx[turnIdx][0]
        y = y + dirIdx[turnIdx][1]
        dir = turnDir(dir, turnIdx)
    } else {
        x = x + goIdx[fourWay.indexOf(dir)][0]
        y = y + goIdx[fourWay.indexOf(dir)][1]
    }

    if (x>=0 && x<N && y>=0 && y<N && board[x][y] !== 1 ) {
        if (board[x][y] === 'A') {
            snake.push([x,y])
            board[x][y] = 1
        } else {
            const [popX,popY] = snake.shift()
            board[popX][popY] = 0
            snake.push([x,y])
            board[x][y] = 1
        }
        console.log(cnt, 'cnt')
        console.log(board,'board')

    } else {
        console.log(cnt, '답')
        return
    }
}

