function solution(land) {
    const n = land.length;
    const m = 4;

    const dp = Array.from(Array(n), () => new Array(m).fill(0));
    dp[0] = land[0];


    for (let i=1; i < n; i++) {
      // 0열 일 때
      dp[i][0] = land[i][0] + Math.max(dp[i-1][1],dp[i-1][2],dp[i-1][3]);
      // 1열 일 때
      dp[i][1] = land[i][1] + Math.max(dp[i-1][0],dp[i-1][2],dp[i-1][3]);
      // 2열 일 때
      dp[i][2] = land[i][2] + Math.max(dp[i-1][0],dp[i-1][1],dp[i-1][3]);
      // 3열 일 때
      dp[i][3] = land[i][3] + Math.max(dp[i-1][0],dp[i-1][1],dp[i-1][2]);
    }

    return Math.max(...dp[n - 1]);
}