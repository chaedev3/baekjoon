function validate_num(x, y) {
  if (x >= -5 && x <= 5 && y >= -5 && y <= 5) {
    return true
  } else {
    return false 
  }
}

function solution(dirs) {
   
    let result = [[0, 0]];
    let unique_dir = new Set();

    for (let i=0; i < dirs.length; i++) {
      const dir = dirs[i];
      const [a, b] = result[result.length - 1];
      if (dir === 'U' && validate_num(a + 1, b)) {
        result.push([a + 1, b]);
        unique_dir.add(`${a},${b},${a+1},${b}`);
        unique_dir.add(`${a+1},${b},${a},${b}`);
      } else if (dir === 'D' && validate_num(a - 1, b)) {
        result.push([a - 1, b]);
        unique_dir.add(`${a},${b},${a-1},${b}`);
        unique_dir.add(`${a-1},${b},${a},${b}`);
      } else if (dir === 'R' && validate_num(a, b + 1)) {
        result.push([a, b + 1]);
        unique_dir.add(`${a},${b},${a},${b+1}`);
        unique_dir.add(`${a},${b+1},${a},${b}`);
      } else if (dir === 'L' && validate_num(a, b - 1)) {
        result.push([a, b - 1]);
        unique_dir.add(`${a},${b},${a},${b-1}`);
        unique_dir.add(`${a},${b-1},${a},${b}`);
      }
    }

    return unique_dir.size / 2;
}