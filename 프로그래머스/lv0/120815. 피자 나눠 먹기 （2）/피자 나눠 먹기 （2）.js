function solution(n) { 
    const array = [1, 2, 3, 6]
    let minV = 10 ** 7 + 1 
    array.forEach((e) => { 
        if (n % e === 0) {
            const pizza = e * (n / e) * (6 / e) 
            if (minV > pizza) {
                 minV = pizza 
            }
        }  
    })
    return minV / 6
} 

