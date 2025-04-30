#### FYI: The project is complete due to unforseen circumstances. Look at unfixed bugs.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* Buisness Requirement 1: Data visualization and Correlation Study
    * We will inspect the house attributes data and conduct a correlation study to understand better on how the attributes are correlated to the sale price of the house.
    * We will plot the main attributes against the sale prices of the houses to visualize insights.

* Buisness Requirement 2: Predicting house sale prices
    * we want to predict the house sale prices, so we will build a regression model to do this.
    * This will allow the client to estimate the market value of her 4 inherited houses and predict the sale prices of any other houses in Iowa.

## ML Business Case

#### Regression Model

* The model objective is to predict the sale price of houses in Ames, Iowa using property features, so that the client can accurately price the four inherited houses and assess future properties without relying on local market guesswork.
* The model provides accurate and reliable sale price predictions for the client's four houses. The client can also use the model through an interactive web app to input house details and receive price estimates instantly.
* The model success metrics are an R2 score of at least 0.75 on the train and test set.
* The model will be considered a failure if the R2 score is lower than 0.75 on the train and test set.
* The model outputs a predicted sale price for a house given its features. These predictions are shown on the dashboard both for the client's four houses and for any custom house entered by the user.
* Heuristics: We assume that historical house sale data from Ames can help predict current or future house prices. This is based on the idea that features like house size, quality, and condition generally stay important over time and influence market value.
* The training data has come from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data) and has around 1400 records of real house sales in Ames, Iowa.
    * Training data target: House sale price
    * Features: All other variables

## Dashboard Design

### Page 1: Quick Project Summary

* Describe project data set
* State buisness requirements

### Page 2: Sale Price Study

* State Buisness requirement 1
* Display the most correlated house features to the sale price of the house.
* It helps the user make sense of what features matter most in the Ames market, which is especially important since the user is not familiar with local pricing patterns.
* Has check-box feature to hide and show individual plots showing the house sale prices for the top correlated variables.

### Page 3: House Sale Price UI

* State buisness requirement 2
* Table of the attributes in their respective predicted sale price for the four inherited houses.
* A section to input a given house data, hit the button and get a clear
message that informs the predicted sale price for that particular house.

### Page 4: ML: House Sale Price

* Displays the comparison between predicted and actual values for the training and test sets.
* Pipeline performance.

## Unfixed Bugs

* This is mainly for the assessors at code institute.
* My project is incomplete due to computer issues and frustration with my computer and loss of my project so close to the deadline led to this incomplete project.

## Deployment

### Heroku

* The App live link is: <https://suth-heritage-housing-issues-ccf1a198931e.herokuapp.com>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* numpy==1.26.1
* pandas==2.1.1
* matplotlib==3.8.0
* seaborn==0.13.2
* plotly==5.17.0
* streamlit==1.40.2
* feature-engine==1.6.1
* imbalanced-learn==0.11.0
* scikit-learn==1.3.1

## Credits

* The project was forked from Code Institute's template, which can be found [here](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)
* The dataset used for this project is from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)
* Snippets of code was taken from Code Institute's [churnometer](https://github.com/Code-Institute-Solutions/churnometer/tree/main) project, but was modified and adapted for my project.


