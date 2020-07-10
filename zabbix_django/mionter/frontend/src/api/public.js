// 定义公共函数
exports.install = function (Vue) {
    Vue.prototype.trim = (str) => {//清除两边空格
        return str.replace(/(^\s*)|(\s*$)/g, '');
    };
    Vue.prototype.transformTimeStamp = (ev) => {//时间格式化
        return new Date(parseInt(ev) * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ');
    };
    //给Number类型增加一个add方法，调用起来更加方便。
    Vue.prototype.sub = (arg1, arg2) => {
        var r1, r2, m, n;
        try { r1 = arg1.toString().split(".")[1].length } catch (e) { r1 = 0 }
        try { r2 = arg2.toString().split(".")[1].length } catch (e) { r2 = 0 }
        m = Math.pow(10, Math.max(r1, r2));
        n = (r1 >= r2) ? r1 : r2;
        return ((arg1 * m - arg2 * m) / m).toFixed(n);
    }
};