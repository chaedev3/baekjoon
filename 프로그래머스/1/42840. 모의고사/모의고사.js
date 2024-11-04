function solution(answers) {
    const pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];
    const answer = [];
    
    for (let i=0; i < pattern.length; i++) {
        let result = 0;
        for (let j=0; j< answers.length; j++) {
            if (answers[j] === pattern[i][j % pattern[i].length]) {
                result += 1;
            }
        }
        answer.push(result) 
    }
    const max_val = Math.max(...answer);
    const a =[]
    for (let i=0; i <answer.length; i++){
        if(max_val === answer[i]) {
            a.push(i + 1)
        }
    }
    return a
}