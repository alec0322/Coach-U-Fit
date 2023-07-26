import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pyautogui

#First, we set up a web application for the user to input the required data

sideb = st.sidebar
def setup_sideb():
    sideb.markdown("*Maintenance Calories: Number of calories you need to consume a day to maintain your weight. Typically equal to your body weight times 15.")
    sideb.markdown("*Calorie goal: Number of calories needed each day to maintain, lose, or gain weight. To lose a pound a week, one would have to consume around 500 kcals below maitenance.")

    if sideb.button("Refresh page"):
        pyautogui.hotkey("ctrl", "F5")

st.title("Coach-U-Fit")
st.subheader("Follow the instructions below to track your calories")

df = pd.read_csv(".../exercise_dataset.csv") #Insert path leading to exercise_dataset.csv here

weight = st.text_input("Input your body weight in pounds (lbs) and press enter")

if(weight and not weight.isnumeric()):
    st.error("The value must be a number")

#Clean the dataframe to only display the exercises to the user
df_exercises = list(df["Activity, Exercise or Sport (1 hour)"].values)
options = st.multiselect("Please select or type any activities, exercises, or sports you have performed today", df_exercises)

cals_burned = 0
if weight and options:
    for i in options:
        cals_burned += int(weight) * df.iloc[df_exercises.index(i)]["Calories per kg"]
    st.success(f"Calories burned: **{cals_burned:.3f}** kcal")    

#For HCI purposes, the use of the regression model is optional to the user
recommend = st.checkbox("**Would you like me to help you make a dietary plan?**")
if recommend and not cals_burned:
    st.error("You need to fill out the prompts above first")

elif recommend and cals_burned:
    setup_sideb()
    st.markdown("Ok! I'll need a few more things from you...")

    maintenance_cals = int(weight) * 15
    st.markdown(f"Maintenance calories: **{maintenance_cals}** kcal*")

    cals_goal = st.text_input("Input your calorie goal*, keep in mind this value depends on what diet you want to pursue")
    cals_food = 0
    if(cals_goal and not cals_goal.isnumeric()):
        st.error("The value must be a number")
    elif cals_goal:
        cals_food = int(cals_goal) + int(cals_burned)
        st.markdown("I'll be using the following equation based on the data you provided me:")
        st.markdown(f"**Food ({cals_food} kcals) = Goal ({cals_goal} kcals) + Burned ({int(cals_burned)} kcals)**")
        st.markdown(f"In other words, today you need to consume **{cals_food}** calories to reach your goals")

        #Now that all user information is collected, we proceed to access the nutrients.csv dataset and implement the regression model

        df_cals = pd.read_csv(".../nutrients_dataset.csv") #Insert path leading to nutrients_dataset.csv here

        #Clean the dataset to only contain necessary columns
        df_cals = df_cals.drop(["Food", "Measure", "Category"], axis=1)

        #By default, the dataset contains a 't' value denoting a miniscule number of a given macronutrient
        #For training purposes, this value will be truncated to 0
        #Additionally, for uniformity all values will be casted to float and NaN values will be dropped
        df_cals = df_cals.replace('t', 0)
        df_cals = df_cals.astype(float)
        df_cals = df_cals.dropna()

        #Set up the features and target variable
        X = df_cals[["Protein", "Fat", "Sat.Fat", "Fiber", "Carbs"]]
        y = df_cals["Calories"]

        #Split the dataset (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        #Define the regression model and train it
        model = LinearRegression()
        model.fit(X_train, y_train)

        st.write('***')
        st.subheader("Almost done!")
        st.write("Please input the quantity in grams of each macronutrient you've consumed today")
        protein = st.slider("Protein (g)", max_value=300)
        fat = st.slider("Fat (g)", max_value=300)
        sat_fat = st.slider("Saturated Fat (g)", max_value=300)
        fiber = st.slider("Fiber (g)", max_value=300)
        carbs = st.slider("Carbs (g)", max_value=300)
        st.write('***')

        #Make a prediction
        prediction = 0
        if protein and fat and sat_fat and fiber and carbs:
            prediction = model.predict([[protein, fat, sat_fat, fiber, carbs]])[0]
            st.success(f"As of now, I predict you have consumed around **{int(prediction)}** calories")
            st.write("Altering the equation above...")

            cals_remaining = int(cals_goal) - int(prediction) + int(cals_burned)
            st.write(f"**Remaining ({cals_remaining} kcals) = Food ({int(prediction)} kcals) - Goal ({cals_goal} kcals) + Burned ({int(cals_burned)} kcals)**")
            st.write(f"...You have about **{round(cals_remaining/10)*10}** calories to go today, keep it up!")
            st.write("")

            if st.button("Show ML benchmarks"):
                r2 = model.score(X_test, y_test)
                st.write(f"R² score: **{r2:.3f}**")