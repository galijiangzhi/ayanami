<template>
    <div :style="root_style">
        <div :style="head_style">
            <svg :style="head_svg_style" t="1709459194370" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2067" data-spm-anchor-id="a313x.search_index.0.i11.5ac83a815574M3" width="200" height="200"><path :style="svg_color" d="M499.890087 912.695652c-221.317565 0-400.695652-179.400348-400.695652-400.695652s179.378087-400.695652 400.695652-400.695652c221.273043 0 400.695652 179.400348 400.695652 400.695652s-179.422609 400.695652-400.695652 400.695652z m0-89.043478c172.121043 0 311.652174-139.53113 311.652174-311.652174s-139.53113-311.652174-311.652174-311.652174-311.652174 139.53113-311.652174 311.652174 139.53113 311.652174 311.652174 311.652174z" fill="#d4237a" p-id="2068" data-spm-anchor-id="a313x.search_index.0.i8.5ac83a815574M3" class="selected"></path><path :style="svg_color" d="M366.32487 422.956522m-44.52174 0a44.521739 44.521739 0 1 0 89.043479 0 44.521739 44.521739 0 1 0-89.043479 0Z" fill="#d4237a" p-id="2069" data-spm-anchor-id="a313x.search_index.0.i7.5ac83a815574M3" class="selected"></path><path :style="svg_color" d="M113.441391 678.199652c3.895652 3.31687 10.395826 6.856348 19.433739 10.150957 21.815652 7.969391 54.093913 12.911304 94.096696 13.957565 86.216348 2.270609 199.613217-13.378783 317.106087-44.855652 117.49287-31.47687 223.49913-74.640696 297.049044-119.718957 34.125913-20.925217 59.592348-41.316174 74.50713-59.124869 6.188522-7.346087 10.061913-13.690435 11.776-18.498783 0.801391-2.31513 0.868174-3.005217 0.890435-2.960696-0.356174-1.224348-4.474435-5.12-16.11687-10.084174-17.318957-7.41287-43.319652-12.688696-76.132174-15.026086l6.322087-88.82087c93.540174 6.633739 156.560696 33.569391 171.920696 90.86887 29.918609 111.682783-172.454957 235.742609-447.176348 309.381565-274.69913 73.594435-512 67.33913-541.94087-44.343652-15.760696-58.88 27.959652-115.2 110.146783-169.115827l48.840348 74.462609c-29.228522 19.166609-50.710261 37.62087-63.042783 53.470609-4.964174 6.41113-8.013913 11.842783-9.305043 15.894261-0.534261 1.736348-0.601043 2.270609-0.623305 2.248348 0.022261 0 0.467478 0.623304 2.226087 2.114782z" fill="#d4237a" p-id="2070" data-spm-anchor-id="a313x.search_index.0.i9.5ac83a815574M3" class="selected"></path></svg>
            <label :style="head_label_style">MODE ONE</label>
        </div>
        <div :style="item_style">
            <Option v-for="item in mode_one" :key="item" />
        </div>
    </div>
</template>
<script>
    import Option from "./option.vue"
    export default{
        data(){
            return{
                windowWidth: window.innerWidth,
                root_style:{
                    width:"800px",
                    minHeight:"130px",
                    minWidth: "800px",
                    borderRadius:"5px",
                    display:'flex',
                    backgroundColor:`${this.$root.$data.color.font}`,
                    flex:"1",
                    margin: "10px",
                    flexShrink:"1" ,
                    display:"flex",
                    flexDirection:"column"
                },
                head_style:{
                    height:"40px",
                    width:"100%",
                    display:"flex",
                    flexDirection:"row",
                    justifyContent: "flex-start" 
                    // backgroundColor:"pink"
                },
                item_style:{
                    flex:"1",
                    width:"calc(100% - 20px)",
                    marginBottom:"10px",
                    backgroundColor:"yellow",
                    display:"flex"
                },
                head_svg_style:{
                    height:"30px",
                    width:"30px",
                    marginLeft:"20px"
                },
                head_label_style:{
                    fontSize:"1.17em",
                    marginLeft:"10px"
                },
                svg_color:{
                    fill:`${this.$root.$data.color.head}`
                },
                mode_one:['11111',"22222",'11111',"22222",'11111',"22222",'11111',"22222",]
    
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
                if (this.windowWidth < 1000) {
                    this.yourFunctionDown();
                    // 当窗口宽度小于768时执行你的函数
                } else {
                    this.yourFunctionUp();
                    // 当窗口宽度大于等于768时执行你的函数
                }
            },
            yourFunctionDown() {
                this.$data.root_style.minWidth="600px"
            },
            yourFunctionUp() {
                this.$data.root_style.minWidth="800px"
            },
        },
        components:{
            Option,
        }
    }
</script>
<style scoped>

</style>