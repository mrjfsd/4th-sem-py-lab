import matplotlib.pyplot as plt
x=["guru","shilpa","shankar","shashikar"]
y=[30,40,50,60]
plt.title("student marks pie chart")
plt.pie(y,labels=x,autopct="%"'d')
plt.show()