<template>
  <div id="home">
    <div> 
      <button v-if="loginType==false" v-on:click="showLoginRegisterBox(1)">登录</button>
      <button v-if="loginType==false" v-on:click="showLoginRegisterBox(2)">注册</button>
      <button @click="toHome" v-if="loginType" >首页</button>
      <button @click="toUserinfo" v-if="loginType" >个人中心</button>
      <button v-if="loginType" v-on:click="showLoginRegisterBox(3)">修改</button>

      <div class="header">
          <h1>{{siteinfo.sitename}}</h1>
          <img :src="siteinfo.logo" alt="">
      </div>
      <hr>
      <div class="content">
          <div class="menu">
            <div v-for="item in menulist" :key="item.id" class="item">
              <div 
              v-if="item.id == choosed "  style="background:#777;color:#fff"
              
              >
                  <a style="color:#fff">{{ item.text }}</a>
              </div>
              <div v-else v-on:click="choosedMenu(item.id)" style="">
                  <a style="color:#000">{{ item.text }}</a>
              </div>
            </div>
          </div>
          <div class="userlist">
              <p>{{ choosed_text }}</p>
              <hr>
              <router-view @hideBox="hideLoginRegisterBox" @changeUI="changeLoginTye" />
                         
          </div>
      </div>
    </div>
    <hr>
    <LoginBox v-if="boxtarget" :target="boxtarget" @hideBox="hideLoginRegisterBox"></LoginBox>
    <div class="foot">
        Copyright © 2020 工作室
    </div>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    
  </div>
</template>

<script>
import axios from 'axios'
import LoginBox from '../src/components/LoginBox'

export default {
  components:{
    LoginBox
  },
  data(){
    return{
      menulist:[],
      webinfo:[],
      choosed:1,
      choosed_text:'Django后端',
      boxtarget:0,
      siteinfo:[],
      loginType:false
    }
  },
  mounted(){
    try {
      if (window.localStorage.getItem('token').length>0) {
        this.loginType = true
      }
    } catch (error) {
      console.log(error)
    }
    
    this.getMenuList()
  },
  methods:{
    toUserinfo(){
      this.$router.push({path:'/userinfo'})
    },
    toHome(){
      this.$router.push({path:'/'})
    },

    // 获取分类列表
    getMenuList(){
      console.log('开始获取分类')
      axios({
        url:'http://127.0.0.1:8000/get-menu-list/',
        type:'json',
        method:'get'
      }).then((res) => {
        console.log(res.data)
        this.menulist = res.data.menu_data
        this.siteinfo = res.data.siteinfo
      })
    },
    choosedMenu(id){
      console.log(id)
      this.choosed = id
      // for (let index = 0; index < this.menulist.length; index++) {
      //   if (id==this.menulist[index].id){
      //     this.choosed_text = this.menulist[index].text
      //   } 
      // }
      for (const key in this.menulist) {
        if (id == this.menulist[key].id) {
          this.choosed_text = this.menulist[key].text
        }
      }
      // 进行ID传参跳转
      this.$router.push({
        path:'/',
        query:{
          menuId:id
        }
      })
    },
    // 展示登录注册框体
    showLoginRegisterBox(value){
      this.boxtarget = value
    },
    // 隐藏父组件 隐藏登录注册框体
    hideLoginRegisterBox(){
      this.boxtarget = 0
    },
    changeLoginTye(bool){
      this.loginType = bool
    }

    // getWebInfo(){
    //   console.log('开始获取网站title')
    //   axios({
    //     url:'http://127.0.0.1:8000/get-web-title/',
    //     type:'json',
    //     method:'get'
    //   }).then((res) => {
    //     console.log(res.data)
    //     this.webinfo = res.data[0]
    //   })
    // },
  },
}
</script>

<style>

</style>
