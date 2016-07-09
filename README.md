# Kaggle Bimbo Bakery Competition

Process to enter the Grupo Bimbo Inventory Demand Competition on Kaggle: 
https://www.kaggle.com/c/grupo-bimbo-inventory-demand


## Objective

The contest requires us to attempt to predict weekly demand for a range of 
stores and products in Mexico based on supplied historical data.

The data supplied include:

* train.csv - 74,000,000 observations of historical demand.  Each line 
represents one store/product combination
* cliente_tabla.csv - Names of clients (stores) - linked to Cliente_ID in 
train.csv and test.csv; 935,000 records
* producto_tabla.csv - Name of products - Linked to Producto_ID in train.csv
and test.csv; 2,500 records
* town_state.csv - 800 records linking town & state to Agencia_ID in train.csv
and test.csv
* test.csv - 7,000,000 records on which predictions are to be made

## General Observations

The training data represent weeks 3-9, while the test data represent weeks 10
and 11.  This means that we need to make predictions under two conditions: 
One where we have data on the preceding seven weeks, and one where we have data
on the preceding eight weeks except for the previous one.

This means that we will probably have to build two different models; one for 
week 10 and one for week 11.

Secondly, there is some noise in the data, and there are likely products and/or
customers in the test set that do not exist in the training set.  We need to 
provide a solution to deal with these situations.

## Exploratory Data Analysis

First, let's have a look at the data we have.