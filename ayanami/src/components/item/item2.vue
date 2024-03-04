<template>
    <div :style="root_style">
        <div :style="div_style"></div>
        <div :style="div_style"></div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                windowWidth: window.innerWidth,
                root_style:{
                    display:'flex',
                    backgroundColor:`${this.$root.$data.color.font}`,
                    width: "calc(33.33% - 20px)",
                    minWidth:"400px",
                    flex:"1",
                    margin: "10px"
                    

                },
                div_style:{
                    height:"100px",
                    width:"100px",
                }
            }
        },
        created() {
            window.addEventListener('resize', this.handleWindowSizeChange);
            // 监听窗口大小变化
        },
        methods:{
            handleWindowSizeChange() {
                this.windowWidth = window.innerWidth;
                // 更新窗口宽度
                if (this.windowWidth < 800) {
                    this.yourFunctionDown();
                    // 当窗口宽度小于768时执行你的函数
                } else {
                    this.yourFunctionUp();
                    // 当窗口宽度大于等于768时执行你的函数
                }
            },
            yourFunctionDown() {
                this.$data.root_style.minWidth="500px"
            },
            yourFunctionUp() {
                this.$data.root_style.minWidth="300px"
            },
        },
    }
</script>