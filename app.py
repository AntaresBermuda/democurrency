import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

st.set_page_config(page_title="League")

st.header("FreqSevModel")
st.subheader("", divider="rainbow")


st.subheader("If you were sent to war, how would you fight your opponents? Pick 3.")

Q1 = st.selectbox("",
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", "Fighter Jet Pilot",
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person"),
    key="q1")

Q1_1 = st.selectbox("",
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", "Fighter Jet Pilot",
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person"),
    key="q1_1")

Q1_2 = st.selectbox("",
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", "Fighter Jet Pilot",
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person"),
    key="q1_2")


st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')
st.subheader("Which Positive Traits describes you best? Pick 3.")


Q2 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2")

Q2_1 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2_1")

Q2_2 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2_2")

st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')
st.subheader("Which Negative Traits describes you best? Pick 2.")


Q3 = st.selectbox("",
    ("-", "Impatient", "Revengeful", "Just Crazy", "Pessimistic", "Angry", "Paranoid", "Lazy", "Selfish", "boastful", "Controlling"),
    key="q3")
Q3_1 = st.selectbox("",
    ("-", "Impatient", "Revengeful", "Just Crazy", "Pessimistic", "Angry", "Paranoid", "Lazy", "Selfish", "boastful", "Controlling"),
    key="q3_1")

st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')
st.subheader("What Weapons do you keep just in case. Pick 2.")


Q4 = st.selectbox("",
    ("-", "Two handguns", "My Fists", "Taser Gun", "FN P90, I'm cultured", "A Medieval Sword", "An ancient book with Magical Spells", "Bow and Arrow", "Lightsaber", "bazooka", "Daggers"),
    key="q4")

Q4_1 = st.selectbox("",
    ("-", "Two handguns", "My Fists", "Taser Gun", "FN P90, I'm cultured", "A Medieval Sword", "An ancient book with Magical Spells", "Bow and Arrow", "Lightsaber", "bazooka", "Daggers"),
    key="q4_1")

st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')
st.subheader("What Superpowers would you like to have? Pick 3.")

Q5 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", 
    "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water/Ice-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5")
Q5_1 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", 
    "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water/Ice-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5_1")
Q5_2 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", 
    "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water/Ice-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5_2")

st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')
st.subheader("Choose 2 pets.")

# Show funny patrick meme if you chose a pet as a rock.
Q6 = st.selectbox("",
    ("-", "Cat", "Dog", "Fish", "Snake", "Bear", "A Rock", "Roach", "Cow", "Hamster", "Bird", "Scorpion", "Fox", "Turtle", "Toad", "Horse", "Monkey", "Humans are the Superior Animal", "I would rather have a Plant"),
    key="q6")
Q6_1 = st.selectbox("",
    ("-", "Cat", "Dog", "Fish", "Snake", "Bear", "A Rock", "Roach", "Cow", "Hamster", "Bird", "Scorpion", "Fox", "Turtle", "Toad", "Horse", "Monkey", "Humans are the Superior Animal", "I would rather have a Plant"),
    key="q6_1")


l = ["-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", "Fighter Jet Pilot",
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person"]
Arr1 = np.array([1 if x == Q1 else 0 for x in l]) + np.array([1 if x == Q1_1 else 0 for x in l]) + np.array([1 if x == Q1_2 else 0 for x in l])

l = ["-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"]
Arr2 = np.array([1 if x == Q2 else 0 for x in l]) + np.array([1 if x == Q2_2 else 0 for x in l]) + np.array([1 if x == Q2_2 else 0 for x in l])

l = ["-", "Impatient", "Revengeful", "Just Crazy", "Pessimistic", "Angry", "Paranoid", "Lazy", "Selfish", "boastful", "Controlling"]
Arr3 = np.array([1 if x == Q3 else 0 for x in l]) + np.array([1 if x == Q3_1 else 0 for x in l])

l = ["-", "Two handguns", "My Fists", "Taser Gun", "FN P90, I'm cultured", "A Medieval Sword", "An ancient book with Magical Spells", "Bow and Arrow", "Lightsaber", "Bazooka", "Daggers"]
Arr4 = np.array([1 if x == Q4 else 0 for x in l]) + np.array([1 if x == Q4_1 else 0 for x in l])

l = ["-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", 
    "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water/Ice-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"]
Arr5 = np.array([1 if x == Q5 else 0 for x in l]) + np.array([1 if x == Q5_1 else 0 for x in l]) + np.array([1 if x == Q5_2 else 0 for x in l])

l = ["-", "Cat", "Dog", "Fish", "Snake", "Bear", "A Rock", "Roach", "Cow", "Hamster", "Bird", "Scorpion", "Fox", "Turtle", "Toad", "Horse", "Monkey", "Humans are the Superior Animal", "I would rather have a Plant"]
Arr6 = np.array([1 if x == Q6 else 0 for x in l]) + np.array([1 if x == Q6_1 else 0 for x in l])

result = list(Arr1[1:])+list(Arr2[1:])+list(Arr3[1:])+list(Arr4)[1:]+list(Arr5[1:])+list(Arr6[1:])

st.write('\n')
st.subheader("", divider="rainbow")
st.write('\n')

if st.button("Generate Result"):
    
    if np.sum(result)<15:
        st.error("You can't leave things blank, you can choose the same thing nire than once if you want.", icon="🚨")
    else:
        st.write(len(result))