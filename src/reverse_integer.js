/**
 * Created by Xuanyu on 5/27/2018.
 */
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    var num = x.toString();
    var flag = 0; // 0 means positive num, 1 means negative num
    if (x < 0) {
        flag = 1;
        num = num.substring(1, num.length);
    } else if (x == 0) {
        return 0;

    }
    num = num.split('').reverse();

    var count = 0;
    for (var c = 0; c < num.length; c++) {

        if (num[c] == 0) {
            count += 1;
        } else {
            break;
        }

    }
    var ans = num.slice(count);
    if (flag == 1) {
        ans = ans.join("");
        if (parseInt(ans) > Math.pow(2, 31)) {
            return 0;
        }
        return parseInt('-' + ans);
    } else {
        if (parseInt(ans.join("")) > Math.pow(2, 31)) {
            return 0;
        }
        return parseInt(ans.join(""));
    }
};