<template>
  <div>
    <Header />
    <!-- 左边栏 -->
    <div class="wrap">
      <div class="leftnav">
        <div class="lefthead">
          <div>导航列表</div>
          <span>描述：监控系统分类</span>
        </div>
        <ul>
          <li :class="activeLi==1?'active':''"
            @click="li(1)">
            <img src="../assets/img/hostmanage.png"
              alt=""
              class="navicon"> 设备管理
          </li>
          <li :class="activeLi==2?'active':''"
            @click="li(2)">
            <img src="../assets/img/syshost.png"
              alt=""
              class="navicon"> 系统监控
          </li>
          <li :class="activeLi==3?'active':''"
            @click="li(3)">
            <img src="../assets/img/warn.png"
              alt=""
              class="navicon"> 告警管理
          </li>

        </ul>
      </div>
      <div class="rightcon">
        <div class="rightwrap">
          <router-view></router-view>
        </div>

      </div>
    </div>

  </div>
</template>
<script>
import Header from '../components/Header'
export default {
  data () {
    return {
      activeLi: 1,
      bread: ''
    }
  },
  methods: {
    li (id) {
      this.activeLi = id
      switch (id) {
        case 1:
          this.$router.push('/sbmonitor')
          break;
        case 2:
          this.$router.push('/sysmonitor')
          break;
        case 3:
          this.$router.push('/warning')
          break;
      }
    }
  },
  components: {
    Header
  }

}
</script>
<style scoped>

.leftnav li:hover {
  color: #2395f1;
}
.leftnav li {
  padding-left: 24px;
  height: 40px;
  line-height: 40px;
  text-decoration: none;
  list-style: none;
  font-size: 16px;
  transition: all 0.3s;
  cursor: pointer;
  margin: 5px 0;
}
.active {
  background-color: #f0fbff;
  border-right: 3px solid #2395f1;
  color: #2395f1;
}

/* 黑头 */
.lefthead {
  background-color: #32363a;
  color: hsla(0, 0%, 100%, 0.85);
  padding: 24px;
}
.lefthead div {
  font-size: 24px;
  margin-bottom: 10px;
}
.lefthead span {
  font-size: 14px;
}
.navicon {
  width: 18px;
  height: 18px;
  position: relative;
  top: 3px;
}
</style>