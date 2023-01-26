<h1>Dit gedeelte heb ik deels overgeslagen, dit wil ik dus niet beoordeeld hebben</h1>

<h2><b>2. Predictive Analytics</b></h2>

<h3>2.1 Selecting a Model</h3>
In dit hoofdstuk beschrijf ik een aantal modellen die gedurende de minor zijn gebruikt.
	
<h4>2.1.1 Foodboost</h4>
Voor het Foodboost project heb ik gebruik gemaakt van de volgende modellen:<br>

* MatrixFactorization, voor het recommender systeem.<br> Hiervoor is gekozen omdat het vaak gebruikt wordt voor het maken van recommender systemen. Dit komt omdat het effectief grote en schaarse data kan verwerken. Door de users en recepten in het product te decompenseren als user-item, kan de matrix de onderliggende patronen en relaties vastleggen. Dit kan leiden tot betere generalisatie en betere voorspellingen, zelfs als deze geen interactiegeschiedenis hebben. Over het algemeen is MatrixFactorization een krachtige techniek die een recommendersysteem en aanbevelingen van hoge kwaliteit kan produceren.
	
* Logistic regression, om te proberen om ingrediënten en tags te groeperen.
Met logistic regression is het mogelijk om te voorspellen of een ingredieënt in een category zou kunnen zitten. Hiervoor heb ik de benodigde data gepivot en numeriek gemaakt.
	
* SVM, om te proberen om de ingrediënten en tags te groeperen via categorie.
Omdat met SVM de beste boundary/hyperplane gevonden zou kunnen worden voor de ingredienten, heb ik dit geprobeerd te gebruiken met de foodboost datasets, met het eerder genoemde ingredienten-groepeer programma. Ik had train en test data gemaakt voor 'tomato' en 'onion', bij tomato kreeg ik een Accuracy van ~85% en bij onion was het rond de 90%. Dit was vlak voor de switch naar het container project, dus ik heb hier verder niet meer naar gekeken

<h4>2.1.2 Cofano</h4>

Voor het container project heb ik gebruik gemaakt van de volgende modellen:

* AC2, om de iteraties van de container indeling te evalueren.
Als groep hadden we eerst gekozen om met het AC2 model te werken, dit wilde we gebruiken om te kijken of de actor dan beter getrained kon worden met het reward/ penalty systeem. Bij mijn oplossing had ik mijn states actions en reward penalty systeem opgesteld voor de agent als een 2x2 grid. Hier vertel ik later over.

* PPO, voor vergelijkingen.
Hier ben ik zelf verder niet bij betrokken geweest, wel hebben we hier samen als groep over overlegt en de andere van de groep zijn hier naartoe geswitched.
Ik ben hier zelf niet verder mee gegaan, maar heb wel onderzocht wat precies het verschil was.

Van wat ik begreep is PPO vrijwel hetzelfde als AC2, het zijn beide RL algoritmes om een agent te trainen. AC2 werk op een value-based approach en PPO met een policy-based approach. AC2 update de policy na een evaluatie van een specifieke actie, terwijl PPO dat direct doet. Ook was PPO een stuk sneller vanwege parallel threads. Ook na zelfstandig testen bleek het dat AC2 veel meer samples nodig had dan PPO om op de zelfde effecifiteit te komen.<br>
Hoe Hidde het opsomde was dat A2C "aggressiefer" is.
	
<h3>2.2 Configuring a Model</h3>

Het configureren van de modellen liet ik meestal over aan de groepsleden die daar meer verstand van hadden, uiteraard heb ik zelf ook geprobeerd om modellen te configureren bijvoorbeeld voor het ingredieënten groeperen:
    
%%% omzetten van data naar numerieke data

<h3>2.3 Training a Model</h3>

<h3>2.4 Evaluating a Model</h3>
	
<h4>2.4.1 FoodBoost</h4>
Voor het foodboost project zijn de volgende evaluatie technieken toegepast:
	
* Leave One Out
* K-Nearestneighbor clustering
	
%%%todo cofano, hoe ik met mijn visualisatie app het model evalueer.
	
<h3>2.5 Visualizing the outcome of a model (explanatory)</h3>
	
<h4>Foodboost app</h4>

<h4>Containers app</h4>
  

## [&#8592; Terug naar index](https://github.com/mbroer/ads_portfolio/blob/main/README.md)
