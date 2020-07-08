import Vue from 'vue'
// 引入 ElementUI
import ElementUI from 'element-ui'
import App from './App.vue'
import router from './router'
import store from './store'
// 映入 ElementUI的样式
import 'element-ui/lib/theme-chalk/index.css'

// 引入 summernote
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import 'popper.js'
import 'summernote'
import 'summernote/lang/summernote-zh-CN'
import 'summernote/dist/summernote.css'

// 引入 自己的CSS样式
import '../src/assets/css/mystyle.css'


Vue.use(ElementUI)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
