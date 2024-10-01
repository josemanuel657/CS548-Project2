# CS548-Project2

Create a folder called data, in which you will put all the csv's from the kaggle database: https://www.kaggle.com/datasets/davidcariboo/player-scores?select=transfers.csv


ideas:

# task 1: description

# task 2: statistcal summary and eda
- prprosses handling missing values
- calculate mean, variance etc of players
- calculate mean, variance etc of teams

# task 3: explain matches idea

- classify game in win, lose, tie
- find how many minutes each player should play to win the game.
- imagine having a dream team what would happen


# task 4: data preprocessing (to analyze matches)
- create the match with all the info (aggregate player level features)
- Z normalization for all values
- creating derived features (mean cards, mean )
- one hot encoding for all features (we will try and explain why it was better or worse)
- something else
- split the data into training set, and a test set


matchID
    stadium
    country
    referee


    clubID 1
        formation
        club manager 1
        away club manager
        country
        domenstic competitoin ID
        calculate average age 
        caluclate foreging/national percentage 
        home/away boolean for countryt, and one for stadium 
        isWin
        goals scored
        mean,varicance golas, yellow cards, etc
        


        playerID 1
            goals scored
            age calculated
            foot 
            height 
            position
            subposition
            current market value
            higuest market value
            country of birth
            minutes played  
            yellow card (mean and variance per game)
            red card (mean and variance per game) 
            goals (mean and variance per game)
            assist (mean and variance per game)


            




            
        playerID 2
        .
        .
        .
    clubID 2


# task 5: traing this with the taining set and testing accuracy

## For testing
    - Accuracy
    - Precision
    - Recall
    - F1 score
 
## for models 
- Naive Bayes:

    - Simple probabilistic model that assumes independence between features.
    - This is a good baseline model, efficient even for large datasets.

- Decision Tree:
    - Variation 1: Gain Ratio: Uses the gain ratio to split nodes, favoring balanced splits.
    - Variation 2: Gini Index: Uses the Gini index to minimize misclassification.
    - Variation 3: Information Gain: Uses entropy to calculate information gain, focusing on the purity of splits.

- Random Forest:
    - Variation 1: Gain Ratio: Builds multiple trees using gain ratio as the splitting criterion.
    - Variation 2: Gini Index: Builds multiple trees with Gini index for node splitting.
    - Variation 3: XGBoost: An optimized version of boosting that builds trees sequentially, correcting errors in each iteration.

- k-Nearest Neighbors (k-NN):
    - Variation 1: Euclidean Distance: Uses Euclidean distance to measure similarity between instances.
    - Variation 2: Manhattan Distance: Uses Manhattan distance as an alternative metric for distance calculation.
    - Variation 3: Number of Neighbors: Experiment with different numbers of neighbors (e.g., k=5, k=10) to find the optimal number.

- Logistic Regression:

    - Variation 1: Default: Standard logistic regression without regularization.
    - Variation 2: L2 Regularization: Uses ridge regularization to reduce overfitting by penalizing large coefficients.
    - Variation 3: L1 Regularization: Uses lasso regularization, which can also perform feature selection by shrinking some coefficients to zero.

# conclusion