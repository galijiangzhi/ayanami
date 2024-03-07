<template>
    <div :style="option_style" @mouseover="changeColor(true)" @mouseout="changeColor(false)" @click="open_web()">
      <img v-if="isimg" :src="responseData.favicon" :style="img_style" @load="imageLoaded" @error="imageError">
      <div v-else :style="start_font_style">{{responseData.title[0]}}</div>
      <h1 :style="h1_style">{{ responseData.title }}</h1>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        option_style: {
          height: "50px",
          width: "calc(20% - 20px)",
          backgroundColor:`${this.$root.$data.color.background}`,
          margin: "10px",
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
          fontSize:"12px",
          height:"100%",
          wordWrap:"break-word",
          flex:"0.9",
          color:`${this.$root.$data.color.font}`,
          border:"10x",
          display:"flex",
          textOverflow: "ellipsis",
          overflow: "hidden",
          alignItems: "center",  // 垂直居中显示
          justifyContent: "center"
        },
        responseData: {
          title:this.url
        },
        isimg:true
      };
    },
    methods:{
      changeColor(mouse){
        if (mouse){
          this.option_style.backgroundColor=`${this.$root.$data.color.head}`,
          this.option_style.boxShadow = `-1px 1px 3px ${this.$root.$data.color.font}`; // 添加阴影效果
        } else {
          this.option_style.backgroundColor=`${this.$root.$data.color.background}`,
          this.option_style.boxShadow = "none"; // 移出时移除阴影效果
        }
      },
      imageError() {
        console.log('图片加载失败');
        this.isimg=false
      },
      open_web(){
        window.open(this.url, '_blank');
      }
    },
    props: ["url"],
    mounted() {
      axios.get('http://www.asuka.sanyueyu.top//url_information', {
        params: {
          url: this.url,
        },
      })
      .then(response => {
        // console.log("后端响应：", response.data); // 将后端响应打印到控制台
        this.responseData = response.data;
        if (this.responseData.favicon.includes(".svg")) {
          console.log("SVG图标");
          this.isimg=false
        // 在这里进行相应的处理，比如显示SVG图标
      } else {
          console.log("其他类型的图标");
        // 在这里进行相应的处理，比如显示其他类型的图标
      }
    })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    }
  };
  
  </script>