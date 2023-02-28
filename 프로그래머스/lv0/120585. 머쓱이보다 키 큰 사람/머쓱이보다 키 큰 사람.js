function solution(array, height) {
    let result = 0 
    array.forEach((e) => {
        if (e > height) {
            result += 1 
        }
    })
    return result 
}