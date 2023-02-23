<template>
    <div class="image-data">
        <table>
            <tr>
                <td><h2>Title</h2></td>
                <td><h2>Genre</h2></td>
                <td><h2>Label</h2></td>
                <td><h2>Country</h2></td>
                <td><h2>Year</h2></td>
                <td><h2>Price ({{ con }})</h2></td>
                <td><h2>Discogs</h2></td>
            </tr>

            <tr  v-if="imageData.data" v-for="data in imageData.data">
                <td>{{ data.title }}</td>
                <td>{{ data.genre }}</td>
                <td>{{ data.label }}</td>
                <td>{{ data.country }}</td>
                <td>{{ data.year }}</td>
                <td>{{ data.price }}</td>
                <td><a :href="data.uri" target="_blank">View on Discogs</a></td>
            </tr>
            
            <tr>
                <td colspan="7"><h1>Not found more</h1></td>
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
        width: 90%;
        border-collapse: collapse;
        color: white;
        font-family: Arial, sans-serif;
        font-size: 14px;
        text-align: center;
    }

    td {
        border: 1px solid #ddd;
        padding: 10px 10px;
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
 
</style>
  