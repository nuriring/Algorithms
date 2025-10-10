function makeObj(w, n) {
    const obj = {}
    for (let i=0; i<w.length; i++) {
        obj[w[i]] = n[i]
    }
    return obj
}

function checkPossibility(hashObj) {
    //nan이 들어갈수있음
    return Object.values(hashObj).every(v => !isNaN(v) && v<=0)
}


function solution(want, number, discount) {
    const hashObj = makeObj(want,number)
    var answer = 0;
    let i = 0
    let j = 0
    let possibility = 0
    let newHash = {}
    while (i+10 <= discount.length) {
        newHash = {...hashObj}
        for (j=i; j<i+10; j++) {
            const target = discount[j]
            newHash[target] -= 1
        }
        // console.log(newHash, 'hashObj')
        // 값중에 0보다 큰 값이 있으면 fail 이야
        // 필요 없는 물건 등록되는건 상관 없어..
        if (checkPossibility(newHash)) {
            answer+=1
        }
        i++
    }
    return answer;
}