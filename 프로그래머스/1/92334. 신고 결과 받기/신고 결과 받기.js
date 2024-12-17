function solution(id_list, report, k) {
    // 신고한 유저 목록을 관리
    const memberList = {};
    // 신고당한 횟수를 관리
    const countList = {};

    // 신고를 처리하는 부분
    for (const r of report) {
      const [a, b] = r.split(" ");

      // 신고한 유저가 이미 신고한 유저 목록을 Set으로 관리하여 중복 신고를 피함
      if (!memberList[b]) {
        memberList[b] = new Set();  // Set을 사용해 중복 신고를 방지
      }
      memberList[b].add(a);  // 중복 신고를 자동으로 제외시킴
    }

    // 신고당한 횟수 확인
    for (const name of Object.keys(memberList)) {
      if (memberList[name].size >= k) {
        for (const n of memberList[name]) {
          countList[n] = (countList[n] || 0) + 1;
        }
      }
    }

    const answer = [];

    for (const id of id_list) {
      console.log(id);
      answer.push(countList[id] || 0);
    }

    return answer
}