import streamlit as strm
import base64
import PyPDF2 
from pdf2image import convert_from_path

# Function to convert PDF pages to images 
def convert_pdf_to_images(pdf_path): 
    images = convert_from_path(pdf_path) 
    return images


strm.title("Insurance")
# Create a button 


# Create a button
if strm.button('Company Presentation'):
    # Display the PDF file
    pdf_file = 'intro.pdf'
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Convert PDF pages to images 
    images = convert_pdf_to_images(pdf_file) 
    # Display images 
    for image in images: 
        strm.image(image, use_container_width =True)
    #pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    #strm.markdown(pdf_display, unsafe_allow_html=True)

strm.title("Needs Questions")
strm.markdown('**Q1- If you became sick or were injured and could not work, would you stil receive a paycheque?**')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('Yes',key='btn1'):
        pass
with col2:
    if strm.button('No',key='btn2'):
        pass
with col3:
    if strm.button('Not a concern',key='btnn3'):
        pass
strm.write('Concerned for?')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('You',key='btnn4'):
        pass
with col2:
    if strm.button('Spouse',key='btnn5'):
        pass
with col3:
    if strm.button('Both',key='btnn6'):
        pass
#-----------------------------------------------------------------------------
strm.markdown('**Q2- If you were to die tomorrow, would your family b able to maintain their standard of living?**')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('Yes',key='btnn7'):
        pass
with col2:
    if strm.button('No',key='btnn8'):
        pass
with col3:
    if strm.button('Not a concern',key='btnn9'):
        pass
strm.write('Concerned for?')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('You',key='btnn10'):
        pass
with col2:
    if strm.button('Spouse',key='btnn11'):
        pass
with col3:
    if strm.button('Both',key='btnn12'):
        pass
#-----------------------------------------------------------------------------
strm.markdown('**Q3- If you develop cancer, or any other critical conitions, do you have an emergency cash fund of 6 to 12 months income to help cover the cost of the non-medical expenses?**')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('Yes',key='btnn13'):
        pass
with col2:
    if strm.button('No'):
        pass
with col3:
    if strm.button('Not a concern',key='btnn14'):
        pass
strm.write('Concerned for?')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('You',key='btnn15'):
        pass
with col2:
    if strm.button('Spouse',key='btnn16'):
        pass
with col3:
    if strm.button('Both',key='btnn17'):
        pass
#-----------------------------------------------------------------------------
strm.markdown('**Q4- If you became sick or were injured, would your current health insurance cover all of the costs?**')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('Yes',key='btnn18'):
        pass
with col2:
    if strm.button('No',key='btnn19'):
        pass
with col3:
    if strm.button('Not a concern',key='btnn20'):
        pass
strm.write('Concerned for?')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('You',key='btnn21'):
        pass
with col2:
    if strm.button('Spouse',key='btnn22'):
        pass
with col3:
    if strm.button('Both',key='btnn23'):
        pass
#---------------------------------------------------------------------------
user_input = strm.text_area('Needs Analysis Notes',height=150)