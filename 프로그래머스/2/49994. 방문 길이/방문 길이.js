function isValidMove(nx, ny) {
//     좌표 평면을 벗어나는지 체크하는 함수
    const valid = nx >= -5 && nx <= 5 && ny >= -5 && ny <=5
    if (!valid) console.log(`🚫 move to (${nx}, ${ny}) is invalid!`);
    // return nx >= -5 && nx <= 5 && ny >= -5 && ny <=5
    return valid
}

function updateLocation(x,y,dir) {
//     명령어를 통해 다음 좌표 결정
    console.log(dir,'음')
    switch (dir) {
        case "U":
            return [x, y+1];
        case "D":
            return [x, y-1];
        case "R":
            return [x+1, y];
        case "L":
            return [x-1,y];
        default:
            return [x, y];
    }
}

function solution(dirs) {
    let x = 0;
    let y = 0;
    
//     중복 경로 제거
    const visited = new Set();
    for (const dir of dirs) {
        const [nx,ny] = updateLocation(x,y,dir)
        console.log(nx,ny, '엥뭐지')
    if (!isValidMove(nx,ny)) {
        console.log("이거 한번도 안돌아가네")
        continue;
    }
    
   try {
  visited.add(`${x},${y},${nx},${ny}`);
  visited.add(`${nx},${ny},${x},${y}`);
} catch (e) {
  console.log("🚨 visited.add 중 에러 발생:", e);
}
        
        
        [x, y] = [nx, ny]
        console.log(x,y, '뭐지?')
    }
    console.log(visited, 'set 출력')
    return visited.size / 2
}