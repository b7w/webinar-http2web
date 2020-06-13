import Vue from 'vue'
import App from './App.vue'

document.title = 'http2web'

let vue = new Vue({
    render: h => h(App),
});

vue.$mount('#app')
