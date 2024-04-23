<template>
    <div :style="dropdown_style" class="dropdown" @click="toggleDropdown">
        <div :style="dropdown_toggle_style">&nbsp {{selectedOption}}</div>
        <div v-if="isOpen" :style="dropdown_menu_style">
            <div :style="zhanwei_div_style"></div>
            <div v-for="option in options" :style="option_style" :key="option" @mouseover="addborder"  @mouseleave="removeborder" @click="selectOption(option)">{{ option }}</div>
            <div :style="zhanwei_div_style"></div>
        </div>
        <svg t="1709252639589" viewBox="0 0 1103 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1440" width="200" height="200" :class="{'rotate':isOpen}" :style="pull_svg_style">
            <path d="M101.022 445.417l450.009 431.641 450.009-431.641c18.368-18.368 55.103-18.368 82.655 0 18.368 18.368 27.552 55.103 0 82.655l-514.296 486.744c-9.184 9.184-9.184 9.184-18.368 9.184s-18.368 0-18.368-9.184v0l-514.296-486.744c-18.368-18.368-18.368-55.103 0-82.655 18.368-18.368 55.103-18.368 82.655 0z" p-id="1441"></path><path d="M569.399 592.359v0c0 9.184-9.184 9.184-18.368 9.184s-18.368 0-18.368-9.184v0l-514.296-495.928c-18.368-18.368-18.368-55.103 0-82.655 18.368-18.368 55.103-18.368 82.655 0l450.009 440.825 450.009-431.641c18.368-18.368 55.103-18.368 82.655 0 18.368 18.368 27.552 55.103 0 82.655l-514.296 486.744z" p-id="1442"></path>
        </svg>
  </div>
</template>
<script>
    export default{
        data(){
            return{
                selectedOption:'Ikari',
                options:['Ikari','Ayanami','sakura','boby'],
                dropdown_style:{  
                },
                dropdown_toggle_style:{
                    // 显示当前选项的div
                    borderRadius:"5px",
                    // backgroundColor:"#f2f2f2",
                    color:`${this.$root.$data.color.font}`,
                    width:"128px",
                    height:"26px",
                    border:`1px solid ${this.$root.$data.color.font}`,
                    display:"flex",
                    alignItems:"center",
                    justifyContent: "flex-start" /* 水平起点对齐 */,
                    fontFamily: 'Inconsolata, Georgia, sans-serif',
                    zIndex: "999"
                },
                dropdown_menu_style:{
                    //下拉列表的style
                    position:"absolute",
                    // backgroundColor:"#fff",
                    width:"165px",
                    top:'50px',
                    border:`1px solid ${this.$root.$data.color.font}`,
                    borderRadius:"5px",
                    marginRight:"100px",
                    fontFamily: 'Inconsolata, Georgia, sans-serif',
                    zIndex: "999"
                    
                },
                option_style:{
                    //具体选项的div
                    padding:"5px",
                    color:`${this.$root.$data.color.font}`,
                    background:`${this.$root.$data.color.background}`,
                    cursor:"pointer",
                    zIndex: "999"
                },
                pull_svg_style:{
                    //下拉图标svg的style
                    width:"20px",
                    height:"16px",
                    fill:`${this.$root.$data.color.font}`,
                    position:"relative",
                    left:"100px",
                    top:"-23px",
                    zIndex: "999"
                    
                },
                zhanwei_div_style:{
                    height:"10px"
                },
                isOpen:false
            };
        },
        methods:{
            selectOption(option){
                this.selectedOption = option
            },
            toggleDropdown(){
                this.isOpen = !this.isOpen;
            },
            addborder(event){
                event.target.style.color = `${this.$root.$data.color.background}`
                event.target.style.backgroundColor = `${this.$root.$data.color.font}`
            }, 
            removeborder(event){
                event.target.style.color = `${this.$root.$data.color.font}`
                event.target.style.backgroundColor = `${this.$root.$data.color.background}`
            }
            
        }

    }
</script>
<style scoped>
    .rotate {
        transition: transform 0.5s ease; /* 添加旋转动画效果 */
        transform: rotate(180deg);
        transform-origin:center ;
    }
</style>