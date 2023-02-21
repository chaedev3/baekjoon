function solution(n) {
    if (n % 2 === 0) {
        return (n * (n + 2)) / 4;  
    } else {
        return ((n - 1) * (n + 1)) / 4; 
    }
}