import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

# ====== ✅ 한글 폰트 설정 (Linux 환경 기준) ======
mpl.rcParams['font.family'] = 'DejaVu Sans'  # Streamlit Cloud에서도 안전하게 보이는 폰트

# ====== 🧠 지질 시대 데이터 (시간 순) ======
periods = [
    ("캄브리아기", 541, 485),
    ("오르도비스기", 485, 444),
    ("실루리아기", 444, 419),
    ("데본기", 419, 359),
    ("석탄기", 359, 299),
    ("페름기", 299, 252),
    ("트라이아스기", 252, 201),
    ("쥐라기", 201, 145),
    ("백악기", 145, 66),
    ("팔레오기", 66, 23),
    ("네오기", 23, 2.6),
    ("제4기", 2.6, 0)
]

# 대별 색상
period_colors = {
    "고생대": "#a6cee3",
    "중생대": "#fb9a99",
    "신생대": "#b2df8a"
}

# 각 기의 지속 시간, 이름, 색상 계산
durations = [start - end for _, start, end in periods]
labels = [name for name, _, _ in periods]
colors = []

for name, start, end in periods:
    if start > 252:
        colors.append(period_colors["고생대"])
    elif start > 66:
        colors.append(period_colors["중생대"])
    else:
        colors.append(period_colors["신생대"])

# ====== 🌀 시계형 원 그래프 그리기 함수 ======
def draw_clock():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    total_duration = sum(durations)
    angles = [d / total_duration * 360 for d in durations]
    
    start_angle = 90
    theta = [start_angle]
    for angle in angles[:-1]:
        theta.append(theta[-1] - angle)
    
    theta_rad = [t * (3.14159 / 180) for t in theta]
    bars = ax.bar(
        x=theta_rad,
        height=[1] * len(angles),
        width=[a * (3.14159 / 180) for a in angles],
        bottom=0,
        color=colors,
        edgecolor='black',  # 경계선은 얇고 검정색
        linewidth=0.5
    )
    
    # 한글 라벨 표시
    for i, bar in enumerate(bars):
        angle_deg = theta[i] - angles[i]/2
        angle_rad = angle_deg * (3.14159 / 180)
        rotation = angle_deg + 90 if angle_deg < 90 or angle_deg > 270 else angle_deg - 90
        ax.text(
            x=angle_rad,
            y=1.1,
            s=labels[i],
            ha='center',
            va='center',
            rotation=rotation,
            rotation_mode='anchor',
            fontsize=9
        )
    
    ax.set_title("🕰️ 현생누대 지질 시계", va='bottom', fontsize=15)
    ax.set_axis_off()
    st.pyplot(fig)

# ====== 🎨 Streamlit 인터페이스 ======
st.set_page_config(layout="centered")
st.title("🕰️ 현생누대 지질 시계")
st.markdown("12개의 지질 기(period)를 시간 비율에 따라 원형 시계 형태로 시각화한 그래프입니다.")
draw_clock()
