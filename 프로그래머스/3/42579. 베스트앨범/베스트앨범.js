function solution(genres, plays) {
    const answer = [];
    // genre 별로 총 play 횟수 구하는 obj
    // genre 를 key로 가지고 [index, play 수] value
    const genreObj = {};
    const playObj = {};
    
    for (let i=0; i < genres.length; i++){
        if (genreObj[genres[i]]) {
            genreObj[genres[i]] += plays[i];
            playObj[genres[i]].push([i, plays[i]]);
        } else {
            genreObj[genres[i]] = plays[i];
            playObj[genres[i]] = [[i, plays[i]]];
        }
    }

    // 총 play 횟수가 많은 genre가 나오도록 정렬
    const sortedGenre = Object.keys(genreObj).sort((a, b) => {
       return genreObj[b] - genreObj[a]; 
    });
    
    // genre 순대로 play 횟수 상위 2개씩 넣어줌
    for (const genre of sortedGenre) {
        const sortedPlay = playObj[genre].sort((a, b) => {
            return a[1] === b[1] ? a[0] - b[0]: b[1]- a[1];
        })
        // console.log(sortedPlay);
        answer.push(...sortedPlay.slice(0, 2).map(play => play[0]));
    }
    return answer;
}