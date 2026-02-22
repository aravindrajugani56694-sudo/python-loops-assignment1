temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = (temps_celsius * 1.8) + 32
print("Celsius :", temps_celsius)
print("Fahrenheit :", temps_fahrenheit)

average = np.mean(temps_fahrenheit)
print("Average Fahrenheit:", round(average, 1)
