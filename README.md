# Portfolio
<details>
  <summary><b>Datacamp courses</b></summary>
  Hieronder heb ik een screenshot toegevoegt van alle datacamp courses die ik tijdens de minor heb gemaakt, de course van 2 Oct was later ingeleverd vanwege persoonlijke omstandigheden, voor de rest is alles op tijd gemaakt.
  
![Portfolio](https://github.com/mbroer/ads_portfolio/blob/main/datacamp.png)
  
</details>

<details>
  <summary><b>Scrum tickets</b></summary>
  Hieronder staan alle scrum tickets op mijn naam die ik heb afgerond. Bij de meeste tickets heb ik een beschrijving van een paar zinnen zodat andere projectleden een beter inzicht kregen van waar ik mee bezig was. Onze projectgroep heeft gebruik gemaakt van de scrumtool Trello.</br></br>
  
  <details>
    <summary><i>Tickets week 1 tm 5</i></summary>
    
![Week 1 tot en met 5](https://github.com/mbroer/ads_portfolio/blob/main/scrum/1-5.png)
    
  </details>
  

  <details>
    <summary><i>Tickets week 6 tm 10</i></summary>
    
![Week 6 tot en met 10](https://github.com/mbroer/ads_portfolio/blob/main/scrum/6-10.png)
    
  </details>
  

  <details>
    <summary><i>Tickets week 11 tm 16</i></summary>
    
![Week 11 tot en met 16](https://github.com/mbroer/ads_portfolio/blob/main/scrum/11-16.png)
  
<h4>Opmerking week 14</h4>
  Ik had een leuke stageplek gevonden die mij zeer goed financieel wilden compenseren, hiervoor moest ik een applicatie maken om mijn kennis te laten zien voordat ze me de stageplek konden geven. Hiervoor had ik een week de tijd en heb dus (met begrip van de groep) deze week niet aan het project gewerkt om 100% van mijn tijd in deze applicatie te kunnen steken. (En ja ik heb de stageplek gekregen.)
    
  </details>

___
</details>


<details>
  <summary><b>Data prep</b></summary>
  
<h2>FoodBoost csv merge</h2>

  <h3>Beschrijving</h3>
Toen we voor het eerst begonnen met het FoodBoost project, stonden alle datasets los van elkaar, hierdoor was het dus lastig om een goed inzicht te krijgen in hoe alles nou in elkaar zat. Je had bijvoorbeeld het ingrediënten bestand waar elk ingrediënt van elk recept onder elkaar stond. Hierdoor kreeg je een bestand van 72000 rows. Hiervoor heb ik een python script gemaakt die alle informatie van het recept op 1 row zet en de data squished in lijsten. Hierdoor was het vooral voor de groep (die toen nog niet veel ervaring had met het joinen van tables etc) een stuk makkelijker om echt te kunnen beginnen met het FoodBoost project.
<br><br>
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
  [Notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/join_all_csv.ipynb)<br><br>
  [CSV bestand](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/food_merge_all.csv)<br><br>
Screenshot resultaat:
  ![Screenshot Resultaat](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/merged.png)
  
  </details>


<h2>FoodBoost simulated users</h2>

  <h3>Beschrijving</h3>
  Ons doel voor het FoodBoost project was om te kijken of een persoon een recept wel of niet lekker zou vinden, om hiervoor een model te maken hadden we dus bestaande informatie nodig om het model te kunnen trainen en testen, een oplossing die ik had bedacht was om een applicatie te schrijven die gebruikers op een semi realistische manier favoriete recepten kan genereren.
  
[Applicatie source code](https://github.com/mbroer/ads_portfolio/tree/main/apps/foodboost/simulated%20users)
  
Ik ben begonnen met het opschonen van de bestaande dataframes, te zien in [ads_cleaner.py](https://github.com/mbroer/ads_portfolio/blob/main/apps/foodboost/simulated%20users/ads_cleaner.py).  Ik heb onnodige kolommen gedropt, zoals stars, url en image. Hierna heb ik dezelfde logica gebruikt als in het vorige hoofdstuk om deze dataframes op elkaar te joinen. Ook heb ik ervoor gezorgd dat kolommen die meerdere keren voorkwamen te droppen.
  
Hierna heb ik utility functies geschreven om makkelijk informatie uit die dataframes te kunnen halen. Denk hierbij het omzetten van een dataframe row in een object, of een functie om alle informatie van een recept op te halen via een ID. Ook een zoek algoritme om makkelijk informatie op te kunnen halen

  %%%plaatjes ofzo
  
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
Output gegenereerde gebruiker<br>
![Gegenereerde user](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/user_gen.png)    
    Gesorteerd op favorite descending ~8000 rows
  </details>

<h2>FoodBoost ingredient translate</h2>
<h2>FoodBoost description scraper</h2>
  
  
  
</details>

<details>
  <summary><b>Data collection</b></summary>
  
</details>

<details>
  <summary><b>Visualisatie</b></summary>
  
</details>

