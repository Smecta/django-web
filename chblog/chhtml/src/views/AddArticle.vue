<template>
  <div id="add-article">
    <el-row :gutter="10">
      <el-col :xs="24" :lg="8">
        <div class="dweb">
          <el-form
            :label-position="'left'"
            label-width="80px"
            :model="article_info"
          >
            <el-form-item label="文章标题">
              <el-input v-model="article_info.title"></el-input>
            </el-form-item>
            <el-form-item label="描述">
              <el-input
                type="textarea"
                :rows="4"
                v-model="article_info.describe"
              ></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
      <el-col :xs="24" :lg="16">
        <div class="dweb">
          <div v-for="(img, index) in cover_list" :key="index">
            <el-image
              v-if="img == cover_img"
              class="cover"
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
            <el-image
              v-else
              class=""
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
          </div>
          <el-button @click="submitAriticle" type="success" round>保存文章</el-button>
        </div>
      </el-col>
      <el-col :xs="24" :lg="24">
        <div class="dweb">
          <div id="summernote"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// @ is an alias to /src
import $ from "jquery";
import axios from 'axios';
import Qs from 'qs'

export default {
  data() {
    return {
      article_info: {
        title: "",
        describe: "",
        contents:""
      },
      cover_list: [],
      cover_img:"",
    };
  },
  mounted() {
    this.summernote();
  },
  methods: {
    // 提交文章
    submitAriticle(){
      let ariticle_data = {
        title : this.article_info.title,
        describe : this.article_info.describe,
        content : this.article_info.contents,
        cover : this.cover_img
      }
      axios.post('http://127.0.0.1:8000/api/add-article/',Qs.stringify(ariticle_data))
      .then(res => {
        console.log(res);
      })
      .catch(err => {
        console.error(err);
      })
    },
    summernote() {
      let self = this;
      $("#summernote").summernote({
        height: 500,
        width: "100%",
        lang: "zh-CN",
        callbacks: {
          // 当输入
          onChange(contents) {
            console.log(contents);
            self.article_info.contents = contents
          },
          // 本地图片上传
          onImageUpload(file) {
            // console.log(file);
            let img = file[0];
            let imgData = new FileReader();
            imgData.readAsDataURL(img);
            // console.log(imgData);
            imgData.onload = function() {
            //   console.log(imgData.result);
              // 插入图片本身
              let imgnode = document.createElement('img')
              imgnode.src = imgData.result
              $("#summernote").summernote('insertNode',imgnode)
              // 推入封面到待选择
              self.cover_list.push(imgData.result);
            };
          },
          // 远程图片添加
          onImageLinkInsert(url){
            //   console.log(url)
              let imgnode = document.createElement('img')
              imgnode.src = url
            //   console.log(imgnode)
              $("#summernote").summernote('insertNode',imgnode)
              self.cover_list.push(url);
          },
          // 删除媒体文件
          onMediaDelete(target){
            //   console.log(target)
              let imgData = target[0].src
              console.log(imgData)
              for(let i = 0; i < self.cover_list.length; i++){
                  if(self.cover_list[i] == imgData){
                      self.cover_list.splice(i,1)
                  }
              }
          }
        },
      });
    },
    chooseCover(img){
        console.log('ok')
        this.cover_img = img
    }
  },
};
</script>

<style scoped>
.dweb {
  min-height: 200px;
  padding: 20px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dweb .el-image:hover{
    border: 2px solid rgb(255,255,45);
}
.dweb .el-image.cover {
    border: 2px solid rgb(255,255,45);
}
.el-form-item {
  margin-top: 22px;
}
.el-input input {
  background: #00000060;
}
.dweb .el-button {
  position: fixed;
  right: 20px;
  z-index: 1001;
  margin-top: 250px;
}

</style>
