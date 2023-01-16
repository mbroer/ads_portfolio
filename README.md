<h1>Portfolio</h1>
Applied Data Science Portfolio<br>
Michael Broer, 20105533
  
<h2>Globaal</h2>
In dit hoofdstuk worden alle globale onderdelen van de minor doorgenomen.
<details>
  <summary><h3>Datacamp courses</h3></summary>
  Hieronder heb ik een screenshot toegevoegt van alle datacamp courses die ik tijdens de minor heb gemaakt, de course van 2 Oct was later ingeleverd vanwege persoonlijke omstandigheden, voor de rest is alles op tijd gemaakt.
  
![Portfolio](https://github.com/mbroer/ads_portfolio/blob/main/datacamp.png)
  
</details>
<details>
  
  <summary><h3>Scrum tickets</h3></summary>
  Hieronder staan alle scrum tickets op mijn naam die ik heb afgerond. Bij de meeste tickets heb ik een beschrijving van een paar zinnen zodat andere projectleden een beter inzicht kregen van waar ik mee bezig was. Onze projectgroep heeft gebruik gemaakt van de scrumtool Trello.</br></br>
  
  <details>
    <summary><h4>Tickets week 1 tm 5</h4></summary>
    
![Week 1 tot en met 5](https://github.com/mbroer/ads_portfolio/blob/main/scrum/1-5.png)
    
  </details>
  

  <details>
    <summary><h4>Tickets week 6 tm 10</h4></summary>
    
![Week 6 tot en met 10](https://github.com/mbroer/ads_portfolio/blob/main/scrum/6-10.png)
    
  </details>
  

  <details>
    <summary><h4>Tickets week 11 tm 16</h4></summary>
    
![Week 11 tot en met 16](https://github.com/mbroer/ads_portfolio/blob/main/scrum/11-16.png)
  
<h4>Opmerking week 14</h4>
  Ik had een leuke stageplek gevonden die mij zeer goed financieel wilden compenseren, hiervoor moest ik een applicatie maken om mijn kennis te laten zien voordat ze me de stageplek konden geven. Hiervoor had ik een week de tijd en heb dus (met begrip van de groep) deze week niet aan het project gewerkt om 100% van mijn tijd in deze applicatie te kunnen steken. (En ja ik heb de stageplek gekregen.)
    
  </details>
  


___
</details>

<details>
  
<summary><h3>Domain knowledge</h3></summary>
  
</details>

<h2>Data</h2>

<details>
  <summary><h3>Data prep</h3></summary>
  
<h3>FoodBoost csv merge</h3>

  <h4>Beschrijving</h4>
Toen we voor het eerst begonnen met het FoodBoost project, stonden alle datasets los van elkaar, hierdoor was het dus lastig om een goed inzicht te krijgen in hoe alles nou in elkaar zat. Je had bijvoorbeeld het ingrediënten bestand waar elk ingrediënt van elk recept onder elkaar stond. Hierdoor kreeg je een bestand van 72000 rows. Hiervoor heb ik een python script gemaakt die alle informatie van het recept op 1 row zet en de data squished in lijsten. Hierdoor was het vooral voor de groep (die toen nog niet veel ervaring had met het joinen van tables etc) een stuk makkelijker om echt te kunnen beginnen met het FoodBoost project.
<br><br>
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
  [Notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/join_all_csv.ipynb)<br><br>
  [CSV bestand](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/food_merge_all.csv)<br><br>
Screenshot resultaat:
  ![Screenshot Resultaat](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/merged.png)
  
  </details>


<h3>FoodBoost simulated users</h3>

  <h4>Beschrijving</h4>
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

<h3>FoodBoost CSV naar Json</h3>
  <h4>Beschrijving</h4>
  Voor het FoodBoost project moest ik voor mijn applicatie een csv bestand omzetten naar json, dit was gelukkig vrij simpel en kon met een file reader simpel mijn csv omzetten zodat ik een json bestand in kon laden en dan via het ID van het recept, de beschrijving van dat recept kon ophalen.
  
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
    %%%link naar notebook
    %%%img resultaat
    
  </details>
  
  <h3>FoodBoost Ingredient Groeperen</h3>
  <h4>Beschrijving</h4>
  Tijdens het foodboost project kwamen we erachter dat het model veel moeite had om voorspellingen te maken, een gebruiker die veel recepten met tomaat lekker vond, zou een lage score geven aan een recept waar ook tomaat in zit, maar dan met een andere naam. Een voorbeeld hiervan is een user met favoriete recepten zoals: tomatensalade, tomatensoep, plakken tomaat en komkommer, en dan een voorspelling op bijvoorbeeld het gerecht gesneden tomaat. Hier gaf het model aan dat de gebruiker gesneden tomaat niet lekker zou vinden. Na discussie gingen wij ervan uit als projectgroep dat het model de correlatie tussen tomaten en tomaat niet kon vinden.

Een oplossing die we hadden verzonnen is om te proberen zoveel mogelijk ingredienten te groeperen in categorieën, dus tomaat, tomaten, tomaatje, tomatenstukes = categorië tomaat.

Ik heb hier geprobeerd een groepeer script voor te maken die automatisch ingredieënten groepeerd in categorieën.
  
Omdat de meeste systemen voor string manipulation alleen werken voor de engelse taal, was de eerste stap om de strings te vertalen naar het engels,
hiervoor heb ik een script gemaakt die via de google translate api de ingredieënten vertaald van het Nederlands naar het Engels:

  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
    <h5>resultaat</h5>
    
[Translated ingredients CSV](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/translated_ingredients.csv)
    
  </details
  
  
%%%translate (link naar data collection), stopwords, verkleinwoorden, simularity score, etc
  
  
</details>

<details>
  <summary><h3>Data collection</h3></summary>
  

  
  
  
  
<h3>FoodBoost Description Scraper</h3>
Voor de applicatie van het FoodBoost project wilde ik de beschrijving van het gerecht tonen omdat het naar mijn mening een cruciaal is voor een gebruiker om een beter idee te krijgen of hij een gerecht wel of niet lekker gaat vinden, en omdat het de applicatie visueel leuker maakt.

![Screenshot app](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/app.png)
  
Deze beschrijvingen stonden niet in de originele databestanden van recepten, maar gelukkig wel een url van waar deze recepten zijn gehaald. Op de meeste pagina’s van deze recepten stond een kleine beschrijving wat het gerecht inhoudt. Hiervoor heb ik een scraper gemaakt in python om deze beschrijvingen op te halen en in csv formaat op te slaan. Ik heb dit gedaan met de python package BeautifulSoup. Ik heb het originele dataframe ingeladen, en vervolgens elke url afgelopen en het ID van het recept waar de url bij hoort opgeslagen, vervolgens heb ik een selector gemaakt voor de description html tekst, en dit bij de ID van het recept gezet. Het uiteindelijke resultaat was een csv die ingeladen kon worden op de applicatie:
  
%%%image
  
  
</details>

<details>
  <summary><h3>Visualisatie</h3></summary>
  <h4>Beschrijving</h4>
  Bij de start van het container project kwam onze groep er snel achter dat het zeer lastig was om een goed beeld te krijgen van wat er nou precies gebeurde, we hadden   een matrix van een grid van containers voorbeeld:<br>
    
[ 0,0,1,<br>
  1,2,1,<br>
  1,0,2 ]<br>
    
  Dit was één laag van containers, en ik zag al gelijk dat dit een probleem zou gaan worden met meerdere containers met meerdere stapels containers. Hierdoor kwam ik met het idee om een applicatie te bouwen om de containers in een grid te kunnen visualiseren in een 3d omgeving. Om dit zo makkelijk mogelijk te maken voor de rest van de projectgroep wilde ik deze applicatie maken in python, ik heb dus gekozen om met de vPython library te werken. vPython is een basic package waar je een 3d omgeving kan maken en een aantal shapes in kunt 'spawnen' op coordinaten. vPython is een verouderde package dus er zaten limitaties op wat ik kon doen. Een snel voorbeeld is dat het onmogelijk is om verschillende textures te gebruiken op één object, hierdoor kon ik niet een rechthoek maken met 5 verschillende container textures (top, bottom, sides, front, back). Hiervoor moest ik dus 6 wall objects maken elk met een eigen texture, deze objecten moesten daarna in de juiste coordinaten worden gezet om het weer een rechthoek te maken.
  
  De source code van de app is hier te vinden: [GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/cofano)
  
 <details>
  <summary><h3>Screenshot applicatie</h3></summary>
   
![Screenshot app](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/app.png)
   
  </details>
  
  <details>
    <summary><h3>Applicatie features</h3></summary>
    <h4>Scenario’s inladen en opslaan.</h4>
    De applicatie kan een scenario inladen en opslaan via json
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/json.png)
    
<h4>Containers handmatig verplaatsen</h4>
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v1.png)
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v2.png)
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/v3.png)
    
<h4>visualisatie grid</h4>
Toont de bounds van plekken waar containers op de “juiste” plek staan, in dit geval dus een 3x3x3 grid
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/grid.png)
    
<h4>Grid x-y-z coordinaten</h4>
Toont de coordinaten van lege plekken in x,y,z formaat, hiermee kun je makkelijker een beeld krijgen van het huidige veld, bijvoorbeeld in plaats van “we willen de container van schip 2 die op rij 0 kolom 1 van de 3e array zetten op rij 2 kolom 1 in de 1e array”, kun je nu zeggen we willen de blauwe container naar plek 2,1,0 krijgen.
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/grid2.png)
    

<h4>Informatie inzien</h4>
Door oven een container te hover met je muis en dan op de ‘i’ toets te drukken krijg je een label overzicht met informatie van die container:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info1.png)
    
Hier krijg je te zien wat het id van de container is, van welk schip het is, de positie, de score, of deze container op een valide plek staat (in dit geval binnen het grid en of deze niet in de lucht zweeft), en of deze container kan worden verplaatst. In dit voorbeeld kan de geselecteerde container niet worden verplaatst, en de zwarte containers zijn de containers waardoor de container niet kan worden verplaatst, in dit geval dus de containers 1 laag naar beneden aan de lange zijde, en de container die boven op de geselecteerde container staat.
In dit voorbeeld kun je zien dat een zwevende container niet op een valide place staat:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info2.png)
    
Met de force validate knop kun je snel alle fout geplaatste containers tonen:
    
![Screenshot json](https://github.com/mbroer/ads_portfolio/blob/main/output/cofano/info3.png)
    
  Andere features waar de applicatie over beschikt zijn:
-	Het onzichtbaar maken van stapels containers om makkelijker inzicht te krijgen op de lager eronder.
-	Alle container labels aan en uit zetten
-	Container selecteren via dropdown (zodat je een container in het midden van een volle grid ook nog kan manipuleren)
-	Realtime scenario saving en loading zodat je niet elke keer de applicatie opnieuw hoeft op te starten, je hoeft alleen op reload scenario te drukken en alles wordt gerefreshed.
-	Force validation dropdown zodat je ook verstopte containers die op een foute plek staan kunt vinden.
-	Low detail mode voor als je honderden containers wilt inladen, wordt er alleen een basic box met een kleur ingeladen in plaats van 6 wall objects met texture en normal maps.
-	Keyboard controls voor viewpoint

    
  </details>
  
  
</details>

<details>
  <summary><h3>Communicatie<h3></summary>
    
    presentaties....
    paper....
    
</details>

