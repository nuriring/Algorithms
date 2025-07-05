function solution(arr, divisor) {
    var answer = [];
    for (i=0; i<arr.length; i++) {
        const rest = arr[i] % divisor
        if (rest === 0) {
            answer.push(arr[i])
        }
    }
    
    answer = answer.sort((a,b) => (a-b))
    console.log(answer, 'answer')
    if (answer.length === 0) {
        return [-1]
    }
    
    return answer;
}