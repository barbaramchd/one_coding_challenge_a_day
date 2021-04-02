"""
Stan model
"""
stan_code = """

// The data block contains all known quantities - typically the observed
// data and any constant hyperparameters.
data {
    int<lower=0> n_data;
    int<lower=0> number_of_products;
    int<lower=1> store_category_number;
    int<lower=0> countries_number;
    int<lower=1> country_id[n_data];
    int<lower=1> store_id[n_data];
    real<lower=0> products_average_price[n_data, number_of_products];

}

// The parameters block contains all unknown quantities - typically the
// parameters of the model. Stan will generate samples from the posterior
// distributions over all parameters.
parameters {
    real<lower=0> base_price[number_of_products];
    real<lower=0> multiplier_store[store_category_number];
    real<lower=0> multiplier_country[countries_number];

}

// The model block contains all probability distributions in the model.
// This of this as specifying the generative model for the scenario.
model {

    // Prior
    base_price ~ cauchy(0,100);
    store_category_number ~ gamma(6,6);
    multiplier_country ~ gamma(6,6);

    for (i in 1:number_of_products) {

    for (j in 1:n_data) {
    products_average_price[j,i] ~ normal(base_price[i]*\
                                        multiplier_store[store_id[j]]*\
                                        multiplier_country[country_id[j]], 1);  ##CHANGE SD
    }
    }
}

"""