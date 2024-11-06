function solution(prices) {
prices.reverse();
let answer = []; 
while (prices.length > 0) {
  const top = prices.pop();
  let result = 0;
  for (let i=prices.length - 1; i > -1; i--) {
    if (top <= prices[i]) {
      result += 1
    } else {
      result += 1 
      break
    }
  }
  answer.push(result)
}

return answer
}