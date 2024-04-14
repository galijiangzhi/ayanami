<template>
    <div  :style="item_style">
        <!-- MOD1 -->
        <Item1 v-if="item_module1.type === '1'"/>
        <Item3 v-else-if="item_module1.type === '3'"/>
        <!-- MOD2 -->
        <Item2 v-if="item_module2.type === '2'"/>
        <!-- MOD3 -->
        <Item1 v-if="item_module3.type === '1'"/>
        <Item3 v-else-if="item_module3.type === '3'"/>
        <!-- MOD4 -->
        <Item2 v-if="item_module4.type === '2'"/>
        <!-- MOD5 -->
        <Item1 v-if="item_module5.type === '1'"/>
        <Item3 v-else-if="item_module5.type === '3'"/>
        <!-- MOD6 -->
        <Item2 v-if="item_module6.type === '2'"/>
    </div>
    
</template>
<script>
    import Item1 from './item/item1.vue'
    import Item2 from './item/item2.vue'
    import Item3 from './item/item3_sousuo.vue'
    export default{
        data(){
            return{
                item_style:{
                    maxWidth:"1300px",
                    width:"calc(100vw - 100px)",
                    height:"100px",
                    // backgroundColor:"blue",
                    display:"flex",
                    justifyContent:"space-around",
                    flexWrap:"wrap",
                    alignItems: "flex-start"
                },
                item_module1:{
                    type:'',
                    data:''
                },
                item_module2:{
                    type:'',
                    data:''
                },
                item_module3:{
                    type:'',
                    data:''
                },
                item_module4:{
                    type:'',
                    data:''
                },
                item_module5:{
                    type:'',
                    data:''
                },
                item_module6:{
                    type:'',
                    data:''
                }
            }
        },
        methods:{
            get_module:function(mod,data){
                mod.type = data.split("|||")[0].toString();
                // mod.data = data.split("|||")[1].toString();
            }
        },
        mounted(){
                // 获取整个地址栏信息
            const fullUrl = window.location.href;
            // 使用split方法将地址栏信息以斜杠分割成数组，并获取最后一个元素
            const segments = fullUrl.split('/');
            this.id = segments[segments.length - 1]; // 将最后一个元素赋值给id
            console.log(this.id); // 输出id的值
            const url = "http://127.0.0.1:42001/get_data?id=" + this.id; // 添加斜杠以连接地址和ID
            console.log(url); // 注意这里是url而不是urll
            fetch(url)
            .then(response =>{
                if(!response.ok){
                    throw new Error('network response was not ok')
                }
                return response.json();
            })
            .then(data=>{
                console.log(data)
                this.get_module(this.item_module1,data[3]);
                this.get_module(this.item_module2,data[4]);
                this.get_module(this.item_module3,data[5]);
                this.get_module(this.item_module4,data[6]);
                this.get_module(this.item_module5,data[7]);
                this.get_module(this.item_module6,data[8]);
            })
        },
        components:{
            Item1,
            Item2,
            Item3,
        }
    }
</script>
