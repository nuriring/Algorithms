function solution(n, left, right) {
    var answer = [];
    // const arr = [...new Array(n)].map((_,i) => new Array(n).fill(i))

    // n이 10 7승이기 때문에 배열을 다 만들어서 자르는 개념x
    // 1차원으로 펼쳤을 때 들어가는 값의 규칙을 파악
    for (let t=left; t<=right; t++) {
        // left index 기준으로 1차원으로 펼쳤을 때 row 위치         
        const row = Math.floor(t / n)
        // col 위치
        const col = t % n
        // row와 col중 더 큰 값의 +1 값이 들어감
        answer.push(Math.max(row, col) + 1)
    }    
    
    return answer;
}