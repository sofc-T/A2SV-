/**
 * @param {number[]} number
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(number, target) {
    for (var i = 0; i < number.length; i++){
        for (var j = 0; j < number.length; j++){
            if ( number[i] + number[j] == target){
                if (i != j ){
                    return [i , j ];
                }  

            }

        }
    } return [-1]
    
};