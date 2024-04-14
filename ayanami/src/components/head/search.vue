<template>
    <div :style="div_style">
        <div :style="label_div_style">
            <label :style="label_style">Search</label>
        </div>
        <div :style="input_div_style">
            <input :style="input_style" placeholder="過濾或篩選所需的信息">
        </div>
        <label> </label>
    </div>
    <div :style="style1">
        <div :style="style2"></div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                div_style:{
                    width:"300px",
                    height:"65px",
                    backgroundColor:`${this.$root.$data.color.head}`,
                    position:"absolute",
                    top:"80px",
                    left:"0px",
                    borderBottomRightRadius:"10px",
                    display:"flex",
                    justifyContent:"flex-start"
                },
                label_div_style:{
                    width:"70px",
                    height:"50px",
                    // backgroundColor:"#ffffff",
                    display:"flex"
                },
                label_style:{
                    fontSize:"1rem",
                    color:`${this.$root.$data.color.font}`
                },
                input_style:{
                    width:"190px",
                    height:"30px",
                    padding:"0px 10px 0px 10px",
                    outline: "none",
                    borderRadius:"5px",
                    backgroundColor:`${this.$root.$data.color.background}`,
                    color:`${this.$root.$data.color.font}`,
                    fontSize:"1rem",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    border:"0px",
                    marginRight:"10px"
                },
                input_div_style:{
                    width:"220px",
                    height:"50px",
                    // backgroundColor:"#dddddd",
                    display:"flex"
                },
                style1:{
                    width:"30px",
                    height:"30px",
                    backgroundColor:`${this.$root.$data.color.head}`,
                    position:"absolute",
                    top:"80px",
                    left:"300px"
                },
                style2:{
                    width:"30px",
                    height:"30px",
                    backgroundColor:`${this.$root.$data.color.background}`,
                    position:"absolute",
                    top:"0px",
                    left:"0px",
                    borderTopLeftRadius:"10px",
                }
            }
        }
    }
</script>
<style scoped>
    input{
        font-family: "PTMono","Courier New",monospace;
    }
    label{
        font-family: "PTMono","Courier New",monospace;
    }
</style>