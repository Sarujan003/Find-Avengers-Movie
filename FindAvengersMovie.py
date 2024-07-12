import streamlit as st
import pandas as pd

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center>-Find Avengers movies-</h2>
    </div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)
    data = pd.read_csv('movie.csv',index_col='title')
    p1 = st.text_input("Search the movie name")
    p1 = p1.strip()

    ls = []
    if st.button("Search"):
        for title in data.index:
            if p1.lower() in title:
                ls.append(title)

        if len(ls)==0:
            st.write(f"No matches found")
            
        else:
            st.write(f"Total matches: {len(ls)}")
            for title in ls:
                col1, col2 = st.columns([1, 3])  # Adjust the column widths as needed

                with col1:
                    st.image(data.loc[title]['photo_path'])

                with col2:
                    st.write(f"Title: {title.capitalize()}")
                    st.write(f"Description: {data.loc[title]['description']}")
                    st.write(f"Year: {data.loc[title]['year']}")
                    st.write(f"IMDb Rating: {data.loc[title]['imdb_rating']}")
                    st.write(f" ")
                    
if __name__ == '__main__':
    main()