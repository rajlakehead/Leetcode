/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */

var flat = function (arr, n) {
    const res = []

    function helper(arr, depth){
        
        arr.forEach((value) => {
            if (typeof value === 'object' && depth < n) {
                helper(value, depth + 1)
            }
            else{
                res.push(value);
            }
        });

    }

    helper(arr, 0)
    return res
    
};