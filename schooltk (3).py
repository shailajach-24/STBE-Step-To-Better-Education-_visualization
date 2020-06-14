#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')
import plotly as pl
import cufflinks as cf
cf.go_offline()
import plotly.offline as py
from plotly import graph_objs as go
from plotly.graph_objs import *


# In[2]:


from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from imutils import paths
from tkinter.filedialog import askopenfilename

import numpy as np 
import pandas as pd 

import pylab as pl
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
pl.style.use('fivethirtyeight')
import seaborn as sns


import warnings
warnings.filterwarnings('ignore')


# In[3]:


from tkinter import simpledialog


# In[4]:


data= pd.read_csv('check_data.csv',index_col='id')
data


# In[5]:


Unit1= data[['TELUGU_U1','HINDI_U1','ENGLISH_U1','MATHS_U1','SCIENCE_U1','SOCIAL_U1']]
Unit2= data[['TELUGU_U2','HINDI_U2','ENGLISH_U2','MATHS_U2','SCIENCE_U2','SOCIAL_U2']]
Unit3= data[['TELUGU_U3','HINDI_U3','ENGLISH_U3','MATHS_U3','SCIENCE_U3','SOCIAL_U3']]
Unit4=data[['TELUGU_U4','HINDI_UNIT4','ENGLISH_U4','MATHS_U4','SCIENCE_UNIT4','SOCIAL_UNIT4']]
Unit5= data[['TELUGU_U5','HINDI_U5','ENGLISH_U5','MATHS_U5','SCIENCE_U5','SOCIAL_U5']]
Unit6= data[['TELUGU_U6','HINDI_U6','ENGLISH_U6','MATHS_U6','SCIENCE_U6','SOCIAL_U6']]
UnitQ=data[['TELUGU_Q','HINDI_Q','ENGLISH__Q','MATHS_U4','SCIENCE_Q','SOCIAL_Q']]
UnitH= data[['TELUGU_H','HINDI_H','ENGLISH_H','MATHS_H','SCIENCE_H','SOCIAL_H']]
UnitPF= data[['TELUGU_PF','HINDI_PF','ENGLISH_PF','MATHS_PF','SCIENCE_PF','SOCIAL_PF']]
UnitF= data[['TELUGU_F','HINDI_F','ENGLISH_F','MATHS_F','SCIENCE_F','SOCIAL_F']]


# In[6]:


ninth= pd.read_csv('check_data1.csv',index_col='id')
ninth


# In[7]:


Unit1= ninth[['TELUGU_U1','HINDI_U1','ENGLISH_U1','MATHS_U1','SCIENCE_U1','SOCIAL_U1']]
Unit2= ninth[['TELUGU_U2','HINDI_U2','ENGLISH_U2','MATHS_U2','SCIENCE_U2','SOCIAL_U2']]
Unit4= ninth[['TELUGU_U4','HINDI_U4','ENGLISH_U4','MATHS_U4','SCIENCE_U4','SOCIAL_U4']]
Unit3=ninth[['TELUGU_U3','HINDI_UNIT3','ENGLISH_U3','MATHS_U3','SCIENCE_UNIT3','SOCIAL_UNIT3']]
Unit5= ninth[['TELUGU_U5','HINDI_U5','ENGLISH_U5','MATHS_U5','SCIENCE_U5','SOCIAL_U5']]
Unit6= ninth[['TELUGU_U6','HINDI_U6','ENGLISH_U6','MATHS_U6','SCIENCE_U6','SOCIAL_U6']]
UnitQ=ninth[['TELUGU_Q','HINDI_Q','ENGLISH_Q','MATHS_U4','SCIENCE_Q','SOCIAL_Q']]
UnitH= ninth[['TELUGU_H','HINDI_H','ENGLISH__H','MATHS_H','SCIENCE_H','SOCIAL_H']]
UnitPF= ninth[['TELUGU_PF','HINDI_PF','ENGLISH_PF','MATHS_PF','SCIENCE_PF','SOCIAL_PF']]
UnitF= ninth[['TELUGU_F','HINDI_F','ENGLISH_F','MATHS_F','SCIENCE_F','SOCIAL_F']]


# In[8]:


ninth_totals=ninth[['TOTAL_U1','TOTAL_U2','TOTAL_Q','UNIT3_TOTAL','TOTAL_U4','TOTAL_H','TOTAL_U5','TOTAL_U6','TOTAL_PF','TOTAL_F']]
ninth_tot=ninth_totals.rename(columns={'TOTAL_U1':'u1','TOTAL_U2':'u2','TOTAL_Q':'Q','UNIT3_TOTAL':'u3','TOTAL_U4':'u4','TOTAL_H':'H','TOTAL_U5':'u5','TOTAL_U6':'u6','TOTAL_PF':'PF','TOTAL_F':'F'})
ninth_tot


# In[ ]:


main = tkinter.Tk()
main.title('school analysis')
main.geometry("1300x1200")
#student_id= simpledialog.askstring("Input", "What is your id?")
#student_id=input('please enter id:')
#A=data.loc[student_id]
#id=student_id
#Name=A['names']
#print('id:',student_id,"\n" 'name:',A['names'],"\n"'Age:',A['AGE'],"\n"'CLASS:',A['CLASS'],"\n"'Gender:',A['GENDER'])
class test:
    def uploaddataset1():
        global filename
        text.delete('1.0', END)
        data= askopenfilename(initialdir = "Dataset")
        pathlabel.config(text=data)
        text.insert(END,"Dataset loaded\n\n")
    def uploaddataset2():
        global filename
        text.delete('1.0', END)
        ninth= askopenfilename(initialdir = "Dataset")
        pathlabel1.config(text=ninth)
        text.insert(END,"Dataset loaded\n\n")
    def student_details():
        global student_id
        student_id= simpledialog.askstring("Input", "What is your id?")
        text.delete('1.0', END)
        text.insert(END,"Student details\n\n")
        #application_window = tk.Tk()
        #student_id= simpledialog.askstring("Input", "What is your id?")
        A=data.loc[student_id]
        text.insert(END,"studentname: {}".format(A['names'])+"\n")
        text.insert(END,"age: {}".format(A['AGE'])+"\n")
        text.insert(END,"class: {}".format(A['CLASS'])+"\n")
        text.insert(END,"gender: {}".format(A['GENDER'])+"\n")
    def unit_details():
        unit_totals=data[['TOTAL_U1','TOTAL_U2','TOTAL_Q','TOTAL_U3','UNIT4_TOTAL','TOTAL_H','TOTAL_U5','TOTAL_U6','TOTAL_PF','TOTAL_F']]
        tot_data=unit_totals.rename(columns={'TOTAL_U1':'u1','TOTAL_U2':'u2','TOTAL_Q':'Q','TOTAL_U3':'u3','UNIT4_TOTAL':'u4','TOTAL_H':'H','TOTAL_U5':'u5','TOTAL_U6':'u6','TOTAL_PF':'PF','TOTAL_F':'F'})
        s0=tot_data.loc[student_id]
        text=[]
        for i in s0:
            if i<=300:
                text.append('bad')
            elif i<=400:
                text.append('good')
            elif i<=500:
                text.append('average')
            else:
                text.append('excellent')
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=s0.index,
            y=s0.values,
            mode="lines+markers+text",
            name="Lines, Markers and Text",
            text=text
                #textposition="auto"
            ))
        fig.show()
        
    def att_details():
              att=data[['ATTENDENCE_U1(%)','ATTENDENCE_U2(%)','ATTENDENCE_Q(%)','ATTENDENCE_U3(%)','ATTENDENCE_U4(%)','ATTENDENCE_H(%)','ATTENDENCE_U5(%)','ATTENDENCE_U6(%)','ATTENDENCE_PF(%)','ATTENDENCE_F(%)']]
        att_data=att.rename(columns={'ATTENDENCE_U1(%)':'u1','ATTENDENCE_U2(%)':'u2','ATTENDENCE_Q(%)':'Q','ATTENDENCE_U3(%)':'u3','ATTENDENCE_U4(%)':'u4','ATTENDENCE_H(%)':'H','ATTENDENCE_U5(%)':'u5','ATTENDENCE_U6(%)':'u6','ATTENDENCE_PF(%)':'PF','ATTENDENCE_F(%)':'F'})
        s=att_data.loc[student_id]
        y=s.tolist()
        x=s.index

        # Use textposition='auto' for direct text
        fig = go.Figure(data=[go.Bar(
                x=x, y=y,
                text=y,
                textposition='auto',
                marker_color='rgb(0,188,0)'
            )])
        fig.show()
    
    def ninth_tenth_tot():
        tenth_totals=data[['TOTAL_U1','TOTAL_U2','TOTAL_Q','TOTAL_U3','UNIT4_TOTAL','TOTAL_H','TOTAL_U5','TOTAL_U6','TOTAL_PF','TOTAL_F']]
        tenth_tot=tenth_totals.rename(columns={'TOTAL_U1':'u1','TOTAL_U2':'u2','TOTAL_Q':'Q','TOTAL_U3':'u3','UNIT4_TOTAL':'u4','TOTAL_H':'H','TOTAL_U5':'u5','TOTAL_U6':'u6','TOTAL_PF':'PF','TOTAL_F':'F'})
        ninth_totals=ninth[['TOTAL_U1','TOTAL_U2','TOTAL_Q','UNIT3_TOTAL','TOTAL_U4','TOTAL_H','TOTAL_U5','TOTAL_U6','TOTAL_PF','TOTAL_F']]
        ninth_tot=ninth_totals.rename(columns={'TOTAL_U1':'u1','TOTAL_U2':'u2','TOTAL_Q':'Q','UNIT3_TOTAL':'u3','TOTAL_U4':'u4','TOTAL_H':'H','TOTAL_U5':'u5','TOTAL_U6':'u6','TOTAL_PF':'PF','TOTAL_F':'F'})
        st1=tenth_tot.loc[student_id]
        st1_x=st1.index
        st1_y=st1.values.tolist()
        st2=ninth_tot.loc[student_id]
        st2_x=st2.index
        st2_y=st2.values.tolist()
        py.iplot({
            'data': [
                Bar(**{
                    'x':st1_x ,
                    'y':st1_y ,
                    'text':st1_y,
                    'textposition':'auto',
                    'name': 'tenth_totl',
                    'type': 'bar'
                }),
                Bar(**{
                    'x':st2_x,
                    'y':st2_y,
                    'text':st2_y,
                    'textposition':'auto',
                    'name': 'ninth_totl',
                    'type': 'bar'
                })
            ],
            'layout': Layout(**{
            'title': 'ninth_total vs tenth_total'
            })
        })
    def ninth_tenth_att():
        tenth_attendence=data[['ATTENDENCE_U1(%)','ATTENDENCE_U2(%)','ATTENDENCE_Q(%)','ATTENDENCE_U3(%)','ATTENDENCE_U4(%)','ATTENDENCE_H(%)','ATTENDENCE_U5(%)','ATTENDENCE_U6(%)','ATTENDENCE_PF(%)','ATTENDENCE_F(%)']]
        tenth_att=tenth_attendence.rename(columns={'ATTENDENCE_U1(%)':'u1','ATTENDENCE_U2(%)':'u2','ATTENDENCE_Q(%)':'Q','ATTENDENCE_U3(%)':'u3','ATTENDENCE_U4(%)':'u4','ATTENDENCE_H(%)':'H','ATTENDENCE_U5(%)':'u5','ATTENDENCE_U6(%)':'u6','ATTENDENCE_PF(%)':'PF','ATTENDENCE_F(%)':'F'})
        ninth_attendence=ninth[['ATTENDENCE_U1(%)','ATTENDENCE_U2(%)','ATTENDENCE_Q(%)','ATTENDENCE_U3(%)','ATTENDENCE_U4(%)','ATTENDENCE_H(%)','ATTENDENCE_U5(%)','ATTENDENCE_U6(%)','ATTENDENCE_PF(%)','ATTENDENCE_F(%)']]
        ninth_att=ninth_attendence.rename(columns={'ATTENDENCE_U1(%)':'u1','ATTENDENCE_U2(%)':'u2','ATTENDENCE_Q(%)':'Q','ATTENDENCE_U3(%)':'u3','ATTENDENCE_U4(%)':'u4','ATTENDENCE_H(%)':'H','ATTENDENCE_U5(%)':'u5','ATTENDENCE_U6(%)':'u6','ATTENDENCE_PF(%)':'PF','ATTENDENCE_F(%)':'F'})

        at1=tenth_att.loc[student_id]
        at2=ninth_att.loc[student_id]
        py.iplot({
            'data': [
                Bar(**{
                    'x':at1.index ,
                    'y':at1.tolist() ,
                    'text':at1.tolist(),
                    'textposition':'auto',
                    'name': 'tenth_at',
                    'type': 'bar'
                }),
                Bar(**{
                    'x':at2.index,
                    'y':at2.tolist(),
                    'text':at2.tolist(),
                    'textposition':'auto',
                    'name': 'ninth_at',
                    'type': 'bar'
                })
            ],
            'layout': Layout(**{
            'title': 'ninth_att vs tenth_att'
            })
        })
        
        
font = ('times', 16, 'bold')
title = Label(main, text='School Analysis')
title.config(bg='forest green', fg='white')
title.config(font=font)
title.config(height=3, width=120)
title.place
font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Dataset1", command=test.uploaddataset1)
upload.place(x=700,y=100)
upload.config(font=font1)

pathlabel = Label(main)
pathlabel.config(bg='dark orchid', fg='white')  
pathlabel.config(font=font1)
pathlabel.place(x=700,y=150)


upload = Button(main, text="Upload Dataset2", command=test.uploaddataset2)
upload.place(x=700,y=150)
upload.config(font=font1)


pathlabel1 = Label(main)
pathlabel1.config(bg='dark orchid', fg='white')  
pathlabel1.config(font=font1)
pathlabel1.place(x=700,y=150)

Data_analysis = Button(main, text="student details", command=test.student_details)
Data_analysis.place(x=700,y=200)
Data_analysis.config(font=font1)

graph1= Button(main, text="unit_details", command=test.unit_details)
graph1.place(x=700,y=250)
graph1.config(font=font1)

graph2= Button(main, text="att_details", command=test.att_details)
graph2.place(x=700,y=300)
graph2.config(font=font1)

graph3= Button(main, text="ninth_tenth_tot", command=test.ninth_tenth_tot)
graph3.place(x=700,y=350)
graph3.config(font=font1)

graph4= Button(main, text="ninth_tenth_att", command=test.ninth_tenth_att)
graph4.place(x=700,y=400)
graph4.config(font=font1)

font1 = ('times', 12, 'bold')
text=Text(main,height=30,width=80)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=100)
text.config(font=font1)

main.config(bg='pale goldenrod')
main.mainloop()


# In[ ]:




