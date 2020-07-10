<template>
  <div class="rightwrap">
    <div class="list">
      <div>
        <h2 class="detail_title">全部监控项共 ({{data.length}}) 个</h2>
        <button class="button"
          @click="addOne">添加监控项</button>
      </div>
      <div>
        <h3 v-if="!data"
          class="h3item">该项没有内容,请查看其它内容</h3>
        <table class="detail_table"
          v-else>
          <thead>
            <tr>
              <td>名称</td>
              <td>key_</td>
              <td>delay</td>
              <td>history</td>
              <td>trends</td>
              <td>status</td>
              <td style="text-align:center">操作</td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item,index) in data"
              :key="index">
              <td>{{item.name}}</td>
              <td>{{item.key_}}</td>
              <td>{{item.delay}}</td>
              <td>{{item.history}}</td>
              <td>{{item.trends}}</td>
              <td>
                <span class="status"
                  :class="item.state==0?'green':'red'">
                </span>
                <span>{{item.state==0?'正常':'出错'}}</span>
              </td>
              <td>
                <button type="button"
                  class="icoBtn"
                  @click="deleteitem(item)">
                  <i class="el-icon-delete"> 删除</i>
                </button>
                <button type="button"
                  @click="editOne(item)"
                  class="icoBtn">
                  <i class="el-icon-edit"> 编辑</i>
                </button>
              </td>

            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 弹出框 -->
    <div class="detail">
      <el-dialog :title="type==1?'添加监控项':'修改监控项'"
        :visible.sync="dialogVisible"
        width="50%">
        <el-form ref="form"
          :model="form"
          label-width="80px">
          <el-form-item label="应用名称:">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="key:">
            <el-select v-model="form.key"
              placeholder="请选择key">
              <el-option v-for="item in keys"
                :key="item.itemid"
                :label="item.key_"
                :value="item.key_">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <span slot="footer"
          class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary"
            @click="sure">确 定</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>
<script>
import { getItem, DeleteItem, PutItem, AddItem, getKey } from '../../api/api'
export default {
  data () {
    return {
      hostid: '',
      applyid: '',
      data: '',
      dialogVisible: false,
      type: 1,
      form: {
        name: '',
        key: ''
      },
      item: '',
      keys: ''
    }
  },
  methods: {
    queryList () {
      this.hostid = this.$route.params.hostid
      this.applyid = this.$route.params.applyid
      getItem(this.hostid, this.applyid).then(res => {
        if (res.data.data) {
          this.data = res.data.data
        }

      }).catch()
    },
    addOne () {
      this.dialogVisible = true
      this.type = 1

      this.form.name = ''
      this.form.key = ''
    },
    editOne (item) {
      this.dialogVisible = true
      this.type = 2
      this.item = item

      this.form.name = item.name
      this.form.key = item.key_
    },
    sure () {
      if (!this.trim(this.form.name)) {
        this.$message.error('监控项名称不能为空');
        return
      }
      if (!this.trim(this.form.key)) {
        this.$message.error('key名称不能为空');
        return
      }
      //添加
      if (this.type == 1) {
        this.addItem()
      } else if (this.type == 2) {
        this.editItem()
      }

    },
    addItem () {
      var data = {
        "name": this.trim(this.form.name),
        "key_": this.trim(this.form.key)
      }
      AddItem(this.hostid, this.applyid, data).then(res => {
        if (res.data.code == 200) {
          this.dialogVisible = false
          this.queryList()
          this.$message({
            message: '添加成功',
            type: 'success'
          });
        } else {
          this.$message.error(res.data.msg)
        }
      }).catch(err => {
        this.$message.error('添加失败')
      })
    },
    editItem () {
      var obj = {
        "name": this.trim(this.form.name),
        "key_": this.trim(this.form.key),
        "itemid": this.item.itemid
      }
      PutItem(this.hostid, this.applyid, obj).then(res => {
        if (res.data.code == 200) {
          this.dialogVisible = false
          this.queryList()
          this.$message({
            message: '修改成功',
            type: 'success'
          });
        } else {
          this.$message.error(res.data.msg)
        }
      }).catch(err => {
        this.$message.error('修改失败')
      })
    },
    deleteitem (item) {
      this.$confirm('你确定删除吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        var data = {
          "itemid": item.itemid
        }
        DeleteItem(this.hostid, this.applyid, { 'data': data }).then(res => {
          if (res.data.code == 200) {
            this.queryList()
            this.$message({
              message: '删除成功',
              type: 'success'
            });
          } else {
            this.$message.error(res.data.msg)
          }
        }).catch(err => {
          this.$message.error('删除失败')
        })

      }).catch(() => {
      });
    }
  },
  mounted () {
    this.queryList()
    getKey().then(res => {
      this.keys = res.data.data
    }).catch(err => {

    })
  },
  watch: {
    $route: {
      handler (newValue, oldValue) {
        this.data = ''
        getItem(newValue.params.hostid, newValue.params.applyid).then(res => {
          if (res.data.data) {
            this.data = res.data.data
          }

        }).catch()
      },
      deep: true
    }
  }
}
</script>

<style >
.button {
  float: right;
  position: relative;
  top: 2px;
}
</style>