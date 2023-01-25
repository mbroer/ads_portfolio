<h1 align="center">Portfolio</h1>
<p align="center">Applied Data Science<br>Michael Broer, 20105533</p>
<br>

<p align="center">Dit portfolio volgt de structuur van het Scoring rubrics document.</p>


<details>
    <summary><h2><b>Knock-out criteria</b></h2></summary>
	
|Num.|Criteria|Voldaan|
|---|---|---|
|1.|The contents of your personal portfolio reflect your contribution to the project, your abilities and what you have learned.|:heavy_check_mark:|
|2.|Your portfolio consists of materials that you either realized individually, or in case of a group effort, a clear statement of what your contribution is in this group effort.|:heavy_check_mark:|
|3.|The (digital) portfolio is written in a very easily accessible way.|:heavy_check_mark:|
|4.|The main document is a reader's guide (index) that shortly introduces your contributions and links to pages where the contributions are described in detail |:heavy_check_mark:|
|5.|Every contribution should be accessible from the reader's guide in a single click.|:heavy_check_mark:|
|6.|The portfolio consists of links to the Python Notebooks or other evidence material about your contribution on the project that you have finished yourself. |:heavy_check_mark:|
<br>
	
</details>

<details>
    <summary><h2><b>Obligatory criteria</b></h2></summary>
    
<details>
    <summary><h3>DataCamp Course completion</h3></summary>
    
Hieronder heb ik een screenshot toegevoegt van alle datacamp courses die ik tijdens de minor heb gemaakt, de course van 2 Oct was later ingeleverd vanwege persoonlijke omstandigheden, voor de rest is alles op tijd gemaakt.
  
![Portfolio](https://github.com/mbroer/ads_portfolio/blob/main/datacamp.png)
    
</details>

<details><summary><h3><del>Reflection on own contribution to the project.</del></h3></summary>komen te vervallen</details>
<details><summary><h3><del>Reflection on own learning objectives.</del></h3></summary>komen te vervallen</details>
<details><summary><h3><del>Evaluation on the group project as a whole.</del></h3></summary>komen te vervallen</details>

</details>

<details>
    <summary><h2><b>Subjects</b></h2></summary>
Student has been working on at least three of the following subjects:
	
|Select 3 subjects|Included|
|---|---|
|Research project|:white_check_mark:|
|Predictive analysis|:white_check_mark:|
|Domain knowledge|:white_check_mark:|
|Data preprocessing|:white_check_mark:|
|Communication|:heavy_check_mark:|
	
	
</details>

___
    
<h2><b>1. Research project</b></h2>

<details>
    <summary><h3>1.1 Task definition</h3></summary>
    
<h4>1.1.1 Foodboost</h4>
Tijdens het Foodboost project heeft onze projectgroep zich bezig gehouden met het voorspellen of een eindgebruiker een gerecht wel of niet lekker zou vinden, met als einddoel om een applicatie te maken die een gebruiker kon helpen een weekmenu samen te stellen voor zijn noddigheden, bijvoorbeeld een dieetdoel. Het is namelijk zeer lastig voor iemand om zelf een gevarieerd weekmenu samen te stellen, dit komt omdat de meeste mensen maar 6/7 favoriete gerechten hebben die ze willen eten. Dit wilde onze groep oplossen met een applicatie. 
<br>
In deze applicatie zouden restricties zitten zoals allergiën, of het een hoofdgerecht/ dessert is (thema zoals sinterklaas/ halloween), of voorkeuren zoals geen zout. De hoofdvraag gedurende het project was: <b>Hoe kunnen we een app maken waarmee gebruikers een persoonlijk advies krijgen wat ze deze week gaan eten, zodat ze makkelijker tot een betere keuze kunnen komen.</b><br>
    
Mijn persoonlijke einddoel was om uiteindelijk de applicatie te bouwen, met het model draaiend op de achtergrond.
Deze applicatie is gerealiseerd, zonder communicatie met het uiteindelijke model, omdat hier geen tijd meer voor was.

De sourcecode van de applicatie is hier terug te vinden:
[GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/foodboost/quiz)
            
<h4>1.1.2 Containers</h4>
Tijdens het Container project heeft onze projectgroep zich bezig gehouden met onderzoeken en ontwikkelen van een schaalbare methode om een optimale indeling van containers op een grid te genereren. Het schaalbare gedeelte is nodig omdat het model ook moet werken bij grotere kades of in een situatie wanneer er met meer container wordt gewerkt dan verwacht. De hoofdvraag gedurende dit project was: <b>Hoe kunnen we met een lijst van containers, een model trainen om die in de beste opstelling neer te zetten op de kade, zodat de stackers, met zo min mogelijk verplaatsingen, de containers naar de schepen kunnen verplaatsen.</b>
    
Mijn persoonlijke eindproduct was het realiseren van een applicatie die visueel het resultaat van het model kon laten zien.
    
De sourcecode van de applicatie is hier terug te vinden:
[GitHub](https://github.com/mbroer/ads_portfolio/tree/main/apps/cofano)
        
</details>

<details>
    <summary><h3>1.2 Evaluation</h3></summary>
    
<h4>1.2.1 Foodboost app</h4>
Mijn eindproduct voor dit product, namelijk de quiz applicatie, kan verbeterd worden in de toekomst door het uiteindelijke model te implementeren in de applicatie. Op dit moment geeft de applicatie een pseudo-random lijst terug, gebaseerd op het thema van de gerechten die je hebt geselecteerd. De reden hiervoor is dat het model niet optijd af was om dit te implementeren in de applcatie voor de externe presentatie. Om dit te realiseren zou het model aangepast moeten worden zodat het een x aantal recepten kan accepteren en op basis daarvan de index terugstuurd naar de applicatie, zodat deze die kan tonen.
    
<h4>1.2.2 Containers app</h4>
De visuele container applicatie kan op meerdere manieren worden verbeterd.
1) Automatisch inladen van output van het model.
Als we nu output van het model visueel willen zien, moeten we de output van het model, bijvoorbeeld:<br>

		array([[[3,3,3],
			[3,3,0],
			[3,0,0]],

			[[1,1,1],
			[1,0,0],
			[1,1,0]],

			[[2,2,2],
			[2,2,2],
			[0,0,0]]]
		)

kopieëren en plakken in een inputbox van de applicatie.
    Als het model en de applicatie gekoppeld zouden worden zou dit automatisch ingeladen kunnen worden zodat dat tijd zou besparen.
2) Tijdlijn voor elke stap die het model zet.
De applicatie zou een stuk geadvanceerder zijn als je bij elke stap van het model de output zou kunnen zien om te evalueren of het model goed werkt. Hiervoor zou je nu voor elke stap een nieuwe scenario moeten maken.
Ik zou dit zelf doen door containers te verplaatsen, hiervoor is al een moves field aangemaakt in de scenario json's

</details>

<details>
    <summary><h3>1.3 Conclusions</h3></summary>
    
</details>

<details>
    <summary><h3>1.4 Planning</h3></summary>
Ik heb gedurende de projecten gebruik gemaatk van de scrumtool Trello, Ik heb geprobeerd iedereen in de projectgroep aan te moedigen om ook van deze tool gebruik te maken, maar dit is alleen gedurende het eerste project gedaan. Ik ben wel gebruik blijven maken van het scrumboard gedurende het tweede project.<br>

Hieronder staan alle scrum tickets op mijn naam die ik heb afgerond. Bij de meeste tickets heb ik een beschrijving van een paar zinnen zodat andere projectleden een beter inzicht kregen van waar ik mee bezig was.</br></br>

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
    
</details>

<h2><b>2. Predictive Analytics</b></h2>
<details>
    <summary><h3>2.1 Selecting a Model</h3></summary>
In dit hoofdstuk beschrijf ik een aantal modellen die ik gedurende de minor heb gebruikt.
	
	
    
</details>
<details>
    <summary><h3>2.2 Configuring a Model</h3></summary>
    
</details>

<details>
    <summary><h3>2.3 Training a Model</h3></summary>
    
</details>

<details>
    <summary><h3>2.4 Evaluating a Model</h3></summary>
	%%%cofano, hoe ik met mijn visualisatie app het model evalueer.
	
    
</details>

<details>
    <summary><h3>2.5 Visualizing the outcome of a model (explanatory)</h3></summary>
	
	  
<details>
  <summary><h4>Foodboost app</h4></summary>
	%%%
  Onze groep wilde voor het foodboost project iets visueels maken voor
</details>
  
<details>
  <summary><h4>Containers app</h4></summary>
  
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

    
</details>


<h2><b>3. Domain knowledge</b></h2> <!-- skippen? -->
<details>
    <summary><h3>3.1 Introduction of the subject field</h3></summary>
    
</details>
<details>
    <summary><h3>3.2 Literature research</h3></summary>
    
</details>

<details>
    <summary><h3>3.3 Explanation of Terminology, jargon and definitions</h3></summary>
    
</details>



<h2><b>4. Data preprocessing</b></h2>
<details>
    <summary><h3>4.1 Data exploration</h3></summary>
    
</details>

<details>
    <summary><h3>4.2 Data cleansing</h3></summary>
    
</details>

<details>
    <summary><h3>4.3 Data preparation</h3></summary>
    
<h3>4.3.1 FoodBoost csv merge</h3>

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


<h3>4.3.2 FoodBoost simulated users</h3>

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
    
    
[Code voor een andere user-generation notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/Simulated_Users.ipynb)
    
    
    
  </details>

<h3>4.3.3 FoodBoost CSV naar Json</h3>
  <h4>Beschrijving</h4>
  Voor het FoodBoost project moest ik voor mijn applicatie een csv bestand omzetten naar json, dit was gelukkig vrij simpel en kon met een file reader simpel mijn csv omzetten zodat ik een json bestand in kon laden en dan via het ID van het recept, de beschrijving van dat recept kon ophalen.
  
  <details>
    <summary><i>Code, bestanden, resultaten</i></summary>
    
    %%%link naar notebook
    %%%img resultaat
    
  </details>
  
  <h3>4.3.4 FoodBoost Ingredient Groeperen</h3>
  <h4>Beschrijving</h4>
  Tijdens het foodboost project kwamen we erachter dat het model veel moeite had om voorspellingen te maken, een gebruiker die veel recepten met tomaat lekker vond, zou een lage score geven aan een recept waar ook tomaat in zit, maar dan met een andere naam. Een voorbeeld hiervan is een user met favoriete recepten zoals: tomatensalade, tomatensoep, plakken tomaat en komkommer, en dan een voorspelling op bijvoorbeeld het gerecht gesneden tomaat. Hier gaf het model aan dat de gebruiker gesneden tomaat niet lekker zou vinden. Na discussie gingen wij ervan uit als projectgroep dat het model de correlatie tussen tomaten en tomaat niet kon vinden.

Een oplossing die we hadden verzonnen is om te proberen zoveel mogelijk ingredienten te groeperen in categorieën, dus tomaat, tomaten, tomaatje, tomatenstukes = categorië tomaat.

Ik heb hier geprobeerd een groepeer script voor te maken die automatisch ingredieënten groepeerd in categorieën.
  
 De Eerste poging was om simularity score te geven aan hoe erg een string op een andere lijkt. Hiervoor gebruiktte ik de package FuzzyWuzzy. Deze package kan kijken hoeveel een string op een andere string lijkt op basis van stopwords verkleinwoorden etc.
 <br>
 Mijn aanpak was om de lijst van ingredienten te sorteren van klein naar groot (aantal letters). Dat deed ik zodat ik maar 1x door de lijst moest loopen. De eerste groeping method was om te kijken of een woord in een ander wordt zit, dus in dit geval zou 'tomaat' de eerste key zijn, en de checkworden de andere 7000 ingredienten.
 zodra er een match plaats vindt wordt de andere key bijvoorbeeld 'tomaatstukjes' worden weggehaald. Ook haalde ik bij alle ingredienten de verkleinwoorden eruit zoals 'tje', 'en' etc. Hiermee kon ik over 7000 ingredienten loopen in een paar seconde, en halveerde ik de lijst van ingredienten in groepen. 
  
[Notebook](https://github.com/mbroer/ads_portfolio/blob/main/notebooks/foodboost/groups.ipynb)
  
Ik vond halvering wel oké, maar vond dat het nog beter kon.
Omdat de meeste systemen voor string manipulation alleen werken voor de engelse taal, was de eerste stap om de strings te vertalen naar het engels,
hiervoor heb ik een script gemaakt die via de google translate api de ingredieënten vertaald van het Nederlands naar het Engels:

<details>
<summary><i>Code, bestanden, resultaten</i></summary>
    
<h5>resultaat</h5>
    
De code voor dit script ben ik helaas verloren.
Het was niet al te veel code, ik laadde alle ingredienten van het CSV in, en stuurde deze naar de google translate api.
    
[Translated ingredients CSV](https://github.com/mbroer/ads_portfolio/blob/main/output/foodboost/translated_ingredients.csv)
    
</details>
  
Met deze strings heb ik onderzoek gedaan naar hoe deze het beste zouden kunnen worden gecombineerd in groups. Hier heb ik gebruik gemaakt van kmeanas clusters. Met behuld van TfidfVectorizer kon ik de ingredienten omzetten naar tf-idf feature vectors, deze heb ik gefit, en getrained. met de predict kon ik voor elk ingredienten een label maken voor de behorende cluster. Met een object map heb ik daarna de ingredienten terug gezet naar de originele ingredienten.
Hier moest ik nog meer onderzoek naar doen om dit goed werkend te krijgen maar we gingen over naar een ander systeem. Dit is dus niet gebruikt voor ons project, maar hiermee heb ik wel meer kennis opgedaan van kmeans.
  
</details>
    
    
</details>

<details>
    <summary><h3>4.4 Data explanation</h3></summary>
    
</details>

<details>
    <summary><h3>4.5 Data visualization (exploratory)</h3></summary>
    
</details>



<h2><b>5. Communication</b></h2> <!-- skippen? -->
<details>
    <summary><h3>5.1 Presentations</h3></summary>

Qua presentaties heb ik niet kunnen bijdragen wat ik had willen doen. Ik heb in totaal maar 2 interne presentaties gepresenteerd, en had een derde voorbereid die niet door is gegaan. Dit komt vooral omdat ik elke maandag ochtend een afspraak heb met mijn fysiotherapeut. Wel heb ik gelukkig kunnen helpen met het maken van slides voor presentaties voor andere. Dit kwam vaak neer op screenshots van de applicaties die ik had gebouwd voor de visualisatie van onderandere het container project.

Hieronder zijn een paar powerpoints die ik heb gepresenteerd of waar ik bij geholpen heb:<br>
[Foodboost usergen](https://github.com/mbroer/ads_portfolio/blob/main/powerpoints/FOODBOOST%2019-09-2022%20intern%20pres.pptx)<br>
[Cofano](https://github.com/mbroer/ads_portfolio/blob/main/powerpoints/cofano.pdf)<br>
[Cofano](https://github.com/mbroer/ads_portfolio/blob/main/powerpoints/cofano4.pptx)<br>
[Cofano app demo](https://github.com/mbroer/ads_portfolio/blob/main/powerpoints/cofano8.pptx)<br>
    
</details>

<details>
    <summary><h3>5.2 Writing paper</h3></summary>
    
Omdat ik tijdens het container project vooral bezig ben geweest met het maken van een visualisatie app heb ik niet veel nieuwe dingen kunnen toevoegen aan het paper, om mezelf wel nuttig te maken voor de groep was mijn taak vooral om andere te helpen met hun onderdelen. Ik heb gezorgd voor ondersteuning door mate van screenshots van de visuele applicatie om onderdelen zoals "onze regels voor het inboxen van containers" te kunnen laten zien in afbeeldingen.<br> Ik heb ongeveer 1 derde / de helft van de paper opnieuw geschreven met ander taalgebruik zodat dat door het hele document consistent was. Dingen die niet helder waren of waar ik het niet zeker over was, plaatste ik comments bij voor andere om mee in discussie te gaan.
Mijn bijdrage aan het paper samengevat:
    
- Alle onderdelen die over visualisatie gingen
- 3 alineas van de discussie geschreven.
- De hoofdstukken Onderzoeksopzet, Dataverzameling, Verzamelde data, Visualisatie resultaten, Analyse compleet herschreven om het consistent te maken.- 
- Verwoorden van alinea's van andere, weghalen van persoonlijke voornaamwoorden (ik, we) etc.
- Mo's complete conclusie en discussie van zijn deel van het paper herschreven
- Spelling, grammatica en opmerkingen verbeteren.
- Opmerkingen met pointers hoe iemand zijn stuk zou kunnen verbeteren.
- Aanbevelen van cruciale toevoegingen, zoals tijd die het model nodig heeft om te voorspellen, het tonen van de cutoff van het model wanneer die het optimum heeft bereikt.
- Discussieren met de andere over onnodige alinea's, denk hierbij aan alineas die uitleggen wat RL of een reward functie is/ doet.
- Meeste opmaak

    
</details>
