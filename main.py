# 导入区
import streamlit as st
from PIL import Image
import base64

# 页面配置
st.set_page_config(
    page_title="劳肖的个人空间",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* 整体风格 - 增添棱角感 */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
    }
    
    /* 主容器样式 */
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* 侧边栏样式 - 棱角设计 */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #2c3e50 0%, #4a6491 100%);
        padding: 1.5rem 1rem;
        box-shadow: 3px 0 10px rgba(0,0,0,0.1);
        color: white !important; /* 确保所有文本为白色 */
    }
    
    /* 确保侧边栏中的所有文本为白色 */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* 侧边栏标题样式 */
    .sidebar-title {
        text-align: center;
        font-size: 1.8rem !important;
        margin-bottom: 1.5rem;
        color: white !important;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* 确保单选按钮标签为白色 */
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* 确保页脚文本为白色 */
    [data-testid="stSidebar"] .footer {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    
    /* 确保导航菜单文本为白色 */
    .stRadio [role="radiogroup"] label {
        color: white !important;
    }
    
    /* 确保单选按钮选中状态文本为白色 */
    .stRadio [role="radiogroup"] [aria-checked="true"] + label {
        color: white !important;
        font-weight: bold;
    }
    
    /* 确保单选按钮悬停状态 */
    .stRadio [role="radiogroup"] label:hover {
        color: #f0f0f0 !important;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    /* 按钮样式 - 棱角设计 */
    .stButton>button {
        background: linear-gradient(to right, #3498db, #2980b9);
        color: white;
        border-radius: 4px; /* 减小圆角 */
        border: none;
        padding: 0.7rem 1.2rem;
        transition: all 0.3s;
        width: 100%;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* 卡片样式 - 棱角设计 */
    .card {
        background: white;
        border-radius: 6px; /* 减小圆角 */
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        padding: 1.8rem;
        margin-bottom: 1.8rem;
        border-left: 4px solid #3498db;
        transition: transform 0.3s;
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* 头像样式 - 圆形设计 */
    .avatar {
        border-radius: 50%;
        border: 4px solid white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        object-fit: cover;
        width: 200px;
        height: 200px;
        margin: 0 auto;
        display: block;
    }
    
    .sidebar-avatar {
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        object-fit: cover;
        width: 100px;
        height: 100px;
        margin: 0 auto 1rem;
        display: block;
    }
    
    /* 页脚样式 */
    .footer {
        text-align: center;
        padding: 1.5rem;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 2.5rem;
        border-top: 1px solid #dee2e6;
    }
    
    /* 选项卡样式 - 棱角设计 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px !important; /* 减小圆角 */
        padding: 0.8rem 1.2rem;
        margin: 0 2px !important;
        background-color: #e9ecef !important;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3498db !important;
        color: white !important;
        font-weight: 600;
    }
    
    /* 标题样式 */
    h1 {
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
        color: #2c3e50;
    }
    
    h2 {
        color: #34495e;
        margin-top: 1.8rem;
    }
    
    /* 分隔线样式 */
    hr {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, rgba(52, 152, 219, 0.1), rgba(52, 152, 219, 0.5), rgba(52, 152, 219, 0.1));
        margin: 1.8rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 函数区
def page1():
    """基本信息页面"""
    st.title("👤 基本信息")
    
    # 使用两列布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 头像显示 - 圆形设计
        try:
            st.markdown('<img src="data:image/jpeg;base64,{}" class="avatar">'.format(
                base64.b64encode(open("tx.jpg", "rb").read()).decode()
            ), unsafe_allow_html=True)
        except:
            st.image("tx.jpg", width=200, caption="个人头像")
    
    with col2:
        # 信息卡片
        st.markdown("""
        <div class="card">
            <h3>劳肖 (Lao Xiao)</h3>
            <p>🎮 游戏爱好者 | ✨ 创意达人</p>
            <hr style="margin: 1rem 0; border-top: 1px solid #eee;">
            <p>👤 <b>性别:</b> 中性</p>
            <p>❤️ <b>爱好:</b> 游戏开发 & 视频创作</p>
            <p>🎮 <b>擅长游戏:</b></p>
            <ul>
                <li>Minecraft - PVP大师</li>
                <li>蛋仔派对 - 竞技高手</li>
                <li>Plant VS Zombie - 策略专家</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # 分隔线
    st.divider()
    
    # 游戏成就展示
    st.subheader("🎮 游戏成就")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 1rem; border-left-color: #e74c3c;">
            <h4>Minecraft</h4>
            <p style="font-size: 1.8rem; font-weight: bold; margin: 0.5rem 0; color: #2c3e50;">91+小时</p>
            <p style="color: #7f8c8d;">国服PVP第91名</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 1rem; border-left-color: #9b59b6;">
            <h4>蛋仔派对</h4>
            <p style="font-size: 1.8rem; font-weight: bold; margin: 0.5rem 0; color: #2c3e50;">传奇段位</p>
            <p style="color: #7f8c8d;">Top 91玩家</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 1rem; border-left-color: #f39c12;">
            <h4>PVZ</h4>
            <p style="font-size: 1.8rem; font-weight: bold; margin: 0.5rem 0; color: #2c3e50;">91关</p>
            <p style="color: #7f8c8d;">无尽模式</p>
        </div>
        """, unsafe_allow_html=True)

def page2():
    """视频作品页面"""
    st.title("🎬 视频作品")
    
    # 视频1
    with st.expander("🔥 优质作品：牢大最超模的专属卡", expanded=True):
        col_vid1, col_desc1 = st.columns([3, 2])
        with col_vid1:
            st.video('牢大最超模的专属卡.mp4')
        with col_desc1:
            st.markdown("""
            <div class="card" style="height: 100%;">
                <h4>视频信息</h4>
                <p>📅 发布于2025年6月</p>
                <p>👁️ 播放量：6362</p>
                <p>👍 点赞：115</p>
                <p>💬 评论：13条</p>
                <hr style="margin: 0.8rem 0;">
                <p>创意十足的卡牌设计，展现独特的游戏理解！</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # 视频2
    with st.expander("😄 搞笑作品：孩子们我太厉害了", expanded=True):
        col_vid2, col_desc2 = st.columns([3, 2])
        with col_vid2:
            st.video('孩子们我没救了.mp4')
        with col_desc2:
            st.markdown("""
            <div class="card" style="height: 100%;">
                <h4>视频信息</h4>
                <p>📅 发布于2025年6月</p>
                <p>👁️ 播放量：611</p>
                <p>👍 点赞：11</p>
                <p>💬 评论：1条</p>
                <hr style="margin: 0.8rem 0;">
                <p>欢乐的游戏瞬间，展现幽默的游戏风格！</p>
            </div>
            """, unsafe_allow_html=True)
    
    # 更多视频占位
    st.divider()
    st.subheader("📺 更多精彩作品")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%); 
                border-radius: 12px; 
                padding: 25px; 
                text-align: center;
                margin: 20px 0;">
        <h4 style="color: #1a73e8; margin-bottom: 15px;">🚀 更多创意内容尽在B站主页</h4>
        <p style="margin-bottom: 20px;">定期更新游戏攻略、搞笑集锦和创意设计</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button(
        '👉 访问我的Bilibili主页', 
        'https://space.bilibili.com/1425010870?spm_id_from=333.1365.0.0',
        use_container_width=True,
        type="primary",
        help="点击跳转到B站主页"
    )
    
    st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

def page3():
    """推荐视频页面"""
    st.divider()
    st.subheader("推荐作品")
    st.info("🌟 正在开发中哦……,敬请期待！", icon="📺")

def page4():
    """小工具页面"""
    st.title("🔧小工具")
    st.write(" ")
    st.write(" ")
    st.title("🎨 阴间换色小程序")
    st.markdown("上传图片，体验独特的色彩变换效果！")
    
    # 上传区域
    with st.container():
        uploaded_file = st.file_uploader('📤 上传图片 (PNG, JPG, JPEG)', type=['png', 'jpeg', 'jpg'])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # 效果说明
        st.info("💡 小提示：三种效果分别对应不同的RGB通道变换", icon="ℹ️")
        
        # 使用选项卡展示效果
        tab1, tab2, tab3 , tab4 = st.tabs(['效果一：幻影紫', '效果二：深海蓝', '效果三：熔岩红','效果四：反色'])
        
        with tab1:
            st.subheader("紫色幻影效果")
            st.image(img_change(img, 0, 2, 1), use_column_width=True)
            st.markdown("""
            <div class="card">
                <h4>效果说明</h4>
                <p>红色和蓝色通道交换，产生神秘紫色调</p>
                <p>适用场景：梦幻场景、夜间氛围</p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.subheader("深海蓝调效果")
            st.image(img_change(img, 1, 0, 2), use_column_width=True)
            st.markdown("""
            <div class="card">
                <h4>效果说明</h4>
                <p>绿色和红色通道交换，呈现深海蓝色</p>
                <p>适用场景：水下世界、冷色调场景</p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.subheader("熔岩炽热效果")
            st.image(img_change(img, 2, 0, 1), use_column_width=True)
            st.markdown("""
            <div class="card">
                <h4>效果说明</h4>
                <p>蓝色和绿色通道交换，创造炽热熔岩感</p>
                <p>适用场景：火焰场景、暖色调氛围</p>
            </div>
            """, unsafe_allow_html=True)
            
        with tab4:
            st.subheader("反色效果")
            width, height = img.size
            img_array = img.load()
            
            for x in range(width):
                for y in range(height):
                    pixel = img_array[x, y]
                    r = 255 - pixel[0]
                    g = 255 - pixel[1]
                    b = 255 - pixel[2]
                    if len(pixel) == 4:
                        a = pixel[3]
                        img_array[x, y] = (r, g, b, a)
                    else:
                        img_array[x, y] = (r, g, b)
            
            st.image(img,use_column_width=True)
            st.markdown("""
            <div class="card">
                <h4>效果说明</h4>
                <p>将图像颜色进行数学反相：每个像素的RGB值被转换为(255 - R, 255 - G, 255 - B)</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("请上传图片以体验换色效果", icon="⚠️")
        
    st.divider() 
    
    #智慧词典
    st.title("📖智能词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    words_dist = {}
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    for i in words_list:
        words_dist[i[1]] = [int(i[0]),i[2]]
        
        
    st.markdown("""
        <style>
            div.stTextInput > div > div > input {
                border: 2px solid #4CAF50 !important;
                border-radius: 5px !important;
                padding: 8px !important;
            }
            div.stTextInput > div > div > input:hover {
                border-color: #FF9800 !important;
                box-shadow: 0 0 5px rgba(255, 152, 0, 0.5);
            }
            div.stTextInput > div > div > input:focus {
                border-color: #9C27B0 !important;
                outline: none;
                box-shadow: 0 0 8px rgba(156, 39, 176, 0.6);
            }
        </style>
        """, unsafe_allow_html=True)
    
    word = st.text_input("请输入要查询的单词")
    if word in words_dist:
        st.write(words_dist[word])
        if word == 'snow':
            st.snow()
        if word == "balloon":
            st.balloons()
        if word == "python":    
            st.title("🐍")
            st.code('''#恭喜你触发彩蛋，这是网站部分源码：
                    def img_change(img, rc, gc, bc):
                    """处理图片颜色通道"""
                    width, height = img.size
                    img_array = img.load()
                    for x in range(width):
                        for y in range(height):
                            r = img_array[x, y][rc]
                            g = img_array[x, y][gc]
                            b = img_array[x, y][bc]
                            img_array[x, y] = (r, g, b)
                    return img''')
    elif len(word) >= 1 and word not in words_dist:
        st.write("😭没有找到该单词")
    if word == "傻逼作者":
        st.write("草泥马")

def page5():
    """联系我页面"""
    st.title("📱 联系我")
    # 使用卡片布局联系方式
    st.markdown("""
    <div class="card">
        <h3 style="text-align:center; margin-bottom: 1.5rem;">📬 联系方式</h3>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="text-align: center; padding: 1rem; width: 30%; min-width: 150px;">
                <div style="background: #3498db; color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 2rem;">💬</div>
                <h4 style="margin: 1rem 0 0.5rem;">微信</h4>
                <p style="font-weight: bold; font-size: 1.1rem; margin: 0;">Xwq3069</p>
            </div>
            <div style="text-align: center; padding: 1rem; width: 30%; min-width: 150px;">
                <div style="background: #9b59b6; color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 2rem;">👾</div>
                <h4 style="margin: 1rem 0 0.5rem;">QQ</h4>
                <p style="font-weight: bold; font-size: 1.1rem; margin: 0;">306975244</p>
            </div>
            <div style="text-align: center; padding: 1rem; width: 30%; min-width: 150px;">
                <div style="background: #e74c3c; color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 2rem;">✉️</div>
                <h4 style="margin: 1rem 0 0.5rem;">Email</h4>
                <p style="font-weight: bold; font-size: 1.1rem; margin: 0;">306975244@qq.com</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 联系表单
    st.divider()
    st.subheader("📨 发送消息")
    #打开文件
    
    with open("leave_messages.txt",'r',encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("您的姓名", placeholder="请输入您的姓名")
        contact = st.text_input("联系方式", placeholder="微信/QQ/电话")
        message = st.text_area("留言内容", height=150, placeholder="请输入您的留言内容...")
        
        submitted = st.form_submit_button("📤 发送消息")
        if submitted:
            if name and message:
                st.success("✅ 消息已发送！我会尽快回复您。")
                st.balloons()
                messages_list.append([str(int(messages_list[-1][0])+1),name,contact,message])
                with open("leave_messages.txt","w",encoding="utf-8") as f:
                    message = ""
                    for i in messages_list:
                        message += i[0] + "#" + i[1] + "#" + i[2] + "#" + i[3] + "\n"
                    message = message[:-1]
                    f.write(message)
                
            else:
                st.warning("⚠️ 请填写姓名和留言内容")

def img_change(img, rc, gc, bc):
    """处理图片颜色通道"""
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

# 框架
st.sidebar.markdown("<h1 class='sidebar-title'>✨ 劳肖的个人空间</h1>", unsafe_allow_html=True)

# 添加头像到侧边栏 - 圆形设计
try:
    st.sidebar.markdown('<img src="data:image/jpeg;base64,{}" class="sidebar-avatar">'.format(
        base64.b64encode(open("tx.jpg", "rb").read()).decode()
    ), unsafe_allow_html=True)
except:
    st.sidebar.image("tx.jpg", width=100, caption="你好！我是劳肖")

# 侧边栏导航
page = st.sidebar.radio("导航菜单", 
                       ['基本信息', '视频作品', '推荐视频', '小工具', '联系我'],
                       index=0)

# 侧边栏分隔线
st.sidebar.divider()

# 侧边页脚
st.sidebar.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.7); font-size: 0.85rem; margin-top: 2rem;">
    <p>© 2025 劳肖的个人空间</p>
    <p>用 91创作 | ✨ 保持热爱</p>
</div>
""", unsafe_allow_html=True)

# 页面路由
if page == '基本信息':
    page1()
elif page == '视频作品':
    page2()
elif page == '推荐视频':
    page3()
elif page == "小工具":
    page4()
elif page == '联系我':
    page5()

# 页脚
st.markdown("""
<div class="footer">
    <p>© 2025 劳肖的个人空间 | 用 91 创作 | ✨ 保持热爱</p>
</div>
""", unsafe_allow_html=True)