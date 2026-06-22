import streamlit as st
import datetime

# ऐप की थीम और टाइटिल सेट करना (Military Theme Look)
st.set_page_config(page_title="Mission Khadakwasla", page_icon="🎖️", layout="centered")

# डार्क मिलिट्री लुक और बैकग्राउंड में भारतीय ध्वज (Indian Flag Watermark) के लिए कस्टम CSS
st.markdown("""
    <style>
    .main { 
        background-image: linear-gradient(rgba(11, 12, 16, 0.85), rgba(11, 12, 16, 0.85)), 
                          url('https://images.unsplash.com/photo-1532375810709-75b1da00537c?q=80&w=1000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #FFFFFF; 
    }
    h1, h2, h3 { color: #FFD700 !important; font-family: 'Courier New', Courier, monospace; text-shadow: 2px 2px 4px #000000; }
    .stButton>button { background-color: #1B2A1C !important; color: #FFD700 !important; border: 2px solid #FFD700 !important; width: 100%; font-weight: bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.5); }
    .stTextInput>div>div>input { background-color: #1F2833 !important; color: #FFFFFF !important; border: 1px solid #45A29E !important; }
    .success-box { padding: 15px; background-color: rgba(27, 42, 28, 0.9); border-left: 5px solid #FFD700; border-radius: 5px; margin-bottom: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5); }
    .time-table-box { padding: 10px; background-color: rgba(31, 40, 51, 0.9); border: 1px dashed #FFD700; border-radius: 5px; margin-bottom: 10px; }
    .cadet-name { font-size: 28px; font-weight: 900; color: #FFD700; text-align: center; letter-spacing: 2px; text-shadow: 3px 3px 6px #000000; margin-top: -10px; margin-bottom: 20px; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# सेशन स्टेट में लॉगिन और डेटा चेक करना
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'missions' not in st.session_state:
    st.session_state.missions = []

# --- 🛡️ LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("🎖️ COMMAND CENTER LOGIN")
    st.subheader("NDA TRACKER - MISSION 2026")
    
    username = st.text_input("ENTER CADET ID")
    password = st.text_input("ENTER SECURITY CODE", type="password")
    
    if st.button("ENTER BASE"):
        if username.lower() == "rohit" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: Invalid Cadet Credentials!")

# --- 🪖 MAIN DASHBOARD ---
else:
    # वेलकम नोट
    st.markdown('<div class="success-box"><h3>🎯 Welcome Future Officer! 🫡</h3><p>Status: Active | Base: Ujjain</p></div>', unsafe_allow_html=True)
    
    # 🇮🇳 तिरंगे के नीचे आपका नाम बोल्ड और तगड़े लुक में
    st.markdown('<div class="cadet-name">⚡ ROHIT YADAV ⚡</div>', unsafe_allow_html=True)
    
    # ⏳ COUNTDOWN TIMER (13 September 2026)
    exam_date = datetime.date(2026, 9, 13)
    today = datetime.date.today()
    days_left = (exam_date - today).days
    
    st.subheader(f"⏳ MISSION COUNTDOWN: {days_left} DAYS LEFT UNTIL JUNG!")
    st.progress(max(0, min(100, int((1 - (days_left / 100)) * 100))))
    
    st.write("---")
    
    # 🕒 🛡️ DAILY TIME TABLE SECTION
    st.subheader("📅 DAILY ROUTINE (COMMAND ORDERS)")
    
    with st.expander("👁️ CLICK TO VIEW YOUR DAILY TIME TABLE", expanded=True):
        st.markdown("""
        <div class="time-table-box">⏰ <b>04:30 AM - 06:00 AM :</b> Physical Training / Running 🏃‍♂️</div>
        <div class="time-table-box">⏰ <b>06:30 AM - 09:00 AM :</b> Mathematics (Session 1) 📐</div>
        <div class="time-table-box">⏰ <b>09:30 AM - 12:00 PM :</b> English (Grammar & Vocab) 📖</div>
        <div class="time-table-box">⏰ <b>01:00 PM - 03:30 PM :</b> General Studies (History/Geography) 🌍</div>
        <div class="time-table-box">⏰ <b>04:00 PM - 05:30 PM :</b> Revision / Science (Physics/Chemistry) 🧪</div>
        <div class="time-table-box">⏰ <b>07:00 PM - 09:00 PM :</b> Mock Test / Previous Year Questions 📝</div>
        <div class="time-table-box">⏰ <b>09:30 PM :</b> Lights Out / Sleep 😴</div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    
    # 📅 WAR ROOM (YOUR CUSTOM SCHEDULE)
    st.subheader("⚔️ WAR ROOM: DAILY MISSION TARGETS")
    
    new_mission = st.text_input("Type your next target (e.g., Maths Calculus 50 Qs, English 30 Synonyms):")
    
    if st.button("ADD TO MISSION"):
        if new_mission:
            st.session_state.missions.append({"task": new_mission, "done": False})
            st.rerun()
            
    st.write("### Today's Briefing:")
    if not st.session_state.missions:
        st.info("No missions assigned for today. Add a target above, Cadet!")
    else:
        for i, m in enumerate(st.session_state.missions):
            cols = st.columns([0.8, 0.2])
            if not m["done"]:
                cols[0].write(f"⬜ {m['task']}")
                if cols[1].button("Neutralize", key=f"btn_{i}"):
                    st.session_state.missions[i]["done"] = True
                    st.success(f"Target Neutralized: {m['task']}! 🔥")
                    st.rerun()
            else:
                cols[0].write(f"✅ ~~{m['task']}~~ (Target Destroyed)")
                
    if st.sidebar.button("LOGOUT FROM BASE"):
        st.session_state.logged_in = False
        st.rerun()
