#%%      文本组件  #%%用于分割代码块##################################
import streamlit as st
print(st.__version__)         # 版本1.9.0

st.title(':tongue:👅文本组件text') # 网页标题
st.header(':ghost:一级标题')       # 一级标题
st.subheader('二级标题')          # 二级标题
st.write('hello')              # 文本内容1
st.text('''                   # 文本内容2
        可以写很多很多东西，这些东西都是随便写，随意的复制都是可以的
        你想写都可以
        ''')
st.markdown(                  # markdown
    '''
    这里的内容和markdown是一样的
    - 比如
    ''')

st.code('print("hello world")')  # 代码格式
st.latex('y= w*x +b ')           # 数学公式
# st.balloons()                  # 动态效果（气球）
# st.snow()                      # 雪花

#%% 数据组件 #######################################################
st.title('数组组件')

import pandas as pd
data = pd.read_csv('app_data/data/titanic_data.csv')
st.dataframe(data)                   # 交互表格
#st.table(data)                      # 静态表格

st.metric('温度','23℃',delta='-2℃') # 温度上升下降显示

col1,col2 = st.columns(2)            # 分为两列显示
with col1:
    st.metric('温度','23℃',delta='-2℃')
with col2:
    st.metric('温度','23℃',delta='2℃')

#%% 图表组件（自带与第三方库）############################################
# 自带
import numpy  as np
data = np.random.random((30,4))
st.line_chart(data)               # 折线图（功能参数较少）
st.area_chart(data)               # 折线面积图
st.bar_chart(data)                # 柱形图
st.map(pd.DataFrame([[23,113]],columns=['lat', 'lon']))  # 广州标记地图
# 第三方库
import matplotlib.pyplot as plt    # matplotlib绘制两图
fig,[ax1,ax2] = plt.subplots(2)    # 定义画布（两个子图）
ax1.plot(data[:,0])
ax1.set_title('test1')
ax2.plot(data[:,1])
ax2.set_title('test2')
plt.subplots_adjust( hspace=0.5)# 子图间距调整

st.pyplot(fig)                    # matplotlib图在前端显示

#%% 多媒体组件（图片、音频、视频）##########################################
# 图片（本地图片或网页图片）
img = plt.imread('app_data/pic/aixin.jpg')
st.image(img)

st.image('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2Ftp05%2F1910021352061916-0-lp.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1660719831&t=710f59a355810fddd28b4cb80f5f2141')

# 音频
with open('app_data/music/稻香-周杰伦.mp3' ,'rb') as f: # rb以二进制形式读取文件
    au = f.read()
st.audio(au)

# 视频
with open('app_data/video/开不了口-广告曲.mp4' ,'rb') as f: # rb以二进制形式读取文件
    au = f.read()
st.video(au)

# 其余输入组件###################
# 1 可选择上传的图像
st.title('输入组件3')
img = st.file_uploader('上传图像')  # 文件上传
st.image(img)                      # 需要上传图像之后，才能去除报错
# st.stop()
# 2 可使用电脑摄像头拍照
st.camera_input('调用电脑摄像头')

# 3 侧边栏
st.sidebar.write('welcome')     # 添加侧边栏

if st.sidebar.button('hello'):  # 添加按钮
    st.write('hello')
if st.sidebar.button('bye'):
    st.write('bye')
    
with open('D:/desktop/体验课/streamlit/Streamlit-杨惠/st_app/video/开不了口-广告曲.mp4' ,'rb') as f: # rb以二进制形式读取文件
    au = f.read()
st.video(au)



