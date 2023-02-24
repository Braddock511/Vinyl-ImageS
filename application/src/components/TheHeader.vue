<template>
    <header>
        <router-link to="/" id="home"><h2><span>Vinyl ImageS</span></h2></router-link>
        <a href="https://github.com/Braddock511/label-from-image" target="_blank" id="github"><img src="../assets/github.svg" /></a>
    </header>
  </template>
  
<style scoped lang="scss">
    header{
        display: flex;
        justify-content: center;
        text-align: center;
        background-color: rgb(34, 36, 35);
        padding: 25px;
        font-size: 22px;

        #home{
            display: block;
            width: 205px;
            span:hover{
                opacity: 0.8;
            }
        }
        
        #github{
            position: absolute;
            top: 0;
            left: 0;
            padding: 20px;

            &:hover{
                opacity: 0.8;
            }
        }
    }

    @media only screen and (max-width: 500px){
        header{
            width: 500px;
        }
    }
</style>
  