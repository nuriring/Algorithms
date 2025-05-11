function solution(arr1, arr2) {
    // 행렬 곱셈 공식 쉽게 이해 링크
    // https://m.blog.naver.com/galaxyenergy/221210591811
    var answer = [[]];
    // 행렬 arr1과 arr2의 행과 열의 수
    const r1 = arr1.length;
    const c1 = arr1[0].length;
    const r2 = arr2.length;
    const c2 = arr2[0].length;
    
    // 결과 저장할 2차원 배열 초기화
    const ret = [];
    for (let i=0; i<r1; i++) {
        ret.push(new Array(c2).fill(0));
    }
    
    // 첫 번째 행렬 arr1의 각 행과 두번째 행렬 arr2의 각 열에 대해
    for (let i=0; i<r1; i++) {
        for (let j=0; j<c2; j++) {
            // 두 행렬의 데이터를 곱해 결과 배열에 더해줌
            // 행렬 끼리 곱할려면 앞 행렬의 열수 == 뒤 행렬의 행수
            for (let k=0; k<c1; k++) {
                ret[i][j] += arr1[i][k] * arr2[k][j]
            }
        }
    }
    return ret;
}