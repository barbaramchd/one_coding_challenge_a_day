# Extracting samples
samples = results.extract()

# Plotting posterior base prices
plt.figure(figsize=(18, 6))

# corr_x and corr_y is used to centralize the annoted mean in the plot
corr_x = 0.43
corr_y = -0.2

for i in range(len(product_list)):
    plt.plot(sts.uniform.rvs(loc=i + 1 - 0.2, scale=0.4, size=4000), samples['base_price'][:, i], ',', alpha=0.5)
    plt.annotate(str(round(samples['base_price'].mean(axis=0)[i], 2)),
                 xy=(i + 1 - 0.2 + corr_x, samples['base_price'].mean(axis=0)[i] + corr_y))

# marking the mean with a black circle
plt.plot(range(1, 1 + len(product_list)), samples['base_price'].mean(axis=0),
         marker='.', linewidth=0, color="black", alpha=0.8, markersize=10)

plt.title('Posterior samples of base prices')
plt.xticks(range(1, len(product_list) + 1), product_list)
plt.ylim(0, 30)
plt.show()

# calculating confidence interval
print("95% Confidence Interval")
print("Lower Bound: ", np.percentile(samples['base_price'], [2.5, 97.5], axis=0)[0])
print("Upper Bound: ", np.percentile(samples['base_price'], [2.5, 97.5], axis=0)[1])