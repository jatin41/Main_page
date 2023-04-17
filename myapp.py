import streamlit as st

data=[]
f=[]
g=[]
def symptom1():
    import streamlit as st
    import pandas as pd
# Read in the CSV file
    df = pd.read_csv('Untitled 2.csv')
    series = pd.concat([df[col] for col in df.columns[1:]])
    # Extract the values for the dropdown
    values = series.sort_values().unique()

# Create the dropdown menu
    n = st.selectbox('Enter symptom 1', ["None"] + list(values),index=0)
    url="./Pages/untitled0.py"
    import csv
    with open('Untitled 2.csv', 'r') as csv_file:
    
        csv_reader = csv.reader(csv_file.readlines())  # Read the file into memory as a list of strings
        next(csv_reader)
        
        
        if n:
            for row in csv_reader:
                for i in range(len(row)):
                    if n in row[i]:
                        data.append(row)
                        st.write(row[0])
                
            
            for j in range(len(data)):
                if 'heart disease' in data[j]:
                    st.write('click here to check for heart disease ')
                    
                    st.markdown(
                           """
                           <a href="https://jatin41-heart-disease-heart-disease-prediction-7phf7n.streamlit.app" target="_blank">Heart disease</a>
                           """,
                           unsafe_allow_html=True
                           )   
                if 'migraine' in data[j]:
                    st.write('Have a medical Diagnosis and click here to check for migraine ')
                    st.markdown(
                           """
                           <a href="https://jatin41-migraine-migraine-vlclyn.streamlit.app" target="_blank">Migraine</a>
                           """,
                           unsafe_allow_html=True
                           )
                if 'Parkinsons'  in data[j]:
                    st.write('click here to check for parkinsons ')
                    st.markdown(
                           """
                           <a href="https://jatin41-parkinsons-parkinsons-fjud3r.streamlit.app" target="_blank">Parkinsons</a>
                           """,
                           unsafe_allow_html=True
                           )
                if 'Diabetes' in data[j]:
                    st.write('click here to check for Diabetes ')
                    st.markdown(
                           """
                           <a href="https://jatin41-my-webapps-diabetes-prediction-twi2ua.streamlit.app/" target="_blank">Diabetes</a>
                           """,
                           unsafe_allow_html=True
                           )
                if 'Covid19' in data[j]:
                   st.write('click here to check for Covid ')
                   st.markdown(
                            """
                           <a href="https://jatin41-covid-covid-y4gv5m.streamlit.app/" target="_blank">Covid 19</a>
                           """,
                           unsafe_allow_html=True
                           )
       
    return data


    
    
def symptom2():
    import streamlit as st
    import pandas as pd
# Read in the CSV file
    df = pd.read_csv('Untitled 2.csv')
    series = pd.concat([df[col] for col in df.columns[1:]])
    # Extract the values for the dropdown
    values = series.sort_values().unique()
    m= st.selectbox('Enter symptom 2',["None"] + list(values),index=0)
    if m:
        for tow in data:
            for i in range(len(tow)):
                if m in tow[i]:
                    st.write(tow[0])
                    f.append(tow)

    return f

    
       
def symptom3():
    import streamlit as st
    import pandas as pd
# Read in the CSV file
    df = pd.read_csv('Untitled 2.csv')
    series = pd.concat([df[col] for col in df.columns[1:]])
    # Extract the values for the dropdown
    values = series.sort_values().unique()
    o= st.selectbox('Enter symptom 3',["None"] + list(values),index=0)
    
    if o:
        for row in f:
            for i in range(len(row)):
                if o in row[i]:
                    st.write(row[0])
                    g.append(row)
                    
    return g

def symptom4():
    import streamlit as st
    import pandas as pd
# Read in the CSV file
    df = pd.read_csv('Untitled 2.csv')
    series = pd.concat([df[col] for col in df.columns[1:]])
    # Extract the values for the dropdown
    values = series.sort_values().unique()
    p= st.selectbox('Enter symptom 4',["None"] + list(values),index=0)
    for row in g:
        for i in range(len(row)):
            if p in row[i]:
                st.write(row[0])
data = symptom1()
if data:
    st.markdown("<h1 style='text-align: center; font-size: 24px; color:red'>Consult the doctor for more info!</h1>", unsafe_allow_html=True)
    f=symptom2()
    if f:
        st.markdown("<h1 style='text-align: center; font-size: 24px; color:red'>Consult the doctor for more info!</h1>", unsafe_allow_html=True)
        g=symptom3()
        if g:
            st.markdown("<h1 style='text-align: center; font-size: 24px; color:red'>Consult the doctor for more info!</h1>", unsafe_allow_html=True)
            symptom4()                
                    
                    
        


  
