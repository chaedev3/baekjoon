function solution(board, moves) {
    const n = board.length;
    let stack = [];
    let result = 0;
    for (const [i, move] of moves.entries()) {
      for (let i=0; i < n; i++) {
        if (board[i][move-1] !== 0) {
          if (stack[stack.length - 1] === board[i][move -1]) {
            stack.pop();
            result += 2;
            board[i][move-1] = 0;
            break;
          } else {
            stack.push(board[i][move-1]);
            board[i][move-1] = 0;
            break;
          }
        }
      }
    }
     return result;
}