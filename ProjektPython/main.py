import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import tkinter as tk
import tkinter.messagebox as messagebox
from pandastable import Table
import seaborn as sns

# trenowanie modelu
def trenowanie_modelu():
    global model, treningowaX, treningowaY
    model = DecisionTreeClassifier()
    model.fit(treningowaX, treningowaY)
    messagebox.showinfo("Trenowanie modelu", "Wytrenowano model")

# testowanie modelu
def testowanie_modelu():
    global model, testowaX, testowaY
    predTestY = model.predict(testowaX)
    accuracy = accuracy_score(testowaY, predTestY)
    messagebox.showinfo("Dokładność zbioru testowego", f"Dokładność zbioru testowego wynosi: {accuracy:.4f}")



columns = ["age", "workclass", "fnlwgt", "education", "education-num",
            "marital-status", "occupation", "relationship",
            "race", "sex", "capital-gain", "capital-loss",
            "hours-per-week", "native-country", "income"]
data = pd.read_csv('Adults_Income.csv', names = columns)

# Niepotrzebna kolumna
data = data.drop(columns = ["fnlwgt"])

# Income musi być w wartości binarnej
data["income"] = data["income"].apply(lambda x: 1 if x == " >50K" else 0)

# Split na podział treningowy oraz testowy
X = data.drop(columns = ["income"])
Y = data["income"]
treningowaX, testowaX, treningowaY, testowaY = train_test_split(X, Y, test_size = 0.2, random_state = 42)

X = pd.get_dummies(X)
data_encoded = pd.get_dummies(data)

treningowaX = treningowaX.reindex(columns = X.columns, fill_value = 0)
testowaX = testowaX.reindex(columns = X.columns, fill_value = 0)

# Interfejs użytkownika GUI
gui = tk.Tk()
gui.title("Adult income")

# Buttons
train_button = tk.Button(gui, text = "Trenowanie modelu", command = trenowanie_modelu)
train_button.pack(side="top")

test_button = tk.Button(gui, text = "Testowanie modelu", command = testowanie_modelu)
test_button.pack(side="top")

# DataFrame
frame = tk.Frame(gui)
frame.pack()
table = Table(frame, dataframe = data, showtoolbar = True, showstatusbar = True, colwidth = 100)
table.show()

gui.mainloop()