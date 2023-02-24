<template>
    <main v-if="!loading">
        <vue-easy-lightbox
        scrollEnabled
        escEnabled
        moveEnabled
        :visible="visible"
        :imgs="img"
        @hide="handleHide"
        ></vue-easy-lightbox>

        <section>
            <form id="upload" @submit.prevent="getDataImage">
                <h1>Upload Image</h1>
                <input type="file" @change="handleFileInput" required>
                <b>Display the median price of vinyl?</b> <br>
                (Upload will take a while longer)
                <div id="price">
                    <input type="checkbox" v-model="withPrice">
                    <select v-model="condition" v-if="withPrice">
                        <option value="M-">M- (Almost Perfect)</option>
                        <option value="M">M (New)</option>
                        <option value="VG+">VG+ (Excellent)</option>
                        <option value="VG">VG (Very Good)</option>
                        <option value="G">G (Good)</option>
                    </select>
                </div>
                <button type="submit">Upload</button>
            </form>

            <div id="preview" v-if="imageData">
                <img id="image-preview" :src="image"  alt="Uploaded Image" @click="showImage">
            </div>
        </section>

        <TheData :imageData="imageData.data" :con="condition" v-if="imageData"/> 
    </main>

    <div id="loading" v-if="loading">
        <img src="../assets/spinner.gif" alt="loading">
    </div>
 </template>
 
<script>
    
    import TheData from './TheData.vue'
    import VueEasyLightbox from 'vue-easy-lightbox'
    import axios from 'axios';

    export default {
        data() {
            return {
                    image: null,
                    imageName: "",
                    imageData: null,
                    visible: false,
                    img: null,
                    withPrice: false,
                    condition: "M-",
                    loading: false
                }
            },
        methods: {
            handleFileInput(e) {
                const file = e.target.files[0];
                this.imageName = file.name
                
                // convert image to base64
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => {this.image = reader.result;};
            },
            
            // call API to read image and get data
            async getDataImage() {
                this.loading = true;
                try 
                {
                    await axios.post('http://127.0.0.1:8000/read-image', {image:this.image, withPrice:this.withPrice, condition:this.condition}, {headers: {'Content-Type': 'application/json'}});
                    this.imageData = await axios.get('http://127.0.0.1:8000/data-image')
                    this.img = this.imageData.data.url 
                } 
                catch (error) 
                {
                    alert('Upload failed.');
                }
                this.loading = false;
            },
            
            showImage() {
                this.show()
            },

            show() {
                this.visible = true
            },

            handleHide() {
                this.visible = false
            }
        },

        components:{
            TheData,
            VueEasyLightbox
        }
    }
</script>

<style scoped lang="scss">
    main{
        display: flex;
        flex-direction: column;
        height: 700px;
        margin-top: 100px;
        
        section{
            display: flex;
            justify-content: center;
            align-items: center;

            #upload {
                display: flex;
                flex-direction: column;
                align-items: center;

                h1 {
                    font-size: 32px;
                    margin-bottom: 20px;
                }

                input[type="file"] {
                    margin-bottom: 10px;
                }

                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }

                button:hover {
                    background-color: #3e8e41;
                }

                #price{
                    display: flex;
                    padding: 10px;
                    gap: 10px;

                    select{
                        width: 200px;
                        padding: 5px;
                        background-color: #2f3131;
                        border: 1px solid black;
                        cursor: pointer;
                    }

                    input[type="checkbox"]{
                        margin-top: 5px;
                        width: 15px;
                        height: 15px;
                    }
                }

            }

            #preview {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;

                #image-preview {
                    max-height: 500px;
                    width: 100%;
                    max-width: 500px;
                    margin: 20px;
                    cursor: pointer;

                    &:hover{
                        opacity: .9;
                    }
                }
            }
        }
    }

    #loading{
        width: 100%;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    @media only screen and (max-width: 800px){
    main{
        margin-top: 50px;

        section{
            flex-direction: column;
            gap: 20px;

            #upload{
                h1{
                    font-size: 24px;
                }

                #price{
                    gap: 10px;

                    select{
                        width: 100%;
                    }
                }
            }

            #preview{
                #image-preview{
                    margin: 10px;
                }
            }
        }
    }
}

    @media only screen and (max-width: 500px){
        main{
            width: 500px;

                section{

                    #preview{
                        #image-preview{
                            width: 450px;
                        }
                    }
                }
        }

        #loading{
            width: 500px;
        }
    }

</style>
 