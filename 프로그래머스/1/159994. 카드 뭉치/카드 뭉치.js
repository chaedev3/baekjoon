function solution(cards1, cards2, goal) {
    let result = "Yes"
while (goal.length > 0) {
  let need_word = goal.shift();

  if (cards1[0] === need_word) {
    cards1.shift();
  } else if (cards2[0] === need_word) {
    cards2.shift();
  } else {
    result = "No";
    break

  }
}

    return result;

}