const fs = require("fs");
const [N, K] = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

class Queue {
  items = [];
  front = 0;
  rear = 0;

  push(item) {
    this.items.push(item);
    this.rear++;
  }

  size() {
    return this.rear - this.front;
  }

  pop() {
    return this.items[this.front++];
  }
}

function solution(N, K) {
  const res = [];
  const queue = new Queue();

  // 1부터 N까지 enqueue
  for (let i = 1; i <= N; i++) {
    queue.push(i);
  }

  while (queue.size() > 0) {
    // K-1번 만큼 회전
    for (let i = 0; i < K - 1; i++) {
      queue.push(queue.pop());
    }
    // K번째 제거
    const removedItem = queue.pop();
    res.push(removedItem);
  }

  return res;
}

console.log(`<${solution(N, K).join(", ")}>`); 
