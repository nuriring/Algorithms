function solution(arr)
{
    var answer = [];
    
    for (const number of arr) {
        let flag = 0
        if (answer.length > 0 && answer[answer.length - 1] === number) {
            answer.pop()
            answer.push(number)
        } else {
            answer.push(number)
        }
    }
    
    return answer;
}