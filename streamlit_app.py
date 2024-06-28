import streamlit as st
import pandas as pd
#import requests
#from st_anggrid import AgGrid

house = pd.read_csv('house_clean.csv')


def main() :
    st.header('Halaman Streamlit Azizah')
    st.subheader('This is Subheader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Pyhtagorean Equation : ')
    st.latex('c^2 = a^2+b^2')


    st.dataframe(house)

# Untuk menulis metric
    st.write('Metrics')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
if __name__ == '__main__' : 
    main()

 # Untuk menampilkan Grid -- masih blm tampil
    #st.write('Menampilkan Dataframe dengan St AgGrid')
    #AgGrid(house)

st.table([x for x in range(1,5)])
  
click_me_btn = st.button('Click Me')
st.write(click_me_btn) #Return True kalo di Click 
check_btn = st.checkbox('Klik Jika Setuju')
if check_btn :
    st.write('Anda Setuju')
  
radio_button= st.radio('Choose below',[x for x in range(1,3)])
st.write('Anda Memilih',radio_button)
    
#slider 
age_slider = st.slider('Berapa Usia Anda',0,100)
st.write('Usia Anda',age_slider)
    
#Input (Typing)
num_input = st.number_input('Input Berapapun')
st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))
      
#Menampilkan menu sidebar 
sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])

#columns :
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
#atau dengan assignment 
#image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
  
#expander 
#dengan with atau dengan assignment 
expander = st.expander("Klik Untuk Detail ")
expander.write('Anda Telah Membuka Detail')

#sidebar 
with st.form("Data Diri"):
    st.write("Area di dalam form")
    slider_val = st.slider("Pilih Angka")
    checkbox_val = st.checkbox("Setuju")

    #Every form must have a submit button.
    submitted = st.form_submit_button("Simpan")
    if submitted:
         st.write("Angka dipilih", slider_val, "checkbox", checkbox_val)

st.write("Area di luar form")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
   st.radio("Select one:", [1, 2])

# SHow and update progress bar
bar = st.progress(50)
time.sleep(3)
bar.progress(100)

with st.status("Authenticaring...") as s:
    time.sleep(2)
    st.write("Some long response.")
    s.update(label="Response")

st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
st.exception(e)

if __name__ == '__main__' :
  main()
