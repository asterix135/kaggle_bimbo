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

I am approaching this primarily using Python statistical and machine learning
tools.

## Exploratory Data Analysis

First, let's have a look at the data we have.

[basic_info2.py](exploratory/basic_info2.py) provides a few summary statistics on the 
training data set shown in [train_describe.txt](exploratory/train_describe.txt):

## Reshape Data

One of the challenges I'm facing is manipulating this data in memory on a 8MB
MacBook.  I managed to blow up the memory a few times.  In order to avoid this,
I've moved much of the data to a MySQL database, which allows for much more 
memory-efficient storage and manipulation.

This means however, that there's a lot of boring data pre-processing that has
to be run to enable me to get complete solutions.

Essentially, I created a MySQL file I called uniques that contains a row for
each unique customer/product combination.  As well, it contains a field 
indicating the id value from the test file if that record exists in the test
file.

## Simple solution 1

The simplest solution that presents itself here is a multiple linear regression
model, using preceding weeks' adjusted demand figure to predict future demand.

Since the test data contains 2 weeks, we need to build 2 different models:

1) We have the previous 6 weeks' data (this will apply to week 10 in the test 
set)
2) We are missing the week immediately prior to the test week, but have the
previous five weeks' data (this will apply to week 11 in the test set)

[Applying this methodology selectively to Week 9 data]
(solutions/time_regression.py) provides results that are noticeably better than
using either the modal or mean value for adjusted demand:

| Approach | RSS |
| --- | --- |
| Mock Week 10 | 59.73 |
| Mock Week 11 | 70.58 |
| Mode | 95.32 |
| Mean | 117.53 |

So, as a first crack at the problem, I ran these two models against any 
client/product combinations in the test file that were also in the training
file.  For any new combinations (new product or new customer), I imputed the 
modal adjusted demand figure.
