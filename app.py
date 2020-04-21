import streamlit as st

st.markdown('# Welcome to Streamlit :wave:  ')
st.markdown('Below are some helpful resources while you get started. If you have any questions dont hesitate to reach out on our [community forum](https://discuss.streamlit.io/) or at hello@streamlit.io')

st.markdown('### Intro to Streamlit Video Series :tv:')

show_image = st.empty()
if st.checkbox('Check out the four part video series', value=False):
    show_image = st.empty()
    if st.checkbox('Part 1: What is Streamlit', value=False):
        st.markdown("#### Synopsis")
        st.markdown("Part 1 of a short video series of Adrien's presentation at PyData in December. In this episode, he discusses the problem he saw in the machine learning workflow and what Streamlit does to address this.")
        st.video('https://www.youtube.com/watch?v=R2nr1uZ8ffc&t=25s')
        
    show_image = st.empty()
    if st.checkbox('Part 2: Install and play with Streamlit', value=False):
        st.video('https://www.youtube.com/watch?v=sxLNCDnqyFc&t=1s')

    show_image = st.empty()
    if st.checkbox('Part 3: Lets build a data app!', value=False):
        st.video('https://www.youtube.com/watch?v=VtrFjkSGgKM&list=PLgkF0qak9G49QlteBtxUIPapT8TzfPuB8&index=1')

    show_image = st.empty()
    if st.checkbox('Part 4: Self-driving use-case', value=False):
        st.video('https://www.youtube.com/watch?v=z8vgmvtgxCs&list=PLgkF0qak9G49QlteBtxUIPapT8TzfPuB8&index=4')

st.markdown('### Streamlit written articles :newspaper:')
show_image = st.empty()
if st.checkbox('Check out our articles', value=False):
    show_image = st.empty()
    if st.checkbox('Turn Python Scripts into Beautiful ML Tools', value=False):
        st.image('https://raw.githubusercontent.com/streamlit/demo-self-driving/master/av_final_optimized.gif')
        st.markdown('[Turn Python Scripts into Beautiful ML Tools](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)')
        
