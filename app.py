from flask import Flask, request, render_template_string
import webbrowser
import threading

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta name="description"
      content="MIP Salawag Altar Servers - Learn, Pray, Serve and Grow.">

<meta name="theme-color" content="#67248d">

<title>MIP Salawag Altar Servers</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    scroll-behavior: smooth;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f7f0fb;
    color: #302039;
    line-height: 1.7;
}

nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: white;
    padding: 14px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    box-shadow: 0 3px 15px rgba(0,0,0,.15);
}

.logo {
    color: #69278f;
    font-size: 20px;
    font-weight: bold;
    white-space: nowrap;
}

.nav-links {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
}

.nav-links a {
    text-decoration: none;
    color: #54206f;
    font-weight: bold;
    transition: .2s;
}

.nav-links a:hover {
    color: #b14bd3;
}

select {
    padding: 8px 10px;
    border-radius: 8px;
    border: 1px solid #a875bd;
    background: white;
    cursor: pointer;
}

.hero {
    min-height: 680px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;

    background:
        linear-gradient(
            rgba(54,12,76,.84),
            rgba(118,40,151,.91)
        ),
        url("https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/3.jpg");

    background-size: cover;
    background-position: center;
}

.hero-content {
    max-width: 950px;
    padding: 35px;
}

.cross {
    font-size: 80px;
    color: #ffd95a;
    animation: float 3s infinite ease-in-out;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-12px);
    }
}

.hero h1 {
    font-size: 52px;
    margin: 10px 0;
}

.hero h2 {
    color: #ffd95a;
    margin-bottom: 20px;
}

.hero p {
    font-size: 19px;
    margin: 8px;
}

.button {
    display: inline-block;
    margin: 20px 5px 0;
    padding: 13px 22px;
    border-radius: 30px;
    background: #ffd95a;
    color: #4b1763;
    text-decoration: none;
    font-weight: bold;
    transition: .2s;
}

.button:hover {
    transform: scale(1.05);
    background: white;
}

.section {
    max-width: 1150px;
    margin: auto;
    padding: 70px 25px;
}

.title {
    text-align: center;
    color: #67248d;
    font-size: 36px;
    margin-bottom: 15px;
}

.subtitle {
    max-width: 850px;
    margin: 0 auto 40px;
    text-align: center;
    color: #6d6172;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 22px;
}

.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    border-top: 5px solid #762aa0;
    box-shadow: 0 5px 20px rgba(60,20,80,.12);
    transition: .25s;
}

.card:hover {
    transform: translateY(-7px);
}

.card h3 {
    color: #67248d;
    margin-bottom: 10px;
}

.info {
    background: #eee0f4;
    border-left: 6px solid #762aa0;
    padding: 22px;
    border-radius: 12px;
    margin-top: 25px;
}

.purple {
    background: linear-gradient(135deg,#46155e,#762b97);
    color: white;
}

.purple .title {
    color: #ffd95a;
}

.lesson {
    background: white;
    padding: 30px;
    margin-bottom: 22px;
    border-radius: 18px;
    border-left: 6px solid #762aa0;
    box-shadow: 0 5px 20px rgba(60,20,80,.12);
}

.lesson h3 {
    color: #67248d;
    margin-bottom: 12px;
}

.lesson ul {
    margin-left: 25px;
}

.lesson li {
    margin: 6px 0;
}

.timeline {
    max-width: 850px;
    margin: auto;
}

.timeline-item {
    background: white;
    padding: 25px;
    margin: 15px 0;
    border-radius: 15px;
    border-left: 5px solid #762aa0;
    box-shadow: 0 4px 15px rgba(50,20,70,.12);
}

.timeline-item h3 {
    color: #67248d;
}

.steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.step {
    background: white;
    color: #302039;
    padding: 28px;
    text-align: center;
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(60,20,80,.12);
}

.number {
    width: 55px;
    height: 55px;
    margin: auto auto 15px;
    border-radius: 50%;
    background: #702994;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    font-weight: bold;
}

.funny {
    background: linear-gradient(135deg,#421353,#762b95);
    color: white;
    padding: 70px 20px;
    text-align: center;
}

.funny .title {
    color: #ffd95a;
}

.joke {
    max-width: 850px;
    margin: 14px auto;
    padding: 18px;
    background: rgba(255,255,255,.12);
    border-radius: 14px;
    transition: .2s;
}

.joke:hover {
    transform: scale(1.03);
}

.gallery {
    background: white;
    padding: 70px 20px;
}

.gallery-grid {
    max-width: 1150px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 20px;
}

.gallery-grid img {
    width: 100%;
    height: 280px;
    object-fit: cover;
    border-radius: 15px;
    cursor: pointer;
    box-shadow: 0 5px 18px rgba(40,20,60,.18);
    transition: .25s;
}

.gallery-grid img:hover {
    transform: scale(1.03);
}

.modal {
    display: none;
    position: fixed;
    z-index: 9999;
    inset: 0;
    background: rgba(0,0,0,.94);
    align-items: center;
    justify-content: center;
}

.modal img {
    max-width: 90%;
    max-height: 85%;
    border-radius: 15px;
}

.close {
    position: absolute;
    top: 10px;
    right: 30px;
    color: white;
    font-size: 50px;
    cursor: pointer;
}

.checklist {
    max-width: 800px;
    margin: auto;
    padding: 30px;
    background: white;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(60,20,80,.12);
}

.check {
    display: block;
    padding: 12px;
    margin: 7px 0;
    background: #f3eaf7;
    border-radius: 10px;
    cursor: pointer;
}

.check input {
    margin-right: 10px;
    transform: scale(1.2);
}

.quiz {
    background: #eadcf0;
    padding: 70px 20px;
    text-align: center;
}

.quiz-box {
    max-width: 850px;
    margin: auto;
    padding: 35px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(60,20,80,.15);
}

.question {
    margin: 25px 0;
}

.question button {
    border: none;
    padding: 11px 20px;
    margin: 5px;
    border-radius: 20px;
    background: #eee;
    cursor: pointer;
    font-weight: bold;
    transition: .2s;
}

.question button:hover {
    background: #d9b9e8;
    transform: translateY(-2px);
}

#result {
    margin-top: 25px;
    color: #67248d;
    font-size: 20px;
    font-weight: bold;
}

.contact {
    max-width: 850px;
    margin: auto;
    padding: 40px;
    background: white;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(60,20,80,.15);
}

.contact h2 {
    color: #67248d;
    margin-bottom: 15px;
}

footer {
    background: #28102f;
    color: white;
    text-align: center;
    padding: 45px 20px;
}

.credit {
    display: inline-block;
    margin-top: 18px;
    color: #ffd95a;
    text-decoration: none;
    font-weight: bold;
    font-size: 19px;
}

.credit:hover {
    color: white;
}

@media(max-width:800px) {

    nav {
        flex-direction: column;
    }

    .hero {
        min-height: 600px;
    }

    .hero h1 {
        font-size: 36px;
    }

    .hero h2 {
        font-size: 21px;
    }

    .hero p {
        font-size: 16px;
    }

    .title {
        font-size: 29px;
    }

    .nav-links a {
        font-size: 14px;
    }

    .gallery-grid img {
        height: 230px;
    }
}
</style>
</head>

<body>

<nav>

<div class="logo">
✝ MIP Salawag
</div>

<div class="nav-links">

<a href="#home">
{% if lang == "en" %}Home
{% elif lang == "fil" %}Tahanan
{% elif lang == "fr" %}Accueil
{% elif lang == "el" %}Αρχική
{% else %}Domus
{% endif %}
</a>

<a href="#about">
{% if lang == "en" %}About
{% elif lang == "fil" %}Tungkol
{% elif lang == "fr" %}À propos
{% elif lang == "el" %}Σχετικά
{% else %}De Nobis
{% endif %}
</a>

<a href="#lessons">
{% if lang == "en" %}Lessons
{% elif lang == "fil" %}Mga Aralin
{% elif lang == "fr" %}Leçons
{% elif lang == "el" %}Μαθήματα
{% else %}Lectiones
{% endif %}
</a>

<a href="#join">
{% if lang == "en" %}Join
{% elif lang == "fil" %}Sumali
{% elif lang == "fr" %}Rejoindre
{% elif lang == "el" %}Εγγραφή
{% else %}Iungere
{% endif %}
</a>

<a href="#mass">⛪</a>
<a href="#photos">📸</a>
<a href="#quiz">🧠</a>

<select onchange="changeLanguage(this.value)">

<option value="en" {% if lang == "en" %}selected{% endif %}>
🇬🇧 English
</option>

<option value="fil" {% if lang == "fil" %}selected{% endif %}>
🇵🇭 Filipino
</option>

<option value="fr" {% if lang == "fr" %}selected{% endif %}>
🇫🇷 Français
</option>

<option value="el" {% if lang == "el" %}selected{% endif %}>
🇬🇷 Ελληνικά
</option>

<option value="la" {% if lang == "la" %}selected{% endif %}>
🇻🇦 Latin
</option>

</select>

</div>
</nav>


<section class="hero" id="home">

<div class="hero-content">

<div class="cross">✝</div>

<h1>
Mary Immaculate Parish
</h1>

<h2>
Salawag • Dasmariñas • Cavite
</h2>

{% if lang == "en" %}

<p><b>ALTAR SERVERS MINISTRY</b></p>
<p>Learn • Pray • Serve • Grow</p>
<p>
Serving Christ at the altar with faith,
discipline, joy and love.
</p>

{% elif lang == "fil" %}

<p><b>MINISTRY NG MGA SAKRISTAN</b></p>
<p>Matuto • Manalangin • Maglingkod • Lumago</p>
<p>
Maglingkod kay Kristo sa altar nang may
pananampalataya, disiplina, saya at pagmamahal.
</p>

{% elif lang == "fr" %}

<p><b>MINISTÈRE DES SERVANTS D'AUTEL</b></p>
<p>Apprendre • Prier • Servir • Grandir</p>
<p>
Servir le Christ à l'autel avec foi,
discipline, joie et amour.
</p>

{% elif lang == "el" %}

<p><b>ΔΙΑΚΟΝΙΑ ΤΩΝ ΥΠΗΡΕΤΩΝ ΤΟΥ ΙΕΡΟΥ</b></p>
<p>Μάθε • Προσευχήσου • Υπηρέτησε • Μεγάλωσε</p>
<p>
Υπηρετούμε τον Χριστό στο ιερό
με πίστη, πειθαρχία, χαρά και αγάπη.
</p>

{% else %}

<p><b>MINISTERIUM SERVORUM ALTARIS</b></p>
<p>Disce • Ora • Servi • Cresce</p>
<p>
Christo ad altare servimus
cum fide, disciplina, gaudio et caritate.
</p>

{% endif %}

<a class="button" href="#lessons">📚 Learn</a>
<a class="button" href="#join">🙏 Join</a>

</div>
</section>


<section class="section" id="about">

<h2 class="title">

{% if lang == "en" %}
About MIP Salawag
{% elif lang == "fil" %}
Tungkol sa MIP Salawag
{% elif lang == "fr" %}
À propos de MIP Salawag
{% elif lang == "el" %}
Σχετικά με το MIP Salawag
{% else %}
De MIP Salawag
{% endif %}

</h2>

<p class="subtitle">
Mary Immaculate Parish – City of Dasmariñas
is part of the Roman Catholic Diocese of Imus.
</p>

<div class="cards">

<div class="card">
<h3>⛪ Parish</h3>
<p>Mary Immaculate Parish – City of Dasmariñas</p>
</div>

<div class="card">
<h3>🙏 Patroness</h3>
<p>Our Lady of the Immaculate Conception</p>
</div>

<div class="card">
<h3>🎉 Feast Day</h3>
<p>December 8</p>
</div>

<div class="card">
<h3>👨‍💼 Parish Priest</h3>
<p>Father Pipo</p>
</div>

<div class="card">
<h3>📍 Location</h3>
<p>
Salawag, City of Dasmariñas,
Cavite, Philippines
</p>
</div>

<div class="card">
<h3>📞 Contact</h3>
<p>
686-0457<br>
0962 470 6080
</p>
</div>

</div>

<div class="info">

<b>Important:</b>

<p>
Parish schedules, ministry requirements and
formation dates may change. Confirm current
information with MIP Salawag.
</p>

</div>

</section>


<section class="section purple" id="ministry">

<h2 class="title">
Altar Servers Ministry 🙏
</h2>

<div class="cards">

<div class="step">
<div class="number">🙏</div>
<h3>Prayer</h3>
<p>Serving begins with a prayerful heart.</p>
</div>

<div class="step">
<div class="number">👂</div>
<h3>Attention</h3>
<p>Listen carefully to the priest and coordinators.</p>
</div>

<div class="step">
<div class="number">🤝</div>
<h3>Teamwork</h3>
<p>Help and respect fellow servers.</p>
</div>

<div class="step">
<div class="number">❤️</div>
<h3>Service</h3>
<p>Serve God and the parish community.</p>
</div>

</div>
</section>


<section class="section" id="mass">

<h2 class="title">
Mass Guide ⛪
</h2>

<div class="timeline">

<div class="timeline-item">
<h3>1️⃣ Before Mass</h3>
<p>
Arrive early, prepare your vestment,
check your assignment and pray.
</p>
</div>

<div class="timeline-item">
<h3>2️⃣ Entrance</h3>
<p>
Participate in the procession according
to the parish arrangement.
</p>
</div>

<div class="timeline-item">
<h3>3️⃣ Liturgy of the Word</h3>
<p>
Listen carefully and remain attentive.
</p>
</div>

<div class="timeline-item">
<h3>4️⃣ Preparation of the Gifts</h3>
<p>
Assist with assigned items when requested.
</p>
</div>

<div class="timeline-item">
<h3>5️⃣ Eucharistic Prayer</h3>
<p>
Maintain a prayerful posture and follow
your assigned duties.
</p>
</div>

<div class="timeline-item">
<h3>6️⃣ Communion</h3>
<p>
Remain attentive and perform your assigned role.
</p>
</div>

<div class="timeline-item">
<h3>7️⃣ Recessional</h3>
<p>
Follow the parish arrangement for the
closing procession.
</p>
</div>

<div class="timeline-item">
<h3>8️⃣ After Mass</h3>
<p>
Return items properly and leave the serving
area clean.
</p>
</div>

</div>
</section>


<section class="section" id="lessons">

<h2 class="title">
Altar Server Academy 📚
</h2>

<p class="subtitle">
Learn the basics and always follow the official
formation of your parish.
</p>

<div class="lesson">

<h3>📖 Lesson 1 — The Mass</h3>

<p>
The Mass is the central act of Catholic worship.
Altar servers assist the ministers so that
the liturgy can be celebrated with order
and reverence.
</p>

<ul>
<li>Know your assignment.</li>
<li>Pay attention.</li>
<li>Follow instructions.</li>
<li>Remain prayerful.</li>
</ul>

</div>


<div class="lesson">

<h3>👕 Lesson 2 — Vestments</h3>

<p>
Treat liturgical clothing with respect.
Keep vestments clean and wear them properly.
</p>

</div>


<div class="lesson">

<h3>🏆 Lesson 3 — Sacred Objects</h3>

<ul>
<li>Chalice</li>
<li>Ciborium</li>
<li>Cruets</li>
<li>Thurible</li>
<li>Incense boat</li>
<li>Processional cross</li>
<li>Lavabo items</li>
</ul>

</div>


<div class="lesson">

<h3>🕯️ Lesson 4 — Candles</h3>

<p>
Carry candles carefully, walk slowly and
never play with fire.
</p>

</div>


<div class="lesson">

<h3>🔔 Lesson 5 — Bells</h3>

<p>
Bells may be used at particular moments
according to liturgical and parish practice.
</p>

<div class="info">
<b>Important server rule:</b>
<p>
The bells are for Mass, not your personal concert. 😂
</p>
</div>

</div>


<div class="lesson">

<h3>🔥 Lesson 6 — Incense</h3>

<p>
When incense is used, follow the exact
training given by your parish coordinator.
Never experiment with fire.
</p>

</div>


<div class="lesson">

<h3>🙏 Lesson 7 — Posture</h3>

<ul>
<li>Stand properly.</li>
<li>Walk calmly.</li>
<li>Avoid unnecessary talking.</li>
<li>Stay attentive.</li>
<li>Follow parish instructions.</li>
</ul>

</div>


<div class="lesson">

<h3>🤝 Lesson 8 — Teamwork</h3>

<p>
Altar serving is a team ministry.
Help one another and respect your fellow servers.
</p>

</div>


<div class="lesson">

<h3>😅 Lesson 9 — Mistakes</h3>

<p>
Mistakes happen while learning.
Stay calm, listen and continue.
Ask your coordinator for help when necessary.
</p>

</div>


<div class="lesson">

<h3>❤️ Lesson 10 — The Heart of Service</h3>

<p>
A good altar server develops humility,
discipline, responsibility, prayerfulness
and love.
</p>

</div>

</section>


<section class="section">

<h2 class="title">
Before Mass Checklist ✅
</h2>

<div class="checklist">

<label class="check">
<input type="checkbox">
I arrived early.
</label>

<label class="check">
<input type="checkbox">
I know my assignment.
</label>

<label class="check">
<input type="checkbox">
My vestment is properly worn.
</label>

<label class="check">
<input type="checkbox">
I checked what I need.
</label>

<label class="check">
<input type="checkbox">
My phone is silent.
</label>

<label class="check">
<input type="checkbox">
I prayed before serving.
</label>

<label class="check">
<input type="checkbox">
I am ready to serve.
</label>

</div>

</section>


<section class="section purple" id="join">

<h2 class="title">
How to Become an Altar Server 🙏
</h2>

<div class="steps">

<div class="step">
<div class="number">1</div>
<h3>Ask</h3>
<p>Talk to the parish or altar-server coordinators.</p>
</div>

<div class="step">
<div class="number">2</div>
<h3>Check</h3>
<p>Ask about current requirements.</p>
</div>

<div class="step">
<div class="number">3</div>
<h3>Train</h3>
<p>Attend formation and practical training.</p>
</div>

<div class="step">
<div class="number">4</div>
<h3>Practice</h3>
<p>Practice your assigned duties.</p>
</div>

<div class="step">
<div class="number">5</div>
<h3>Serve</h3>
<p>Serve faithfully and respectfully.</p>
</div>

<div class="step">
<div class="number">6</div>
<h3>Grow</h3>
<p>Continue learning and growing in faith.</p>
</div>

</div>

<br>

<p style="text-align:center">
<b>
Always confirm the official requirements with MIP Salawag.
</b>
</p>

</section>


<section class="section">

<h2 class="title">
Qualities of a Good Altar Server 🌟
</h2>

<div class="cards">

<div class="card">
<h3>🙏 Prayerful</h3>
<p>Remembers that serving is an act of faith.</p>
</div>

<div class="card">
<h3>⏰ Responsible</h3>
<p>Arrives prepared and on time.</p>
</div>

<div class="card">
<h3>👂 Attentive</h3>
<p>Listens and watches carefully.</p>
</div>

<div class="card">
<h3>🤝 Helpful</h3>
<p>Helps fellow servers.</p>
</div>

<div class="card">
<h3>❤️ Humble</h3>
<p>Doesn't serve just for attention.</p>
</div>

<div class="card">
<h3>📚 Teachable</h3>
<p>Accepts correction and keeps learning.</p>
</div>

</div>
</section>


<section class="funny">

<h2 class="title">
Altar Server Survival Guide 😂
</h2>

<div class="joke">
🔔 The bells are NOT your personal concert.
</div>

<div class="joke">
🕯️ Candles are NOT portable flashlights.
</div>

<div class="joke">
😇 Look prayerful even when thinking about lunch.
</div>

<div class="joke">
👀 Don't invent a new liturgical movement when confused.
</div>

<div class="joke">
🏃 Running is for outside, not during Mass.
</div>

<div class="joke">
😂 Everyone makes mistakes. Learn and keep serving.
</div>

</section>


<section class="gallery" id="photos">

<h2 class="title">
MIP Salawag Gallery 📸
</h2>

<p class="subtitle">
Click any image to enlarge it.
</p>

<div class="gallery-grid">

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/1.jpg"
onclick="openPhoto(this.src)"
alt="MIP Salawag activity 1"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/2.jpg"
onclick="openPhoto(this.src)"
alt="MIP Salawag activity 2"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/3.jpg"
onclick="openPhoto(this.src)"
alt="MIP Salawag activity 3"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/4.jpg"
onclick="openPhoto(this.src)"
alt="MIP Salawag activity 4"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/5.jpg"
onclick="openPhoto(this.src)"
alt="MIP Salawag activity 5"
loading="lazy"
>

</div>

</section>


<div
class="modal"
id="photoModal"
onclick="closePhoto()"
>

<span
class="close"
onclick="closePhoto()"
>
&times;
</span>

<img
id="bigPhoto"
alt="MIP Salawag enlarged photo"
>

</div>


<section class="quiz" id="quiz">

<h2 class="title">
Altar Server Quiz 🧠
</h2>

<p class="subtitle">
Test your knowledge!
</p>

<div class="quiz-box">

<div class="question">

<p>
<b>
1. Should an altar server arrive early?
</b>
</p>

<button onclick="answer(true)">
Yes 👍
</button>

<button onclick="answer(false)">
No 😴
</button>

</div>


<div class="question">

<p>
<b>
2. What should you do after making a mistake?
</b>
</p>

<button onclick="answer(true)">
Stay calm 😇
</button>

<button onclick="answer(false)">
Panic 🏃
</button>

</div>


<div class="question">

<p>
<b>
3. Are bells for random entertainment?
</b>
</p>

<button onclick="answer(false)">
Yes 😂
</button>

<button onclick="answer(true)">
No 🔔
</button>

</div>


<div class="question">

<p>
<b>
4. Should servers help each other?
</b>
</p>

<button onclick="answer(true)">
Yes 🤝
</button>

<button onclick="answer(false)">
No 😈
</button>

</div>


<div class="question">

<p>
<b>
5. What should guide your service?
</b>
</p>

<button onclick="answer(true)">
Faith and reverence 🙏
</button>

<button onclick="answer(false)">
Showing off 😎
</button>

</div>


<div id="result">
Answer all five!
</div>

</div>

</section>


<section class="section">

<div class="contact">

<h2>
Mary Immaculate Parish ⛪
</h2>

<p>
City of Dasmariñas, Cavite, Philippines
</p>

<br>

<p>
📞 <b>686-0457</b>
</p>

<p>
📱 <b>0962 470 6080</b>
</p>

<br>

<p>
For current schedules, requirements and
formation information, contact the parish directly.
</p>

<a
class="button"
href="https://www.dioceseofimus.org/parishes/59"
target="_blank"
rel="noopener noreferrer"
>
Official Diocese Page
</a>

</div>

</section>


<footer>

<p style="font-size:45px">
✝
</p>

<p>
<span style="color:#ffd95a;font-weight:bold;">
MIP Salawag Altar Servers
</span>
</p>

<p>
Serve with faith. Serve with joy. ❤️
</p>

<a class="credit" href="#home">
Hugo made this
</a>

</footer>


<script>

function changeLanguage(language) {
    window.location.href =
        "/?lang=" + encodeURIComponent(language);
}


function openPhoto(source) {
    document.getElementById("photoModal").style.display = "flex";
    document.getElementById("bigPhoto").src = source;
}


function closePhoto() {
    document.getElementById("photoModal").style.display = "none";
}


document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        closePhoto();
    }
});


let score = 0;
let answered = 0;


function answer(correct) {

    answered++;

    if (correct) {
        score++;
    }

    if (answered === 5) {

        const result =
            document.getElementById("result");

        if (score === 5) {

            result.innerHTML =
                "🏆 PERFECT SCORE! Senior-server energy detected! 😇";

        } else if (score >= 3) {

            result.innerHTML =
                "👏 Great job! Keep learning and serving!";

        } else {

            result.innerHTML =
                "😂 Time for another lesson! You can do it!";
        }

        setTimeout(function() {
            score = 0;
            answered = 0;
        }, 100);
    }
}


/* Save checklist */

const checkboxes =
    document.querySelectorAll(".check input");


checkboxes.forEach(function(box, index) {

    const saved =
        localStorage.getItem("mip-check-" + index);

    if (saved === "true") {
        box.checked = true;
    }

    box.addEventListener("change", function() {

        localStorage.setItem(
            "mip-check-" + index,
            box.checked
        );

    });

});

</script>

</body>
</html>
"""


@app.route("/")
def home():
    lang = request.args.get("lang", "en")

    allowed_languages = ["en", "fil", "fr", "el", "la"]

    if lang not in allowed_languages:
        lang = "en"

    return render_template_string(
        HTML,
        lang=lang
    )


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":

    print()
    print("==============================================")
    print("       MIP SALAWAG ALTAR SERVERS")
    print("==============================================")
    print()
    print("Website is starting...")
    print()
    print("Open this address:")
    print("http://127.0.0.1:5000")
    print()
    print("Press CTRL+C to stop the website.")
    print()

    threading.Timer(
        1.5,
        open_browser
    ).start()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
