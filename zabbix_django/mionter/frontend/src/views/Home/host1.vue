<template>
  <div>
    <div class="min_head">
      <div class="min_headl">
        设备监控共 ({{card.length}}) 个项目
      </div>
      <div class="min_headr">
        <button class="button"
          @click="addOne">添加项目</button>
      </div>
    </div>
    <div class="maincon">
      <div class="card"
        v-for="(c,index) in card"
        @click="toApp(c.hostid)"
        :key="index">
        <div class="card_img"
          :style=" {'background':index>7?colors[index%7]:colors[index] }">
          <img src="../../assets/img/project.png"
            alt="">
        </div>
        <h4 class="card_title">
          <span class="status"
            :class="c.available ==1? 'green':'red'"></span>
          {{c.host}}<br />
          <span style="font-size:14px">{{c.ip}}:{{c.port}}</span>
        </h4>
        <div class="cardBtn cardleft"
          @click.stop="editOne(c)">
          <el-tooltip effect="dark"
            content="编辑"
            placement="right-start">
            <el-button><i class="el-icon-edit"></i></el-button>
          </el-tooltip>
        </div>
        <div class="cardBtn cardright"
          @click.stop="deletehost(c)">
          <el-tooltip effect="dark"
            content="删除"
            placement="right-start">
            <el-button><i class="el-icon-delete"></i></el-button>
          </el-tooltip>
        </div>
      </div>
    </div>

    <!-- 弹出框 -->
    <div class="detail">
      <el-dialog :title="type==1?'添加主机':'修改主机'"
        :visible.sync="dialogVisible"
        width="40%">
        <el-form ref="form"
          :model="form"
          label-width="80px">
          <el-form-item label="主机名:">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="主机组:">
            <el-select v-model="hostgroup"
              placeholder="请选择主机组">
              <el-option v-for="item in hostgroupData"
                :key="item.groupid"
                :label="item.name"
                :value="item.groupid">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="模板列表:">
            <el-select v-model="templateli"
              multiple
              placeholder="请选择模板列表">
              <el-option v-for="item in templatelist"
                :key="item.templateid"
                :label="item.name"
                :value="item.templateid">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="ip:">
            <el-input v-model="form.ip"></el-input>
          </el-form-item>
          <el-form-item label="端口:">
            <el-input v-model="form.port"></el-input>
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
import { getHost, getHostApp, getHostgroup, AddHost, getTemplate, PutHost, DeleteHost, getItem } from '../../api/api'
export default {
  data () {
    return {
      colors: ['rgb(35, 149, 241)', 'rgb(114, 101, 230)', 'rgb(245, 49, 127)', 'rgb(255, 191, 0)',
        'rgb(245, 106, 0)', 'rgb(191, 191, 191)', 'rgb(0, 168, 84)'],
      card: [],

      dialogVisible: false,
      form: {
        name: '',
        ip: '',
        port: ''
      },
      hostgroupData: '',
      hostgroup: '',
      templateli: '',
      templatelist: '',
      hostItem: '',
      type: 1,
    }
  },
  methods: {
    toApp (hostid) {
      getHostApp(hostid).then(res => {
        var applyid = res.data.data[0].applicationid
        this.$router.push({
          path: `/detail/${hostid}/${applyid}`,
        })
      }).catch(err => {
        console.log(err)
      })

    },
    addOne () {
      this.dialogVisible = true
      this.type = 1

      this.form.name = ''
      this.form.ip = ''
      this.form.port = ''
      this.hostgroup = ''
      this.templateli = ''
    },
    editOne (c) {
      this.dialogVisible = true
      this.type = 2
      this.hostItem = c

      this.form.name = c.name
      this.form.ip = c.ip
      this.form.port = c.port

      var arrt = []
      c.templateids.map(el => {
        arrt.push(el.templateid)
      })
      this.templateli = arrt
      this.hostgroup = c.hostgroupids[0].groupid
    },
    sure () {
      if (!this.trim(this.form.name)) {
        this.$message.error('主机名不能为空');
        return
      }
      if (!this.hostgroup) {
        this.$message.error('请选择主机组');
        return
      }
      if (this.templateli <= 0) {
        this.$message.error('请选择模板列表');
        return
      }
      if (!this.trim(this.form.ip)) {
        this.$message.error('ip不能为空');
        return

      }
      if (this.trim(this.form.ip)) {
        var reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/
        if (reg.test(this.trim(this.form.ip)) == false) {
          this.$message.error('ip格式不正确');
          return
        }
      }
      if (!this.trim(this.form.port)) {
        this.$message.error('port不能为空');
        return
      }
      if (this.trim(this.form.port)) {
        var port = this.trim(this.form.port)
        if (!(/^[1-9]\d*$/.test(port) && 1 <= 1 * port && 1 * port <= 65535)) {
          this.$message.error('port格式不正确');
          return
        }
      }
      //添加
      if (this.type == 1) {
        this.addHost()
      } else if (this.type == 2) {
        this.editHost()
      }
    },
    addHost () {
      var data = {
        "hostname": this.trim(this.form.name),
        "ip": this.trim(this.form.ip),
        "port": this.trim(this.form.port),
        "groupid": this.hostgroup,
        "templateid": this.templateli
      }
      AddHost(data).then(res => {
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

    editHost () {
      var obj = {
        "hostname": this.trim(this.form.name),
        "ip": this.trim(this.form.ip),
        "port": this.trim(this.form.port),
        "groupid": this.hostgroup,
        "templateid": this.templateli,
        "hostid": this.hostItem.hostid
      }
      PutHost(obj).then(res => {
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
    deletehost (c) {
      this.$confirm('你确定删除吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        var data = {
          "hostid": c.hostid
        }
        DeleteHost({ 'data': data }).then(res => {
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
      getHost().then(res => {
        this.card = res.data.data
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted () {
    this.queryList()

    getHostgroup().then(res => {
      this.hostgroupData = res.data.data
    }).catch(err => {
      this.$message.error(err)
    })
    getTemplate().then(res => {
      this.templatelist = res.data.data
    }).catch(err => {
      this.$message.error(err)
    })
  }
}
</script>
<style scoped>
.maincon {
  display: flex;
  flex-wrap: wrap;
}
.maincon .card {
  width: 25%;
  text-align: center;
  color: rgba(13, 27, 62, 0.65);
  padding: 24px;
  cursor: pointer;
  position: relative;
}
.maincon .card:hover {
  background-color: #ececec;
  box-shadow: 0 4px 8px rgba(50, 50, 93, 0.11), 0 4px 6px rgba(0, 0, 0, 0.08);
  top: -5px;
}
.maincon .card:hover .cardBtn {
  display: block;
}
.card_title {
  font-size: 18px;
  font-weight: 400;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-top: 20px;
  margin-bottom: 10px;
}
.card_img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}
.card_img img {
  width: 50px;
  height: 50px;
}
.cardBtn {
  position: absolute;
  top: 10px;
  color: #2395f1;
  display: none;
}
.cardBtn .el-button {
  border: none;
  color: #2395f1;
  background: none;
  padding: 5px;
  font-size: 16px;
}
.cardleft {
  left: 10px;
}
.cardright {
  right: 10px;
}
</style>
