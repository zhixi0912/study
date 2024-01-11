<template>
  <div class="item-container">
      <div class="item" v-for="n in 10000">{{item}}</div>
  </div>
</template>

<style lang="scss" scoped>
.item-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  border: 3px solid #ff4400;
  .item {
    width: 5px;
    height: 3px;
    background: #ccc;
    margin: 0.1em;
  }
}
</style>
