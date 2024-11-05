function solution(arr1, arr2) {
    let result = [...new Array(arr1.length)].map((_, i)=> new Array(arr2[0].length).fill(0));

for (let i=0; i < arr1.length; i ++) {
  for (let j=0; j < arr2[0].length; j ++) {
    let num = 0;
    for (let x=0; x < arr1[0].length; x++) {
      num = num + arr1[i][x] * arr2[x][j];  
    }
    result[i][j] = (num);
  }

}
    return result;
}