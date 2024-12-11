// obj 동일한 지 판별해주는 함수
function is_equal(obj1, obj2) { 
  const key1 = Object.keys(obj1);
  const key2 = Object.keys(obj2);
  // key가 다르면 out 
  if (key1.length !== key2.length) return false;

  // key 돌면서 다른 거 있는 지 확인
  for (const key of key1) {
    const val1 = obj1[key];
    const val2 = obj2[key]; 
    if (val1 !== val2) {
      return false;
    }
  }
  return true;
}


function solution(want, number, discount) {
    let answer = 0;
  // 1. want, number를 obj 로 변환
  const want_obj = {};
  for (const index in want) {
    want_obj[want[index]] = number[index];
  }

  // 2. 가입한 날짜 ~ 10까지 포함되는 품목 구하는 obj
  for (let i=0; i < discount.length -9; i++) {
    const discount_obj = {};
    for (let j=i; j < i + 10; j++) {
      if (discount_obj[discount[j]]) {
        discount_obj[discount[j]] += 1
      } else {
        discount_obj[discount[j]] = 1
      }
    }
    // 3. 1에서 구한 obj & 2에서 구한 obj 같은 지 봐야함
    if (is_equal(want_obj, discount_obj)) {
      answer += 1;
    }
  }
  return answer;
}