<template>
  <div class="sysWrap">
    <div style="color: rgba(13,27,62,.65);font-size:14px;">
      请选择主机：
      <el-select v-model="valueHost"
        @change="changeHost"
        placeholder="请选择">
        <el-option v-for="item in optionsHost"
          :key="item.hostid"
          :value="item.hostid"
          :label="item.host">
        </el-option>
      </el-select>
      <span style="display:inline-block;padding-left:30px;">请选择应用项：</span>
      <el-select v-model="valueApply"
        @change="changeApply"
        placeholder="请选择">
        <el-option v-for="item in optionsApply"
          :key="item.applicationid"
          :label="item.name"
          :value="item.applicationid">
        </el-option>
      </el-select>
    </div>
    <div>
      <h3 v-if="!data"
        class="h3item">该项没有内容,请前往设备监控设置！</h3>
      <table class="detail_table"
        v-else>
        <thead>
          <tr>
            <td>监控项</td>
            <td>接口路径</td>
            <td>刷新频率</td>
            <td>状态</td>
            <td>最新值</td>
            <td>变化</td>
            <td>更新时间</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item,index) in data"
            :key="index">
            <td class="td1">{{item.name}}</td>
            <td>{{item.key_}}</td>
            <td>{{item.delay}}</td>
            <td>
              <span class="status"
                :class="item.status==0?'green':'red'">
              </span>
              <span>{{item.status==0?'正常':'出错'}}</span>
            </td>
            <td>{{item.lastvalue}} {{item.units}}</td>
            <td>{{sub(item.lastvalue, item.prevvalue)>0?'+':''}}{{sub(item.lastvalue, item.prevvalue)}}{{item.units}}</td>
            <td>{{transformTimeStamp(item.lastclock)}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import { getHost, getHostApp, getItem } from '../../api/api'
export default {
  data () {
    return {
      optionsHost: [],
      valueHost: '',
      optionsApply: [],
      valueApply: '',
      hostid: '',
      applyid: '',
      data: ''
    }
  },
  methods: {
    queryApply (hostid) {
      if (hostid) {
        this.hostid = hostid
        getHostApp(hostid).then(res => {
          this.optionsApply = res.data.data
          this.valueApply = res.data.data[0].name
          this.applyid = res.data.data[0].applicationid
          this.queryData(this.hostid, this.applyid)
        }).catch(err => {
          console.log(err)
        })
      }
    },
    queryData (hostid, applyid) {
      getItem(hostid, applyid).then(res => {
        this.data = res.data.data
      }).catch(err => {
        console.log(err)
      })
    },
    changeHost (hostid) {
      if (hostid) {
        this.hostid = hostid
        this.valueApply = ''
        getHostApp(hostid).then(res => {
          this.optionsApply = res.data.data
          this.valueApply = res.data.data[0].name
          this.applyid = res.data.data[0].applicationid
          this.queryData(this.hostid, this.applyid)
        }).catch(err => {
          console.log(err)
        })
      }
    },
    changeApply (applyid) {
      if (applyid) {
        this.applyid = applyid
        this.queryData(this.hostid, this.applyid)
      }
    }
  },
  mounted () {
    getHost().then(res => {
      this.optionsHost = res.data.data
      this.valueHost = res.data.data[0].host
      this.hostid = res.data.data[0].hostid
      this.queryApply(this.hostid)
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>
<style>
.sysWrap .el-input__inner {
  height: 35px;
  line-height: 35px;
}
.sysWrap .el-input__icon {
  line-height: 35px;
}
</style>
<style scoped>
.td1 {
  color: #2395f1;
  cursor: pointer;
}
.status {
  bottom: 1px;
}
</style>>

