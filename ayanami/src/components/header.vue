<!-- 该文件用于构建主页的头部导航栏 -->
<template>
    <div :class="header" :style=header_style>
        <Logo />
    </div>
</template>
<script>
    import Logo from './head/logo.vue'
    export default{
        data(){
            return{
                header:"header",
                header_style:{
                    backgroundColor:"#181818",
                    height: "64px",
                    width: "100%",
                    padding:"8px"
                }
            }
        },
        components:{
            Logo
        }
    }
</script>
<style>
    .header{
        

    }
</style>