<template>
    <main>
        <vue-easy-lightbox
        scrollDisabled
        escDisabled
        moveDisabled
        :visible="visible"
        :imgs="img"
        @hide="handleHide"
        ></vue-easy-lightbox>

        <section>
            <div id="Upload">
                <h1>Upload Image</h1>
                <input type="file" @change="handleFileInput">
                Display the median price of vinyl? <br>
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
                <button @click="getDataImage">Upload</button>
            </div>

            <div id="preview" v-if="imageData">
                <img id="image-preview" :src="image"  alt="Uploaded Image" @click="showSingle">
            </div>
        </section>

        

        <TheData :imageData="imageData.data" :con="condition" v-if="imageData"/>
    </main>
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
                    condition: "M-"
                }
            },
        methods: {
            handleFileInput(e) {
                const file = e.target.files[0];
                this.imageName = file.name
                
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => {this.image = reader.result;};
            },

            async getDataImage() {
                    try 
                    {
                        // await axios.post('http://127.0.0.1:8000/read-image', {image:this.image, withPrice:this.withPrice, condition:this.condition}, {headers: {'Content-Type': 'application/json'}});
                        this.imageData = await axios.get('http://127.0.0.1:8000/data-image')
                    } 
                    catch (error) 
                    {
                        alert('Upload failed.');
                    }
            },
            showSingle() {
                this.img = this.imageData.data.url 
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
    justify-content: center;
    height: 1000px;
    
    section{
        display: flex;
        justify-content: center;
        align-items: center;

        #Upload {
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
                    background-color: #282a3a;
                    border: 1px solid black;
                    cursor: pointer;
                }

                input[type="checkbox"]{
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
                margin: 20px;
                cursor: pointer;

                &:hover{
                    opacity: .9;
                }
            }
        }
    }
}
</style>
 