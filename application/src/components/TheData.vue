<template>
    <div class="image-data">
        <table>
            <tr>
                <td><h2>Title</h2></td>
                <td><h2>Genre</h2></td>
                <td><h2>Label</h2></td>
                <td><h2>Country</h2></td>
                <td><h2>Year</h2></td>
                <td><h2>Condition: {{ con }}</h2></td>
                <td><h2>Discogs</h2></td>
            </tr>

            <tr  v-if="imageData.data" v-for="data in imageData.data">
                <td>{{ data.title }}</td>
                <td>{{ data.genre }}</td>
                <td>{{ data.label }}</td>
                <td>{{ data.country }}</td>
                <td>{{ data.year }}</td>
                <td>{{ data.price }}$</td>
                <td><a :href="data.uri" target="_blank">View on Discogs</a></td>
            </tr>
            
            <tr>
                <td colspan="7">
                    <h2>Not found more <br>(Make sure the image is not blur)</h2>
                </td>
            </tr>
        </table>        
    </div>
</template>
  
<script>
    export default {
        props: ['imageData', 'con']
    }
</script>
  
<style scoped lang="scss">
    .image-data {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        
        table {
            border-collapse: collapse;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-bottom: 50px;
            width: 65%;
            
            td {
                border: 1px solid #ddd;
                padding: 15px;
                font-size: 18px;
            }

            a {
                display: inline-block;
                width: 100%;
                padding: 5px 10px;
                border-radius: 4px;
                text-decoration: none;
                color: #fff;
                background-color: #4CAF50;
                transition: background-color 0.3s ease;

                &:hover{
                    background-color: #3e8e41;
                }
            }
        }
    }

    @media only screen and (max-width: 1100px){
        .image-data {
            table{
                margin: 0px 10px 0px 10px;
            }
        }
    }

    @media only screen and (max-width: 800px){
        .image-data {
            table{
                td{
                    font-size: 14px;
                }

                h2{
                    font-size: 16px;
                }
            }
        }
    }

    @media only screen and (max-width: 600px){
        .image-data {
            margin-top: 20px;
        }
    }

    @media only screen and (max-width: 600px){
        .image-data {
            table{
                td{
                    font-size: 10px;
                }

                h2{
                    font-size: 12px;
                }
            }
        }
    }
 
</style>
  