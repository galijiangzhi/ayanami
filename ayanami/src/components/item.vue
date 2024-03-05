<template>
    <div  :style="item_style">
        <Item1 />
        <Item2 />

    </div>
    
</template>
<script>
    import Item1 from './item/item1.vue'
    import Item2 from './item/item2.vue'
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

                }
            }
        },
        components:{
            Item1,
            Item2,
        }
    }
</script>
