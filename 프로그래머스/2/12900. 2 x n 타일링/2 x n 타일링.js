function solution(n) {
    const arr = [];
    arr[0] = 1;
    arr[1] = 2;

    for (let i=2; i < n; i++) {
      
      arr[i] = (arr[i - 1] + arr[i - 2]) > 1000000007 ? (arr[i - 1] + arr[i - 2]) % 1000000007: arr[i - 1] + arr[i - 2];
    }

    return arr[n - 1];
}