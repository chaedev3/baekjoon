function solution(s)
{
   const stack = [s[0]]
for (let i=1; i < s.length; i++) {
  const top = stack[stack.length - 1]
  if (top === s[i]) {
    stack.pop()
  } else {
    stack.push(s[i]) 
  }
}
let result = 0 
if (stack.length === 0) {
  result = 1 
}
  return result
}