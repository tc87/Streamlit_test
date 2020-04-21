import streamlit as st

st.markdown('# Welcome to Streamlit :wave:  ')
st.markdown("Below are some helpful resources while you get started. If you have any questions don't hesitate to reach out on our [community forum](https://discuss.streamlit.io/)!")

st.markdown('### - Intro to Streamlit video series :tv:')

st.empty()
if st.checkbox('Check out the four part video series', value=False):
    st.empty()
    if st.checkbox('Part 1: What is Streamlit', value=False):
        st.markdown("#### Synopsis")
        st.markdown("Part 1 of a short video series of Adrien's presentation at PyData in December. In this episode, he discusses the problem he saw in the machine learning workflow and what Streamlit does to address this.")
        st.video('https://www.youtube.com/watch?v=R2nr1uZ8ffc&t=25s')
        
    st.empty()
    if st.checkbox('Part 2: Install and play with Streamlit', value=False):
        st.video('https://www.youtube.com/watch?v=sxLNCDnqyFc&t=1s')

    st.empty()
    if st.checkbox('Part 3: Lets build a data app!', value=False):
        st.video('https://www.youtube.com/watch?v=VtrFjkSGgKM&list=PLgkF0qak9G49QlteBtxUIPapT8TzfPuB8&index=1')

    st.empty()
    if st.checkbox('Part 4: Self-driving use-case', value=False):
        st.video('https://www.youtube.com/watch?v=z8vgmvtgxCs&list=PLgkF0qak9G49QlteBtxUIPapT8TzfPuB8&index=4')

st.markdown('### - Streamlit written articles :newspaper:')
st.empty()
if st.checkbox('Check out our articles', value=False):
    st.empty()
    if st.checkbox('Turn Python Scripts into Beautiful ML Tools', value=False):
        st.markdown('🐍[Introducing Streamlit, an app framework built for ML engineers](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)')
        st.image('https://raw.githubusercontent.com/streamlit/demo-self-driving/master/av_final_optimized.gif')
    st.empty()
    if st.checkbox('Build an app to generate photorealistic faces using TensorFlow and Streamlit', value=False):
        st.markdown('👤[We’ll show you how to quickly build a Streamlit app to synthesize celebrity faces using GANs, Tensorflow, and st.cache.](https://medium.com/p/build-an-app-to-synthesize-photorealistic-faces-using-tensorflow-and-streamlit-dd2545828021?source=email-39dfc90d7a34--writer.postDistributed&sk=f0e8b46538383d501f34b0369e868d50)')
        st.image('https://github.com/streamlit/demo-face-gan/blob/master/GAN-demo.gif?raw=true')  

st.markdown('### - Streamlit links :link:')    
st.empty()
if st.checkbox('Documentation', value=False):
    st.markdown("* 📄 [Official documentation](https://docs.streamlit.io/): learn how to use Streamlit and browser our API. We also have suggestions for installing Streamlit in a virtual environment in Windows, Mac, and Linux")
    st.markdown("* 👷‍♀️ [Contributing](https://github.com/streamlit/streamlit/wiki/Contributing): learn about how to contribute to Streamlit")
    st.markdown("* 🗺 [Roadmap](https://github.com/streamlit/streamlit/wiki/Roadmap): check out what what we're planning on releasing next")

st.empty()
if st.checkbox('Questions, answers, discussion', value=False):
    st.markdown("* 🔮 [FAQ](https://github.com/streamlit/streamlit/wiki/FAQ): answers to the most common questions we hear")
    st.markdown("* 💪 [Community resources](https://github.com/streamlit/streamlit/wiki/Community-Resources): articles, videos, etc, created by the community to help others get things done with Streamlit")
    st.markdown("* 💬 [Discussion Forum](https://discuss.streamlit.io): If the answer is not in the FAQ or Community Resource section, ask a question at on our forum!")

st.empty()
if st.checkbox('Installing in a virtual environment', value=False):
    st.markdown("* 🏠[Windows](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-windows) instructions")
    st.markdown("* 🍎[Mac and Linux](https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment#on-mac--linux) instructions ")
