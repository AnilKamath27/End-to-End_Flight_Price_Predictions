# Flight Booking Price Prediction

## Software and Tools Requirements

1. [GitHub](https://github.com/)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitHubDesktop](https://desktop.github.com/)

Create new enviroment

```
conda create -p venv python==3.11.4 -y
```
---
Scope: The objective of the study is to analyse the flight booking dataset obtained from “Ease My Trip” website. The 'Random Forest Regression' statistical algorithm would be used to train the dataset and predict a continuous target variable. 'Easemytrip' is an internet platform for booking flight tickets, and hence a platform that potential passengers use to buy tickets. A thorough study of the data will aid in the discovery of valuable insights that will be of enormous value to passengers.

**Attributes**
- Airline - Name of the airline company
- Flight - Plane's flight code
- Source City - City from which the flight takes off
- Departure Time - Time of Departure
- Stops - Number of stops between the source and destination cities
- Arrival Time - Time of Arrival
- Destination City - City where the flight will land
- Class - Contains information on seat class
- Duration - Overall amount of time taken to travel between cities in hours.
- Days left - Subtracting the trip date by the booking date.
- Price - Ticket price


**Project Overview**

**Step 1: Importing Necessary Libraries**
- In this initial step, the required Python libraries are imported to support data manipulation, visualization, and machine learning.

**Step 2: Exploratory Data Analysis (EDA)**
- The dataset ('Flight_Booking.csv') is loaded and inspected.
- Unnecessary columns ('Unnamed: 0' and 'flight') are removed.
- An examination of data information, including data types and missing values, is performed.
- Summary statistics, such as mean, median, and quartiles, are computed to understand the data's distribution and central tendencies.
- Various data visualizations are generated, including line plots, bar plots, and heatmaps, to gain insights into the relationships between variables, such as pricing variations with respect to airlines, departure times, stops, and more.

**Step 3: Data Preprocessing**
- Prior to model development, data preprocessing is essential.
- The dataset is divided into feature variables (X) and the target variable (y), with 'price' being the target variable for prediction.
- Numeric features are standardized using the StandardScaler to ensure uniform scales.
- Categorical features are one-hot encoded to convert them into a numerical format suitable for modeling.

**Step 4: Model Selection and Evaluation**
- Machine learning models suitable for regression tasks are chosen, including Linear Regression, Random Forest Regressor, Gradient Boosting Regressor, and XGBoost Regressor.
- Each model is set up as a pipeline, encompassing preprocessing and the chosen regression algorithm.
- Cross-validation techniques are employed to assess model performance, employing metrics such as R-squared (R²) scores, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
- The models' results are compared, and the best-performing model is selected.

**Step 5: Feature Importance**
- A Linear Regression model is utilized to compute feature importance, aiding in the identification of the most influential features for predicting flight prices.
- The top k features are chosen based on their importance scores.
- The dataset is transformed to include only these selected features.

**Step 6: Model Tuning (Optional)**
- Hyperparameter tuning can be conducted for the selected model (XGBoost Regressor) using GridSearchCV.
- GridSearchCV systematically explores various hyperparameters to find the optimal combination.
- However, in this case, hyperparameter tuning is not pursued due to the model's high accuracy, minimizing the risk of overfitting.

**Step 7: Final Model Training and Evaluation**
- A final pipeline is constructed, encompassing preprocessing and the chosen model (XGBoost Regressor).
- The ultimate model is trained on the training dataset.
- Model evaluation metrics, including MAE, MSE, RMSE, and R² score, are computed on the test dataset.
- Distribution plots are generated to visualize the alignment between predicted and actual flight prices.

**Conclusion:**
- This project successfully develops a flight price prediction model with an impressive accuracy rate of approximately 97%.
- Key steps, such as data preprocessing, feature selection, and model evaluation, contribute significantly to the model's accuracy.
- The XGBoost Regressor is designated as the final model due to its superior performance among the tested models.
- Distribution plots effectively demonstrate the strong alignment between predicted and actual prices, affirming the model's capability to capture underlying data patterns.

Overall, this project showcases a proficient grasp of data analysis, preprocessing, modeling, and evaluation techniques in machine learning. The attained accuracy underscores the model's effectiveness in predicting flight prices, with potential for further improvements through additional data and features.