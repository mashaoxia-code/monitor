<template>
  <div class="detail">
    <Header />
    <!-- 左边栏 -->
    <div class="wrap">
      <div class="leftnav">
        <div class="lefthead">
          <el-input v-model="input"
            placeholder="请输入内容"></el-input>
          <button class="button"
            @click="addOne">添加应用</button>
        </div>
        <ul>
          <li :class="activeLi==index?'active':''"
            class="detail_li"
            v-for="(item,index) in leftData"
            :key="index"
            @click="changeItem(item.applicationid,index)">
            <i class="el-icon-tickets"></i> {{item.name}}
            <!-- 操作 -->
            <span class="btns">
              <span @click.stop="deletehostApp(item)">
                <el-tooltip class="item"
                  effect="dark"
                  content="删除"
                  placement="top-start"
                  @>
                  <el-button><i class="el-icon-delete"></i></el-button>
                </el-tooltip>
              </span>
              <span @click.stop="editOne(item)">
                <el-tooltip class="item"
                  effect="dark"
                  content="编辑"
                  placement="top-start">
                  <el-button><i class="el-icon-edit"></i></el-button>
                </el-tooltip>
              </span>
            </span>
          </li>
        </ul>
      </div>
      <div class="rightcon">
        <router-view />
      </div>
    </div>

    <!-- 弹出框 -->
    <div class="detail">
      <el-dialog :title="type==1?'添加应用项':'修改应用项'"
        :visible.sync="dialogVisible"
        width="30%">
        <el-form ref="form"
          :model="form"
          label-width="80px">
          <el-form-item label="应用名称:">
            <el-input v-model="form.name"></el-input>
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
import { getHostApp, getItem, PutHostApp, DeleteHostApp, AddHostApp } from '../../api/api'
import Header from '../../components/Header'
export default {
  data () {
    return {
      activeLi: 0,
      input: '',
      leftData: '',
      dialogVisible: false,
      form: {
        name: '',
      },
      type: 1,
      hostid: '',
      hostAppItem: ''
    }
  },
  methods: {
    changeItem (applyid, index) {
      this.activeLi = index
      this.$router.push({
        path: `/detail/${this.hostid}/${applyid}`,
      })
    },
    addOne () {
      this.dialogVisible = true
      this.type = 1

      this.form.name = ''
    },
    editOne (item) {
      this.dialogVisible = true
      this.type = 2
      this.hostAppItem = item

      this.form.name = item.name
    },
    sure () {
      if (!this.trim(this.form.name)) {
        this.$message.error('应用项名称不能为空');
        return
      }
      //添加
      if (this.type == 1) {
        this.addHostApp()
      } else if (this.type == 2) {
        this.editHostApp()
      }
    },
    addHostApp () {
      var data = {
        "name": this.trim(this.form.name),
      }
      AddHostApp(this.hostid, data).then(res => {
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
    editHostApp () {
      var obj = {
        "name": this.trim(this.form.name),
        "applicationid": this.hostAppItem.applicationid
      }
      PutHostApp(this.hostid, obj).then(res => {
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
    // 删除
    deletehostApp (item) {
      this.$confirm('你确定删除吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        var data = {
          "applicationid": item.applicationid
        }
        DeleteHostApp(this.hostid, { 'data': data }).then(res => {
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
    },
    queryList () {
      getHostApp(this.$route.params.hostid).then(res => {
        this.leftData = res.data.data
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted () {
    this.hostid = this.$route.params.hostid
    getHostApp(this.$route.params.hostid).then(res => {
      this.leftData = res.data.data
      this.leftData.map((el, index) => {
        if (this.$route.params.applyid == el.applicationid) {
          this.activeLi = index
        }
      })
    }).catch(err => {
      console.log(err)
    })
  },
  components: {
    Header
  }

}
</script>
<style scoped>
.lefthead {
  background-color: #ddd;
  color: hsla(0, 0%, 100%, 0.85);
  padding: 12px;
  display: flex;
  justify-content: space-between;
}
.leftnav li {
  color: rgba(13, 27, 62, 0.65);
  margin: 5px;
  margin-left: 20px;
  padding: 3px 5px;
  border-radius: 2px;
  height: 30px;
  line-height: 30px;
  list-style: none;
  font-size: 14px;
  transition: all 0.3s;
  cursor: pointer;
  box-sizing: content-box;
}
.active {
  background-color: #d5ebfc;
}

.item {
  float: right;
  font-weight: normal;
}

.button {
  float: right;
  position: relative;
  top: 2px;
}
.btns {
  display: none;
}
.detail_li:hover .btns {
  display: inline;
}
.btns .el-button {
  border: none;
  background: none;
  padding: 0 5px;
  font-size: 14px;
  color: rgba(39, 56, 72, 0.85);
  position: relative;
  bottom: 3px;
}
.btns .el-button:hover {
  color: #2395f1;
}
</style>