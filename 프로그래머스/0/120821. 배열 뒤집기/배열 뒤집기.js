function solution(num_list) {
    var answer = [];
    for (let i=num_list.length-1; i>-1; i--) {
        answer.push(num_list[i])
    }
    console.log(answer,'답')
    return answer;
    
}