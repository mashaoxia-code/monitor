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
    </div>
    <div>
      <h3 v-if="!data"
        class="h3item">该项没有内容,请前往设备监控设置！</h3>
      <table class="detail_table"
        v-else>
        <thead>
          <tr>
            <td>Severity</td>
            <td>name</td>
            <td>expression</td>
            <td>opdata</td>
            <td>状态</td>
            <td>更新时间</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item,index) in data"
            :key="index">
            <td class="td1">{{item.priority}}</td>
            <td class="td2">{{item.description}}</td>
            <td >{{item.expression}}</td>
            <td >{{item.opdata}}</td>
            <td>
              <span class="status"
                :class="item.status==0?'green':'red'">
              </span>
              <span>{{item.status==0?'正常':'出错'}}</span>
            </td>
            <td>{{transformTimeStamp(item.lastchange)}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import { getHost, getTrigger, AddTrigger, PutTrigger, DeleteTrigger } from '../../api/api'
export default {
  data () {
    return {
      optionsHost: [],
      valueHost: '',
      hostid: '',
      data: ''
    }
  },
  methods: {
    queryApply (hostid) {
      if (hostid) {
        this.hostid = hostid
        getTrigger(hostid).then(res => {
          this.data = res.data.data
        }).catch(err => {
          console.log(err)
        })
      }
    },
    changeHost (hostid) {
      if (hostid) {
        this.hostid = hostid
        getTrigger(hostid).then(res => {
          this.data = res.data.data
        }).catch(err => {
          console.log(err)
        })
      }
    },
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
<style scoped>
.sysWrap .el-input__inner {
  height: 32px;
  line-height: 32px;
}
.sysWrap .el-input__icon {
  line-height: 32px;
}
.td1 {
  color: #2395f1;
  cursor: pointer;
}
.status {
  bottom: 2px;
}
.h3item {
  color: rgba(13, 27, 62, 0.55);
  font-weight: normal;
  text-align: center;
  margin-top: 18%;
}
</style>
