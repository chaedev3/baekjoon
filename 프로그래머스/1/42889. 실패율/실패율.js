function solution(N, stages) {
    let result = [...new Array(N)].map((_, i) => new Array(2).fill(0));

    for (let i=0; i<stages.length;i++) {
      const num = stages[i];
      if (num === N + 1) {
        result.map((arr, i) => {
          arr[1] += 1; 
          return arr;}
        )
      } else {
        result[num - 1][0] += 1
        result.map((arr, i) => {
          if (i < num) {
            arr[1] += 1;
            return arr;
          }
        })
      }
    }

    let answer = [];
    for (const [a, b] of result.entries()) {
      const num1 = b[0];
      const num2 = b[1];

      answer.push([num1 / num2, a]);
    }

    answer.sort((a, b) => b[0] - a[0]);

    let final_result = answer.map((arr, i) => {
      const num = arr[1];
      return num + 1
    })
    return final_result
    }