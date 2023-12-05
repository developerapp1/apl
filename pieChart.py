import matplotlib.pyplot as plt

programming_languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.pie(popularity, labels=programming_languages, autopct="%1.1f%%")
plt.title('Popularity of Programming Languages')
plt.show()
