<script lang="ts" setup>
import { useRoute, useRouter } from "vue-router"

const route = useRoute()
const router = useRouter()

router.replace({ path: "/" + route.params.path, query: route.query })
</script>

<template>
  <div />
</template>

<style scoped>
.box {
  background: darkblue;
}
</style>