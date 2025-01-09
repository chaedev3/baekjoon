function solution(tri) {
    const n = tri.length;
    const result = Array.from(Array(n), () => Array(n).fill(0));

    result[n-1] = tri[n-1];

    for (let i=n-2; i>=0; i--) {
      for (let j=0; j <i+1; j++) {
        result[i][j] = tri[i][j] + Math.max(result[i+1][j],result[i+1][j+1]);
      }
    }
    return result[0][0];
}