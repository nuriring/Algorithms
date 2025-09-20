function solution(s) {
    var answer = 0;
    const stack = []
    const strings = s.split(' ')
    for (const char of strings) {
        if (char === 'Z' && stack.length) {
            stack.pop()
        } else {
            stack.push(Number(char))
        }
    }
    answer = stack.reduce((a,b) => (a+b), 0)
    
    
    return answer
}