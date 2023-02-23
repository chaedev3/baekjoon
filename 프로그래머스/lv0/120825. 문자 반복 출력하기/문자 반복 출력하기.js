function solution(my_string, n) {
    let newWords = '' 
    for(const str of my_string) {
        newWords = newWords + str.repeat(n)
    }
    return newWords
}