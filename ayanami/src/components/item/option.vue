<template>
    <div :style="option_style"></div>
</template>
<script>
    export default{
        data(){
            return{
                option_style:{
                    height:"100px",
                    width:"100px",
                    backgroundColor:"red"
                }
            }
        }
    }
</script>