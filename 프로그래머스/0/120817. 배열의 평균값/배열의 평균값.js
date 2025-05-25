function solution(numbers) {
    let sum = 0;
    for (const number of numbers)
    {
        sum = sum + number
        console.log(sum, '합')
        
    }
    return sum/numbers.length
}