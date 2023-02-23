function solution(strlist) {
    let lengthList = [] 
    strlist.forEach((e) => {
        lengthList.push(e.length)
    })
    return lengthList 
}