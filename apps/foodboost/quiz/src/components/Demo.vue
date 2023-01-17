<template>

<div class="form-group">
  <div class="collapse show" id="tagCollapsable">
    <div class="container py-5">
        <div class="display-4">Selecteer categorië</div>
        <div id="row_1" class="row justify-content-center">
          <div class="col-md-4 py-5">

                <select class="selectpicker form-control border-0 mb-1 px-4 py-4 rounded shadow">
                    <option value="None">Categorieën</option>
                </select>

          </div>
        </div>
    </div>
  </div>
</div>

<div class="form-group">
  <div class="collapse" id="quizCollapsable">
    <div class="container py-5">

      <!-- DEMO 1 -->
      <div>
        <div class="display-3">Maak een keuze</div>

        <div id="row_1" class="row justify-content-center">
          <div class="col-md-4">
            <div class="customcard hover hover-1 text-white rounded">

                <img id="image1" src="https://static.ah.nl/static/recepten/img_049133_1024x748_JPG.jpg" alt="">
                <div class="hover-overlay"></div>
                <div class="hover-1-content px-5 py-4">
                    <h4 class="hover-1-title text-uppercase font-weight-bold mb-0"> <span id="recipe_title1" class="font-weight-light"> </span></h4>
                    <p id="desc1" class="rounded hover-1-description font-weight-light mb-0"></p>
                    <input id="id1" type="hidden" class="recipe_id" value="34657" />
                </div>

            </div>
          </div> <!-- col end -->

          <div class="col-md-4">
            <div class="customcard hover hover-1 text-white rounded">
              <img id="image2" src="https://static.ah.nl/static/recepten/img_007839_1024x748_JPG.jpg" alt="">
              <div class="hover-overlay"></div>
              <div class="hover-1-content px-5 py-4">
                <h4 class="hover-1-title text-uppercase font-weight-bold mb-0"> <span id="recipe_title2" class="font-weight-light"> </span></h4>
                <p id="desc2" class="rounded hover-1-description font-weight-light mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
                <input id="id2" type="hidden" class="recipe_id" value="34657" />
              </div>
            </div>
          </div> <!-- col end -->

        </div> <!-- row end -->

        <div class="row justify-content-center py-4">
          <div class="col-md-4">
            <div class="customcard hover hover-1 text-white rounded">
              <img id="image3" src="https://static.ah.nl/static/recepten/img_RAM_PRD156799_1024x748_JPG.jpg" alt="">
              <div class="hover-overlay"></div>
              <div class="hover-1-content px-5 py-4">
                <h4 class="hover-1-title text-uppercase font-weight-bold mb-0"> <span id="recipe_title3" class="font-weight-light"> </span></h4>
                <p id="desc3" class="rounded hover-1-description font-weight-light mb-0"></p>
                <input id="id3" type="hidden" class="recipe_id" value="34657" />
              </div>
            </div>
          </div> <!-- col end -->

          <div class="col-md-4">
            <div class="customcard hover hover-1 text-white rounded">
              <img id="image4" src="https://static.ah.nl/static/recepten/img_007689_1024x748_JPG.jpg" alt="">
              <div class="hover-overlay"></div>
              <div class="hover-1-content px-5 py-4">
                <h4 class="hover-1-title text-uppercase font-weight-bold mb-0"> <span id="recipe_title4" class="font-weight-light"> </span></h4>
                <p id="desc4" class="rounded hover-1-description font-weight-light mb-0"></p>
                <input id="id4" type="hidden" class="recipe_id" value="34657" />
              </div>
            </div>
          </div> <!-- col end -->
        </div> <!-- row end -->

      </div>
      <div class="row justify-content-center">
          <div class="col-md-8">
            <h4 id="description_global" style="min-height: 75px" class="fw-bold"></h4>
          </div>
      </div>
        <h2 id="counter" class="fw-bold"></h2>
    </div>
  </div>
</div>

<div class="form-group">
  <div class="collapse" id="weekmenuCollapsable">
    <div class="container py-5">
      <div class="py-5">
        <div class="display-3">Weekoverzicht</div>
          <div id="row_1" class="row justify-content-center">
            <div class="col-md-4">

              <table id="weekmenu" class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Dag</th>
                    <th scope="col">Recept</th>
                  </tr>
                </thead>
                <tbody>
                  <tr id="day1"></tr>
                  <tr id="day2"></tr>
                  <tr id="day3"></tr>
                  <tr id="day4"></tr>
                  <tr id="day5"></tr>
                  <tr id="day6"></tr>
                  <tr id="day7"></tr>
                </tbody>
              </table>
              <button id="refreshbtn" type="button" class="btn btn-secondary btn-lg">Terug naar overzicht</button>
            </div>
          </div>
      </div>
    </div>
  </div>
</div>

</template>

<script>
import dataset from './dataset.json';
import description from './desc.json';
import { Collapse } from 'bootstrap';
import Choices from 'choices.js';

export default 
{
  name: "DemoComponent",
};

window.addEventListener("DOMContentLoaded", init, false);
var input_recipe_ids = [];
var cleaned_dataset = [];
var quiz_dataset = [];
var accept_input = true;
var nodupes = [];

const RECIPES_TO_SELECT = 5;
const a_days = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'];

function initTagsDropdown(select)
{
  var tags = ['5-ingrediënten', 'amerikaans', 'aziatisch', 'bakken', 'barbecue', 'bijgerecht', 'biologisch', 'borrel', 'borrelhapje', 'brood/sandwiches', 'brunch', 'budget', 'camping', 'chinees', 'couscous', 'curry', 'diner', 'drankje met alcohol', 'drankje zonder alcohol', 'eiwitrijk', 'engels', 'frans', 'frituren', 'gebak', 'gezond', 'glutenvrij', 'gourmet', 'grillen', 'halloween', 'hollands', 'hoofdgerecht', 'in te vriezen', 'indiaas', 'indonesisch', 'italiaans', 'japans', 'kerst', 'keukenmachine', 'kindergerecht', 'kinderrecepten', 'koken', 'lactosevrij', 'lunch', 'maaltijdsoep', 'marokkaans', 'mediterraan', 'mexicaans', 'midden-oosters', 'moederdag', 'nagerecht', 'noedels', 'ontbijt', 'oud &amp; nieuw', 'oven', 'pasen', 'pasta', 'picknick', 'quiche', 'rijst', 'roerbakken/wokken', 'salade', 'saus/dressing', 'sinterklaas', 'sinterklaasavond', 'slank', 'snel', 'soep', 'spaans', 'stamppot', 'stoven', 'suikerbewust', 'thais', 'traktatie', 'tussendoortje', 'vaderdag', 'valentijn', 'veganistisch', 'vegetarisch', 'verjaardag', 'vooraf te maken', 'voorgerecht', 'wat eten we vandaag', 'wrap', 'zonder vlees', 'zonder vlees/vis', 'zuid-amerikaans'];

    for(var i=0; i<tags.length; i++) 
    {
      var elem = document.createElement("option");
      elem.text = tags[i];
      elem.value = tags[i];

      select.add(elem);
    }
}

function init()
{
  console.log("init");

  cleaned_dataset = cleanDataset();

  const element = document.querySelector('.selectpicker');

  initTagsDropdown(element);
  initWeekMenuDays();


  const choices = new Choices(element, { 
    loadingText: 'Laden...',
    noResultsText: 'Geen resulaten gevonden',
    noChoicesText: 'Geen keuzes om uit te kiezen',
    itemSelectText: 'Klik om te selecteren',
  });

  element.addEventListener( 'choice', function(event)  
  {
    gotoQuiz(event.detail.choice.value)
  }, false, );

}

function gotoQuiz(tag)
{
  console.log("selected "+tag);
  setupListeners();
  document.getElementById("counter").innerHTML = "0/" + RECIPES_TO_SELECT;

  var filtered = [];

  cleaned_dataset.forEach(function(element, index) { 
    if(element.list_tags.includes(tag))
    {
      element.id = index;
      filtered.push(element);
    }
  });

  console.log("filtered recipes length: "+filtered.length);
  nodupes = [];

  quiz_dataset = filtered;

  var element = document.getElementById("tagCollapsable");
  var myCollapse = new Collapse(element);
  myCollapse.toggle();

  element = document.getElementById("quizCollapsable");
  myCollapse = new Collapse(element);
  myCollapse.toggle();

  fillCards();
}

function cleanDataset()
{
  console.log("recipes loaded: " + Object.keys(dataset).length);

  var clean = [];

  Object.entries(dataset).forEach(function(e, i) 
  {
    let row = e[1];

    if(row.list_ingredient && row.list_ingredient != 'nan')
     row.list_ingredient          = eval(row.list_ingredient);

    if(row.list_ingredient_quantity && row.list_ingredient_quantity != 'nan')
      row.list_ingredient_quantity = eval(row.list_ingredient_quantity);

    //if(row.list_ingredient_unit && row.list_ingredient_unit != 'nan')
    //  row.list_ingredient_unit     = eval(row.list_ingredient_unit);
    
    //if(row.list_nutrition && row.list_nutrition != 'nan')
    //  row.list_nutrition           = eval(row.list_nutrition);
    
    //if(row.list_nutrition_values && row.list_nutrition_values != 'nan')
    //  row.list_nutrition_values    = eval(row.list_nutrition_values);
    
    if(row.list_tags && row.list_tags != 'nan')
      row.list_tags                = eval(row.list_tags);

    row.descr = description[ ""+(i+1) ].d;

    clean.push(row);
  });

  console.log("dataset cleaned");
  console.log(clean[0]);
  console.log(clean[8705]);
  return clean;
}

function setupListeners()
{
  for (var element of document.getElementsByClassName("hover-1")) 
  {
    element.addEventListener("click", selected_recipe, false);
    element.onmouseenter = function(){ showTooltip(this) };
    element.onmouseleave = function(){ hideTooltip('') };
  }
    
  document.getElementById("refreshbtn").onclick = function(){

  //var element = document.getElementById("quizCollapsable");

  new Collapse(document.getElementById("weekmenuCollapsable")).toggle();
  new Collapse(document.getElementById("tagCollapsable")).toggle();

  input_recipe_ids = [];
  quiz_dataset = [];

  clearWeekMenu();

    //window.location.reload()
  };
}

function showTooltip(elem)
{
  setTimeout(function() { 
    if( elem.matches(':hover') )
    {
      let d = cleaned_dataset[elem.querySelector('input').value].descr;

      setToolTipText(d == 'nan' ? 'Geen beschrijving beschikbaar!' : d);
    }
  }, 500);
}

function hideTooltip()
{
  let dom = document.getElementById("description_global");

  dom.classList.add("fade_out_custom");

  setTimeout(function() {  setToolTipText(''); }, 150);
}

function setToolTipText(text)
{
  let dom = document.getElementById("description_global");
  dom.innerHTML = text;

  dom.classList.remove("fade_out_custom");

  if(text == '')
    dom.classList.remove("fade_custom");
  else
    dom.classList.add("fade_custom");
}

function selected_recipe()
{
  if(!accept_input)
    return;

  accept_input = false;

  const recipe_id = this.getElementsByClassName("recipe_id")[0].value;
  const counter = document.getElementById("counter");

  //if(!input_recipe_ids.includes(recipe_id))
    input_recipe_ids.push(recipe_id);

  //console.log(input_recipe_ids);

  counter.innerHTML = input_recipe_ids.length + "/" + RECIPES_TO_SELECT;

  if(input_recipe_ids.length >= RECIPES_TO_SELECT)
  {
    setTimeout(function() { 
      showWeekMenu();
    }, 100);

    cardsSpin();

    accept_input = true;
    return;
  }

  cardsFold();

  setTimeout(function() { 
    accept_input = true;
  }, 1000);

  //fillCards();
}

function insertCard(recipe_id, id)
{
  let recipe = quiz_dataset[recipe_id];

  var img = document.getElementById("image"+id);
  var title = document.getElementById("recipe_title"+id);
  var desc = document.getElementById("desc"+id);
  var hidden_id = document.getElementById("id"+id);



  img.src = recipe.image;

  title.innerHTML = recipe.recipe.length > 30 ? recipe.recipe.substring(0, 30) + "..." : recipe.recipe;
  hidden_id.value = recipe.id;
  desc.innerHTML = `Voor ${recipe.persons} personen.<br>
                    Bereidingstijd: ${recipe.time}min,
                    Calorieën: ${recipe.calories}<br>
                    `;
}

function fillCards()
{
  //console.log(quiz_dataset.length);

  for(var i=1;i<=4;i++)
  {
    let rand = Math.floor(Math.random() * quiz_dataset.length);

    let j =0;
    while(input_recipe_ids.includes(rand) || nodupes.includes(rand))
    {
      j++;
      rand = Math.floor(Math.random() * quiz_dataset.length);
      if(j > 20 && !nodupes.includes(rand))
        break; //just give up
    }

    nodupes.push(rand);
    insertCard(rand, i);
  }

  nodupes = [];
}

function insertSingleCardAtPos(pos)
{
  let rand = Math.floor(Math.random() * quiz_dataset.length);

  let i = 0;
  while(input_recipe_ids.includes(rand) || nodupes.includes(rand))
  {
    i++;
    rand = Math.floor(Math.random() * quiz_dataset.length);

    if(i > 20 && !nodupes.includes(rand))
    {
      break; //just give up
    }
  }

  nodupes.push(rand);

  insertCard(rand, pos);
}

function cardsSpin()
{
  var cards = document.getElementsByClassName("customcard");

  Array.prototype.forEach.call(cards, function(elem, index) 
  {
    elem.classList.add("no-hover");
    elem.classList.add("cardspin");
  });

  cards = document.getElementsByClassName("customcard");

  setTimeout(function() { 
      Array.prototype.forEach.call(cards, function(elem, index) 
      {
        elem.classList.remove("no-hover");
        elem.classList.remove("cardspin");
      });

    }, 1000);
}

function cardsFold()
{

  hideTooltip();
  
  var cards = document.getElementsByClassName("customcard");

  Array.prototype.forEach.call(cards, function(elem, index) 
  {
    elem.classList.add("no-hover");

    setTimeout(function() { 
      elem.classList.add("cardflip");

      updateCard(elem, index);

    }, index * 150 - (index * 50));
     
  });

  Array.prototype.forEach.call(cards, function(elem) 
  {
      elem.classList.remove("no-hover");
      elem.classList.remove("cardflip");
  });

  nodupes = [];
}

function updateCard(elem, index, nodupes)
{
  //elem = elem.getElementsByTagName('img')[0];

  setTimeout(function() { 
    insertSingleCardAtPos(index+1);

    //elem.src = "https://static.ah.nl/static/recepten/img_007839_1024x748_JPG.jpg";
  }, 100);

}


function showWeekMenu()
{
  /* model hier dus */

  let ds = quiz_dataset; //cleaned_dataset voor kompleet random

  for(let i=0;i<7;i++)
  {
    let rand = Math.floor(Math.random() * ds.length);
    fillWeekMenu(i, ds[rand]);
  }

  var element = document.getElementById("quizCollapsable");
  var element2 = document.getElementById("weekmenuCollapsable");

  var myCollapse = new Collapse(element);
  var myCollapse2 = new Collapse(element2);

  myCollapse.toggle();
  myCollapse2.toggle();
}

function initWeekMenuDays()
{
  let startday = new Date().getDate();

  for( let i=0; i < a_days.length; i++) 
  {
    let row = document.getElementById("day" + (i+1));

    let rowhead = document.createElement('th');
    rowhead.classList.add('text-start');
    rowhead.scope = "row";

    rowhead.innerHTML = a_days[(i + startday) % a_days.length];
    row.appendChild(rowhead);
  }

}

function fillWeekMenu(day, recipe)
{
  var row = document.getElementById("day" + (day+1));

  var newel = document.createElement('td');
  newel.classList.add("text-end")

  newel.innerHTML += `<a href="${recipe.url}" target="_blank" class="link-dark">${recipe.recipe}</a>`;

  row.appendChild(newel);
}

function clearWeekMenu()
{
  for(let i=1; i<=7;i++)
    document.getElementById("day" + i).querySelector('td').remove();
}

</script>

<style scoped>

.hover {
  overflow: hidden;
  position: relative;
  padding-bottom: 60%;
  transition: all 0.5s cubic-bezier(.71,0,.33,1.56) 0ms;
  -webkit-user-select: none; /* Safari */        
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
}

.hover:not(.no-hover):hover {
  transform: scale(1.05);
  transition: all 0.5s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.hover-overlay {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 90;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.hover img {
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.hover-content {
  position: relative;
  z-index: 99;
  text-align: center;
}

.hover-1 img {
  width: 105%;
  position: absolute;
  top: 0;
  left: -5%;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.hover-1-content {
  position: absolute;
  bottom: 0;
  left: 0;
  z-index: 99;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
  text-align: center;
}

.hover-1 .hover-overlay {
  background: rgba(0, 0, 0, 0.5);
}

.hover-1-description {
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
  opacity: 0;
}

.hover-1:hover .hover-1-content {
  bottom: 2rem;
}

.hover-1:hover .hover-1-description {
  opacity: 1;
  transform: none;
  background-color: rgba(0, 0, 0, 0.5);
}

.hover-1:hover .hover-1-title {
  opacity: 0;
  transform: none;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.hover-1-title {
  opacity: 1;
  transform: none;
  transition: all 0.4s cubic-bezier(.71,0,.33,1.56) 0ms;
  background-color: rgba(1,1,1,0);
  min-width:300px
}

.hover-1:hover img {
  left: 0;

}

.hover-1:hover .hover-overlay {
  opacity: 0;
}

.cardflip
{
  -webkit-transform-style: preserve-3d;
  /*-webkit-backface-visibility: hidden;*/

  animation-duration: .5s;
  animation-name: flip;
}

.cardspin
{
  -webkit-transform-style: preserve-3d;
  transition: all 0.35s cubic-bezier(.71,0,.33,1.56) 0ms;
  animation-duration: .3s;
  animation-name: disapp;
}

@keyframes disapp
{
  0%{
    scale: 100%;
    -webkit-filter: blur(0px);
    opacity:100%;
  }
  25% {
    scale: 120%;
    -webkit-filter: blur(0px);
    opacity:100%;
  }
  50% {
    scale: 80%;
    opacity:50%;
  }
  75% {
    scale: 40%;
    opacity:0%;
  }
  100% {
    scale: 0%;
    -webkit-filter: blur(2px);
    opacity:0%;
  }
}

@keyframes flip 
{

  25% {
    transform: rotateY( 90deg );
    -webkit-filter: blur(1px);
  }

  50% {
    /* transform: rotateY( 180deg ); */
    -webkit-filter: blur(2px);
  }

  75% {
    /*transform: rotateY( 270deg );*/
    -webkit-filter: blur(1px);
  }

  100% {
    /*transform: rotateY( 360deg );*/
    -webkit-filter: blur(0px);
  }

}

.table td, .table th
{
    text-align:left;
}

#right, .table td + td, .table th + th
{
    text-align:right !important;
}

.btn.outline {
  background: none;
  padding: 12px 22px;
}

.btn-primary.outline {
  border: 2px solid #0099cc;
  color: #0099cc;
}

.btn-primary.outline:hover, .btn-primary.outline:focus, .btn-primary.outline:active, .btn-primary.outline.active, .open > .dropdown-toggle.btn-primary {
  color: #33a6cc;
  border-color: #33a6cc;
}
.btn-primary.outline:active, .btn-primary.outline.active {
  border-color: #007299;
  color: #007299;
  box-shadow: none;
}


.table body {
  text-align: right !important;
  color: red;
}

.py-5{
  height: 100%;
}

html, body {height: 100%}

.bg-light {
  background: #eef0f4;
}

.choices__list--dropdown .choices__item--selectable {
  padding-right: 1rem;
}

.choices__list--single {
  padding: 0;
}

.card {
  transform: translateY(-50%);
}

.choices[data-type*=select-one]:after {
  right: 1.5rem;
}

.shadow {
  box-shadow: 0.3rem 0.3rem 1rem rgba(178, 200, 244, 0.23);
}

a {
  text-decoration: none;
  color: inherit;
  transition: all 0.3s;
}

.fade_custom{
  animation-duration: .35s;
  animation-name: text_fade;
  transition: all 0.35s cubic-bezier(.71,0,.33,1.56) 0ms;
}

.fade_out_custom{
  animation-duration: .2s;
  animation-name: text_fade_out;
  transition: all 0.2s cubic-bezier(.71,0,.33,1.56) 0ms;
}

@keyframes text_fade 
{
  0% {
    scale: 0%;
    opacity: 0%;
  }

  20% {
    scale: 25%;
    opacity: 25%;

  }

  45% {
    scale: 50%;
    opacity: 50%;

  }

  75% {
    scale: 125%;
    opacity: 100%;

  }

  100% {
    scale: 100%;
    opacity: 100%;
  }

}

@keyframes text_fade_out
{
  0% {
    scale: 100%;
    opacity: 100%;
  }

  20% {
    scale: 125%;
    opacity: 75%;
  }

  45% {
    scale: 50%;
    opacity: 50%;
  }

  75% {
    scale: 25%;
    opacity: 25%;
  }

  100% {
    scale: 0%;
    opacity: 0%;
  }

}


</style>

 <style>
        @import "~/node_modules/choices.js/public/assets/styles/base.min.css";
        @import "~/node_modules/choices.js/public/assets/styles/choices.min.css";
  </style>