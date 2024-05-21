# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
<<<<<<< HEAD
    df = pd.read_csv("gapminder.tsv", sep="\t") # 외부 텍스트 데이터  -> 데이터프레임 반환
    return df

def plot_matplotlib():
    st.title(" Bar Plot")
    df = load_data() # 데이터 준비
    # 그래프 그리기
    fig, ax = plt.subplots()
    
    # 막대 그래프 
=======
    df = pd.read_csv("gapminder.tsv", sep="\t") #외부 텍스트 데이터 -> 데이터프레임 반환
    return df

def plot_matplotlib():
    st.title("bar plot")
    df = load_data() #데이터준비
    #그래프 그리기
    fig, ax = plt.subplots()
    
    # 막대그래프
>>>>>>> a2fc80b917052043d36ef0a9ff96a01d0148ed5f
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs. lifeExp")
<<<<<<< HEAD
    # 웹 앱 시각화
    st.pyplot(fig)

def main():
    st.title("데이터 시각화 : 표  & 그래프")
    
    df = load_data() # 데이터 불러오기 : 데이터프레임
    st.dataframe(df, use_container_width=True) # 첫번째 표

    #두번째 표
    st.title("컬럼별 최대값 표")
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib() # 그래프
=======
    
    st.pyplot(fig)

def main():
    st.title("데이터 시각화 : 표와 그래프)")
    
    df = load_data() #데이터 불러오기 : 데이터 프레임
    st.dataframe(df, use_container_width=True) #첫번째표

    #두번째 표
    st.title("컬럼별 최대값 표") 
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib() #그래프
>>>>>>> a2fc80b917052043d36ef0a9ff96a01d0148ed5f
    
    
if __name__ == "__main__":
    main()