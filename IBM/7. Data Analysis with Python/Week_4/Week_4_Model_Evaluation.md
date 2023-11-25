Model - This can be defined as a mathematical equation to predict our target price 

Simple Liner Regression - Depends on a single variable to predict a relationship 
x - The predictor (independent) variable - x 
y = The Target(Dependent) variable -y 

y = mx + c (x = steepness of the line )
E = 1/n (sum(o->n)(yi - yi.)^2)    - This is the mean squared error. We need to minimise this 

Model Evaluation (Finding out the relation between the two values )
Horizontal axis - Independent Variable 
Vertical axis - dependent Variable (price)
Fitted line - Representation of the scattered points predicting the value 

Pipelines
They make the code flow better 
Normalisation -> Transformation -> Linear regression 

Two methods to evaluate a fit of a model 
1. Mean squared error (Best method to predict of tyhe model is valid or not )
   - sum(Actual-predicted)^2/n (Over here only the vertical axis values are calculated (Predictions))

2. R^2 = (1- MSE(Actual,predicted)/MSE(Actual, Average))
This value lies between 0-1

If the R^2 value tends towards 0 then it is a poor fit for the data


Decision making 
x = newdf[['highway-mpg']]
y = ['price']
lm.score(x,y)
1. First we train the model 
   - lm.fit(x,y)
2. We predict the model
   - lm.prdeict(x,y)
3. Calculate result 
   - lm.coef