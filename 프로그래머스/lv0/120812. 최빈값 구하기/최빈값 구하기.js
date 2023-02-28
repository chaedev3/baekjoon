function solution(array) {
    let map = new Map();
    // 배열의 길이가 1인 경우에는 바로 그 값을 반환한다. 
    if (array.length === 1) {
        return array[0]; 
    }
    // 배열의 최댓값만큼 Map을 초기화한다. 
    for (let i = 0; i <= Math.max(...array); i ++)     {
        map.set(i, 0);
    }
    // 순회하며 Map에 빈도수를 update
    for (let i = 0; i < array.length; i ++) {
        map.set(array[i], map.get(array[i]) + 1); 
    }
    // Map의 값 부분만 뽑아내서 배열로 반환하기 
    const arr = Array.from(map.values()); 
    // 최빈값을 찾기 
    const max = Math.max(...arr);
    // 최빈값이 여러개라면 -1, 아니라면 최빈값에 해당하는 원소 반환하기 
    if (arr.indexOf(max) != arr.lastIndexOf(max)) {
        return -1; 
    } else {
        return arr.indexOf(max); 
    }
}