class Queue {
    
    constructor() {
        this.items = [];
        this.weight = 0;
    } 
    
    push(item) {
        this.items.push(item);
        this.weight += item;
        this.rear++;
    }
    
    pop() {
        const val = this.items.shift();
        this.weight -= val;
        return val;
    }
    
    isEmpty() {
        return this.rear === this.front
    }
}



function solution(bridge_length, weight, truck_weights) {
    // 트럭은 1초마다 다리위에서 한칸
    // 큐에 넣어주면서, 시간을 +1
    // 다리 위가 큐라고 생각하면, 무게제한이 있음
    // 1초씩 이동하면서, bridege_length 가 되면 선입 선출 해줘야 함
    const bridge = new Queue();
    let time = 0;
    
    // 다리를 길이만큼 0으로 채워 시작 (빈다리)
    for (let i = 0; i<bridge_length; i++) {
        bridge.push(0)
    }
    
    // 실을 트럭이 남거나, 다리위에 트럭이 남아있거나
    while (truck_weights.length > 0 || bridge.weight > 0) {
        // 1초에 트럭이 한칸 씩 이동
        bridge.pop();
        time++;
        
        if (truck_weights.length > 0) {
            const next = truck_weights[0];
            if (bridge.weight + next <= weight) {
                truck_weights.shift(); //대기 트럭에서 꺼냄
                bridge.push(next); //다리에 진입
            } else {
                bridge.push(0); //못 올라가면 다리길이만큼 또 빈칸
            }
        } else {
            bridge.push(0); // 대기 트럭 없으면 빈칸
        }
    }
    
    
    return time;
}