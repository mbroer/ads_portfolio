import { createApp } from "vue";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import Choices from 'choices.js/public/assets/scripts/choices.min.js';

//import { parse } from '@vanillaes/csv'

/*
var request = new XMLHttpRequest();
request.open("GET", "./w.txt", false);
request.send(null)	
var my_JSON_object = JSON.parse(request.responseText);
console.log(my_JSON_object.result[0]); 
*/

createApp(App).mount("#app");