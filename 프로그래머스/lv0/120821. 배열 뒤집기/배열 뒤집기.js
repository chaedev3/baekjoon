function solution(num_list) {
    let reverse_list = [] 
    for(let i = num_list.length - 1; i >= 0 ; i--) {
        reverse_list.push(num_list[i]) 
    }
    return reverse_list
}