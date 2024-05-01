/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let arr = Array(functions.length)
        let count = functions.length;
        functions.forEach((fn, index) => {
            fn()
            .then(val => 
            {arr[index] = val
                if (--count === 0){
                resolve(arr)

            }

            })
            .catch(reason => reject(reason));
        });
            

    });

    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */