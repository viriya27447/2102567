# viriya.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class ViriyaModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, data):
        # แยก feature และ target
        X = data[['feature1', 'feature2']]  # เปลี่ยนตามชื่อคอลัมน์ของคุณ
        y = data['target']  # เปลี่ยนตามชื่อคอลัมน์ของคุณ

        # แบ่งข้อมูลเป็น training และ testing set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # เทรนโมเดล
        self.model.fit(X_train, y_train)

    def predict(self, inputs):
        # ทำนายผล
        return self.model.predict([inputs])