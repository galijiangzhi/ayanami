<template>
    <div :style="dropdown_style" class="dropdown" @click="toggleDropdown">
        <div :style="dropdown_toggle_style">&nbsp {{selectedOption}}</div>
        <div v-if="isOpen" :style="dropdown_menu_style">
            <div v-for="option in options" :style="option_style" :key="option" @click="selectOption(option)">{{ option }}</div>
        </div>
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
                    borderRadius:"5px",
                    // backgroundColor:"#f2f2f2",
                    color:`${this.$root.$data.color.font}`,
                    width:"128px",
                    height:"26px",
                    border:`2px solid ${this.$root.$data.color.font}`,
                    display:"flex",
                    alignItems:"center",
                    justifyContent: "flex-start" /* 水平起点对齐 */
                },
                dropdown_menu_style:{
                    position:"absolute",
                    // backgroundColor:"#fff",
                    width:"128px",
                    boxShadow:"0 2px 4px rgba(0, 0, 0, 0.2)",
                    borderRadius:"5px",
                    marginRight:"100px"
                },
                option_style:{
                    padding:"10px",
                    
                    cursor:"pointer"
                },
                isOpen:false
            };
        },
        methods:{
            toggleDropdown(){
                this.isOpen = !this.isOpen;
            },
            
        }

    }
</script>
<style scoped>

</style>