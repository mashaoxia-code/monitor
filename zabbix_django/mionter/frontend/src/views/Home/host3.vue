<template>
  <div>
    <h2 class="detail_title">全部模板共 ({{templatelist.length}}) 个</h2>

    <table class="detail_table">
      <thead>
        <tr>
          <td>模板名称</td>
          <td>模板描述</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item,index) in templatelist"
          :key="index">
          <td class="td1"
            @click="templateDetail(item.templateid)">{{item.name}}</td>
          <td class="td2">{{item.description?item.description:'暂无描述'}}</td>
        </tr>
      </tbody>
    </table>

    <el-dialog title="standard template"
      :visible.sync="templateVisible"
      width="80%">
      <el-select v-model="value"
        placeholder="请选择"
        @change="changeApplication">
        <el-option v-for="item in options"
          :key="item.applicationid"
          :label="item.name"
          :value="item.applicationid">
        </el-option>
      </el-select>
      <h3 v-if="!listdata"
        class="h3item">该项没有内容！</h3>
      <table class="detail_table"
        v-else>
        <thead>
          <tr>
            <td>名称</td>
            <td>key_</td>
            <td>delay</td>
            <td>history</td>
            <td>trends</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in listdata"
            :key="item.itemid">
            <td>{{item.name}}</td>
            <td>{{item.key_}}</td>
            <td>{{item.delay}}</td>
            <td>{{item.history}}</td>
            <td>{{item.trends}}</td>
          </tr>
        </tbody>
      </table>
      <span slot="footer"
        class="dialog-footer">
        <el-button @click="templateVisible = false">取 消</el-button>
        <el-button type="primary"
          @click="templateVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import { getTemplate, getTemplateApplication, getTemplateItem } from '../../api/api'
export default {
  data () {
    return {
      templatelist: '',
      templateVisible: false,
      options: [],
      value: '',
      listdata: [],
      template: ''
    }
  },
  methods: {
    templateDetail (templateid) {
      this.templateVisible = true
      this.template = templateid
      getTemplateApplication(templateid).then(res => {
        this.options = res.data.data
        this.value = this.options[0].applicationid
        this.queryItem(templateid, this.value)
      })
    },
    queryItem (templateid, applicationid) {
      getTemplateItem(templateid, applicationid).then(res => {
        this.listdata = res.data.data
      })
    },
    changeApplication () {
      this.queryItem(this.template, this.value)
    }
  },
  mounted () {
    getTemplate().then(res => {
      this.templatelist = res.data.data
    }).catch(err => {

    })
  }
}
</script>
<style scoped>
.td1 {
  color: #2395f1;
  width: 50%;
  cursor: pointer;
}
.td2 {
  width: 50%;
}

.el-select {
  float: right;
  margin-bottom: 20px;
}
</style>
