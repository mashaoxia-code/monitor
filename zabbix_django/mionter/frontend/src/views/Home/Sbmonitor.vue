<template>
  <div>
    <div class="tab">
      <div v-for="(item,index) in ['主机列表','主机组列表','模板列表']"
        :key="index"
        @click="tabSwitch(index)"
        :class="tabIndex==index?'active':''"
        :style="index==2?'border-right:none':''">
        {{item}}
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  data () {
    return {
      tabIndex: 0,
    }
  },
  methods: {
    tabSwitch (index) {
      this.tabIndex = index
      if (index == 0) {
        this.$router.push('/host1')
      } else if (index == 1) {
        this.$router.push('/host2')
      } else {
        this.$router.push('/host3')
      }
    }
  },
  mounted () {
    if (this.$route.path == '/host1') {
      this.tabIndex = 0
    } else if (this.$route.path == '/host2') {
      this.tabIndex = 1
    } else if (this.$route.path == '/host3') {
      this.tabIndex = 2
    }
  },
  watch: {
    $route: {
      handler (newValue, oldValue) {
        if (this.$route.path == '/host1') {
          this.tabIndex = 0
        } else if (this.$route.path == '/host2') {
          this.tabIndex = 1
        } else if (this.$route.path == '/host3') {
          this.tabIndex = 2
        }
      },
      deep: true
    }
  }
}
</script>
<style scoped>
.tab {
  background-color: #eceef1;
  display: flex;
  margin-bottom: 20px;
  margin-top: -15px;
  margin-left: -15px;
  color: rgba(13, 27, 62, 0.65);
  margin-right: -15px;
}
.tab div {
  margin: 0;
  border-right: 2px solid #e9e9e9;
  border-bottom: 1px solid #e9e9e9;
  border-radius: 4px 4px 0 0;
  border-left: 0;
  background: #fafafa;
  padding: 0 16px;
  transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
  line-height: 38px;
  cursor: pointer;
}
.tab .active {
  border-bottom: none !important;
  background: #fff;
  color: #2395f1;
}
.tab div:hover {
  color: #4fb6ff;
}
</style>