# Car Price Predictions


## Overview
Our capstone project is focused on predicting vehicle prices using machine learning.  Our goal is to build a web application that accurately predicts vehicle prices based on inputs using our machine learning model.  To develop our model we used correlation to see how each variable impacted the vehicle selling price.  Once we explored the data and selected variables we ran a Linear Regression, Lasso Regression, and Principal Componenet Analysis to see which provided the most accurate results for use in our application.  


## Instructions
   1.  Clean the data, removing irrelevant/null information
   2.  Explore the data checking values/types
   3.  Look for correlation between our target and feature variables
   4.  Seperate and scale our target and feature variables
   4.  Fit and predict using our variables and the Lasso/Linear Models
   5.  Analyze prediction metrics and decide which model will provide the best results
   6.  After model selection we need to encode the scaled variables for our web application
   7.  We then need to define the features and create inputs in our web app
   8.  Using the encoded variables and feature inputs our imported model will predict the price of the vehicle.
   
## Conclusion
   Both the Linear and Lasso Regression models did a good job at predicting vehicle prices.  The r2 score for both models was just shy of 1.0.  It was difficult to eliminate some of the underperforming features from the model because they were necessary for inputs in our web application.  Overall the model accurately predicts vehicle prices granted the inputs make sense.
   
   
