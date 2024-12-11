function solution(record) {
    const obj = {};

    for (const r of record) {
      const arr = r.split(" ");
      const [command, uid, name] = arr;
      if (command === 'Enter' || command === 'Change') {
        obj[uid] = name;
      }
    }
    const answer = [];
    for (const r of record) {
      const arr = r.split(" ");
      const [command, uid, name] = arr;


      if (command === 'Enter') {
        answer.push(`${obj[uid]}님이 들어왔습니다.`);
      } else if (command === 'Leave') {
        answer.push(`${obj[uid]}님이 나갔습니다.`);
      }

    }
    return answer;
}