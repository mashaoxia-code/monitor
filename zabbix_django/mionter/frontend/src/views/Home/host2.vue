<template>
  <div>
    <div class="min_head">
      <div class="min_headl">
        全部主机组共 ({{data.length}}) 个
      </div>
      <div class="min_headr">
        <button class="button"
          @click="dialogVisibleAdd=true">添加主机组</button>
      </div>
    </div>

    <table class="detail_table">
      <thead>
        <tr>
          <td>主机组名称</td>
          <td>成员</td>
          <td class="td2"
            style="padding-right:65px">操作</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item,index) in data"
          :key="index">
          <td>{{item.name}}</td>
          <td v-if="item.hosts.length >0">
            <span v-for="el in item.hosts"
              :key="el.hostid">
              （{{el.host}}）
            </span>
          </td>
          <td v-else>
            暂无成员
          </td>
          <td class="td2">
            <button type="button"
              class="icoBtn"
              @click="deleteHostgroup(item)">
              <i class="el-icon-delete"> 删除</i>
            </button>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <button type="button"
              @click="edit(item)"
              class="icoBtn">
              <i class="el-icon-edit"> 编辑</i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 弹出框 -->
    <div class="detail">
      <el-dialog title="添加主机组"
        :visible.sync="dialogVisibleAdd"
        width="30%">
        <el-form ref="form"
          :model="form"
          label-width="80px">
          <el-form-item label="主机组名:">
            <el-input v-model="form.addname"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer"
          class="dialog-footer">
          <el-button @click="dialogVisibleAdd = false">取 消</el-button>
          <el-button type="primary"
            @click="addHostgroup">确 定</el-button>
        </span>
      </el-dialog>

      <el-dialog title="修改主机组"
        :visible.sync="dialogVisibleEdit"
        width="30%">
        <el-form ref="form"
          :model="form"
          label-width="80px">
          <el-form-item label="主机组名:">
            <el-input v-model="form.editname"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer"
          class="dialog-footer">
          <el-button @click="dialogVisibleEdit = false">取 消</el-button>
          <el-button type="primary"
            @click="editHostgroup">确 定</el-button>
        </span>
      </el-dialog>
    </div>

  </div>
</template>
<script>
import { getHostgroup, DeleteHostgroup, PutHostgroup, AddHostgroup } from '../../api/api'
export default {
  data () {
    return {
      data: [],
      dialogVisibleAdd: false,
      dialogVisibleEdit: false,
      form: {
        addname: '',
        editname: '',
      },
      groupItem: ''
    }
  },
  methods: {
    // 添加 点击确定
    addHostgroup () {
      if (!this.trim(this.form.addname)) {
        this.$message.error('主机组名不能为空');
        return
      }
      var data = {
        'name': this.trim(this.form.addname)
      }
      AddHostgroup(data).then(res => {
        if (res.data.code == 200) {
          this.dialogVisibleAdd = false
          this.queryList()
          this.$message({
            message: '添加成功',
            type: 'success'
          });
          this.form.addname = ''
        } else {
          this.$message.error(res.data.msg)
        }
      }).catch(err => {
        this.$message.error('添加失败')
      })
    },
    // 删除
    deleteHostgroup (item) {
      this.$confirm('你确定删除吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        var data = {
          "groupid": item.groupid
        }
        DeleteHostgroup({ 'data': data }).then(res => {
          if (res.data.code == 200) {
            this.queryList()
            this.$message({
              message: '删除成功',
              type: 'success'
            });
          } else {
            this.$message.error('修改失败')
          }

        }).catch(err => {
          this.$message.error('删除失败')
        })

      }).catch(() => {
      });
    },
    edit (item) {
      this.groupItem = item
      this.form.editname = item.name
      this.dialogVisibleEdit = true
    },
    editHostgroup () {
      if (!this.trim(this.form.editname)) {
        this.$message.error('主机组名不能为空');
        return
      }
      var obj = {
        'name': this.trim(this.form.editname),
        "groupid": this.groupItem.groupid
      }
      PutHostgroup(obj).then(res => {
        if (res.data.code == 200) {
          this.dialogVisibleEdit = false
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

    queryList () {
      getHostgroup().then(res => {
        this.data = res.data.data
      }).catch(err => {
        console.log(err)
      })
    }
  },

  mounted () {
    this.queryList()
  }
}
</script>
<style scoped>
.td2 {
  text-align: right;
}

.detail_table tbody td {
  padding: 15px 10px;
}
</style>
