import axios from 'axios'

let server = axios.create({
    baseURL: 'http://122.70.157.50:18310', //请求url
    timeout: 15000, //超时处理
    withCredentials: true, //是否跨域
});
server.interceptors.request.use(
    config => {
        let token = localStorage.getItem('token')
        let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
        config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
        if (token) {
            config.headers.authorization = 'JWT ' + token
        }
        return config
    }, err => {
        // 对请求错误做些什么
        console.log(err)
        return Promise.reject(err)
    })

// 二、响应拦截器 忽略
server.interceptors.response.use(
    res => res, err => {
        try {
            if (err.response.statusText === 'Unauthorized') {
                localStorage.setItem('token', '')
            }
        } catch (error) {
            return Promise.reject(err)
        }
    }
)

export default server