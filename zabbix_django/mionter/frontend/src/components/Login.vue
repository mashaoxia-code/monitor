<template>
  <div class="container">
    <div class="form">
      <div class="login_img">
        <img src="../assets/img/head.png"
          alt="">
      </div>
      <div class="form_title">欢迎登录Zabbix</div>
      <div>
        <div>
          <div>
            <img src="../assets/img/user.png"
              alt=""
              class="icon">
            <input type="text"
              placeholder="用户名"
              v-model="username">
          </div>
          <div>
            <img src="../assets/img/password.png"
              alt=""
              class="icon">
            <input type="password"
              v-model="password"
              placeholder="密码"
              v-on:keyup.13="onSubmit">
          </div>
          <button @click="
              onSubmit">登&emsp;录</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { loginSubmit } from '../api/api'
export default {
  data () {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    onSubmit () {
      if (!this.username) {
        this.$message.error('用户名不能为空');
        return
      }
      if (!this.password) {
        this.$message.error('密码不能为空');
        return
      }
      var data = {
        username: this.trim(this.username),
        password: this.trim(this.password)
      }
      loginSubmit(data).then(res => {
        console.log(res)
        localStorage.setItem('token', res.data.token)
        this.$message({
          message: '登录成功',
          type: 'success'
        });
        localStorage.setItem('zabbix-name', this.trim(this.username))
        this.$router.push({
          path: '/',
          query: {
            username: this.trim(this.username)
          }
        })
      }).catch(err => {
        console.log(err)
        this.$message.error('用户名和密码有误');
      })
    }
  },
}
</script>
<style scoped>
.container {
  height: 100vh;
  width: 100%;
  background-size: 100% 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url("../assets/img/back.png") no-repeat;
  background-size: 100% 100%;
}
.form {
  text-align: center;
  border-radius: 5px;
  color: rgba(13, 27, 62, 0.65);
  background: #fff;
  border: 1px solid #e9e9e9;
  padding: 2% 4%;
  width: 420px;
  position: relative;
}
.form span {
  display: inline-block;
  min-width: 70px;
}
.form div {
  margin-bottom: 15px;
}
.form_title {
  text-align: center;
  font-weight: 200;
  color: #2e2e5a;
  font-size: 28px;
  padding: 20px 0;
  padding-top: 45px;
}
.form button {
  border-radius: 5px;
  background-color: #1473cc;
  background-image: linear-gradient(90deg, #6d69fe 0, #48a0fa) !important;
  border: none !important;
  color: #fff;
  font-weight: bold;
  width: 100%;
  height: 38px;
  text-align: center;
  margin-top: 20px;
  padding: 2px 16px;
  font-size: 13px;
  border-radius: 4px;
  cursor: pointer;
  position: relative;
}
.form input {
  padding: 6px 9px;
  width: 100%;
  color: rgba(13, 27, 62, 0.65);
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  transition: all 0.3s;
  height: 42px;
  line-height: 42px;
  padding-left: 20px;
}
.icon {
  position: absolute;
  width: 10px;
  height: 10px;
  margin-top: 16px;
  margin-left: 7px;
}
.login_img {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: -75px;
  margin-bottom: 0 !important;
}
.login_img img {
  width: 150px;
  height: 150px;
}
</style>