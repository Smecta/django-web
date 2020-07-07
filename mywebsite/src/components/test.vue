<template>
    <div id="login-userinfo">
        <img src="../assets/img/admin.jpg" alt="">
        <p>{{ nickName }}</p>
    </div>
</template>

<script>
import { eventBus} from '../main.js'

export default {
    props:['testName'],
    data(){
      return{
        nickName:""
      }
    },
    mounted(){
      eventBus.$on('changeTestName',(data) =>{
        console.log(data)
        this.nickName = data
      })
    }
}
</script>