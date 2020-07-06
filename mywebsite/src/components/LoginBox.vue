<template>
<div id="login" @click.self="hideSelf" >
    <div id="loginbox">
        <div class="form">
            <div v-if="target==1 || target==2" class="item">
                <div class="span">
                    用户名：
                </div>
                
                <input v-model="username" type="text" placeholder="输入用户名">
            </div>
            <div v-if="target==1 || target==2" class="item">
                <div class="span">
                    密码：
                </div>
                <input v-model="password" type="text" placeholder="输入密码">
            </div>
            <div v-if="target==2" class="item">
                <div class="span">
                    重复密码：
                </div>
                <input v-model="password2" type="text" placeholder="再次输入密码">
            </div>
            <div v-if="target==3" class="item">
                <div class="span">
                    网站名称
                </div>
                
                <input v-model="sitename" type="text" placeholder="输入网站名称">
            </div>
            <div v-if="target==3" class="item">
                <div class="span">
                    图片上传
                </div>
                
                <input id="uploadlogo" @change="uploadImg($event)" type="file" style="width:50px" >
            </div>
            <div v-if="target==3" class="item">
                <img :src="testLogo" alt="">
            </div>
            <button v-if="target==1" @click="toLogin">登录</button>
            <button v-if="target==2" @click="toRegister">注册</button>
            <button v-if="target==3" @click="toUpload">确定</button>
        </div>
  </div> 
</div>
  
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Qs from 'qs'

export default {
  name: 'LoginBox',
  props:['target'],
  data(){
      return{
          username:'',
          password:'',
          password2:'',
          sitename:'',
          testLogo:""
      }
  },
  mounted(){
      console.log(this.target)
  },
  methods:{
      // 确定修改网站名称函数
      toUpload(){
          let sitename = this.sitename
          let logo = this.testLogo
          console.log(sitename)
          if(sitename.length > 0 && logo.length > 0 ){
            axios({
                url:"http://127.0.0.1:8000/upload-logo/",
                method:'put',
                headers:{
                    "Content-Type":"application/x-www-form-urlencoded"
                },
                data:Qs.stringify({
                        sitename,
                        logo
                    }),
            }).then((res) => {
                console.log(res)
                if(res.data =="ok"){
                    window.location.reload()
                }
            })
          }else{
              alert('没有输入标题或者图片')
          }
      },
      uploadImg(e){
        //   console.log(e)
          let logo = e.target.files[0]
          console.log(logo)
          let Img = new FormData()
          Img.append("logo", logo)
          axios({
              url:"http://127.0.0.1:8000/upload-logo/",
              method:'post',
              headers:{
                "Content-Type":"application/x-www-form-urlencoded"
              },
              data:Img

          }).then((res) => {
              console.log(res)
              if (res.data){
                  this.testLogo = "http://127.0.0.1:8000/"+"upload/"+ res.data.img
              }
          })
      },
      hideSelf(){
          this.$emit('hideBox')
      },
        // 注册
      toRegister(){
          let username = this.username
          let password = this.password
          let password2 = this.password2
          console.log(username, password,password2)
          if(username.length > 0 && password.length > 0 && password2.length > 0){
              if(password!=password2){
                  alert('两次输入密码不同')
                   
              }else{
                axios({
                    url:'http://127.0.0.1:8000/register/',
                    data:Qs.stringify({
                        username,
                        password,
                        password2
                    }),
                    method:'post',
                    headers:{
                        "Content-Type":"application/x-www-form-urlencoded"
                    }
                }).then((res) => {
                    console.log(res)
                    switch (res.data) {
                        case 'same':
                            alert('存在同名用户')
                            break;
                    
                        default:
                            break;
                    }
                })
              }
          }else{
              alert('缺少必填项')
          }
      },  
        //   登录    
      toLogin(){
          
        console.log(this.username,this.password)
        let username = this.username
        let password = this.password
        if(username.length >0 && password.length>0 ){
            axios({
                url:'http://127.0.0.1:8000/login/',
                data:Qs.stringify({
                    username,
                    password
                }),
                method:'post',
                headers:{
                    "Content-Type":"application/x-www-form-urlencoded"
                }
            }).then((res) => {
                console.log(res)
                switch (res.data) {
                    case 'none':
                        alert('用户不存在')
                        break;
                    case 'pwderr':
                        alert('密码错误')
                        break;
                    default:
                        console.log(res.data.token)
                        window.localStorage.setItem('token',res.data.token)
                        alert('登录成功')
                        window.location.reload()
                }
            })
        }else{
            alert('用户名或密码不能为空')
        }
        
      }
  }

}
</script>

<style>
    #login {
        position:absolute;
        width:700px;
        height:100vh;
        display:flex;
        justify-content: center;
        align-items: center;
        top:0;
        background: #00000010;
        
    }
    #loginbox{
        width:300px;
        height:300px;
        border: 1px solid #000;
        background: #00000070;
        display:flex;
        justify-content: center;
        align-items: center;
        color:#fff;
        border-radius: 20px;
    }
    #loginbox .form .item {
        font-weight: 700;
        margin:10px auto;
    }
    #loginbox .form .item input{
        border-radius: 10px;
        /* background: none; */
        /* outline: none; */
        caret-color: rgba(0, 0, 0, 0);
        border:1px solid #ccc;
    }
    #loginbox .form .item .span {
        float:left;
        width:80px;
    }
</style>
