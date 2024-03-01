<template>
    <div :style="svg_div_style">
        <svg aria-hidden="true" data-prefix="fas" data-icon="table" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" tabindex="-2" class="svg-inline--fa fa-table fa-w-16 layout-icon selected" data-original-title="null" :style="pull_svg_style">
            <path fill="currentColor" d="M464 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h416c26.51 0 48-21.49 48-48V80c0-26.51-21.49-48-48-48zM224 416H64v-96h160v96zm0-160H64v-96h160v96zm224 160H288v-96h160v96zm0-160H288v-96h160v96z"></path>
        </svg>
        <svg aria-hidden="true" data-prefix="fas" data-icon="th-list" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" tabindex="-2" class="svg-inline--fa fa-th-list fa-w-16 layout-icon  has-tooltip" data-original-title="null" :style="pull_svg_style">
            <path  fill="currentColor" d="M149.333 216v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24v-80c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zM125.333 32H24C10.745 32 0 42.745 0 56v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24zm80 448H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm-24-424v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24zm24 264H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24z"></path>
        </svg>
        <svg  aria-hidden="true" data-prefix="fas" data-icon="columns" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" tabindex="-2" class="svg-inline--fa fa-columns fa-w-16 layout-icon  has-tooltip" data-original-title="null" aria-describedby="tooltip_z0zlzqp1jx" :style="pull_svg_style">
            <path fill="currentColor" d="M464 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h416c26.51 0 48-21.49 48-48V80c0-26.51-21.49-48-48-48zM224 416H64V160h160v256zm224 0H288V160h160v256z"></path>
        </svg>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                svg_div_style:{
                    width:"100px",
                    height:"25px",
                    backgroundColor:"pink",
                },
                pull_svg_style:{
                    //下拉图标svg的style
                    width:"17px",
                    height:"17px",
                    marginTop:"10px",
                    padding: "3px",
                    borderRadius:"5px",
                    position:"relative",
                    top:"0px",
                    border :`1px solid ${this.$root.$data.color.font}`
                    
                },
            }
        }
    }
</script>