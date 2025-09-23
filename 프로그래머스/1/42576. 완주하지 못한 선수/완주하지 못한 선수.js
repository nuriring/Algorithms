function solution(participant, completion) {
    var answer = '';
    const checkObj = {};
    for (const runner of participant) {
        // 동명이인 체크를 위해 등장횟수로 평가
        checkObj[runner] = (checkObj[runner] || 0) + 1
        
    }
    for (const completeRunner of completion) {
        checkObj[completeRunner] -= 1
    }
    
    
    answer = Object.keys(checkObj).find(k => checkObj[k] == 1)
    
    return answer;
}