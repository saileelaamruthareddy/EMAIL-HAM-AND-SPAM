import pickle
import streamlit as st
import os
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Display title
image_path = (inomatics .png'rb')  # Replace with your actual PNG image file path

# Display the PNG image
st.image(image_path)
spam_image_path = (spam .png'rb')  # Replace with your actual PNG image file path for spam
st.title("Predicting Email Spam or Ham")


model = pickle.load(open(r"C:\users\saile\AI MACHINE LEARNING\model.pkl",'rb'))
bow = pickle.load(open(r"C:\users\saile\AI MACHINE LEARNING\bow.pkl",'rb'))


email = st.text_input("Enter the email:")

if st.button("Classify Email"):
    if email:
        # Transform input email using CountVectorizer
        data = bow.transform([email]).toarray()
        prediction = model.predict(data)[0]
        # Display the prediction result
        st.write(f"The email is classified as: **{prediction}**")
        
        # Display the spam image if classified as spam
        if prediction == 'spam':
            st.image(spam_image_path)
 
