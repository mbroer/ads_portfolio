<h1>Portfolio</h1>
Applied Data Science Portfolio<br>
Michael Broer, 20105533

<h2>0. Obligatory criteria</h2>
    
<details>
    <summary><h3>0.1 DataCamp Course completion.</h3></summary>
    
Hieronder heb ik een screenshot toegevoegt van alle datacamp courses die ik tijdens de minor heb gemaakt, de course van 2 Oct was later ingeleverd vanwege persoonlijke omstandigheden, voor de rest is alles op tijd gemaakt.
  
![Portfolio](https://github.com/mbroer/ads_portfolio/blob/main/datacamp.png)
    
</details>

<details><summary><h3><del>0.2 Reflection on own contribution to the project.</del></h3></summary>komen te vervallen</details>
<details><summary><h3><del>0.3 Reflection on own learning objectives.</del></h3></summary>komen te vervallen</details>
<details><summary><h3><del>0.4 Evaluation on the group project as a whole.</del></h3></summary>komen te vervallen</details>

    
<h2>1. Research project</h2>

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

kopieëren en plakken in een inputbox van de visuele applicatie.
    Als het model en de applicatie gekoppeld zouden worden zou dit automatisch ingeladen kunnen worden dat tijd zou besparen.
2) Tijdlijn voor elke stap die het model zet.
De applicatie zou een stuk geadvanceerder zijn als je bij elke stap van het model de output zou kunnen zien om te evalueren of het model goed werkt. Hiervoor zou je nu voor elke stap een nieuwe scenario moeten maken.
Ik zou dit zelf doen door containers te verplaatsen, hiervoor is al een moves field aangemaakt in de scenario json's
    
    
    
</details>

<details>
    <summary><h3>1.3 Conclusions</h3></summary>
    
</details>

<details>
    <summary><h3>1.4 Planning</h3></summary>
    
</details>


<h2>2. Predictive Analytics</h2>
<details>
    <summary><h3>2.1 Selecting a Model</h3></summary>
    
</details>
<details>
    <summary><h3>2.2 Configuring a Model</h3></summary>
    
</details>

<details>
    <summary><h3>2.3 Training a Model</h3></summary>
    
</details>

<details>
    <summary><h3>2.4 Evaluating a Model</h3></summary>
    
</details>

<details>
    <summary><h3>2.5 Visualizing the outcome of a model (explanatory)</h3></summary>
    
</details>


<h2>3. Domain knowledge</h2>
<details>
    <summary><h3>3.1 Introduction of the subject field</h3></summary>
    
</details>
<details>
    <summary><h3>3.2 Literature research</h3></summary>
    
</details>

<details>
    <summary><h3>3.3 Explanation of Terminology, jargon and definitions</h3></summary>
    
</details>



<h2>4. Data preprocessing</h2>
<details>
    <summary><h3>4.1 Data exploration</h3></summary>
    
</details>

<details>
    <summary><h3>4.2 Data cleansing</h3></summary>
    
</details>

<details>
    <summary><h3>4.3 Data preparation</h3></summary>
    
</details>

<details>
    <summary><h3>4.4 Data explanation</h3></summary>
    
</details>

<details>
    <summary><h3>4.5 Data visualization (exploratory)</h3></summary>
    
</details>



<h2>5. Communication</h2>
<details>
    <summary><h3>5.1 Presentations</h3></summary>
    
</details>

<details>
    <summary><h3>5.2 Writing paper</h3></summary>
    
</details>
