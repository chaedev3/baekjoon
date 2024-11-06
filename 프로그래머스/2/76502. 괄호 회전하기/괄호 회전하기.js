function solution(s) {
    let result = 0
for (let i=0; i < s.length; i++) {
  const new_word = s.slice(i, s.length) + s.slice(0, i) 
  const stack = [new_word[0]]

  for (let j=1; j < s.length; j++) {
    const top = stack[stack.length - 1]
    if (top === "(" && new_word[j] === ")") {
      stack.pop() 
    } else if (top === "[" && new_word[j] === "]") {
      stack.pop()
    } else if (top === "{" && new_word[j] === "}") {
      stack.pop()
    } else {
      stack.push(new_word[j]) 
    }
  }
  if (stack.length === 0) {
    result += 1 
  }
}
    return result
}