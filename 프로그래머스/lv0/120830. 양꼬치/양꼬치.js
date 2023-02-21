function solution(n, k) {
    if (10 <= n) {
        return 12000 * n + 2000 * k - 2000 * parseInt(n / 10)
    } else {
        return 12000 * n + 2000 * k
    }; 
}