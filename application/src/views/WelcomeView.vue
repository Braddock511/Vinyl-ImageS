<template>
    <TheHeader />
    <main>
        <div id="info">
            <p>The "Vinyl ImageS" application helps users determine the title, genre, label, where it's from, release year, and optionally the value of the vinyl records from the uploaded image. As a user, you can upload a photo of the vinyl record and select the condition of the vinyl from the drop-down menu.</p>
            <p>All data is taken from the discogs website: <a href="https://discogs.com/" target="_blank">discogs.com</a></p>
            
            <router-link to="/upload" id="upload"><h2>Go to upload</h2></router-link>
        </div>

    </main>

</template>

<script>

    import TheHeader from '@/components/TheHeader.vue'

    export default {
        components:{
        TheHeader,
        }
    }
</script>

<style scoped lang="scss">
    main{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 100px;

        #info{
            width: 50%;
            font-size: large;

            p{
                font-size: larger;
            }
            
            #upload{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
                font-size: large;

                h2{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: rgb(1, 83, 151);
                    border-radius: 12px;
                    height: 50px;
                    margin-top: 38px;
                    outline: 0;
                    text-align: center;
                    width: 30%;

                    &:hover {
                        background-color: rgb(0, 70, 128);
                    }
                }
            }

            a{
                color: rgb(211, 211, 211);

                &:hover{
                    color: white;
                }
            }
        }
    }
</style>