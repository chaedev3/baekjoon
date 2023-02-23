function solution(num_list) {
    let evenNum = 0 
    let oddNum = 0 

    num_list.forEach((e) => {
        if (e % 2 === 0) {
        evenNum += 1 
    } else {
        oddNum += 1 
    }
    }) 
    return [evenNum, oddNum]
}