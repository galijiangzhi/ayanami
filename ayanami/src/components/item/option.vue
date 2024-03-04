<template>
    <div :style="option_style">
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
      };
    },
    props: ["url"],
  };
  </script>