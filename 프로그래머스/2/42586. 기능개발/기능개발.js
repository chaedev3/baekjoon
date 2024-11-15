function solution(progresses, speeds) {
    const remain_prog = progresses.map(num => 100 - num);
const result = [];
for (let i = 0; i < progresses.length; i ++) {
  result.push(Math.ceil(remain_prog[i] / speeds[i]));
}
console.log(result);
const answer = [];
let num = 1;
let top = result.shift();
while (result.length > 0) {
  if (top >= result[0]) {
    result.shift();
    num += 1;
  } else {
    answer.push(num);
    num = 1;
    top = result.shift();
  }
}
answer.push(num);

    return answer;
}