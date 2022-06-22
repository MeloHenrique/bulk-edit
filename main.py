import streamlit as st
from moviepy.editor import *
import random
from zipfile import ZipFile


def edit_videos(videos):
    e = random.randint(0, 9999)
    print(str(e))
    zipObj = ZipFile('videos'+str(e)+'.zip', 'w')
    for video in videos:
        with open(video.name, mode='wb') as f:
            f.write(video.read())
            f.close()
        clip = VideoFileClip(video.name)
        clip = clip.subclip(0, (clip.duration - 0.3))
        clip = clip.rotate(0.01)
        clip = clip.fx(vfx.colorx, 0.99)
        editedName = "edited-" + video.name.replace(video.name.split('.')[len(video.name.split('.')) - 1], "") + \
                     video.name.split('.')[len(video.name.split('.')) - 1]
        clip.write_videofile(editedName)
        zipObj.write(editedName)
        clip.close()
    zipObj.close()
    with open('videos'+str(e)+'.zip', 'rb') as c:
        st.sidebar.download_button('Download 📁', c, file_name='videos'+str(e)+'.zip')


st.title('Bulk Edit')

video_file = open('tutorial.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

uploaded_videos = st.sidebar.file_uploader("Upload mp4 file", type=["mp4", "mpeg"], accept_multiple_files=True)
if uploaded_videos is not None:
    st.sidebar.button('Edit ✂️', on_click=edit_videos, args=[uploaded_videos])
