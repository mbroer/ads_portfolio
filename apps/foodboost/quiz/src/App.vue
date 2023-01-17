<template>
  <DemoComponent msg=""></DemoComponent>
  <!--<QuizComponent msg=""></QuizComponent>-->
</template>

<script>

//import QuizComponent from './components/Quiz.vue'
import DemoComponent from './components/Demo.vue'

export default {
  name: 'App',
  components: {
    //QuizComponent,
    DemoComponent
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.py-5
{
  background-color: #fff4e0;

}

.header{
  background-color: red;
}
</style>

