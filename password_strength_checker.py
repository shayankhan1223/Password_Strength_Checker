import streamlit as st
import random
import re

# App Header
st.title("🔐 Password Strength Checker & Generator")

# Function to check password strength
def password_strength_checker(password):
    score = 0
    
    # Conditions for checking password strength
    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        st.error("❌ Include at least one lowercase letter")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        st.error("❌ Include at least one uppercase letter")
    
    if re.search(r"[\d]", password):
        score += 1
    else:
        st.error("❌ Include at least one number")
    
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~]", password):
        score += 1
    else:
        st.error("❌ Include at least one special character")
    
    # Password Strength Feedback
    if score == 5:
        st.success("✅ Strong Password!")
    elif score == 4 or score == 3:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password!!")

# Function to generate a strong password
def generate_password(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}[]:;<>,.?/~`|-\="
    return "".join(random.choice(chars) for _ in range(length))

# User Input
password = st.text_input("Enter your password", type="password")
if password:
    password_strength_checker(password)

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")
length = st.number_input("Enter password length", min_value=8, max_value=50, value=12, step=1)
if st.button("Generate Password"):
    new_password = generate_password(length)
    st.success(f"**Generated Password:** {new_password}")
