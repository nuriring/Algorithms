function solution(s)
{
    var answer = -1;
    const stack = []
    let top = -1
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for (const c of s) {
        // 스택이 비어 있으면         
        if (stack.length === 0) {
            stack.push(c)
            top += 1
        } else {
            // 최상단과 비교             
            if (stack[top] === c) {
                stack.pop()
                top -= 1
            } else {
                stack.push(c)
                top += 1
            }
        }
    }
    
    answer = stack.length === 0 ? 1 : 0

    return answer;
}