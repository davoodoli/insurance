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
with open("intro.pdf", "rb") as pdf_file: 
    pdf_bytes = pdf_file.read()
strm.download_button( label="Company Presentation", data=pdf_bytes, file_name="intro.pdf", mime="application/pdf" )
#if strm.button('Company Presentation'):
    # Display the PDF file
    #pdf_file = 'intro.pdf'

    # Read the PDF file and encode it to base64
    #with open(pdf_file, "rb") as f:
       # base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        

strm.title("Needs Questions")
strm.markdown('**Q1- If you became sick or were injured and could not work, would you stil receive a paycheque?**')
col1, col2, col3 = strm.columns(3)
with col1:
    if strm.button('Yes',key='btn1'):
        strm.write('Workers Compensation(on the job only)?')
        if strm.button('Yes',key='btn29'):
            pass
        if strm.button('No',key='btn30'):
            pass

        strm.write('Sick days?')
        if strm.button('Yes',key='btn31'):
            pass
        if strm.button('No',key='btn32'):
            pass

        strm.write('Short term or Long term Disability?')
        if strm.button('Yes',key='btn33'):
            pass
        if strm.button('No',key='btn34'):
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
        strm.write('Pay Funeral costs?')
        if strm.button('Yes',key='btn35'):
            pass
        if strm.button('No',key='btn36'):
            pass

        strm.write('Pay the mortgage/rent and other bills?')
        if strm.button('Yes',key='btn37'):
            pass
        if strm.button('No',key='btn38'):
            pass

        strm.write('Do you have mortgage insurance(if yes ask for statements)?')
        if strm.button('Yes',key='btn39'):
            pass
        if strm.button('No',key='btn40'):
            pass

        strm.write('Do you have any other creditor insurance?')
        if strm.button('Yes',key='btn43'):
            pass
        if strm.button('No',key='btn44'):
            pass

        strm.write('Replace your income?')
        if strm.button('Yes',key='btn41'):
            pass
        if strm.button('No',key='btn42'):
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
        strm.write('Specifically, would you have a fund to pay the costs associated with cancer?')
        if strm.button('Yes',key='btn43'):
            pass
        if strm.button('No',key='btn44'):
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
        strm.write('Costs for a hospital stay?')
        if strm.button('Yes',key='btn45'):
            pass
        if strm.button('No',key='btn46'):
            pass
        strm.write('Deductibles and Co-Payments?')
        if strm.button('Yes',key='btn47'):
            pass
        if strm.button('No',key='btn48'):
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

#---------------------------------------------------------------------------

strm.title("Personal Info")
user_input = strm.text_input('First Name')
user_input = strm.text_input('Last Name')
user_input = strm.text_input('Date of Birth')
user_input = strm.text_input('Occupation')

options = ['Select:','Protecting your paycheque', 'Protecting your family life styles', 'protection against critical illness'
,'Portection against unexpected medical expenses'] 
selected_option = strm.selectbox('Your primary concern from understandnig your needs?',options)

user_input = strm.text_input('Marital Status')

strm.write('Ages of Dependent Children')

col1, col2, col3 = strm.columns(3)
with col1:
    user_input = strm.text_input('Age',key="a1")
with col2:
    user_input = strm.text_input('Age',key="a2")
with col3:
    user_input = strm.text_input('Age',key="a3")

#---------------------------------------------------------------------------
strm.title("Income")


user_input = strm.text_input('Gross Active Income')
user_input = strm.text_input('Passive Annual Income')
user_input = strm.text_input('Monthly Obligations')

user_input = strm.text_input('Total Assets')
user_input = strm.text_input('Total Liabilities')



options = ['Select:','Residence-Owner', 'Residence-Tenant', 'Residence-Other'] 
selected_option = strm.selectbox('Residence',options)

#---------------------------------------------------------------------------

strm.title("Coverage and Recommendations")


strm.markdown('**Hospitalization**')
col1, col2, col3 = strm.columns(3)
with col1:
    user_input = strm.text_input('Accident Daily Amount')
with col2:
    user_input = strm.text_input('Sickness Daily Amount')
with col3:
    user_input = strm.text_input('Insurer')

strm.write('Applicant Total Needs:')

col1, col2 = strm.columns(2)
with col1:
    user_input = strm.text_input('Accident Daily Amount ')
with col2:
    user_input = strm.text_input('Sickness Daily Amount ')



strm.markdown('**Disability**')
col1, col2, col3 = strm.columns(3)
with col1:
    user_input = strm.text_input('Accident Monthly Amount ')
with col2:
    user_input = strm.text_input('Sickness Monthly Amount ')
with col3:
    user_input = strm.text_input('Insurer ')


strm.markdown('**Critical Illness**')
col1, col2 = strm.columns(2)
with col1:
    user_input = strm.text_input('Critical Illness Lump sum Amount ')
with col2:
    user_input = strm.text_input('Insurer  ')
strm.write('Applicant Total Needs:')
user_input = strm.text_input('Critical Illness Lump sum Amount  ')



strm.markdown('**Cancer**')
col1, col2 = strm.columns(2)
with col1:
    user_input = strm.text_input('Cancer Daily Amount ')
with col2:
    user_input = strm.text_input('Insurer   ')
strm.write('Applicant Total Needs:')
user_input = strm.text_input('Cancer Daily Amount  ')


strm.markdown('**Total montly amount of money spent on existing life, Accident and sickness and critical illness insurance**')
user_input = strm.text_input('Amount  ')
