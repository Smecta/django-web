<template>
<div class="userlist">
    <div v-for="item in imglist" :key="item.pk" class="user">
        <img :src="apiurl+'upload/'+item.headImg" alt="">
        <p>{{ item.nickName }}</p>
        <button @click="deletUser(item.id)" >删除</button>
    </div>   
</div>
    
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Qs from 'qs'

export default {
    data(){
        return{
            apiurl:'http://127.0.0.1:8000/',
            imglist:[],
            menuId:1
        }
    },
    mounted(){
        // this.getData()
        this.getUserList(this.menuId)
    },
    watch:{
        $route(to){
            console.log(to.query.menuId)
            this.menuId = to.query.menuId
            this.getUserList(this.menuId)
        }
    },
    methods:{
        // getData(){
        //     axios({
        //         url:"http://127.0.0.1:8000/api/",
        //         type:'json',
        //         method:"get",
        //     }).then((res) => {
        //         console.log(res)
        //         // this.imglist = res.data.newsdata
        //     })
        // }

        // 开始后端请求
        getUserList(id){
            console.log('获取分类列表:'+id)
            axios({
                url:'http://127.0.0.1:8000/get-user-list/',
                type:'json',
                params:{
                    id,
                },
                method:'get'
            }).then((res) => {
                console.log(res)
                this.imglist = res.data
            })
        },
        deletUser(id){
            axios({
                url:'http://127.0.0.1:8000/get-user-list/',
                type:'json',
                headers:{
                    "Content-Type":"application/x-www-form-urlencoded"
                },
                data:Qs.stringify({
                    id,
                }),
                method:'delete'
            }).then((res => {
                console.log(res)
                if(res.data=="ok"){
                    this.getUserList(this.menuId)
                }
            }))
        }
    }

}
</script>

<style>

</style>
