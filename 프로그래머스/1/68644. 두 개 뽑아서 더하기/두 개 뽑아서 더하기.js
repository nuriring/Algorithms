function solution(numbers) {
    var answer = [];
    for (i=0; i<numbers.length; i++) {
        for (j=0; j<numbers.length; j++) {
            if (i!==j) {
                console.log(numbers[i] + numbers[j], '합 출력')
                answer.push(numbers[i]+numbers[j])
            }
        }
    }
    console.log([...new Set(answer)].sort((a,b) => (a-b)), '중복제거 후 정렬')
    answer = [...new Set(answer)].sort((a,b) => (a-b))
    return answer;
}