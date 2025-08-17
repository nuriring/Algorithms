function solution(progresses, speeds) {
    var answer = [];
    // 배포까지 남은 일수, 잔여 작업량이라 생각하면 편함
    const dayLeft = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]))
    console.log(dayLeft, 'dayLeft')
    const N = progresses.length
    let count = 0 //배포에 포함해야할 작업 수
    // 기준 배포일, 가장 먼저 배포해야 될 작업량부터 기준
    let criteriaDay = dayLeft[0]
    for (i=0; i<N; i++) {
        // 현재 작업량이 기준 작업량보다 작거나 같으면
        // 해당 배포일에 더 작은 작업량 까지 다 완료되서 배포가 가능해지므로 count ++
        if (dayLeft[i] <= criteriaDay) {
            count ++;
        // 작업량이 더 많이 남았으면 배포에 포함 못 시키고, 해당 작업부터 새로운 기준이 됨 count도 리셋
        } else {
            answer.push(count)
            count = 1
            criteriaDay = dayLeft[i]
        }
    }
    
    // 마지막으로 카운트된 작업들도 다 포함
    answer.push(count)
    return answer;
}