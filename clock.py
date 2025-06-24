import streamlit as st
import matplotlib.pyplot as plt

# 지질 시대 데이터
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

durations = [start - end for _, start, end in periods]
total_duration = sum(durations)
angles = [d / total_duration * 360 for d in durations]

colors = [
    "#a6cee3", "#a6cee3", "#a6cee3", "#a6cee3", "#a6cee3", "#a6cee3",
    "#fb9a99", "#fb9a99", "#fb9a99",
    "#b2df8a", "#b2df8a", "#b2df8a"
]
labels = [name for name, _, _ in periods]

def draw_clock():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
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
        edgecolor='white'
    )
    for i, bar in enumerate(bars):
        angle_deg = theta[i] - angles[i]/2
        angle_rad = angle_deg * (3.14159 / 180)
        ax.text(
            x=angle_rad,
            y=1.1,
            s=labels[i],
            ha='center',
            va='center',
            rotation=angle_deg - 90 if angle_deg > 180 else angle_deg + 90,
            rotation_mode='anchor',
            fontsize=9
        )
    ax.set_title("현생누대 지질 시계 (Phanerozoic Eon Clock)", va='bottom', fontsize=14)
    ax.set_axis_off()
    st.pyplot(fig)

# Streamlit 인터페이스
st.title("🕰️ 현생누대 지질 시계")
st.markdown("고생대-중생대-신생대를 12개의 기(Period)로 나눈 지질 시계를 시간 비율에 맞게 시각화합니다.")
draw_clock()
