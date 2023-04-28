import pickle
import streamlit as sl

model = pickle.load(open('Estimasi_JumlahKaloriDalamMakananStarbucks.sav', 'rb'))

sl.title('Estimasi Jumlah Kalori Makanan Di Menu Starbucks')
sl.write('---')

Protein = sl.number_input('Input Protein(g)')
Total_Fat = sl.number_input('Input Total Lemak(g)')
Sodium = sl.number_input('Input Sodium (mg)')
Total_Carbohydrate = sl.number_input('Input Total Karbohidrat(g)')
Sugars = sl.number_input('Input Total Gula(g)')

predict = ''

if sl.button('Estimasi Kalori'):
    predict = model.predict(
        [[Protein,Total_Fat,Sodium,Total_Carbohydrate,Sugars]]
    )
    sl.write ('Estimasi jumlah kalori makanan menu di Starbucks (kCal) : ', predict)