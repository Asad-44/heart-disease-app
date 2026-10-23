# Heart Disease Prediction System

A machine learning web app that estimates whether a patient is at risk of heart disease from four input attributes. Built for the Machine Learning Fundamentals course (AIC354) at COMSATS University Islamabad, Lahore Campus.

**Live demo:** [https://heart-disease-appgit-5mursn88qhgat9v3mxpyzd.streamlit.app/]

> **Disclaimer:** This project is for educational purposes only. It is not a medical tool and must not be used for diagnosis or health decisions.

## Dataset

[UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) (Cleveland subset). The original target (0 to 4) is converted to binary: 0 = no disease, 1 = disease present. Rows with missing values are removed.

## Input Features

| Feature | Description |
|---|---|
| `age` | Age in years |
| `sex` | Male / Female |
| `cp` | Chest pain type (Typical angina, Atypical angina, Non-anginal pain, Asymptomatic) |
| `thalach` | Maximum heart rate achieved |

**Output:** Low risk / High risk of heart disease

## Model

- Algorithm: Random Forest Classifier (scikit-learn)
- Categorical features (`sex`, `cp`) are label encoded
- Train/test split: 80/20
- Test accuracy: [your accuracy]%. Only four features are used, so performance is limited.

## Project Structure

```
heart-disease-app/
├── app.py              # Streamlit application
├── heart_model.pkl     # Trained model
├── encoders.pkl        # Fitted label encoders
├── heart.csv           # Dataset used for training
├── requirements.txt    # Python dependencies
└── README.md
```

## Run Locally

```bash
git clone https://github.com/Asad-44/heart-disease-app.git
cd heart-disease-app
pip install -r requirements.txt
streamlit run app.py
```

## Machine Learning Workflow

1. Data collection and understanding
2. Preprocessing and feature selection
3. Label encoding
4. Training and saving the model
5. Testing and evaluation
6. Application phase (this web app)

## Limitations

- Only four input attributes are used.
- Small dataset (about 300 patients), so results should not be generalized.

## Author

Muhammad Asad Shafiq
BS Software Engineering, COMSATS University Islamabad, Lahore Campus
GitHub: [Asad-44](https://github.com/Asad-44)
