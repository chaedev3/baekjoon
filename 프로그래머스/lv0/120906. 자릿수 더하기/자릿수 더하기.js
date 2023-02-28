function solution(n) {
    let result = 0 
    for (i = 1000000; i >= 1; i /= 10) {
        result += Math.floor(n / i)
        n = n - Math.floor(n / i) * i 
    }
    return result
}