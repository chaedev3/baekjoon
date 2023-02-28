function solution(my_string) {
    let result = 0; 
    for (i = 0; i < my_string.length; i++) {
        if(parseInt(my_string[i])) {
            result += parseInt(my_string[i])
        }  
    }
    return result
}