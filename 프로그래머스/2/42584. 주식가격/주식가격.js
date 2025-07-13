function solution(prices) {
    var answer = [];
    const test = [5, 4, 3, 2, 1];
    const countArr = Array(prices.length).fill(0)
    for (const [idx,price] of prices.entries()) {
        // console.log(idx, price, 'idx와 price')
        let secondAcc = 0
        for (let i=idx + 1; i<prices.length; i++) {
            secondAcc ++ 
            
            if (price > prices[i]) {
                break
            }
        }
        countArr[idx] = secondAcc
    }
    // console.log(countArr, 'countArr')
    return countArr;
}