

function solution(s) {
    console.log(s.length)
    console.log(s.length/2,'문자열최대길이')
    let mmin = Infinity
    let answer
    for (let i=1; i <= parseInt(s.length/2); i++) {
        console.log(i,'i')
        let cnt = 1
        answer = 0
        let flag
        let letter = ''
        for (let j=0; j < s.length-i; j+=i) {
            console.log(j,'j')
            console.log(s.substring(j,j+i),'좌')
            console.log(s.substring(j+i,j+2*i),'우')
            
            if (s.substring(j,j+i) === s.substring(j+i,j+2*i)) {
                flag = true
                letter = s.substring[j,j+i]
                cnt += 1
            } else {
                // flag = false
            }
            
            if (cnt>1) {
                answer += cnt.toString()+letter
                cnt = 1
                flag = false
            }
        }
        console.log(answer,'비교비교')
        if (answer<mmin) {
            mmin = answer
        }
    }

    return answer;
}