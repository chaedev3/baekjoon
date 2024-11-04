function solution(numbers) {
    const l = numbers.length;
    const answer = [];
    for (let i = 0; i < l; i ++) {
        for (let j = i + 1; j < l; j ++) {
            answer.push(numbers[i] + numbers[j]);
        }
    }

    const result = [...new Set(answer)] 
    result.sort((a, b) => a - b)
    return result;
}