<template>
    <TheHeader />
    <TheUpload />
</template>

<script>
  import TheUpload from '@/components/TheUpload.vue'
  import TheHeader from '@/components/TheHeader.vue'

  export default {
    components:{
      TheHeader,
      TheUpload
    }
  }
</script>