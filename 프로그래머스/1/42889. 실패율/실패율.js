function solution(N, stages) {
    var answer = [];
    // 실패율 배열 초기화
//     const failRate = new Array(N).fill(0)
//     console.log(failRate, '실패율 배열 초기화')
//     for (let i=0; i<N; i++) {
//         let failSum = 0
//         let arriveSum = 0
//         for (let j=0; j<stages.length; j++) {
//         // 통과 못하고, 스테이지에 도달자체는 해야함             
//             if (stages[j] <= i+1 && stages[j] >= i+1)  {
//                 failSum += 1
//             }
//             if (stages[j] >= i+1) {
//                 arriveSum += 1
//             }
//         }
//         console.log(i, failSum, arriveSum, '뭐지')
//         failRate[i] = failSum/arriveSum
//     }
    
    
    
//     console.log(failRate, '실패율 기록 후')

    // 스테이지별 도전자 수
    const challenger = new Array(N+2).fill(0)
    for (const stage of stages) {
        challenger[stage] += 1;
    }
    
    console.log(challenger, '스테이지별 도전자수')
    
    // 스테이지별 실패한 사용자 수
    const fails = {}
    let total = stages.length
    
    // 각 스테이지를 순회하며, 실패율 계산
    for (let i = 1; i<=N; i++) {
        if (challenger[i] === 0) {
            //도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0
            continue;
        }
        
        // 실패율 계산
        fails[i] = challenger[i]/total
        
        // 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌 (도달한 사람만 실패율에 포함되므로)
        total -= challenger[i]
    }
    
    console.log(fails, '실패율')
    // entries는 [[index], [value]]를 뱉음
    // sort 메소드는 안정 정렬을 제공하기 때문에, value가 같으면 우선 조회된 key값 부터 나열됨
    const result = Object.entries(fails).sort((a,b) => b[1] - a[1])
    console.log(result, '뭐가 나오지')
    
    return result.map((v) => Number(v[0]))
    
    

    // return answer;
}