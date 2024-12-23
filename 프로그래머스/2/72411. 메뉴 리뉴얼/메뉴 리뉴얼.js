function combination(arr, n) {
    if (n === 1) return arr.map((v) => [v]);
    const result = [];
    
    arr.forEach((fixed, idx, arr) => {
        const newArr = arr.slice(idx+1);
        const combins = combination(newArr, n - 1);
        const combine = combins.map((v) => [fixed, ...v]);
        result.push(...combine);
    })
    
    return result;
}

function solution(orders, course) {
    const answer = [];
    for (const cour of course) {
        const menu = [];
        for (const order of orders) {
            const order_arr = order.split('').sort();
            const a = combination(order_arr, cour);
            menu.push(...a);
        }
        const obj = {};
        for (const me of menu) {
            const key = me.join('');
            obj[key] = (obj[key] || 0) + 1;
        }
        const max = Math.max(...Object.values(obj));
        if (max > 1) {
            for (const [key, value] of Object.entries(obj)) {
                if (value === max) {
                    answer.push(key);
                }
            }
        }
    }
    return answer.sort();
}