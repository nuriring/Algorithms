function rotate(s) {
    const firstChar = s[0]
    const remainS = s.slice(1)
    return remainS + firstChar
}

function checkRight(s) {
    const stack = []
    let top = -1
    for (const c of s) {
        if (c === "(" || c === "{" || c ==="[") {
            stack.push(c)
            top += 1
        } else {
            if (stack.length === 0) {
                return false
            }
            if (c === ")") {
                if (stack.length !== 0 && stack[top] === "(") {
                    stack.pop()
                    top -= 1
                }
            }
            if (c === "}") {
                if (stack.length !== 0 && stack[top] === "{") {
                    stack.pop()
                    top -= 1
                }
            }
            if (c === "]") {
                if (stack.length !== 0 && stack[top] === "[") {
                    stack.pop()
                    top -= 1
                }
            }
        } 
    }
    
    return stack.length === 0
}

function solution(s) {
    let rotatedS = s
    let answer = 0
    if (checkRight(s)) {
        answer += 1
    }
    for (i=1; i<s.length; i++) {
        rotatedS = rotate(rotatedS)
        if (checkRight(rotatedS)) {
            answer += 1
        }
    }

    return answer;
}