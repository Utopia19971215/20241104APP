# 导入需要的库
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.header("Predicting the probability of early loop diuretic resistance in the heart failure patients  using machinelearning")
st.sidebar.header('Variables')
st.image("1.png")
# 输入框
a = st.sidebar.number_input("DE")
b = st.sidebar.number_input("Urea nitrogen, mg/dL")
c = st.sidebar.number_input("Creatinine, mg/dL")
d = st.sidebar.number_input("Anion gap, mEq/L")
e = st.sidebar.number_input("PTT, seconds")
f = st.sidebar.number_input("Sosm, mmol/L")
g = st.sidebar.number_input("Serum potassium, mEq/L")
h = st.sidebar.number_input("Serum chloride, mEq/L")
i = st.sidebar.number_input("Bicarbonate, mmol/L")
j = st.sidebar.number_input("SBP, mmHg")

# 如果按下按钮
if st.button("Predict"):  # 显示按钮
    # 加载训练好的模型
    model = joblib.load("XGBoost.pkl")
    # 将输入存储DataFrame
    X = pd.DataFrame([[a, b, c, d, e, f, g, h, i, j]],
                     columns=['DE', 'Ureanitrogen', 'Creatinine', 'Aniongap', 'PTT', 'sosm',
       'Potassium', 'Chloride', 'Bicarbonate', 'SBP'])
    # 进行预测
    prediction = model.predict(X)[0]
    Predict_proba = model.predict_proba(X)[:, 1][0]
    # 输出预测结果
    if prediction == 0:
        st.subheader(f"Model predicted outcome for early loop diuretic resistance: No")
    else:
        st.subheader(f"Model predicted outcome for early loop diuretic resistance: Yes")
    # 输出概率
    st.subheader(f"Probability of predicting early loop diuretic resistance: {'%.2f' % float(Predict_proba * 100) + '%'}")

