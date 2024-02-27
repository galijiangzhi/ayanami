<template>
        <a :class="a_class" :style="a_style" @mouseover="addborder"  @mouseleave="removeborder" v-for="item in index_list" :key="item">{{ item }}</a>
</template>
<script>
    export default{
        data(){
            return{
                a_class:"index_a",
                index_list:["github链接","文档","联系本人"],
                a_style:{
                    height:"37px",
                    width:"80px",
                    marginLeft:"10px",
                    backgroundColor:"#462a5b",
                    border:"0px",
                    borderRadius:"5px",
                    display: "flex",  // 使用 flex 布局
                    justifyContent: "center",  // 水平居中
                    alignItems: "center",  // 垂直居中
                    color:this.$root.$data.color.font,
                    boxSizing: "border-box"
                },
            }
        },
        methods:{
            addborder(event) {
                event.target.style.border = `1px solid ${this.$root.$data.color.font}`; // 添加内边框样式
             },
            removeborder(event) {
                event.target.style.border = "none"; // 移除内边框样式
            }
        }
    }
</script>
<style>


</style>