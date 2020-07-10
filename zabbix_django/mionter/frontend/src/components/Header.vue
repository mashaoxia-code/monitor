<template>
  <div class="head">
    <div class="title">
      <a href="/">Zabbix 监控系统</a>
      <span class="item logout"
        @click="logout">退出登录</span>
      <span class="item">欢迎您，{{this.$route.query.username || username}}</span>

    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      username: '',
    }
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      this.$router.push('/login')
    },
  },
  mounted () {
    this.username = localStorage.getItem('zabbix-name')
  }
}
</script>
<style scoped>
.head {
  background: #32363a;
  height: 60px;
  line-height: 60px;
  width: 100%;
  box-shadow: 0 6px 0 0 rgba(0, 0, 0, 0.01), 0 15px 32px 0 rgba(0, 0, 0, 0.06);
}
.title {
  padding-left: 24px;
  font-size: 18px;
  color: #fff;
}
.title a {
  text-decoration: none;
  color: #fff;
}
.item {
  float: right;
  padding-right: 24px;
  color: #fff;
  font-size: 16px;
}
.logout {
  font-size: 15px;
  color: hsla(0, 0%, 100%, 0.67);
  cursor: pointer;
}
.logout:hover {
  color: #fff;
}
</style>
