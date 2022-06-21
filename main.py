import streamlit as st
from moviepy.editor import *
import tempfile
from zipfile import ZipFile
import shutil
import base64


def edit_videos(videos):
    zipObj = ZipFile('videos.zip', 'w')
    with tempfile.TemporaryDirectory() as tmpdirname:
        for video in videos:
            with open(tmpdirname + "/" + video.name, mode='wb') as f:
                f.write(video.read())
                f.close()
            clip = VideoFileClip(tmpdirname + "/" + video.name)
            clip = clip.subclip(0, (clip.duration - 0.3))
            clip = clip.rotate(0.01)
            clip = clip.fx(vfx.colorx, 0.5)
            editedName = "edited-" + video.name.replace(video.name.split('.')[len(video.name.split('.')) - 1], "") + video.name.split('.')[len(video.name.split('.')) - 1]
            clip.write_videofile(tmpdirname + "/" + editedName)
            zipObj.write(tmpdirname + "/" + editedName)
            clip.close()
    zipObj.close()
    with open("videos.zip", 'rb') as c:
        st.sidebar.download_button('Download 📁', c, file_name="videos.zip")




st.title('Bulk Edit')

uploaded_videos = st.sidebar.file_uploader("Upload mp4 file", type=["mp4", "mpeg"], accept_multiple_files=True)
if uploaded_videos is not None:
    st.sidebar.button('Edit ✂️', on_click=edit_videos, args=[uploaded_videos])
