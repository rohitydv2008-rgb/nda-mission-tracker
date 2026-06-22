import streamlit as st
import datetime

# ऐप की थीम और टाइटिल सेट करना (Military Theme Look)
st.set_page_config(page_title="Mission Khadakwasla", page_icon="🎖️", layout="centered")

# डार्क मिलिट्री लुक के लिए कस्टम CSS स्टाइलिंग
st.markdown("""
    <style>
    .main { background-color: #0B0C10; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #1B2A1C !important; color: #FFD700 !important; border: 2px solid #FFD700 !important; width: 100%; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1F2833 !important; color: #FFFFFF !important; border: 1px solid #45A29E !important; }
    .success-box { padding: 15px; background-color: #1B2A1C; border-left: 5px solid #FFD700; border-radius: 5px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# सेशन स्टेट में लॉगिन चेक करना
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
        if username.lower() == "rohit" and password == "1234":  # आप अपना पासवर्ड बदल सकते हैं
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: Invalid Cadet Credentials!")

# --- 🪖 MAIN DASHBOARD ---
else:
    # वेलकम नोट जो आपने माँगा था
    st.markdown('<div class="success-box"><h3>🎯 Welcome Future Officer, Cadet Rohit! 🫡</h3><p>Status: Active | Base: Ujjain</p></div>', unsafe_allow_html=True)
    
    # ⏳ COUNTDOWN TIMER (13 September 2026)
    exam_date = datetime.date(2026, 9, 13)
    today = datetime.date.today()
    days_left = (exam_date - today).days
    
    st.subheader(# LIVE COUNTDOWN
        f"⏳ MISSION COUNTDOWN: {days_left} DAYS LEFT UNTIL JUNG!"
    )
    st.progress(max(0, min(100, int((1 - (days_left / 100)) * 100)))) # प्रोग्रेस बार
    
    st.write("---")
    
    # 📅 WAR ROOM (YOUR CUSTOM SCHEDULE)
    st.subheader("⚔️ WAR ROOM: DAILY MISSION TARGETS")
    
    # खुद टाइप करके टारगेट डालने वाला इनपुट बॉक्स
    new_mission = st.text_input("Type your next target (e.g., Maths Calculus 50 Qs, English 30 Synonyms):")
    
    if st.button("ADD TO MISSION"):
        if new_mission:
            st.session_state.missions.append({"task": new_mission, "done": False})
            st.rerun()
            
    # आज के टारगेट्स की लिस्ट दिखाना
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
                
    # लॉगआउट बटन
    if st.sidebar.button("LOGOUT FROM BASE"):
        st.session_state.logged_in = False
        st.rerun()
