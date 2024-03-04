<template>
    <div :style="option_style">
      <div>{{ title }}</div>
      <img :src="iconLink" alt="Icon">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        option_style: {
          height: "50px",
          width: "calc(20% - 20px)",
          backgroundColor: "red",
          margin: "10px",
          boxSizing: "border-box"
        },
        title: "",
        iconLink: ""
      };
    },
    props: ["url"],
    mounted() {
      fetch(this.url)
        .then(response => response.text())
        .then(htmlContent => {
          // 解析HTML内容以获取标题
          const titleMatch = htmlContent.match(/<title>(.*?)<\/title>/i);
          if (titleMatch) {
            this.title = titleMatch[1];
          }
  
          // 获取页面图标
          const iconMatch = htmlContent.match(/<link rel="icon" href="(.*?)"/i);
          if (iconMatch) {
            this.iconLink = iconMatch[1];
          }
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  };
  </script>