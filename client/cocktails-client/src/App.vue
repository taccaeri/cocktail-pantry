<template>
  <div id="app">
    <Cocktails />
  </div>
</template>
<script>
import Cocktails from "./components/Cocktail.vue";
export default {
  name: "App",
  components: {
    Cocktail,
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
