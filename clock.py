import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

# ✅ 한글 폰트 설정 (Streamlit Cloud에서도 보이는 기본 글꼴 사용)
mpl.rcParams['font.family'] = 'NanumGothic'  # 혹은 'Malgun Gothic' (로컬)

# ====== 지질 시대 데이터 (시간순 정렬) ======
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

# 색상 매핑
colors = []
for name, start, end in periods:
    if start > 252:
        colors.append("#a6cee3")  # 고생대
    elif start > 66:
        colors.append("#fb9a99")  # 중생대
    else:
        colors.append("#b2df8a")  # 신생대

# 각 기간 지속 시간 및 전체 합산
durations = [start - end for _, start, end in periods]
total_duration = sum(durations)
angles = [d / total_duration * 360 for d in durations]
labels = [name for name, _, _ in periods]

# ====== 시계형 원 그래프 함수 ======
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
        edgecolor='black',
        linewidth=0.5
    )

    for i, bar in enumerate(bars):
        angle_deg = theta[i] - angles[i] / 2
        angle_rad = angle_deg * (3.14159 / 180)
        rotation = angle_deg + 90 if angle_deg < 90 or angle_deg > 270 else angle_deg - 90
        ax.text(
            x=angle_rad,
            y=1.05,
            s=labels[i],
            ha='center',
            va='center',
            rotation=rotation,
            rotation_mode='anchor',
            fontsize=9
        )

    ax.set_title("🕰️ 현생누대 지질 시계", va='bottom', fontsize=16)
    ax.set_axis_off()
    st.pyplot(fig)

# ====== Streamlit 앱 UI ======
st.set_page_config(layout="centered")
st.title("🕰️ 현생누대 지질 시계")
st.markdown("각 지질 기(period)를 시간 비율에 따라 원형으로 시각화한 그래프입니다.")
draw_clock()
