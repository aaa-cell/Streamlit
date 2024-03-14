import streamlit as st
import pandas as pd

# 通过不同的输入组件获取用户的个人信息
st.set_page_config(page_title='获取用户的个人信息', page_icon='🍦')    # 修改网页名称，图标等
st.title('收集用户的个人信息')            # 添加标题

with st.form('report'):     # 构建为表单（例如：登录），后面连接提交按钮
    name = st.text_input("姓名:")
    age = st.number_input('年龄', min_value=0, max_value=120, format='%d')
    gender = st.selectbox("性别:", ["男", "女"])
    # 所有城市选项
    cities = ["北京", "上海", "广州", "深圳", "杭州", "成都", "重庆", "武汉", "南京", "西安","其他"]
    city = st.selectbox("城市:", cities)
    if city == "其他":
        city = st.text_input('请输入其他城市:')
    email = st.text_input("邮箱:")
    phone = st.text_input("电话:", max_chars=11)
    # 检查电话号码是否为11位数
    if len(phone) != 11:
        st.error("请输入11位数的电话号码")
    else:
        st.write(f"电话: {phone}")

    ######################
    res = [[name, age, gender, city, email, phone]]                      # 将填写的内容保存至此

    if st.form_submit_button('提交问卷'):  # 提交按钮（一般添加判断）
    # 检查必填字段是否都已填写
        if not all([name, phone, email]):
            st.error("请填写所有必填字段")
        data = pd.DataFrame(res, columns=['name', 'age', 'gender', 'city', 'email', 'phone']) # 提交后，数据存放至数据框
        #st.dataframe(data)               # 可展示
        data.to_csv('report_result.csv', encoding='utf-8-sig', mode='a')  # mode='a'追加，保存至本地
        st.write('感谢您的参与！')          # 点击提交后，输出此内容
        st.balloons()                    # 以及气球
    
        with st.expander('是否查看数据'):   # 数据展开组件：是否展开数据
            st.dataframe(data)
