<template>
    <div :style="div_style">aaaaaaaaaaaa</div>
</template>
<script>
    export default{
        data(){
            return{
                div_style:{
                    width:"300px",
                    height:"70px",
                    backgroundColor:"red",
                    position:"absolute",
                    top:"80px",
                    left:"0px",
                    borderBottomRightRadius:"10px"
                }
            }
        }
    }
</script>