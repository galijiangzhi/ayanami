<template>
    <div :style="option_style">
      <h1 :style="h1_style">{{ responseData.title }}</h1>
      <input type="text" :style="input_st" @keydown.enter="handleEnter">
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        option_style: {
          height: "40px",
          width: "49%",
          backgroundColor:`${this.$root.$data.color.background}`,
          margin: "3px",
          boxSizing: "border-box",
          display:"flex",
          borderRadius:"5px"
        },
        img_style:{
          width:"25px",
          height:"25px",
          margin:"10px"
        },
        start_font_style:{
          width:"25px",
          height:"25px",
          margin:"10px",
          color:"#00ccb4",
          fontSize:"25px",
          display:"flex"
        },
        h1_style:{
          fontSize:"15px",
          height:"100%",
          width:"70px",
        //   background:"red",
          wordWrap:"break-word",
        //   flex:"0.9",
          color:`${this.$root.$data.color.font}`,
          border:"10x",
          display:"flex",
          textOverflow: "ellipsis",
          overflow: "hidden",
          alignItems: "center",  // 垂直居中显示
          justifyContent: "center"
        },
        input_st:{
            flex:"1",
            height:"90%",
            background:"rgba(255,255,255,0.3)",
            borderRadius:"5px",
            border:"0px"
        },
        responseData: {
          title:this.tit,
          url_a:this.url
        },
      };
    },
    props: ["url","tit"],
    methods:{
      handleEnter(event){
        if (event.key === 'Enter'){
          var userInput = event.target.value;
          // yolov5
          // console.log(userInput)
          // console.log(this.responseData.url_a)
          var url = this.responseData.url_a + userInput
          // https://www.baidu.com/s?wd=yolov5

          console.log(url)
          window.open(url,'_blank');
          event.target.value = '';
        }
      }
    }
}  
  </script>