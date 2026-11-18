import streamlit as st

st.set_page_config(
    page_title="Тест на симпатию 💗",
    page_icon="💗",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #351344, #100817 65%);
    color: #ffffff;
}

h1, h2, h3, p, label {
    color: white !important;
}

.hero {
    text-align: center;
    padding: 55px 15px 35px;
}

.hero h1 {
    font-size: 44px;
    color: #ff75c8 !important;
    text-shadow: 0 0 22px #ff4fa3;
}

.hero p {
    font-size: 18px;
    color: #e7c9f5 !important;
}

.stProgress > div > div > div {
    background: linear-gradient(90deg, #ff4fa3, #b45cff);
}

.stRadio > div {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 117, 200, 0.25);
    border-radius: 16px;
    padding: 15px;
}

.stRadio label {
    color: white !important;
}

.stButton > button {
    background: linear-gradient(90deg, #ff4fa3, #a855f7);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 25px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    box-shadow: 0 0 20px #ff4fa3;
    transform: scale(1.02);
}

div[data-testid="stCaptionContainer"] {
    color: #d7b5e9;
}


</style>
""", unsafe_allow_html=True)

questions = [
    "Ты часто думаешь об этом человеке?",
    "Тебе хочется чаще с ним общаться?",
    "Ты радуешься, когда он пишет первым?",
    "Ты замечаешь, когда он находится рядом?",
    "Тебе интересно узнавать о нём новое?",
    "Ты вспоминаешь ваши разговоры?",
    "Тебе хочется проводить с ним больше времени?",
    "Ты улыбаешься, когда видишь его сообщение?",
    "Тебе важно его мнение?",
    "Ты скучаешь, когда долго не общаетесь?",
    "Ты стараешься выглядеть особенно приветливо при встрече?",
    "Тебе интересно, как прошёл его день?",
    "Ты замечаешь его настроение?",
    "Тебе хочется делиться с ним новостями?",
    "Ты иногда представляешь ваше совместное время?",
    "Ты обращаешь внимание на его комплименты?",
    "Тебе приятно получать от него внимание?",
    "Ты хочешь узнать его поближе?",
    "Ты волнуешься перед встречей с ним?",
    "Ты легко можешь забыть о нём на весь день?",
    "Ты ищешь повод начать разговор?",
    "Тебе нравится его чувство юмора?",
    "Ты замечаешь мелочи в его поведении?",
    "Тебе совершенно безразлично, общается ли он с другими?",
    "Ты хочешь чаще видеться с ним?",
    "Тебе приятно слышать его голос?",
    "Ты рассказываешь о нём друзьям?",
    "Ты ждёшь возможности снова пообщаться?",
    "Тебе хочется узнать, нравишься ли ты ему?",
    "Ты чувствуешь, что он для тебя особенный?"
]

answers = [
    "1 — Совсем нет",
    "2 — Скорее нет",
    "3 — Иногда",
    "4 — Скорее да",
    "5 — Определённо да"
]

if "started" not in st.session_state:
    st.session_state.started = False
if "current" not in st.session_state:
    st.session_state.current = 0
if "results" not in st.session_state:
    st.session_state.results = {}

if not st.session_state.started:
    st.markdown("""
    <div class="hero">
        <h1>💗 Тест на симпатию</h1>
        <p>А ты точно знаешь, насколько сильно он тебе нравится?</p>
        <p>30 вопросов помогут разобраться в своих чувствах.</p>
        <p>Отвечай честно. Здесь нет неправильных ответов ✨</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💗 НАЧАТЬ ТЕСТ"):
        st.session_state.started = True
        st.rerun()

else:
    number = st.session_state.current

    if number < len(questions):
        st.title("💗 Тест на симпатию")
        st.progress((number + 1) / len(questions))
        st.caption(f"Вопрос {number + 1} из {len(questions)}")

        st.subheader(questions[number])

        selected = st.radio(
            "Выбери свой ответ:",
            answers,
            index=None,
            key=f"question_{number}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if number > 0:
                if st.button("← Назад"):
                    st.session_state.current -= 1
                    st.rerun()

        with col2:
            if st.button("Далее →"):
                if selected is None:
                    st.warning("Сначала выбери ответ 💗")
                else:
                    st.session_state.results[number] = int(selected[0])
                    st.session_state.current += 1
                    st.rerun()

    else:
        score = sum(st.session_state.results.values())
        percent = round((score - 30) / 120 * 100)

        st.balloons()
        st.balloons()

        st.markdown("""
                <div style="
                    text-align:center;
                    padding:25px;
                    background:linear-gradient(135deg,#351344,#1b0d27);
                    border:1px solid #ff75c8;
                    border-radius:25px;
                    box-shadow:0 0 30px rgba(255,79,163,0.25);
                ">
                    <h1 style="color:#ff75c8 !important;">💖 ТВОЙ РЕЗУЛЬТАТ</h1>
                    <p style="color:#e7c9f5 !important;">
                        Вот что показал твой тест
                    </p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(
            f"""
                    <h1 style="
                        text-align:center;
                        font-size:85px;
                        color:#ff75c8 !important;
                        text-shadow:0 0 25px #ff4fa3;
                    ">{percent}%</h1>
                    """,
            unsafe_allow_html=True
        )

        st.progress(percent / 100)

        if percent < 25:
            st.subheader("✨ Лёгкий интерес")
            st.write("Возможно, тебе просто приятно общаться с этим человеком.")
        elif percent < 50:
            st.subheader("💗 Симпатия зарождается")
            st.write("Кажется, этот человек начинает занимать твои мысли.")
        elif percent < 75:
            st.subheader("💕 Он тебе действительно нравится")
            st.write("Похоже, ты испытываешь к нему особенную симпатию.")
        else:
            st.subheader("💘 Сильная симпатия")
            st.write("Кажется, этот человек действительно тебе небезразличен!")

        st.caption("Это шуточный тест — только ты знаешь свои настоящие чувства.")

        if st.button("💗 Пройти ещё раз"):
            st.session_state.clear()
            st.rerun()
