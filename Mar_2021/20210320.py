# Importing libraries

import pystan
import scipy as sp
import scipy.stats as sts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the dataframe
data = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vREjEVcBtcjU4G8KV5T4IsSa6OSEyDewcxJ4OPtPVIpewjdWBg--HIctvMMcbOrmBw6swEl0TH80e4B/pub?gid=1459555462&single=true&output=csv')

# drop unecessary columns
data = data.drop(['Timestamp', 'Email Address', 'Your name'], axis=1)

# renaming columns so it is easier to access them
data.rename({'Country where you (and the grocery store) are': 'country', 'Currency (e.g. EUR, GBP, USD)': 'currency',
             'Grocery store name and street address (or URL if shopping online)': 'store',
             'Price perception of the store brand': 'perception',
             'Average rental price near the grocery store': 'rental',
             'Product 1 quantity (kg)': 'apples1_kg', 'Product 1 price': 'apples1_price',
             'Product 2 quantity (kg)': 'apples2_kg', 'Product 2 price': 'apples2_price',
             'Product 3 quantity (kg)': 'apples3_kg', 'Product 3 price': 'apples3_price',
             'Product 1 quantity (kg).1': 'bananas1_kg', 'Product 1 price.1': 'bananas1_price',
             'Product 2 quantity (kg).1': 'bananas2_kg', 'Product 2 price.1': 'bananas2_price',
             'Product 3 quantity (kg).1': 'bananas3_kg', 'Product 3 price.1': 'bananas3_price',
             'Product 1 quantity (kg).2': 'tomatoes1_kg', 'Product 1 price.2': 'tomatoes1_price',
             'Product 2 quantity (kg).2': 'tomatoes2_kg', 'Product 2 price.2': 'tomatoes2_price',
             'Product 3 quantity (kg).2': 'tomatoes3_kg', 'Product 3 price.2': 'tomatoes3_price',
             'Product 1 quantity (kg).3': 'potatoes1_kg', 'Product 1 price.3': 'potatoes1_price',
             'Product 2 quantity (kg).3': 'potatoes2_kg', 'Product 2 price.3': 'potatoes2_price',
             'Product 3 quantity (kg).3': 'potatoes3_kg', 'Product 3 price.3': 'potatoes3_price',
             'Product 1 quantity (kg).4': 'flour1_kg', 'Product 1 price.4': 'flour1_price',
             'Product 2 quantity (kg).4': 'flour2_kg', 'Product 2 price.4': 'flour2_price',
             'Product 3 quantity (kg).4': 'flour3_kg', 'Product 3 price.4': 'flour3_price',
             'Product 1 quantity (kg).5': 'rice1_kg', 'Product 1 price.5': 'rice1_price',
             'Product 2 quantity (kg).5': 'rice2_kg', 'Product 2 price.5': 'rice2_price',
             'Product 3 quantity (kg).5': 'rice3_kg', 'Product 3 price.5': 'rice3_price',
             'Product 1 quantity (liters)': 'milk1', 'Product 1 price.6': 'milk1_price',
             'Product 2 quantity (liters)': 'milk2', 'Product 2 price.6': 'milk2_price',
             'Product 3 quantity (liters)': 'milk3', 'Product 3 price.6': 'milk3_price',
             'Product 1 quantity (kg).6': 'butter1_kg', 'Product 1 price.7': 'butter1_price',
             'Product 2 quantity (kg).6': 'butter2_kg', 'Product 2 price.7': 'butter2_price',
             'Product 3 quantity (kg).6': 'butter3_kg', 'Product 3 price.7': 'butter3_price',
             'Product 1 quantity (count)': 'eggs1', 'Product 1 price.8': 'eggs1_price',
             'Product 2 quantity (count)': 'eggs2', 'Product 2 price.8': 'eggs2_price',
             'Product 3 quantity (count)': 'eggs3', 'Product 3 price.8': 'eggs3_price',
             'Product 1 quantity (kg).7': 'chicken1_kg', 'Product 1 price.9': 'chicken1_price',
             'Product 2 quantity (kg).7': 'chicken2_kg', 'Product 2 price.9': 'chicken2_price',
             'Product 3 quantity (kg).7': 'chicken3_kg', 'Product 3 price.9': 'chicken3_price', },
            axis=1, inplace=True)

# standarlizing the multiple entries for USA
# also standarlizing the entry for "Other" store since in my perception
# that can be considered a luxury store
data = data.replace({'country': {'United States': 'USA', 'US': 'USA', 'USA (San Francisco)': 'USA',
                                 'United States of America': 'USA', 'Dallas, TX, USA': 'USA',
                                 'San Francisco, USA': 'USA', 'San Francisco': 'USA', 'United States ': 'USA',
                                 'San Francisco, United States': 'USA'},
                     'perception': {'Small store in expensive neighborhood (high prices)': 'Luxury (expensive)'}})

# normalizing the prices, or in other words, getting price per unit
for i in range(5, len(data.columns[5:65]) + 5, 2):
    data[data.columns[i + 1]] = data[data.columns[i + 1]] / data[data.columns[i]]

data = data.drop(['apples1_kg', 'apples2_kg', 'apples3_kg', 'bananas1_kg', 'bananas2_kg', 'bananas3_kg',
                  'tomatoes1_kg', 'tomatoes2_kg', 'tomatoes3_kg', 'potatoes1_kg', 'potatoes2_kg', 'potatoes3_kg',
                  'flour1_kg', 'flour2_kg', 'flour3_kg', 'rice1_kg', 'rice2_kg', 'rice3_kg', 'milk1', 'milk2', 'milk3',
                  'butter1_kg', 'butter2_kg', 'butter3_kg', 'eggs1', 'eggs2', 'eggs3', 'chicken1_kg',
                  'chicken2_kg', 'chicken3_kg'], axis=1)

# averaging the product prices
for i in range(5, len(data.columns[5:35]) + 5, 3):
    data['average' + str((i - 5) // 3)] = data.iloc[:, i:i + 3].mean(axis=1, skipna=True)

# one student did not find any chicken prices
# so I am substituting the NaN value with the average from a student who looked
# for the product prices in the same supermarket
data['average9'] = data['average9'].fillna(13.205700)

# converting everything values on the rental prices's column to float
data['rental'] = pd.to_numeric(data['rental'])

# dictionary to convert all the different currencies to USD.
# it works as, for example, 1 CAD corresponds to 0.80 USD on 03/12/2021 (according to Google)
dict_currency_converter = {
    "CAD": 0.80,
    "SEK": 0.12,
    "UAH": 0.036,
    "KES": 0.0091,
    "BRL": 0.18,
    "BDT": 0.012,
    "USD": 1
}

# converting average prices using dict_currency_converter
for i in range(35, len(data.columns[35:45]) + 35):
    data[data.columns[i]] = data[data.columns[i]] * data['currency'].map(dict_currency_converter)

# converting rental prices using dict_currency_converter
data['rental'] = data['rental'] * data['currency'].map(dict_currency_converter)

# show first 5 rows of table
data.head()

stan_code = """

// The data block contains all known quantities - typically the observed
// data and any constant hyperparameters.
data {
    int<lower=0> n_data;                 // number of data
    int<lower=0> number_of_products;     // number of products
    int<lower=1> store_category_number;  // number of store categories
    int<lower=0> countries_number;       // number of countries
    int<lower=1> country_id[n_data];     // countries ids
    int<lower=1> store_id[n_data];       // stores ids
    real<lower=0> products_average_price[n_data, number_of_products];  // average prices

}

// The parameters block contains all unknown quantities - typically the
// parameters of the model. Stan will generate samples from the posterior
// distributions over all parameters.
parameters {
    real<lower=0> base_price[number_of_products];   // base price of the product
    real<lower=0> multiplier_store[store_category_number];  // store multiplier
    real<lower=0> multiplier_country[countries_number];     // country multiplier

}

// The model block contains all probability distributions in the model.
// This of this as specifying the generative model for the scenario.
model {

    // Priors
    base_price ~ cauchy(4, 2);
    store_category_number ~ gamma(6,6);
    multiplier_country ~ gamma(6,6);

    // Model for the price
    for (i in 1:number_of_products) {

    for (j in 1:n_data) {
    products_average_price[j,i] ~ normal(base_price[i]*\
                                        multiplier_store[store_id[j]]*\
                                        multiplier_country[country_id[j]], 0.6);  // likelihood function
    }
    }
}

"""

# list of products as show in the assignment instructions
product_list = ["Apples","Bananas", "Tomatoes", "Potatoes", "Flour", "Rice", "Milk", "Butter","Eggs","Chicken breasts"]

stan_data = {
    "n_data": data.shape[0],
    "number_of_products": len(product_list),
    "store_category_number":len(data["perception"].unique()),
    "countries_number":len(data["country"].unique()),
    "country_id": pd.factorize(data["country"].values)[0]+1,  # +1 to start counting from "1"
    "store_id": pd.factorize(data["perception"].values)[0]+1,  # +1 to start counting from "1"
    "products_average_price": data.iloc[:,-10:]
}

stan_model = pystan.StanModel(model_code=stan_code)

results = stan_model.sampling(data=stan_data)
print(results)