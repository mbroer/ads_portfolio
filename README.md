<h1 align="center">Portfolio</h1>
<p align="center">Applied Data Science<br>Michael Broer, 20105533</p>
<br>
<p align="center">Om het nakijken zo makkelijk mogelijk te maken, heb ik het portfolio in de structuur van het Scoring rubrics document geschreven, echter is dit document niet chronologisch consistent, dus in sommige onderdelen waar ik over vertel, komt de context pas in een later onderdeel tevoorschijn.
</p>

<br>

<details>
    <summary><h4><b>Knock-out criteria</b></h2></summary>
	
|Num.|Criteria|Voldaan|
|---|---|---|
|1.|The contents of your personal portfolio reflect your contribution to the project, your abilities and what you have learned.|:heavy_check_mark:|
|2.|Your portfolio consists of materials that you either realized individually, or in case of a group effort, a clear statement of what your contribution is in this group effort.|:heavy_check_mark:|
|3.|The (digital) portfolio is written in a very easily accessible way.|:heavy_check_mark:|
|4.|The main document is a reader's guide (index) that shortly introduces your contributions and links to pages where the contributions are described in detail |:heavy_check_mark:|
|5.|Every contribution should be accessible from the reader's guide in a single click.|:heavy_check_mark:|
|6.|The portfolio consists of links to the Python Notebooks or other evidence material about your contribution on the project that you have finished yourself. |:heavy_check_mark:|
<br>
	
___
	
</details><!--end ko-->

<details>
    <summary><h4><b>Obligatory criteria</b></h4></summary>
    
<details>
    <summary><h5>DataCamp Course completion</h5></summary>
    
Hieronder heb ik een screenshot toegevoegt van alle datacamp courses die ik tijdens de minor heb gemaakt, de course van 2 Oct was later ingeleverd vanwege persoonlijke omstandigheden, voor de rest is alles op tijd gemaakt.
  
![Portfolio](https://github.com/mbroer/ads_portfolio/blob/main/datacamp.png)
    
</details>

<details><summary><h6><del>Reflection on own contribution to the project.</del></h6></summary>komen te vervallen</details>
<details><summary><h6><del>Reflection on own learning objectives.</del></h6></summary>komen te vervallen</details>
<details><summary><h6><del>Evaluation on the group project as a whole.</del></h6></summary>komen te vervallen</details>

___
	
</details><!--end obligatory-->

<details>
    <summary><h4><b>Subjects</b></h4></summary>
Student has been working on at least three of the following subjects:
	
|Onderwerpen|In portfolio|
|---|---|
|Research project|:heavy_multiplication_x:|
|Predictive analysis|:heavy_multiplication_x:|
|Domain knowledge|:heavy_multiplication_x:|
|Data preprocessing|:heavy_multiplication_x:|
|Communication|:heavy_check_mark:|
	
	
</details>

## [1. Research Project](https://github.com/mbroer/ads_portfolio/blob/main/Research%20Project.md)
## [2. Predictive Analytics](https://github.com/mbroer/ads_portfolio/blob/main/Predictive%20Analytics.md)

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
- Bijlage

    
</details>
