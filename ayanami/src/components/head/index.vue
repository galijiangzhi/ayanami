<template>
        <button :style="button_style" v-for="item in index_list" :key="item">{{ item }}</button>
</template>
<script>
    export default{
        data(){
            return{
                index_list:["github链接","文档","联系本人"],
                button_style:{
                    height:"37px",
                    width:"80px",
                    marginLeft:"10px"
                }
            }
        }
    }
</script>
<style scoped>
</style>