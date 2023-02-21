function solution(numer1, denom1, numer2, denom2) {
    let top = numer1 * denom2 + numer2 * denom1; 
    let bottom = denom1 * denom2 
    let maxV = 1; 
    for(let i = 1; i <= top; i ++) {
        if (top % i === 0 && bottom % i === 0) {
            maxV = i 
        }
    }
    return [top / maxV, bottom / maxV]; 
}