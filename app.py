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
content="Mary Immaculate Parish - City of Dasmariñas | Altar Servers Ministry">

<meta name="theme-color" content="#6b218c">

<title>MIP Salawag | Altar Servers</title>

<style>

/* =========================================================
   RESET
========================================================= */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    scroll-behavior: smooth;
}

:root {
    --purple: #68218b;
    --purple-dark: #351044;
    --purple-light: #8e43aa;
    --gold: #f6c945;
    --gold-light: #ffe88a;
    --cream: #faf7fc;
    --text: #302438;
    --muted: #706578;
    --white: #ffffff;
    --green: #2e9b65;
    --red: #d94a4a;
    --shadow: 0 8px 30px rgba(50, 15, 65, .12);
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: var(--cream);
    color: var(--text);
    line-height: 1.7;
}

a {
    color: inherit;
}

button,
select {
    font-family: inherit;
}


/* =========================================================
   TOP BAR
========================================================= */

.topbar {
    background: var(--purple-dark);
    color: white;
    padding: 7px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    font-size: 13px;
}

.topbar-right {
    display: flex;
    gap: 15px;
}


/* =========================================================
   NAVIGATION
========================================================= */

nav {
    position: sticky;
    top: 0;
    z-index: 5000;
    background: white;
    box-shadow: 0 3px 18px rgba(0,0,0,.14);
}

.nav-inner {
    max-width: 1250px;
    margin: auto;
    padding: 13px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--purple);
    font-weight: 800;
    font-size: 18px;
    white-space: nowrap;
}

.logo-cross {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: var(--purple);
    color: var(--gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}

.nav-links {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
    gap: 8px;
}

.nav-links a {
    text-decoration: none;
    color: #4c275b;
    padding: 8px 10px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: bold;
    transition: .2s;
}

.nav-links a:hover {
    background: #f1e4f6;
    color: var(--purple);
}

.language {
    padding: 9px 11px;
    border: 1px solid #c8a7d3;
    border-radius: 8px;
    color: var(--purple);
    background: white;
    cursor: pointer;
    font-weight: bold;
}


/* =========================================================
   HERO / PARISH HEADER
========================================================= */

.hero {
    background:
        linear-gradient(
            90deg,
            rgba(42, 10, 55, .94),
            rgba(104, 33, 139, .75)
        ),
        url("https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/3.jpg");

    background-size: cover;
    background-position: center;

    min-height: 500px;

    display: flex;
    align-items: center;
}

.hero-inner {
    max-width: 1250px;
    width: 100%;
    margin: auto;
    padding: 70px 25px;
    color: white;
}

.breadcrumb {
    color: #ead8ef;
    font-size: 14px;
    margin-bottom: 25px;
}

.breadcrumb span {
    color: var(--gold);
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,.14);
    border: 1px solid rgba(255,255,255,.25);
    padding: 8px 14px;
    border-radius: 30px;
    margin-bottom: 18px;
    color: var(--gold-light);
    font-weight: bold;
}

.hero h1 {
    font-family: Georgia, serif;
    font-size: clamp(36px, 6vw, 66px);
    line-height: 1.1;
    max-width: 850px;
}

.hero h2 {
    color: var(--gold);
    margin-top: 12px;
    font-size: 22px;
}

.hero p {
    max-width: 750px;
    margin-top: 15px;
    font-size: 18px;
    color: #f5eaf8;
}

.hero-buttons {
    margin-top: 25px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.btn {
    display: inline-block;
    border: none;
    text-decoration: none;
    padding: 12px 20px;
    border-radius: 25px;
    cursor: pointer;
    font-weight: bold;
    transition: .2s;
}

.btn:hover {
    transform: translateY(-2px);
}

.btn-gold {
    background: var(--gold);
    color: #42204e;
}

.btn-white {
    background: white;
    color: var(--purple);
}


/* =========================================================
   GENERAL
========================================================= */

.container {
    max-width: 1180px;
    margin: auto;
    padding: 70px 22px;
}

.section-heading {
    text-align: center;
    margin-bottom: 40px;
}

.section-heading h2 {
    color: var(--purple);
    font-family: Georgia, serif;
    font-size: 35px;
}

.section-heading p {
    color: var(--muted);
    max-width: 800px;
    margin: 8px auto 0;
}

.gold-line {
    width: 70px;
    height: 4px;
    background: var(--gold);
    margin: 13px auto;
    border-radius: 5px;
}


/* =========================================================
   PARISH PROFILE
========================================================= */

.profile-grid {
    display: grid;
    grid-template-columns: 1.15fr .85fr;
    gap: 30px;
    align-items: stretch;
}

.profile-card {
    background: white;
    border-radius: 18px;
    box-shadow: var(--shadow);
    overflow: hidden;
}

.profile-card-inner {
    padding: 28px;
}

.profile-card h3 {
    color: var(--purple);
    margin-bottom: 10px;
}

.patron-icon {
    width: 80px;
    height: 80px;
    background: #f2e4f7;
    color: var(--purple);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    margin-bottom: 18px;
}

.fact-list {
    list-style: none;
}

.fact-list li {
    padding: 11px 0;
    border-bottom: 1px solid #eee;
}

.fact-list li:last-child {
    border-bottom: 0;
}

.fact-list strong {
    color: var(--purple);
}


/* =========================================================
   PRIESTS
========================================================= */

.priest-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.priest {
    background: #fbf8fc;
    border: 1px solid #eadcf0;
    padding: 20px;
    border-radius: 15px;
}

.priest-photo {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    background: linear-gradient(135deg, #6b238e, #b36ac9);
    color: var(--gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    margin-bottom: 12px;
}

.priest h4 {
    color: var(--purple);
    margin-bottom: 4px;
}


/* =========================================================
   SERVICES
========================================================= */

.services {
    background: #f0e6f4;
}

.service-grid {
    max-width: 1000px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.service {
    background: white;
    padding: 23px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(50,20,70,.08);
    text-align: center;
    transition: .2s;
}

.service:hover {
    transform: translateY(-4px);
}

.service-icon {
    font-size: 30px;
    margin-bottom: 5px;
}

.service h3 {
    color: var(--purple);
    font-size: 17px;
}


/* =========================================================
   ALERT
========================================================= */

.notice {
    background: #fff8df;
    border-left: 5px solid var(--gold);
    padding: 18px;
    border-radius: 10px;
    margin-top: 25px;
}


/* =========================================================
   ALTAR SERVER
========================================================= */

.purple-section {
    background:
        linear-gradient(
            135deg,
            #32103f,
            #6b238e
        );
    color: white;
}

.purple-section .section-heading h2 {
    color: var(--gold);
}

.purple-section .section-heading p {
    color: #e8d9ed;
}

.server-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
}

.server-card {
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.16);
    padding: 27px 20px;
    border-radius: 16px;
    text-align: center;
    transition: .2s;
}

.server-card:hover {
    background: rgba(255,255,255,.16);
    transform: translateY(-5px);
}

.server-card .icon {
    font-size: 40px;
}

.server-card h3 {
    color: var(--gold);
    margin: 8px 0;
}


/* =========================================================
   LESSONS
========================================================= */

.lesson-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.lesson {
    background: white;
    padding: 27px;
    border-radius: 17px;
    border-top: 5px solid var(--purple);
    box-shadow: var(--shadow);
}

.lesson h3 {
    color: var(--purple);
    margin-bottom: 10px;
}

.lesson ul {
    margin: 12px 0 0 23px;
}

.lesson li {
    margin: 5px 0;
}


/* =========================================================
   CHECKLIST
========================================================= */

.checklist {
    max-width: 800px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: var(--shadow);
}

.check {
    display: block;
    padding: 13px;
    margin: 8px 0;
    border-radius: 10px;
    background: #f5edf8;
    cursor: pointer;
}

.check:hover {
    background: #ecdef1;
}

.check input {
    transform: scale(1.25);
    margin-right: 10px;
}


/* =========================================================
   GAMES
========================================================= */

.games-section {
    background: #160b1d;
    color: white;
}

.games-section .section-heading h2 {
    color: var(--gold);
}

.games-section .section-heading p {
    color: #d9c9df;
}

.game-menu {
    max-width: 1050px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.game-card {
    background: linear-gradient(145deg,#2c1239,#49145e);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    cursor: pointer;
    transition: .25s;
}

.game-card:hover {
    transform: translateY(-6px) scale(1.01);
    border-color: var(--gold);
}

.game-card .game-icon {
    font-size: 50px;
}

.game-card h3 {
    color: var(--gold);
    margin: 8px 0;
}

.game-card p {
    color: #ded0e2;
    font-size: 14px;
}

.game-screen {
    max-width: 900px;
    margin: 30px auto 0;
    background: white;
    color: var(--text);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 40px rgba(0,0,0,.25);
    display: none;
}

.game-screen.active {
    display: block;
}

.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 20px;
}

.game-header h3 {
    color: var(--purple);
    font-size: 25px;
}

.score {
    background: var(--purple);
    color: white;
    padding: 8px 14px;
    border-radius: 20px;
    font-weight: bold;
}

.game-question {
    background: #f5edf8;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin: 15px 0;
}

.game-question h4 {
    color: var(--purple);
    font-size: 20px;
}

.game-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-top: 15px;
}

.game-option {
    border: 2px solid #e3d3e9;
    background: white;
    padding: 13px;
    border-radius: 12px;
    cursor: pointer;
    font-weight: bold;
    transition: .2s;
}

.game-option:hover {
    border-color: var(--purple);
    background: #f7eff9;
}

.correct {
    background: #dff6e9 !important;
    border-color: var(--green) !important;
}

.wrong {
    background: #ffe4e4 !important;
    border-color: var(--red) !important;
}

.game-message {
    text-align: center;
    font-weight: bold;
    color: var(--purple);
    margin-top: 15px;
    min-height: 28px;
}

.game-buttons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}


/* =========================================================
   MEMORY GAME
========================================================= */

.memory-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    max-width: 500px;
    margin: auto;
}

.memory-card {
    aspect-ratio: 1;
    border: none;
    border-radius: 12px;
    background: var(--purple);
    color: white;
    font-size: 30px;
    cursor: pointer;
}

.memory-card.open {
    background: #f2e4f7;
    color: var(--purple);
}

.memory-card.matched {
    background: #dff6e9;
    color: var(--green);
}


/* =========================================================
   ORDER GAME
========================================================= */

.order-list {
    max-width: 600px;
    margin: auto;
}

.order-item {
    padding: 14px;
    background: #f3eaf6;
    border: 2px solid transparent;
    border-radius: 10px;
    margin: 8px;
    cursor: pointer;
    font-weight: bold;
}

.order-item.selected {
    border-color: var(--gold);
    background: #fff7d9;
}


/* =========================================================
   REACTION GAME
========================================================= */

.reaction-box {
    height: 240px;
    border-radius: 20px;
    background: #777;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    user-select: none;
}

.reaction-ready {
    background: var(--green);
}

.reaction-wait {
    background: var(--red);
}


/* =========================================================
   RANK
========================================================= */

.rank-box {
    max-width: 800px;
    margin: 35px auto 0;
    background: white;
    color: var(--text);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
}

.rank-title {
    color: var(--purple);
    font-size: 25px;
    font-weight: bold;
}

.xp-bar {
    height: 18px;
    background: #eadfeb;
    border-radius: 20px;
    overflow: hidden;
    margin: 15px 0;
}

.xp-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg,var(--purple),var(--gold));
    transition: .4s;
}


/* =========================================================
   GALLERY
========================================================= */

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.gallery-grid img {
    width: 100%;
    height: 260px;
    object-fit: cover;
    border-radius: 15px;
    cursor: pointer;
    box-shadow: var(--shadow);
    transition: .25s;
}

.gallery-grid img:hover {
    transform: scale(1.025);
}


/* =========================================================
   MODAL
========================================================= */

.modal {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 10000;
    background: rgba(0,0,0,.94);
    align-items: center;
    justify-content: center;
    padding: 30px;
}

.modal.active {
    display: flex;
}

.modal img {
    max-width: 94%;
    max-height: 88%;
    border-radius: 15px;
}

.close {
    position: absolute;
    top: 10px;
    right: 25px;
    color: white;
    font-size: 50px;
    cursor: pointer;
}


/* =========================================================
   CONTACT
========================================================= */

.contact-section {
    background: #f0e6f4;
}

.contact-card {
    max-width: 850px;
    margin: auto;
    background: white;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    box-shadow: var(--shadow);
}

.contact-card h2 {
    color: var(--purple);
    font-family: Georgia, serif;
    margin-bottom: 12px;
}

.contact-number {
    color: var(--purple);
    font-size: 20px;
    font-weight: bold;
    margin: 7px;
}


/* =========================================================
   FOOTER
========================================================= */

footer {
    background: #241029;
    color: #ddd0e3;
    text-align: center;
    padding: 50px 20px;
}

.footer-cross {
    color: var(--gold);
    font-size: 45px;
}

.footer-title {
    color: var(--gold);
    font-size: 19px;
    font-weight: bold;
    margin: 8px;
}


/* =========================================================
   CONFETTI
========================================================= */

.confetti {
    position: fixed;
    top: -20px;
    width: 10px;
    height: 15px;
    z-index: 20000;
    pointer-events: none;
    animation: fall 2.5s linear forwards;
}

@keyframes fall {
    to {
        transform: translateY(110vh) rotate(720deg);
        opacity: 0;
    }
}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:900px) {

    .profile-grid,
    .lesson-grid {
        grid-template-columns: 1fr;
    }

    .server-grid {
        grid-template-columns: repeat(2,1fr);
    }

    .game-menu {
        grid-template-columns: repeat(2,1fr);
    }

    .gallery-grid {
        grid-template-columns: repeat(2,1fr);
    }

    .service-grid {
        grid-template-columns: repeat(2,1fr);
    }

}

@media(max-width:650px) {

    .topbar {
        justify-content: center;
        text-align: center;
    }

    .topbar-right {
        display: none;
    }

    .nav-inner {
        flex-direction: column;
    }

    .nav-links {
        justify-content: center;
    }

    .hero {
        min-height: 550px;
    }

    .hero-inner {
        padding: 50px 20px;
    }

    .hero h1 {
        font-size: 39px;
    }

    .server-grid,
    .game-menu,
    .gallery-grid,
    .service-grid,
    .priest-grid {
        grid-template-columns: 1fr;
    }

    .game-options {
        grid-template-columns: 1fr;
    }

    .memory-grid {
        grid-template-columns: repeat(3,1fr);
    }

    .container {
        padding: 55px 17px;
    }

    .section-heading h2 {
        font-size: 29px;
    }

}

</style>
</head>


<body>


<!-- =====================================================
     TOP BAR
====================================================== -->

<div class="topbar">

<div>
✝ Roman Catholic Parish • City of Dasmariñas
</div>

<div class="topbar-right">
<span>📞 686-0457</span>
<span>📱 0962 470 6080</span>
</div>

</div>


<!-- =====================================================
     NAVIGATION
====================================================== -->

<nav>

<div class="nav-inner">

<div class="logo">
<div class="logo-cross">✝</div>
<span>MIP Salawag</span>
</div>

<div class="nav-links">

<a href="#home">{{ t.nav_home }}</a>
<a href="#parish">{{ t.nav_parish }}</a>
<a href="#servers">{{ t.nav_servers }}</a>
<a href="#lessons">{{ t.nav_lessons }}</a>
<a href="#games">🎮 {{ t.nav_games }}</a>
<a href="#photos">📸</a>
<a href="#contact">📞</a>

<select
class="language"
onchange="changeLanguage(this.value)"
>

<option value="en" {% if lang == "en" %}selected{% endif %}>
🇬🇧 English
</option>

<option value="fil" {% if lang == "fil" %}selected{% endif %}>
🇵🇭 Filipino
</option>

<option value="fr" {% if lang == "fr" %}selected{% endif %}>
🇫🇷 French
</option>

<option value="el" {% if lang == "el" %}selected{% endif %}>
🇬🇷 Greek
</option>

<option value="la" {% if lang == "la" %}selected{% endif %}>
🇻🇦 Latin
</option>

</select>

</div>

</div>

</nav>


<!-- =====================================================
     HERO
====================================================== -->

<section class="hero" id="home">

<div class="hero-inner">

<div class="breadcrumb">
{{ t.breadcrumb }}
<span>› {{ t.parish_name }}</span>
</div>

<div class="hero-badge">
✝ {{ t.hero_badge }}
</div>

<h1>
{{ t.parish_name }}
</h1>

<h2>
{{ t.location }}
</h2>

<p>
{{ t.hero_text }}
</p>

<div class="hero-buttons">

<a class="btn btn-gold" href="#servers">
🙏 {{ t.server_button }}
</a>

<a class="btn btn-white" href="#games">
🎮 {{ t.game_button }}
</a>

</div>

</div>

</section>


<!-- =====================================================
     PARISH PROFILE
====================================================== -->

<section class="container" id="parish">

<div class="section-heading">

<h2>{{ t.parish_profile }}</h2>

<div class="gold-line"></div>

<p>{{ t.parish_profile_sub }}</p>

</div>


<div class="profile-grid">


<div class="profile-card">

<div class="profile-card-inner">

<div class="patron-icon">
🙏
</div>

<h3>{{ t.patron }}</h3>

<h2 style="color:#68218b;">
{{ t.patron_name }}
</h2>

<p style="margin-top:8px;">
{{ t.feast }}
</p>

<div class="notice">
<b>ℹ️ {{ t.official_note_title }}</b>
<br>
{{ t.official_note }}
</div>

</div>

</div>


<div class="profile-card">

<div class="profile-card-inner">

<h3>📋 {{ t.parish_facts }}</h3>

<ul class="fact-list">

<li>
<strong>{{ t.parish_label }}:</strong>
{{ t.parish_name }}
</li>

<li>
<strong>{{ t.location_label }}:</strong>
{{ t.location }}
</li>

<li>
<strong>{{ t.patron_label }}:</strong>
{{ t.patron_name }}
</li>

<li>
<strong>{{ t.feast_label }}:</strong>
{{ t.feast_short }}
</li>

<li>
<strong>{{ t.phone_label }}:</strong>
686-0457
</li>

<li>
<strong>{{ t.mobile_label }}:</strong>
0962 470 6080
</li>

</ul>

</div>

</div>


</div>

</section>


<!-- =====================================================
     PRIESTS
====================================================== -->

<section class="container" style="padding-top:10px;">

<div class="section-heading">

<h2>{{ t.priests }}</h2>

<div class="gold-line"></div>

</div>


<div class="priest-grid">


<div class="priest">

<div class="priest-photo">
✝
</div>

<h4>
Rev. Fr. John Paulo S. Bautista, SHMI
</h4>

<p>
{{ t.parish_priest }}
</p>

</div>


<div class="priest">

<div class="priest-photo">
✝
</div>

<h4>
Rev. Fr. Alberto J. Failago, SHMI
</h4>

<p>
{{ t.parochial_vicar }}
</p>

</div>


</div>

</section>


<!-- =====================================================
     SERVICES
====================================================== -->

<section class="services">

<div class="container">

<div class="section-heading">

<h2>{{ t.services }}</h2>

<div class="gold-line"></div>

<p>
{{ t.services_sub }}
</p>

</div>


<div class="service-grid">

<div class="service">
<div class="service-icon">⛪</div>
<h3>{{ t.mass }}</h3>
</div>

<div class="service">
<div class="service-icon">💧</div>
<h3>{{ t.baptism }}</h3>
</div>

<div class="service">
<div class="service-icon">🙏</div>
<h3>{{ t.confession }}</h3>
</div>

<div class="service">
<div class="service-icon">💍</div>
<h3>{{ t.wedding }}</h3>
</div>

<div class="service">
<div class="service-icon">🕊️</div>
<h3>{{ t.confirmation }}</h3>
</div>

<div class="service">
<div class="service-icon">🕯️</div>
<h3>{{ t.funeral }}</h3>
</div>

<div class="service">
<div class="service-icon">🍞</div>
<h3>{{ t.first_communion }}</h3>
</div>

<div class="service">
<div class="service-icon">✝️</div>
<h3>{{ t.blessing }}</h3>
</div>

<div class="service">
<div class="service-icon">❤️</div>
<h3>{{ t.anointing }}</h3>
</div>

</div>


<div class="notice">

<b>⚠️ {{ t.schedule_warning_title }}</b>

<br>

{{ t.schedule_warning }}

</div>

</div>

</section>


<!-- =====================================================
     ALTAR SERVER MINISTRY
====================================================== -->

<section class="purple-section" id="servers">

<div class="container">

<div class="section-heading">

<h2>{{ t.server_title }}</h2>

<div class="gold-line"></div>

<p>{{ t.server_sub }}</p>

</div>


<div class="server-grid">


<div class="server-card">

<div class="icon">🙏</div>

<h3>{{ t.prayer }}</h3>

<p>{{ t.prayer_text }}</p>

</div>


<div class="server-card">

<div class="icon">👂</div>

<h3>{{ t.attention }}</h3>

<p>{{ t.attention_text }}</p>

</div>


<div class="server-card">

<div class="icon">🤝</div>

<h3>{{ t.teamwork }}</h3>

<p>{{ t.teamwork_text }}</p>

</div>


<div class="server-card">

<div class="icon">❤️</div>

<h3>{{ t.service }}</h3>

<p>{{ t.service_text }}</p>

</div>


</div>

</div>

</section>


<!-- =====================================================
     LESSONS
====================================================== -->

<section class="container" id="lessons">

<div class="section-heading">

<h2>{{ t.academy }}</h2>

<div class="gold-line"></div>

<p>{{ t.academy_sub }}</p>

</div>


<div class="lesson-grid">


<div class="lesson">

<h3>📖 {{ t.lesson1_title }}</h3>

<p>{{ t.lesson1 }}</p>

<ul>
<li>{{ t.lesson1_a }}</li>
<li>{{ t.lesson1_b }}</li>
<li>{{ t.lesson1_c }}</li>
<li>{{ t.lesson1_d }}</li>
</ul>

</div>


<div class="lesson">

<h3>👕 {{ t.lesson2_title }}</h3>

<p>{{ t.lesson2 }}</p>

</div>


<div class="lesson">

<h3>🏆 {{ t.lesson3_title }}</h3>

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

<h3>🕯️ {{ t.lesson4_title }}</h3>

<p>{{ t.lesson4 }}</p>

</div>


<div class="lesson">

<h3>🔔 {{ t.lesson5_title }}</h3>

<p>{{ t.lesson5 }}</p>

<div class="notice">
{{ t.bell_rule }}
</div>

</div>


<div class="lesson">

<h3>🔥 {{ t.lesson6_title }}</h3>

<p>{{ t.lesson6 }}</p>

</div>


<div class="lesson">

<h3>🙏 {{ t.lesson7_title }}</h3>

<ul>
<li>{{ t.posture1 }}</li>
<li>{{ t.posture2 }}</li>
<li>{{ t.posture3 }}</li>
<li>{{ t.posture4 }}</li>
<li>{{ t.posture5 }}</li>
</ul>

</div>


<div class="lesson">

<h3>🤝 {{ t.lesson8_title }}</h3>

<p>{{ t.lesson8 }}</p>

</div>


<div class="lesson">

<h3>😅 {{ t.lesson9_title }}</h3>

<p>{{ t.lesson9 }}</p>

</div>


<div class="lesson">

<h3>❤️ {{ t.lesson10_title }}</h3>

<p>{{ t.lesson10 }}</p>

</div>


</div>

</section>


<!-- =====================================================
     CHECKLIST
====================================================== -->

<section class="services">

<div class="container">

<div class="section-heading">

<h2>{{ t.checklist_title }}</h2>

<div class="gold-line"></div>

</div>


<div class="checklist">

<label class="check">
<input type="checkbox">
{{ t.check1 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check2 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check3 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check4 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check5 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check6 }}
</label>

<label class="check">
<input type="checkbox">
{{ t.check7 }}
</label>

</div>

</div>

</section>


<!-- =====================================================
     GAMES CENTER
====================================================== -->

<section class="games-section" id="games">

<div class="container">

<div class="section-heading">

<h2>🎮 {{ t.games_title }}</h2>

<div class="gold-line"></div>

<p>{{ t.games_sub }}</p>

</div>


<div class="game-menu">


<div class="game-card" onclick="openGame('quizGame')">

<div class="game-icon">🧠</div>

<h3>{{ t.game_quiz }}</h3>

<p>{{ t.game_quiz_desc }}</p>

</div>


<div class="game-card" onclick="openGame('massGame')">

<div class="game-icon">⛪</div>

<h3>{{ t.game_mass }}</h3>

<p>{{ t.game_mass_desc }}</p>

</div>


<div class="game-card" onclick="openGame('memoryGame')">

<div class="game-icon">🕯️</div>

<h3>{{ t.game_memory }}</h3>

<p>{{ t.game_memory_desc }}</p>

</div>


<div class="game-card" onclick="openGame('reactionGame')">

<div class="game-icon">⚡</div>

<h3>{{ t.game_reaction }}</h3>

<p>{{ t.game_reaction_desc }}</p>

</div>


<div class="game-card" onclick="openGame('objectGame')">

<div class="game-icon">🏺</div>

<h3>{{ t.game_objects }}</h3>

<p>{{ t.game_objects_desc }}</p>

</div>


<div class="game-card" onclick="openGame('challengeGame')">

<div class="game-icon">🏆</div>

<h3>{{ t.game_challenge }}</h3>

<p>{{ t.game_challenge_desc }}</p>

</div>


</div>


<!-- ================= QUIZ ================= -->

<div class="game-screen" id="quizGame">

<div class="game-header">

<h3>🧠 {{ t.game_quiz }}</h3>

<div class="score">
<span id="quizScore">0</span> pts
</div>

</div>

<div class="game-question">

<h4 id="quizQuestion">
{{ t.q1 }}
</h4>

<div class="game-options" id="quizOptions"></div>

</div>

<div class="game-message" id="quizMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="startQuiz()">
🔄 {{ t.play_again }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= MASS ORDER ================= -->

<div class="game-screen" id="massGame">

<div class="game-header">

<h3>⛪ {{ t.game_mass }}</h3>

<div class="score">
<span id="massScore">0</span> pts
</div>

</div>

<div class="game-question">

<h4>{{ t.mass_instruction }}</h4>

<p style="margin:10px 0;">
{{ t.mass_instruction2 }}
</p>

<div class="order-list" id="massList"></div>

</div>

<div class="game-message" id="massMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="checkMassOrder()">
✅ {{ t.check_answer }}
</button>

<button class="btn btn-white" onclick="startMassGame()">
🔄 {{ t.restart }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= MEMORY ================= -->

<div class="game-screen" id="memoryGame">

<div class="game-header">

<h3>🕯️ {{ t.game_memory }}</h3>

<div class="score">
<span id="memoryScore">0</span> pts
</div>

</div>

<p style="text-align:center;margin-bottom:15px;">
{{ t.memory_instruction }}
</p>

<div class="memory-grid" id="memoryGrid"></div>

<div class="game-message" id="memoryMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="startMemory()">
🔄 {{ t.restart }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= REACTION ================= -->

<div class="game-screen" id="reactionGame">

<div class="game-header">

<h3>⚡ {{ t.game_reaction }}</h3>

<div class="score">
<span id="reactionScore">0</span> pts
</div>

</div>

<p style="text-align:center;margin-bottom:15px;">
{{ t.reaction_instruction }}
</p>

<div
class="reaction-box"
id="reactionBox"
onclick="reactionClick()"
>
{{ t.reaction_start }}
</div>

<div class="game-message" id="reactionMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="startReaction()">
▶ {{ t.start }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= SACRED OBJECTS ================= -->

<div class="game-screen" id="objectGame">

<div class="game-header">

<h3>🏺 {{ t.game_objects }}</h3>

<div class="score">
<span id="objectScore">0</span> pts
</div>

</div>

<div class="game-question">

<h4 id="objectQuestion">
{{ t.object_q }}
</h4>

<div class="game-options" id="objectOptions"></div>

</div>

<div class="game-message" id="objectMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="startObjectGame()">
🔄 {{ t.restart }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= CHALLENGE ================= -->

<div class="game-screen" id="challengeGame">

<div class="game-header">

<h3>🏆 {{ t.game_challenge }}</h3>

<div class="score">
<span id="challengeScore">0</span> pts
</div>

</div>

<div class="game-question">

<h4 id="challengeQuestion">
{{ t.challenge_q }}
</h4>

<div class="game-options" id="challengeOptions"></div>

</div>

<div class="game-message" id="challengeMessage"></div>

<div class="game-buttons">

<button class="btn btn-gold" onclick="startChallenge()">
🔄 {{ t.restart }}
</button>

<button class="btn btn-white" onclick="closeGames()">
✕ {{ t.close }}
</button>

</div>

</div>


<!-- ================= RANK ================= -->

<div class="rank-box">

<div class="rank-title">
🏅 {{ t.rank_title }}
</div>

<h2 id="rankName" style="color:#68218b;margin-top:8px;">
🌱 {{ t.rank_beginner }}
</h2>

<p>
{{ t.total_xp }}:
<strong id="totalXP">0</strong>
</p>

<div class="xp-bar">
<div class="xp-fill" id="xpFill"></div>
</div>

<p id="rankDescription">
{{ t.rank_beginner_desc }}
</p>

</div>


</div>

</section>


<!-- =====================================================
     GALLERY
====================================================== -->

<section class="container" id="photos">

<div class="section-heading">

<h2>📸 {{ t.gallery }}</h2>

<div class="gold-line"></div>

<p>{{ t.gallery_sub }}</p>

</div>


<div class="gallery-grid">

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/1.jpg"
onclick="openPhoto(this.src)"
alt="Mary Immaculate Parish"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/2.jpg"
onclick="openPhoto(this.src)"
alt="Mary Immaculate Parish"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/3.jpg"
onclick="openPhoto(this.src)"
alt="Mary Immaculate Parish"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/4.jpg"
onclick="openPhoto(this.src)"
alt="Mary Immaculate Parish"
loading="lazy"
>

<img
src="https://www.dioceseofimus.org/storage/parishes/dasmarinas/mary-immaculate/activity/5.jpg"
onclick="openPhoto(this.src)"
alt="Mary Immaculate Parish"
loading="lazy"
>

</div>

</section>


<!-- =====================================================
     PHOTO MODAL
====================================================== -->

<div
class="modal"
id="photoModal"
onclick="closePhoto()"
>

<span class="close">
&times;
</span>

<img id="bigPhoto" alt="Enlarged parish photograph">

</div>


<!-- =====================================================
     CONTACT
====================================================== -->

<section class="contact-section" id="contact">

<div class="container">

<div class="section-heading">

<h2>{{ t.contact_title }}</h2>

<div class="gold-line"></div>

</div>


<div class="contact-card">

<h2>
⛪ {{ t.parish_name }}
</h2>

<p>
{{ t.location }}
</p>

<br>

<div class="contact-number">
📞 686-0457
</div>

<div class="contact-number">
📱 0962 470 6080
</div>

<br>

<p>
{{ t.contact_note }}
</p>

<br>

<a
class="btn btn-gold"
href="https://www.dioceseofimus.org/parishes/59"
target="_blank"
rel="noopener noreferrer"
>
🌐 {{ t.official_page }}
</a>

</div>

</div>

</section>


<!-- =====================================================
     FOOTER
====================================================== -->

<footer>

<div class="footer-cross">
✝
</div>

<div class="footer-title">
MIP Salawag Altar Servers
</div>

<p>
{{ t.footer }}
</p>

<p style="margin-top:15px;font-size:12px;color:#9d8ba4;">
{{ t.footer_note }}
</p>

</footer>


<script>

/* =========================================================
   LANGUAGE
========================================================= */

function changeLanguage(language) {

    window.location.href =
        "/?lang=" + encodeURIComponent(language);

}


/* =========================================================
   PHOTO
========================================================= */

function openPhoto(src) {

    document
        .getElementById("photoModal")
        .classList.add("active");

    document
        .getElementById("bigPhoto")
        .src = src;

}


function closePhoto() {

    document
        .getElementById("photoModal")
        .classList.remove("active");

}


document.addEventListener("keydown", function(event) {

    if (event.key === "Escape") {
        closePhoto();
    }

});


/* =========================================================
   GAMES
========================================================= */

function closeGames() {

    document
        .querySelectorAll(".game-screen")
        .forEach(function(screen) {
            screen.classList.remove("active");
        });

}


function openGame(id) {

    closeGames();

    const screen =
        document.getElementById(id);

    screen.classList.add("active");

    screen.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

    if (id === "quizGame") {
        startQuiz();
    }

    if (id === "massGame") {
        startMassGame();
    }

    if (id === "memoryGame") {
        startMemory();
    }

    if (id === "objectGame") {
        startObjectGame();
    }

    if (id === "challengeGame") {
        startChallenge();
    }

}


/* =========================================================
   XP / RANK SYSTEM
========================================================= */

let totalXP =
    parseInt(
        localStorage.getItem("mip-total-xp") || "0"
    );

function saveXP(amount) {

    totalXP += amount;

    localStorage.setItem(
        "mip-total-xp",
        totalXP
    );

    updateRank();

    confetti();

}


function updateRank() {

    document.getElementById("totalXP").textContent =
        totalXP;

    let name;
    let description;
    let icon;
    let progress;

    if (totalXP >= 1000) {

        name = "{{ t.rank_master }}";
        description = "{{ t.rank_master_desc }}";
        icon = "👑";
        progress = 100;

    }

    else if (totalXP >= 500) {

        name = "{{ t.rank_senior }}";
        description = "{{ t.rank_senior_desc }}";
        icon = "🕯️";
        progress = ((totalXP - 500) / 500) * 100;

    }

    else if (totalXP >= 250) {

        name = "{{ t.rank_faithful }}";
        description = "{{ t.rank_faithful_desc }}";
        icon = "⭐";
        progress = ((totalXP - 250) / 250) * 100;

    }

    else if (totalXP >= 100) {

        name = "{{ t.rank_server }}";
        description = "{{ t.rank_server_desc }}";
        icon = "🙏";
        progress = ((totalXP - 100) / 150) * 100;

    }

    else {

        name = "{{ t.rank_beginner }}";
        description = "{{ t.rank_beginner_desc }}";
        icon = "🌱";
        progress = (totalXP / 100) * 100;

    }

    document.getElementById("rankName").textContent =
        icon + " " + name;

    document.getElementById("rankDescription").textContent =
        description;

    document.getElementById("xpFill").style.width =
        Math.min(progress,100) + "%";

}


/* =========================================================
   CONFETTI
========================================================= */

function confetti() {

    for (let i = 0; i < 25; i++) {

        const piece =
            document.createElement("div");

        piece.className = "confetti";

        piece.style.left =
            Math.random() * 100 + "vw";

        piece.style.background =
            [
                "#f6c945",
                "#68218b",
                "#ffffff",
                "#65c99b",
                "#ff7a7a"
            ][
                Math.floor(Math.random() * 5)
            ];

        piece.style.animationDelay =
            Math.random() * .5 + "s";

        document.body.appendChild(piece);

        setTimeout(function() {
            piece.remove();
        }, 3000);

    }

}


/* =========================================================
   QUIZ GAME
========================================================= */

const quizQuestions = [

    {
        q: "{{ t.q1 }}",
        answers: [
            ["{{ t.yes }}", true],
            ["{{ t.no }}", false]
        ]
    },

    {
        q: "{{ t.q2 }}",
        answers: [
            ["{{ t.stay_calm }}", true],
            ["{{ t.panic }}", false]
        ]
    },

    {
        q: "{{ t.q3 }}",
        answers: [
            ["{{ t.random_yes }}", false],
            ["{{ t.random_no }}", true]
        ]
    },

    {
        q: "{{ t.q4 }}",
        answers: [
            ["{{ t.help_yes }}", true],
            ["{{ t.help_no }}", false]
        ]
    },

    {
        q: "{{ t.q5 }}",
        answers: [
            ["{{ t.faith }}", true],
            ["{{ t.showing_off }}", false]
        ]
    }

];

let quizIndex = 0;
let quizPoints = 0;

function startQuiz() {

    quizIndex = 0;
    quizPoints = 0;

    document.getElementById("quizScore").textContent = "0";
    document.getElementById("quizMessage").textContent = "";

    showQuizQuestion();

}


function showQuizQuestion() {

    if (quizIndex >= quizQuestions.length) {

        document.getElementById("quizMessage").textContent =
            quizPoints === 5
            ? "{{ t.perfect }}"
            : "{{ t.quiz_finished }}";

        saveXP(quizPoints * 20);

        return;
    }

    const item =
        quizQuestions[quizIndex];

    document.getElementById("quizQuestion").textContent =
        item.q;

    const box =
        document.getElementById("quizOptions");

    box.innerHTML = "";

    item.answers.forEach(function(answer) {

        const button =
            document.createElement("button");

        button.className = "game-option";

        button.textContent =
            answer[0];

        button.onclick = function() {

            if (answer[1]) {

                quizPoints++;

                document.getElementById(
                    "quizScore"
                ).textContent =
                    quizPoints;

                button.classList.add("correct");

            }

            else {

                button.classList.add("wrong");

            }

            quizIndex++;

            setTimeout(
                showQuizQuestion,
                450
            );

        };

        box.appendChild(button);

    });

}


/* =========================================================
   MASS ORDER GAME
========================================================= */

const correctMassOrder = [
    "Before Mass",
    "Entrance",
    "Liturgy of the Word",
    "Preparation of the Gifts",
    "Eucharistic Prayer",
    "Communion",
    "Recessional",
    "After Mass"
];

let selectedMass = [];

function startMassGame() {

    selectedMass = [];

    document.getElementById("massScore").textContent = "0";

    document.getElementById("massMessage").textContent =
        "";

    const shuffled =
        [...correctMassOrder]
        .sort(() => Math.random() - .5);

    const list =
        document.getElementById("massList");

    list.innerHTML = "";

    shuffled.forEach(function(item) {

        const div =
            document.createElement("div");

        div.className = "order-item";

        div.textContent =
            item;

        div.onclick = function() {

            if (div.classList.contains("selected")) {
                return;
            }

            div.classList.add("selected");

            selectedMass.push(item);

            div.textContent =
                selectedMass.length +
                ". " +
                item;

        };

        list.appendChild(div);

    });

}


function checkMassOrder() {

    if (selectedMass.length !== correctMassOrder.length) {

        document.getElementById("massMessage").textContent =
            "{{ t.select_all }}";

        return;

    }

    let correct = true;

    for (
        let i = 0;
        i < correctMassOrder.length;
        i++
    ) {

        if (
            selectedMass[i] !==
            correctMassOrder[i]
        ) {

            correct = false;
            break;

        }

    }

    if (correct) {

        document.getElementById("massScore").textContent =
            "100";

        document.getElementById("massMessage").textContent =
            "{{ t.mass_correct }}";

        saveXP(100);

    }

    else {

        document.getElementById("massMessage").textContent =
            "{{ t.mass_wrong }}";

    }

}


/* =========================================================
   MEMORY GAME
========================================================= */

const memorySymbols = [
    "🕯️",
    "🕯️",
    "🔔",
    "🔔",
    "✝️",
    "✝️",
    "🙏",
    "🙏",
    "⛪",
    "⛪",
    "📖",
    "📖"
];

let memoryFirst = null;
let memorySecond = null;
let memoryLock = false;
let memoryMatches = 0;

function startMemory() {

    memoryFirst = null;
    memorySecond = null;
    memoryLock = false;
    memoryMatches = 0;

    document.getElementById("memoryScore").textContent =
        "0";

    document.getElementById("memoryMessage").textContent =
        "";

    const values =
        [...memorySymbols]
        .sort(() => Math.random() - .5);

    const grid =
        document.getElementById("memoryGrid");

    grid.innerHTML = "";

    values.forEach(function(symbol) {

        const button =
            document.createElement("button");

        button.className =
            "memory-card";

        button.textContent =
            "?";

        button.dataset.symbol =
            symbol;

        button.onclick =
            function() {

                memoryClick(button);

            };

        grid.appendChild(button);

    });

}


function memoryClick(card) {

    if (
        memoryLock ||
        card.classList.contains("open") ||
        card.classList.contains("matched")
    ) {
        return;
    }

    card.classList.add("open");

    card.textContent =
        card.dataset.symbol;

    if (!memoryFirst) {

        memoryFirst = card;
        return;

    }

    memorySecond = card;
    memoryLock = true;

    if (
        memoryFirst.dataset.symbol ===
        memorySecond.dataset.symbol
    ) {

        memoryFirst.classList.add("matched");
        memorySecond.classList.add("matched");

        memoryMatches++;

        memoryFirst = null;
        memorySecond = null;
        memoryLock = false;

        document.getElementById("memoryScore").textContent =
            memoryMatches * 20;

        if (memoryMatches === 6) {

            document.getElementById("memoryMessage").textContent =
                "{{ t.memory_win }}";

            saveXP(120);

        }

    }

    else {

        setTimeout(function() {

            memoryFirst.classList.remove("open");
            memorySecond.classList.remove("open");

            memoryFirst.textContent = "?";
            memorySecond.textContent = "?";

            memoryFirst = null;
            memorySecond = null;

            memoryLock = false;

        }, 700);

    }

}


/* =========================================================
   REACTION GAME
========================================================= */

let reactionWaiting = false;
let reactionReady = false;
let reactionStartTime = 0;
let reactionTimer = null;

function startReaction() {

    const box =
        document.getElementById("reactionBox");

    const message =
        document.getElementById("reactionMessage");

    reactionWaiting = true;
    reactionReady = false;

    box.className =
        "reaction-box reaction-wait";

    box.textContent =
        "{{ t.wait }}";

    message.textContent =
        "";

    clearTimeout(reactionTimer);

    reactionTimer =
        setTimeout(function() {

            reactionReady = true;
            reactionWaiting = false;
            reactionStartTime = performance.now();

            box.className =
                "reaction-box reaction-ready";

            box.textContent =
                "{{ t.click_now }}";

        }, 1200 + Math.random() * 2500);

}


function reactionClick() {

    const box =
        document.getElementById("reactionBox");

    const message =
        document.getElementById("reactionMessage");

    if (reactionWaiting) {

        clearTimeout(reactionTimer);

        reactionWaiting = false;

        box.className =
            "reaction-box reaction-wait";

        box.textContent =
            "{{ t.too_early }}";

        message.textContent =
            "{{ t.try_again }}";

        return;

    }

    if (!reactionReady) {
        return;
    }

    const elapsed =
        Math.round(
            performance.now() -
            reactionStartTime
        );

    reactionReady = false;

    let points = 0;

    if (elapsed < 300) {
        points = 100;
    }
    else if (elapsed < 500) {
        points = 70;
    }
    else if (elapsed < 800) {
        points = 40;
    }
    else {
        points = 20;
    }

    document.getElementById("reactionScore").textContent =
        points;

    box.className =
        "reaction-box";

    box.textContent =
        elapsed + " ms";

    message.textContent =
        "{{ t.reaction_result }} " +
        points +
        " XP!";

    saveXP(points);

}


/* =========================================================
   SACRED OBJECT GAME
========================================================= */

const objectQuestions = [

    {
        q: "{{ t.object_q1 }}",
        a: [
            ["Chalice", true],
            ["Bell", false],
            ["Candle", false],
            ["Book", false]
        ]
    },

    {
        q: "{{ t.object_q2 }}",
        a: [
            ["Ciborium", true],
            ["Cruet", false],
            ["Thurible", false],
            ["Cross", false]
        ]
    },

    {
        q: "{{ t.object_q3 }}",
        a: [
            ["Thurible", true],
            ["Chalice", false],
            ["Cruet", false],
            ["Ciborium", false]
        ]
    },

    {
        q: "{{ t.object_q4 }}",
        a: [
            ["Processional cross", true],
            ["Chalice", false],
            ["Bell", false],
            ["Cruet", false]
        ]
    }

];

let objectIndex = 0;
let objectPoints = 0;

function startObjectGame() {

    objectIndex = 0;
    objectPoints = 0;

    document.getElementById("objectScore").textContent =
        "0";

    document.getElementById("objectMessage").textContent =
        "";

    showObjectQuestion();

}


function showObjectQuestion() {

    if (
        objectIndex >=
        objectQuestions.length
    ) {

        document.getElementById("objectMessage").textContent =
            "{{ t.object_finished }}";

        saveXP(objectPoints * 10);

        return;

    }

    const item =
        objectQuestions[objectIndex];

    document.getElementById("objectQuestion").textContent =
        item.q;

    const box =
        document.getElementById("objectOptions");

    box.innerHTML = "";

    item.a.forEach(function(answer) {

        const button =
            document.createElement("button");

        button.className =
            "game-option";

        button.textContent =
            answer[0];

        button.onclick = function() {

            if (answer[1]) {

                objectPoints += 10;

                button.classList.add("correct");

            }

            else {

                button.classList.add("wrong");

            }

            document.getElementById("objectScore").textContent =
                objectPoints;

            objectIndex++;

            setTimeout(
                showObjectQuestion,
                400
            );

        };

        box.appendChild(button);

    });

}


/* =========================================================
   CHALLENGE GAME
========================================================= */

const challengeQuestions = [

    {
        q: "{{ t.challenge_q1 }}",
        a: [
            ["{{ t.arrive_early }}", true],
            ["{{ t.arrive_late }}", false]
        ]
    },

    {
        q: "{{ t.challenge_q2 }}",
        a: [
            ["{{ t.listen }}", true],
            ["{{ t.ignore }}", false]
        ]
    },

    {
        q: "{{ t.challenge_q3 }}",
        a: [
            ["{{ t.pray }}", true],
            ["{{ t.play }}", false]
        ]
    },

    {
        q: "{{ t.challenge_q4 }}",
        a: [
            ["{{ t.help }}", true],
            ["{{ t.competition }}", false]
        ]
    },

    {
        q: "{{ t.challenge_q5 }}",
        a: [
            ["{{ t.humble }}", true],
            ["{{ t.showoff }}", false]
        ]
    },

    {
        q: "{{ t.challenge_q6 }}",
        a: [
            ["{{ t.ask_help }}", true],
            ["{{ t.guess }}", false]
        ]
    }

];

let challengeIndex = 0;
let challengePoints = 0;

function startChallenge() {

    challengeIndex = 0;
    challengePoints = 0;

    document.getElementById("challengeScore").textContent =
        "0";

    document.getElementById("challengeMessage").textContent =
        "";

    showChallenge();

}


function showChallenge() {

    if (
        challengeIndex >=
        challengeQuestions.length
    ) {

        document.getElementById("challengeMessage").textContent =
            "{{ t.challenge_finished }}";

        saveXP(challengePoints * 15);

        return;

    }

    const item =
        challengeQuestions[challengeIndex];

    document.getElementById("challengeQuestion").textContent =
        item.q;

    const box =
        document.getElementById("challengeOptions");

    box.innerHTML = "";

    item.a.forEach(function(answer) {

        const button =
            document.createElement("button");

        button.className =
            "game-option";

        button.textContent =
            answer[0];

        button.onclick = function() {

            if (answer[1]) {

                challengePoints += 1;

                button.classList.add("correct");

            }

            else {

                button.classList.add("wrong");

            }

            document.getElementById("challengeScore").textContent =
                challengePoints * 15;

            challengeIndex++;

            setTimeout(
                showChallenge,
                400
            );

        };

        box.appendChild(button);

    });

}


/* =========================================================
   CHECKLIST STORAGE
========================================================= */

const checklist =
    document.querySelectorAll(".check input");

checklist.forEach(function(box,index) {

    const saved =
        localStorage.getItem(
            "mip-check-" + index
        );

    if (saved === "true") {
        box.checked = true;
    }

    box.addEventListener(
        "change",
        function() {

            localStorage.setItem(
                "mip-check-" + index,
                box.checked
            );

        }
    );

});


/* =========================================================
   INITIALIZE
========================================================= */

updateRank();

</script>

</body>
</html>
"""


# ============================================================
# TRANSLATIONS
# ============================================================

TRANSLATIONS = {

"en": {

"nav_home": "Home",
"nav_parish": "Parish",
"nav_servers": "Servers",
"nav_lessons": "Lessons",
"nav_games": "Games",

"breadcrumb": "Home › Directories › Parishes ›",
"hero_badge": "Mary Immaculate Parish",

"parish_name": "Mary Immaculate Parish - City of Dasmariñas",
"location": "Salawag, City of Dasmariñas, Cavite, Philippines",

"hero_text":
"Welcome to the MIP Salawag Altar Servers Ministry — a place to learn, pray, serve and grow in faith.",

"server_button": "Altar Servers",
"game_button": "Games Center",

"parish_profile": "Parish Profile",
"parish_profile_sub":
"Learn about the parish, its patron, clergy and services.",

"patron": "Patron of the Church",
"patron_name": "Our Lady of the Immaculate Conception",
"feast": "Feast Day: December 8",
"feast_short": "December 8",

"official_note_title": "Official Information",
"official_note":
"Parish schedules and information may change. Please confirm current details with the parish.",

"parish_facts": "Parish Information",
"parish_label": "Parish",
"location_label": "Location",
"patron_label": "Patron",
"feast_label": "Feast",
"phone_label": "Telephone",
"mobile_label": "Mobile",

"priests": "Priests",
"parish_priest": "Parish Priest",
"parochial_vicar": "Parochial Vicar",

"services": "Schedule of Services",
"services_sub":
"Service categories listed by the parish directory.",

"mass": "Mass",
"baptism": "Baptism",
"confession": "Confession",
"wedding": "Wedding",
"confirmation": "Confirmation",
"funeral": "Funeral",
"first_communion": "First Communion",
"blessing": "Blessing",
"anointing": "Anointing of the Sick",

"schedule_warning_title": "Schedule Notice",
"schedule_warning":
"Schedules are subject to change without prior notice. Please contact the parish for updated information.",

"server_title": "Altar Servers Ministry",
"server_sub":
"Serve Christ at the altar with faith, discipline, joy and love.",

"prayer": "Prayer",
"prayer_text": "Serving begins with a prayerful heart.",
"attention": "Attention",
"attention_text": "Listen carefully and follow instructions.",
"teamwork": "Teamwork",
"teamwork_text": "Help and respect your fellow servers.",
"service": "Service",
"service_text": "Serve God and the parish community.",

"academy": "Altar Server Academy",
"academy_sub":
"Learn the basics and always follow the official formation of your parish.",

"lesson1_title": "Lesson 1 — The Mass",
"lesson1":
"The Mass is the central act of Catholic worship. Altar servers assist the ministers so that the liturgy may be celebrated with order and reverence.",
"lesson1_a": "Know your assignment.",
"lesson1_b": "Pay attention.",
"lesson1_c": "Follow instructions.",
"lesson1_d": "Remain prayerful.",

"lesson2_title": "Lesson 2 — Vestments",
"lesson2":
"Treat liturgical clothing with respect. Keep vestments clean and wear them properly.",

"lesson3_title": "Lesson 3 — Sacred Objects",

"lesson4_title": "Lesson 4 — Candles",
"lesson4":
"Carry candles carefully, walk slowly and never play with fire.",

"lesson5_title": "Lesson 5 — Bells",
"lesson5":
"Bells may be used at particular moments according to liturgical and parish practice.",
"bell_rule":
"The bells are for Mass, not your personal concert. 🔔",

"lesson6_title": "Lesson 6 — Incense",
"lesson6":
"When incense is used, follow the exact training given by your parish coordinator. Never experiment with fire.",

"lesson7_title": "Lesson 7 — Posture",
"posture1": "Stand properly.",
"posture2": "Walk calmly.",
"posture3": "Avoid unnecessary talking.",
"posture4": "Stay attentive.",
"posture5": "Follow parish instructions.",

"lesson8_title": "Lesson 8 — Teamwork",
"lesson8":
"Altar serving is a team ministry. Help one another and respect your fellow servers.",

"lesson9_title": "Lesson 9 — Mistakes",
"lesson9":
"Mistakes happen while learning. Stay calm, listen and continue. Ask your coordinator for help when necessary.",

"lesson10_title": "Lesson 10 — The Heart of Service",
"lesson10":
"A good altar server develops humility, discipline, responsibility, prayerfulness and love.",

"checklist_title": "Before Mass Checklist",
"check1": "I arrived early.",
"check2": "I know my assignment.",
"check3": "My vestment is properly worn.",
"check4": "I checked what I need.",
"check5": "My phone is silent.",
"check6": "I prayed before serving.",
"check7": "I am ready to serve.",

"games_title": "Altar Server Games Center",
"games_sub":
"Learn while playing. Your XP and progress are saved in your browser.",

"game_quiz": "Altar Server Quiz",
"game_quiz_desc": "Test your basic altar-server knowledge.",

"game_mass": "Order of the Mass",
"game_mass_desc": "Put the Mass guide in the correct order.",

"game_memory": "Sacred Memory",
"game_memory_desc": "Match the sacred symbols.",

"game_reaction": "Server Reaction",
"game_reaction_desc": "Test your reaction speed.",

"game_objects": "Sacred Objects",
"game_objects_desc": "Identify important liturgical objects.",

"game_challenge": "Server Challenge",
"game_challenge_desc": "A fast challenge about serving.",

"play_again": "Play Again",
"close": "Close",
"restart": "Restart",
"start": "Start",
"check_answer": "Check Answer",

"q1": "Should an altar server arrive early?",
"q2": "What should you do after making a mistake?",
"q3": "Are bells for random entertainment?",
"q4": "Should servers help each other?",
"q5": "What should guide your service?",

"yes": "Yes 👍",
"no": "No 😴",
"stay_calm": "Stay calm 😇",
"panic": "Panic 🏃",
"random_yes": "Yes 😂",
"random_no": "No 🔔",
"help_yes": "Yes 🤝",
"help_no": "No ",
"faith": "Faith and reverence 🙏",
"showing_off": "Showing off 😎",

"perfect": "🏆 PERFECT SCORE! Excellent server knowledge!",
"quiz_finished": "👏 Quiz complete! Keep learning and serving!",

"mass_instruction": "Arrange the stages correctly.",
"mass_instruction2":
"Tap each item in the correct order.",

"select_all": "Please select every item first.",
"mass_correct":
"🏆 Excellent! You know the basic Mass sequence!",
"mass_wrong":
"Not quite. Try again and remember the order.",

"memory_instruction":
"Find all matching pairs.",

"memory_win":
"🎉 Amazing memory! All pairs matched!",

"reaction_instruction":
"Wait for the green screen, then tap as quickly as possible.",

"reaction_start":
"Press Start",

"wait":
"WAIT...",

"click_now":
"CLICK NOW!",

"too_early":
"Too early!",

"try_again":
"Try again.",

"reaction_result":
"Reaction score:",

"object_q":
"Which object is associated with the Eucharistic liturgy?",

"object_q1":
"Which object is used to hold the Eucharistic wine?",
"object_q2":
"Which object is used to hold consecrated hosts?",
"object_q3":
"Which object is used for incense?",
"object_q4":
"Which object is carried in procession?",

"object_finished":
"🏆 Object challenge complete!",

"challenge_q":
"Should a server arrive prepared and on time?",

"challenge_q1":
"What is better before Mass?",
"challenge_q2":
"What should a server do when the coordinator gives instructions?",
"challenge_q3":
"What should a server do before serving?",
"challenge_q4":
"How should servers treat one another?",
"challenge_q5":
"What attitude should a server have?",
"challenge_q6":
"What should you do when you are unsure?",

"arrive_early": "Arrive early",
"arrive_late": "Arrive late",
"listen": "Listen carefully",
"ignore": "Ignore the instruction",
"pray": "Pray",
"play": "Play around",
"help": "Help one another",
"competition": "Compete for attention",
"humble": "Be humble",
"showoff": "Show off",
"ask_help": "Ask for help",
"guess": "Guess randomly",

"challenge_finished":
"🏆 Challenge complete! Great work!",

"rank_title": "Altar Server Rank",
"total_xp": "Total XP",

"rank_beginner": "Beginner",
"rank_beginner_desc": "Keep learning. Every server starts somewhere.",

"rank_server": "Altar Server",
"rank_server_desc": "You are building good serving habits.",

"rank_faithful": "Faithful Server",
"rank_faithful_desc": "Excellent progress. Keep serving with joy.",

"rank_senior": "Senior Server",
"rank_senior_desc": "Strong knowledge and experience.",

"rank_master": "Master Server",
"rank_master_desc": "Outstanding! Keep growing in faith and service.",

"gallery": "Featured Pictures",
"gallery_sub": "Photos from Mary Immaculate Parish.",

"contact_title": "Contact the Parish",
"contact_note":
"For current schedules, requirements and formation information, contact the parish directly.",

"official_page": "Official Diocese Page",

"footer":
"Serve with faith. Serve with joy. Serve with love. ❤️",

"footer_note":
"This altar-server learning website is an educational project. Always follow the instructions and formation of your parish."
},


"fil": {

"nav_home": "Tahanan",
"nav_parish": "Parokya",
"nav_servers": "Mga Sakristan",
"nav_lessons": "Mga Aralin",
"nav_games": "Mga Laro",

"breadcrumb": "Tahanan › Direktoryo › Mga Parokya ›",
"hero_badge": "Parokya ng Mary Immaculate",

"parish_name": "Mary Immaculate Parish - Lungsod ng Dasmariñas",
"location": "Salawag, Lungsod ng Dasmariñas, Cavite, Pilipinas",

"hero_text":
"Maligayang pagdating sa MIP Salawag Altar Servers Ministry — isang lugar upang matuto, manalangin, maglingkod at lumago sa pananampalataya.",

"server_button": "Mga Sakristan",
"game_button": "Sentro ng mga Laro",

"parish_profile": "Impormasyon ng Parokya",
"parish_profile_sub":
"Alamin ang tungkol sa parokya, patrona, mga pari at mga serbisyo.",

"patron": "Patrona ng Simbahan",
"patron_name": "Our Lady of the Immaculate Conception",
"feast": "Kapistahan: Disyembre 8",
"feast_short": "Disyembre 8",

"official_note_title": "Opisyal na Paalala",
"official_note":
"Maaaring magbago ang mga iskedyul at impormasyon. Mangyaring kumpirmahin ang kasalukuyang detalye sa parokya.",

"parish_facts": "Impormasyon ng Parokya",
"parish_label": "Parokya",
"location_label": "Lokasyon",
"patron_label": "Patrona",
"feast_label": "Kapistahan",
"phone_label": "Telepono",
"mobile_label": "Cellphone",

"priests": "Mga Pari",
"parish_priest": "Kura Paroko",
"parochial_vicar": "Parochial Vicar",

"services": "Mga Serbisyo",
"services_sub":
"Mga uri ng serbisyong nakalista sa direktoryo ng parokya.",

"mass": "Banal na Misa",
"baptism": "Binyag",
"confession": "Kumpisal",
"wedding": "Kasal",
"confirmation": "Kumpil",
"funeral": "Libing",
"first_communion": "Unang Komunyon",
"blessing": "Pagpapala",
"anointing": "Pagpapahid ng Langis sa Maysakit",

"schedule_warning_title": "Paalala sa Iskedyul",
"schedule_warning":
"Maaaring magbago ang mga iskedyul. Makipag-ugnayan sa parokya para sa pinakabagong impormasyon.",

"server_title": "Ministry ng mga Sakristan",
"server_sub":
"Maglingkod kay Kristo sa altar nang may pananampalataya, disiplina, saya at pagmamahal.",

"prayer": "Panalangin",
"prayer_text": "Nagsisimula ang paglilingkod sa pusong nananalangin.",
"attention": "Pansin",
"attention_text": "Makinig nang mabuti at sundin ang mga tagubilin.",
"teamwork": "Pagtutulungan",
"teamwork_text": "Tulungan at igalang ang kapwa sakristan.",
"service": "Paglilingkod",
"service_text": "Maglingkod sa Diyos at sa komunidad ng parokya.",

"academy": "Akademya ng mga Sakristan",
"academy_sub":
"Alamin ang mga pangunahing kaalaman at laging sundin ang opisyal na formation ng inyong parokya.",

"lesson1_title": "Aralin 1 — Ang Banal na Misa",
"lesson1":
"Ang Misa ang sentrong pagsamba ng mga Katoliko. Tinutulungan ng mga sakristan ang mga ministro upang maging maayos at marangal ang liturhiya.",
"lesson1_a": "Alamin ang iyong assignment.",
"lesson1_b": "Magbigay ng buong pansin.",
"lesson1_c": "Sundin ang mga tagubilin.",
"lesson1_d": "Manatiling nananalangin.",

"lesson2_title": "Aralin 2 — Kasuotang Panliturhiya",
"lesson2":
"Igalang ang mga kasuotang panliturhiya. Panatilihing malinis at isuot nang tama.",

"lesson3_title": "Aralin 3 — Mga Banal na Kagamitan",

"lesson4_title": "Aralin 4 — Mga Kandila",
"lesson4":
"Dalhin nang maingat ang mga kandila, maglakad nang dahan-dahan at huwag paglaruan ang apoy.",

"lesson5_title": "Aralin 5 — Mga Kampana",
"lesson5":
"Maaaring gamitin ang mga kampana sa mga partikular na bahagi ayon sa liturhiya at kaugalian ng parokya.",
"bell_rule":
"Ang kampana ay para sa Misa, hindi para sa personal mong concert. 🔔",

"lesson6_title": "Aralin 6 — Insenso",
"lesson6":
"Kapag gumagamit ng insenso, sundin ang eksaktong training mula sa coordinator. Huwag mag-eksperimento sa apoy.",

"lesson7_title": "Aralin 7 — Kilos at Postura",
"posture1": "Tumayo nang maayos.",
"posture2": "Maglakad nang mahinahon.",
"posture3": "Iwasan ang hindi kailangang pag-uusap.",
"posture4": "Manatiling alerto.",
"posture5": "Sundin ang tagubilin ng parokya.",

"lesson8_title": "Aralin 8 — Pagtutulungan",
"lesson8":
"Ang pagiging sakristan ay isang ministry ng teamwork. Tulungan at igalang ang isa't isa.",

"lesson9_title": "Aralin 9 — Mga Pagkakamali",
"lesson9":
"Normal ang magkamali habang natututo. Manatiling kalmado, makinig at magpatuloy. Humingi ng tulong kung kailangan.",

"lesson10_title": "Aralin 10 — Puso ng Paglilingkod",
"lesson10":
"Ang mabuting sakristan ay may kababaang-loob, disiplina, pananagutan, panalangin at pagmamahal.",

"checklist_title": "Checklist Bago ang Misa",
"check1": "Dumating ako nang maaga.",
"check2": "Alam ko ang aking assignment.",
"check3": "Maayos ang aking kasuotan.",
"check4": "Naihanda ko ang aking kailangan.",
"check5": "Naka-silent ang cellphone ko.",
"check6": "Nananalangin ako bago maglingkod.",
"check7": "Handa na akong maglingkod.",

"games_title": "Sentro ng mga Laro ng Sakristan",
"games_sub":
"Matuto habang naglalaro. Ang iyong XP at progress ay naka-save sa browser.",

"game_quiz": "Quiz ng Sakristan",
"game_quiz_desc": "Subukan ang iyong kaalaman tungkol sa pagiging sakristan.",

"game_mass": "Ayos ng Misa",
"game_mass_desc": "Ayusin ang mga bahagi ng Misa sa tamang pagkakasunod.",

"game_memory": "Sacred Memory",
"game_memory_desc": "Hanapin ang magkaparehong simbolo.",

"game_reaction": "Reaction ng Sakristan",
"game_reaction_desc": "Subukan ang bilis ng iyong reaction.",

"game_objects": "Mga Banal na Kagamitan",
"game_objects_desc": "Kilalanin ang mahahalagang kagamitan sa liturhiya.",

"game_challenge": "Sakristan Challenge",
"game_challenge_desc": "Mabilis na challenge tungkol sa paglilingkod.",

"play_again": "Maglaro Muli",
"close": "Isara",
"restart": "Ulitin",
"start": "Simulan",
"check_answer": "Suriin ang Sagot",

"q1": "Dapat bang dumating nang maaga ang sakristan?",
"q2": "Ano ang dapat gawin pagkatapos magkamali?",
"q3": "Para ba sa random na entertainment ang kampana?",
"q4": "Dapat bang magtulungan ang mga sakristan?",
"q5": "Ano ang dapat gumabay sa paglilingkod?",

"yes": "Oo 👍",
"no": "Hindi 😴",
"stay_calm": "Manatiling kalmado 😇",
"panic": "Mag-panic 🏃",
"random_yes": "Oo 😂",
"random_no": "Hindi 🔔",
"help_yes": "Oo 🤝",
"help_no": "Hindi",
"faith": "Pananampalataya at paggalang 🙏",
"showing_off": "Pagpapakitang-gilas 😎",

"perfect": "🏆 PERFECT SCORE! Napakagaling!",
"quiz_finished": "👏 Tapos na ang quiz! Patuloy na matuto at maglingkod!",

"mass_instruction": "Ayusin ang mga bahagi sa tamang pagkakasunod.",
"mass_instruction2": "Pindutin ang bawat item ayon sa tamang order.",

"select_all": "Piliin muna ang lahat ng item.",
"mass_correct": "🏆 Mahusay! Alam mo ang pangunahing pagkakasunod ng Misa!",
"mass_wrong": "Hindi pa tama. Subukan muli.",

"memory_instruction": "Hanapin ang lahat ng magkaparehang pares.",
"memory_win": "🎉 Napakahusay! Nahanap mo ang lahat!",

"reaction_instruction":
"Hintayin ang berdeng screen at pindutin ito nang mabilis.",

"reaction_start": "Pindutin ang Start",
"wait": "HINTAY...",
"click_now": "PINDUTIN NGAYON!",
"too_early": "Masyadong maaga!",
"try_again": "Subukan muli.",
"reaction_result": "Reaction score:",

"object_q": "Aling kagamitan ang nauugnay sa liturhiya ng Eukaristiya?",
"object_q1": "Aling kagamitan ang ginagamit para sa alak ng Eukaristiya?",
"object_q2": "Aling kagamitan ang lalagyan ng mga consecrated hosts?",
"object_q3": "Aling kagamitan ang ginagamit para sa insenso?",
"object_q4": "Aling bagay ang dinadala sa prusisyon?",

"object_finished": "🏆 Tapos na ang object challenge!",

"challenge_q": "Dapat bang dumating na handa at nasa oras ang sakristan?",
"challenge_q1": "Ano ang mas mabuti bago ang Misa?",
"challenge_q2": "Ano ang dapat gawin kapag may tagubilin ang coordinator?",
"challenge_q3": "Ano ang dapat gawin bago maglingkod?",
"challenge_q4": "Paano dapat tratuhin ang kapwa sakristan?",
"challenge_q5": "Anong ugali ang dapat mayroon ang sakristan?",
"challenge_q6": "Ano ang dapat gawin kapag hindi sigurado?",

"arrive_early": "Dumating nang maaga",
"arrive_late": "Dumating nang late",
"listen": "Makinig nang mabuti",
"ignore": "Huwag pansinin",
"pray": "Manalangin",
"play": "Maglaro",
"help": "Magtulungan",
"competition": "Mag-agawan ng attention",
"humble": "Maging mapagpakumbaba",
"showoff": "Magpakitang-gilas",
"ask_help": "Humingi ng tulong",
"guess": "Manghula",

"challenge_finished": "🏆 Tapos na ang challenge! Mahusay!",

"rank_title": "Ranggo ng Sakristan",
"total_xp": "Kabuuang XP",

"rank_beginner": "Nagsisimula",
"rank_beginner_desc": "Patuloy na matuto. Lahat ay nagsisimula sa simula.",

"rank_server": "Sakristan",
"rank_server_desc": "Unti-unti kang nagkakaroon ng mabubuting serving habits.",

"rank_faithful": "Tapat na Sakristan",
"rank_faithful_desc": "Napakagandang progreso. Magpatuloy sa paglilingkod.",

"rank_senior": "Senior Sakristan",
"rank_senior_desc": "Malakas ang iyong kaalaman at karanasan.",

"rank_master": "Master Sakristan",
"rank_master_desc": "Napakahusay! Patuloy na lumago sa pananampalataya at paglilingkod.",

"gallery": "Mga Larawan",
"gallery_sub": "Mga larawan mula sa Mary Immaculate Parish.",

"contact_title": "Makipag-ugnayan sa Parokya",
"contact_note":
"Para sa kasalukuyang iskedyul, requirements at formation, direktang makipag-ugnayan sa parokya.",

"official_page": "Opisyal na Diocese Page",

"footer":
"Maglingkod nang may pananampalataya. Maglingkod nang may saya. ❤️",

"footer_note":
"Ito ay educational project. Laging sundin ang opisyal na formation at tagubilin ng inyong parokya."
},


"fr": {

"nav_home": "Accueil",
"nav_parish": "Paroisse",
"nav_servers": "Servants",
"nav_lessons": "Leçons",
"nav_games": "Jeux",

"breadcrumb": "Accueil › Répertoire › Paroisses ›",
"hero_badge": "Paroisse Mary Immaculate",

"parish_name": "Paroisse Mary Immaculate - Ville de Dasmariñas",
"location": "Salawag, Ville de Dasmariñas, Cavite, Philippines",

"hero_text":
"Bienvenue au ministère des servants d'autel de MIP Salawag — un lieu pour apprendre, prier, servir et grandir dans la foi.",

"server_button": "Servants d'autel",
"game_button": "Centre de jeux",

"parish_profile": "Profil de la paroisse",
"parish_profile_sub":
"Découvrez la paroisse, sa patronne, ses prêtres et ses services.",

"patron": "Patronne de l'église",
"patron_name": "Notre-Dame de l'Immaculée Conception",
"feast": "Fête : 8 décembre",
"feast_short": "8 décembre",

"official_note_title": "Information officielle",
"official_note":
"Les horaires et informations peuvent changer. Veuillez confirmer les détails actuels auprès de la paroisse.",

"parish_facts": "Informations paroissiales",
"parish_label": "Paroisse",
"location_label": "Lieu",
"patron_label": "Patronne",
"feast_label": "Fête",
"phone_label": "Téléphone",
"mobile_label": "Mobile",

"priests": "Prêtres",
"parish_priest": "Curé",
"parochial_vicar": "Vicaire paroissial",

"services": "Services",
"services_sub":
"Catégories de services indiquées dans le répertoire paroissial.",

"mass": "Messe",
"baptism": "Baptême",
"confession": "Confession",
"wedding": "Mariage",
"confirmation": "Confirmation",
"funeral": "Funérailles",
"first_communion": "Première Communion",
"blessing": "Bénédiction",
"anointing": "Onction des malades",

"schedule_warning_title": "Avis sur les horaires",
"schedule_warning":
"Les horaires peuvent changer sans préavis. Contactez la paroisse pour obtenir les informations actuelles.",

"server_title": "Ministère des servants d'autel",
"server_sub":
"Servir le Christ à l'autel avec foi, discipline, joie et amour.",

"prayer": "Prière",
"prayer_text": "Le service commence par un cœur dans la prière.",
"attention": "Attention",
"attention_text": "Écoutez attentivement et suivez les instructions.",
"teamwork": "Travail d'équipe",
"teamwork_text": "Aidez et respectez les autres servants.",
"service": "Service",
"service_text": "Servez Dieu et la communauté paroissiale.",

"academy": "Académie des servants d'autel",
"academy_sub":
"Apprenez les bases et suivez toujours la formation officielle de votre paroisse.",

"lesson1_title": "Leçon 1 — La Messe",
"lesson1":
"La Messe est l'acte central du culte catholique. Les servants aident les ministres afin que la liturgie soit célébrée avec ordre et révérence.",
"lesson1_a": "Connaissez votre tâche.",
"lesson1_b": "Restez attentif.",
"lesson1_c": "Suivez les instructions.",
"lesson1_d": "Restez dans la prière.",

"lesson2_title": "Leçon 2 — Vêtements liturgiques",
"lesson2":
"Respectez les vêtements liturgiques. Gardez-les propres et portez-les correctement.",

"lesson3_title": "Leçon 3 — Objets sacrés",

"lesson4_title": "Leçon 4 — Bougies",
"lesson4":
"Portez les bougies avec soin, marchez lentement et ne jouez jamais avec le feu.",

"lesson5_title": "Leçon 5 — Cloches",
"lesson5":
"Les cloches peuvent être utilisées à certains moments selon la liturgie et la pratique paroissiale.",
"bell_rule":
"Les cloches sont pour la Messe, pas pour votre concert personnel. 🔔",

"lesson6_title": "Leçon 6 — Encens",
"lesson6":
"Lorsque l'encens est utilisé, suivez exactement la formation donnée par votre coordinateur.",

"lesson7_title": "Leçon 7 — Posture",
"posture1": "Tenez-vous correctement.",
"posture2": "Marchez calmement.",
"posture3": "Évitez les conversations inutiles.",
"posture4": "Restez attentif.",
"posture5": "Suivez les instructions paroissiales.",

"lesson8_title": "Leçon 8 — Travail d'équipe",
"lesson8":
"Le service de l'autel est un ministère d'équipe. Aidez-vous et respectez-vous.",

"lesson9_title": "Leçon 9 — Les erreurs",
"lesson9":
"Les erreurs arrivent pendant l'apprentissage. Restez calme, écoutez et continuez.",

"lesson10_title": "Leçon 10 — Le cœur du service",
"lesson10":
"Un bon servant développe l'humilité, la discipline, la responsabilité, la prière et l'amour.",

"checklist_title": "Liste avant la Messe",
"check1": "Je suis arrivé tôt.",
"check2": "Je connais ma tâche.",
"check3": "Mon vêtement liturgique est correctement porté.",
"check4": "J'ai préparé ce dont j'ai besoin.",
"check5": "Mon téléphone est silencieux.",
"check6": "J'ai prié avant de servir.",
"check7": "Je suis prêt à servir.",

"games_title": "Centre de jeux des servants",
"games_sub":
"Apprenez en jouant. Votre XP et votre progression sont sauvegardés dans votre navigateur.",

"game_quiz": "Quiz du servant",
"game_quiz_desc": "Testez vos connaissances de base.",

"game_mass": "Ordre de la Messe",
"game_mass_desc": "Placez les étapes de la Messe dans le bon ordre.",

"game_memory": "Mémoire sacrée",
"game_memory_desc": "Trouvez les symboles correspondants.",

"game_reaction": "Réaction du servant",
"game_reaction_desc": "Testez votre vitesse de réaction.",

"game_objects": "Objets sacrés",
"game_objects_desc": "Identifiez les objets liturgiques importants.",

"game_challenge": "Défi du servant",
"game_challenge_desc": "Un défi rapide sur le service.",

"play_again": "Rejouer",
"close": "Fermer",
"restart": "Redémarrer",
"start": "Commencer",
"check_answer": "Vérifier",

"q1": "Un servant doit-il arriver tôt ?",
"q2": "Que faut-il faire après une erreur ?",
"q3": "Les cloches sont-elles destinées au divertissement ?",
"q4": "Les servants doivent-ils s'aider ?",
"q5": "Qu'est-ce qui doit guider votre service ?",

"yes": "Oui 👍",
"no": "Non 😴",
"stay_calm": "Rester calme 😇",
"panic": "Paniquer 🏃",
"random_yes": "Oui 😂",
"random_no": "Non 🔔",
"help_yes": "Oui 🤝",
"help_no": "Non",
"faith": "Foi et révérence 🙏",
"showing_off": "Se faire remarquer 😎",

"perfect": "🏆 SCORE PARFAIT ! Excellent !",
"quiz_finished": "👏 Quiz terminé ! Continuez à apprendre et à servir !",

"mass_instruction": "Placez les étapes dans le bon ordre.",
"mass_instruction2": "Touchez chaque élément dans le bon ordre.",
"select_all": "Sélectionnez d'abord tous les éléments.",
"mass_correct": "🏆 Excellent !",
"mass_wrong": "Pas encore. Réessayez.",

"memory_instruction": "Trouvez toutes les paires.",
"memory_win": "🎉 Excellente mémoire !",

"reaction_instruction": "Attendez l'écran vert puis touchez-le rapidement.",
"reaction_start": "Commencer",
"wait": "ATTENDEZ...",
"click_now": "MAINTENANT !",
"too_early": "Trop tôt !",
"try_again": "Réessayez.",
"reaction_result": "Score de réaction :",

"object_q": "Quel objet est associé à la liturgie eucharistique ?",
"object_q1": "Quel objet contient le vin eucharistique ?",
"object_q2": "Quel objet contient les hosties consacrées ?",
"object_q3": "Quel objet est utilisé pour l'encens ?",
"object_q4": "Quel objet est porté en procession?",
"object_finished": "🏆 Défi des objets terminé !",

"challenge_q": "Un servant doit-il être prêt et à l'heure ?",
"challenge_q1": "Que vaut-il mieux faire avant la Messe ?",
"challenge_q2": "Que doit faire un servant lorsqu'un coordinateur donne une instruction ?",
"challenge_q3": "Que doit faire un servant avant de servir ?",
"challenge_q4": "Comment traiter les autres servants ?",
"challenge_q5": "Quelle attitude doit avoir un servant ?",
"challenge_q6": "Que faire en cas de doute ?",

"arrive_early": "Arriver tôt",
"arrive_late": "Arriver tard",
"listen": "Écouter attentivement",
"ignore": "Ignorer",
"pray": "Prier",
"play": "Jouer",
"help": "S'entraider",
"competition": "Chercher l'attention",
"humble": "Être humble",
"showoff": "Se mettre en avant",
"ask_help": "Demander de l'aide",
"guess": "Deviner",

"challenge_finished": "🏆 Défi terminé ! Bravo !",

"rank_title": "Rang du servant",
"total_xp": "XP total",

"rank_beginner": "Débutant",
"rank_beginner_desc": "Continuez à apprendre. Chaque servant commence quelque part.",
"rank_server": "Servant d'autel",
"rank_server_desc": "Vous développez de bonnes habitudes.",
"rank_faithful": "Servant fidèle",
"rank_faithful_desc": "Excellent progrès.",
"rank_senior": "Servant senior",
"rank_senior_desc": "Très bonnes connaissances et expérience.",
"rank_master": "Maître servant",
"rank_master_desc": "Remarquable ! Continuez à grandir dans la foi.",

"gallery": "Photos",
"gallery_sub": "Photos de la paroisse Mary Immaculate.",

"contact_title": "Contacter la paroisse",
"contact_note":
"Pour les horaires, conditions et formations actuels, contactez directement la paroisse.",
"official_page": "Page officielle du diocèse",

"footer":
"Servir avec foi. Servir avec joie. Servir avec amour. ❤️",

"footer_note":
"Projet éducatif. Suivez toujours la formation et les instructions officielles de votre paroisse."
},


"el": {

"nav_home": "Αρχική",
"nav_parish": "Ενορία",
"nav_servers": "Υπηρέτες",
"nav_lessons": "Μαθήματα",
"nav_games": "Παιχνίδια",

"breadcrumb": "Αρχική › Κατάλογος › Ενορίες ›",
"hero_badge": "Ενορία Mary Immaculate",

"parish_name": "Ενορία Mary Immaculate - Πόλη Dasmariñas",
"location": "Salawag, Πόλη Dasmariñas, Cavite, Φιλιππίνες",

"hero_text":
"Καλώς ήρθατε στη διακονία των υπηρετών του ιερού της MIP Salawag — ένας χώρος για να μαθαίνουμε, να προσευχόμαστε, να υπηρετούμε και να μεγαλώνουμε στην πίστη.",

"server_button": "Υπηρέτες του Ιερού",
"game_button": "Κέντρο Παιχνιδιών",

"parish_profile": "Προφίλ Ενορίας",
"parish_profile_sub":
"Μάθετε για την ενορία, την προστάτιδα, τους ιερείς και τις υπηρεσίες της.",

"patron": "Προστάτιδα του Ναού",
"patron_name": "Παναγία της Αμώμου Συλλήψεως",
"feast": "Εορτή: 8 Δεκεμβρίου",
"feast_short": "8 Δεκεμβρίου",

"official_note_title": "Επίσημη Πληροφορία",
"official_note":
"Τα προγράμματα και οι πληροφορίες μπορεί να αλλάξουν. Επιβεβαιώστε τα τρέχοντα στοιχεία με την ενορία.",

"parish_facts": "Πληροφορίες Ενορίας",
"parish_label": "Ενορία",
"location_label": "Τοποθεσία",
"patron_label": "Προστάτιδα",
"feast_label": "Εορτή",
"phone_label": "Τηλέφωνο",
"mobile_label": "Κινητό",

"priests": "Ιερείς",
"parish_priest": "Εφημέριος",
"parochial_vicar": "Εφημέριος συνεργάτης",

"services": "Υπηρεσίες",
"services_sub":
"Κατηγορίες υπηρεσιών που αναφέρονται στον κατάλογο της ενορίας.",

"mass": "Θεία Λειτουργία",
"baptism": "Βάπτισμα",
"confession": "Εξομολόγηση",
"wedding": "Γάμος",
"confirmation": "Χρίσμα",
"funeral": "Κηδεία",
"first_communion": "Πρώτη Θεία Κοινωνία",
"blessing": "Ευλογία",
"anointing": "Ευχέλαιο",

"schedule_warning_title": "Σημείωση Προγράμματος",
"schedule_warning":
"Τα προγράμματα μπορεί να αλλάξουν. Επικοινωνήστε με την ενορία για τις τελευταίες πληροφορίες.",

"server_title": "Διακονία των Υπηρετών του Ιερού",
"server_sub":
"Υπηρετούμε τον Χριστό στο ιερό με πίστη, πειθαρχία, χαρά και αγάπη.",

"prayer": "Προσευχή",
"prayer_text": "Η υπηρεσία αρχίζει με καρδιά προσευχής.",
"attention": "Προσοχή",
"attention_text": "Ακούτε προσεκτικά και ακολουθείτε τις οδηγίες.",
"teamwork": "Ομαδικότητα",
"teamwork_text": "Βοηθάτε και σέβεστε τους άλλους υπηρέτες.",
"service": "Υπηρεσία",
"service_text": "Υπηρετείτε τον Θεό και την ενοριακή κοινότητα.",

"academy": "Ακαδημία Υπηρετών του Ιερού",
"academy_sub":
"Μάθετε τα βασικά και ακολουθείτε πάντα την επίσημη εκπαίδευση της ενορίας.",

"lesson1_title": "Μάθημα 1 — Η Θεία Λειτουργία",
"lesson1":
"Η Θεία Λειτουργία είναι η κεντρική πράξη της καθολικής λατρείας. Οι υπηρέτες βοηθούν τους λειτουργούς ώστε η λειτουργία να τελείται με τάξη και ευλάβεια.",
"lesson1_a": "Γνωρίζετε την αποστολή σας.",
"lesson1_b": "Παραμένετε προσεκτικοί.",
"lesson1_c": "Ακολουθείτε τις οδηγίες.",
"lesson1_d": "Παραμένετε προσευχόμενοι.",

"lesson2_title": "Μάθημα 2 — Λειτουργικά Ενδύματα",
"lesson2":
"Να σέβεστε τα λειτουργικά ενδύματα και να τα φοράτε σωστά.",

"lesson3_title": "Μάθημα 3 — Ιερά Αντικείμενα",

"lesson4_title": "Μάθημα 4 — Κεριά",
"lesson4":
"Μεταφέρετε τα κεριά προσεκτικά, περπατάτε αργά και ποτέ μην παίζετε με τη φωτιά.",

"lesson5_title": "Μάθημα 5 — Κώδωνες",
"lesson5":
"Οι κώδωνες χρησιμοποιούνται σε συγκεκριμένες στιγμές σύμφωνα με τη λειτουργική και ενοριακή πρακτική.",
"bell_rule":
"Οι κώδωνες είναι για τη Θεία Λειτουργία, όχι για προσωπική συναυλία. 🔔",

"lesson6_title": "Μάθημα 6 — Θυμίαμα",
"lesson6":
"Όταν χρησιμοποιείται θυμίαμα, ακολουθείτε ακριβώς την εκπαίδευση του συντονιστή.",

"lesson7_title": "Μάθημα 7 — Στάση",
"posture1": "Στέκεστε σωστά.",
"posture2": "Περπατάτε ήρεμα.",
"posture3": "Αποφεύγετε περιττές συζητήσεις.",
"posture4": "Παραμένετε προσεκτικοί.",
"posture5": "Ακολουθείτε τις οδηγίες της ενορίας.",

"lesson8_title": "Μάθημα 8 — Ομαδικότητα",
"lesson8":
"Η υπηρεσία στο ιερό είναι ομαδική διακονία. Βοηθάτε και σέβεστε ο ένας τον άλλον.",

"lesson9_title": "Μάθημα 9 — Λάθη",
"lesson9":
"Τα λάθη συμβαίνουν κατά τη μάθηση. Παραμένετε ήρεμοι, ακούτε και συνεχίζετε.",

"lesson10_title": "Μάθημα 10 — Η Καρδιά της Υπηρεσίας",
"lesson10":
"Ο καλός υπηρέτης αναπτύσσει ταπεινοφροσύνη, πειθαρχία, υπευθυνότητα, προσευχή και αγάπη.",

"checklist_title": "Έλεγχος πριν από τη Θεία Λειτουργία",
"check1": "Έφτασα νωρίς.",
"check2": "Γνωρίζω την αποστολή μου.",
"check3": "Φοράω σωστά το ένδυμά μου.",
"check4": "Έχω ετοιμάσει ό,τι χρειάζομαι.",
"check5": "Το κινητό μου είναι αθόρυβο.",
"check6": "Προσευχήθηκα πριν υπηρετήσω.",
"check7": "Είμαι έτοιμος να υπηρετήσω.",

"games_title": "Κέντρο Παιχνιδιών Υπηρετών",
"games_sub":
"Μάθετε παίζοντας. Οι πόντοι XP και η πρόοδός σας αποθηκεύονται στον browser.",

"game_quiz": "Κουίζ Υπηρέτη",
"game_quiz_desc": "Δοκιμάστε τις βασικές σας γνώσεις.",

"game_mass": "Σειρά της Θείας Λειτουργίας",
"game_mass_desc": "Βάλτε τα στάδια της Θείας Λειτουργίας στη σωστή σειρά.",

"game_memory": "Ιερή Μνήμη",
"game_memory_desc": "Βρείτε τα ίδια σύμβολα.",

"game_reaction": "Αντίδραση Υπηρέτη",
"game_reaction_desc": "Δοκιμάστε την ταχύτητα αντίδρασής σας.",

"game_objects": "Ιερά Αντικείμενα",
"game_objects_desc": "Αναγνωρίστε σημαντικά λειτουργικά αντικείμενα.",

"game_challenge": "Πρόκληση Υπηρέτη",
"game_challenge_desc": "Μια γρήγορη πρόκληση για την υπηρεσία.",

"play_again": "Ξανά",
"close": "Κλείσιμο",
"restart": "Επανεκκίνηση",
"start": "Έναρξη",
"check_answer": "Έλεγχος",

"q1": "Πρέπει ο υπηρέτης να φτάνει νωρίς;",
"q2": "Τι πρέπει να κάνεις μετά από ένα λάθος;",
"q3": "Οι κώδωνες είναι για τυχαία διασκέδαση;",
"q4": "Πρέπει οι υπηρέτες να βοηθούν ο ένας τον άλλον;",
"q5": "Τι πρέπει να καθοδηγεί την υπηρεσία σου;",

"yes": "Ναι 👍",
"no": "Όχι 😴",
"stay_calm": "Μείνε ήρεμος 😇",
"panic": "Πανικός 🏃",
"random_yes": "Ναι 😂",
"random_no": "Όχι 🔔",
"help_yes": "Ναι 🤝",
"help_no": "Όχι",
"faith": "Πίστη και ευλάβεια 🙏",
"showing_off": "Επίδειξη 😎",

"perfect": "🏆 ΤΕΛΕΙΟ ΣΚΟΡ! Εξαιρετικά!",
"quiz_finished": "👏 Το κουίζ ολοκληρώθηκε! Συνεχίστε να μαθαίνετε και να υπηρετείτε!",

"mass_instruction": "Βάλτε τα στάδια στη σωστή σειρά.",
"mass_instruction2": "Πατήστε κάθε στοιχείο με τη σωστή σειρά.",
"select_all": "Επιλέξτε πρώτα όλα τα στοιχεία.",
"mass_correct": "🏆 Εξαιρετικά!",
"mass_wrong": "Όχι ακόμη. Δοκιμάστε ξανά.",

"memory_instruction": "Βρείτε όλα τα ζευγάρια.",
"memory_win": "🎉 Εξαιρετική μνήμη!",

"reaction_instruction": "Περιμένετε την πράσινη οθόνη και πατήστε γρήγορα.",
"reaction_start": "Έναρξη",
"wait": "ΠΕΡΙΜΕΝΕ...",
"click_now": "ΠΑΤΗΣΕ ΤΩΡΑ!",
"too_early": "Πολύ νωρίς!",
"try_again": "Δοκιμάστε ξανά.",
"reaction_result": "Σκορ αντίδρασης:",

"object_q": "Ποιο αντικείμενο σχετίζεται με την Ευχαριστιακή Λειτουργία;",
"object_q1": "Ποιο αντικείμενο χρησιμοποιείται για τον ευχαριστιακό οίνο;",
"object_q2": "Ποιο αντικείμενο περιέχει τους καθαγιασμένους άρτους;",
"object_q3": "Ποιο αντικείμενο χρησιμοποιείται για το θυμίαμα;",
"object_q4": "Ποιο αντικείμενο μεταφέρεται στην πομπή;",
"object_finished": "🏆 Η πρόκληση αντικειμένων ολοκληρώθηκε!",

"challenge_q": "Πρέπει ο υπηρέτης να είναι έτοιμος και στην ώρα του;",
"challenge_q1": "Τι είναι καλύτερο πριν από τη Θεία Λειτουργία;",
"challenge_q2": "Τι πρέπει να κάνει ο υπηρέτης όταν ο συντονιστής δίνει οδηγίες;",
"challenge_q3": "Τι πρέπει να κάνει πριν υπηρετήσει;",
"challenge_q4": "Πώς πρέπει να φέρεται στους άλλους υπηρέτες;",
"challenge_q5": "Ποια στάση πρέπει να έχει;",
"challenge_q6": "Τι πρέπει να κάνει όταν δεν είναι σίγουρος;",

"arrive_early": "Να φτάσει νωρίς",
"arrive_late": "Να φτάσει αργά",
"listen": "Να ακούσει προσεκτικά",
"ignore": "Να αγνοήσει",
"pray": "Να προσευχηθεί",
"play": "Να παίξει",
"help": "Να βοηθήσει",
"competition": "Να ανταγωνιστεί",
"humble": "Να είναι ταπεινός",
"showoff": "Να επιδειχθεί",
"ask_help": "Να ζητήσει βοήθεια",
"guess": "Να μαντέψει",

"challenge_finished": "🏆 Η πρόκληση ολοκληρώθηκε!",

"rank_title": "Βαθμίδα Υπηρέτη",
"total_xp": "Συνολικό XP",

"rank_beginner": "Αρχάριος",
"rank_beginner_desc": "Συνεχίστε να μαθαίνετε. Κάθε υπηρέτης ξεκινά από κάπου.",
"rank_server": "Υπηρέτης του Ιερού",
"rank_server_desc": "Αναπτύσσετε καλές συνήθειες υπηρεσίας.",
"rank_faithful": "Πιστός Υπηρέτης",
"rank_faithful_desc": "Εξαιρετική πρόοδος.",
"rank_senior": "Έμπειρος Υπηρέτης",
"rank_senior_desc": "Ισχυρές γνώσεις και εμπειρία.",
"rank_master": "Μάστερ Υπηρέτης",
"rank_master_desc": "Εξαιρετικά! Συνεχίστε να μεγαλώνετε στην πίστη.",

"gallery": "Φωτογραφίες",
"gallery_sub": "Φωτογραφίες από την ενορία Mary Immaculate.",

"contact_title": "Επικοινωνία με την Ενορία",
"contact_note":
"Για τα τρέχοντα προγράμματα, απαιτήσεις και εκπαίδευση, επικοινωνήστε απευθείας με την ενορία.",

"official_page": "Επίσημη Σελίδα Επισκοπής",

"footer":
"Υπηρετήστε με πίστη. Υπηρετήστε με χαρά. Υπηρετήστε με αγάπη. ❤️",

"footer_note":
"Εκπαιδευτικό έργο. Ακολουθείτε πάντα την επίσημη εκπαίδευση και τις οδηγίες της ενορίας."
},


"la": {

"nav_home": "Domus",
"nav_parish": "Paroecia",
"nav_servers": "Ministrantes",
"nav_lessons": "Lectiones",
"nav_games": "Ludi",

"breadcrumb": "Domus › Directoria › Paroeciae ›",
"hero_badge": "Paroecia Mariae Immaculatae",

"parish_name": "Paroecia Mariae Immaculatae - Civitas Dasmariñas",
"location": "Salawag, Civitas Dasmariñas, Cavite, Philippinae",

"hero_text":
"Salvete ad ministerium ministrantium altaris MIP Salawag — locum ad discendum, orandum, serviendum atque in fide crescendum.",

"server_button": "Ministrantes",
"game_button": "Centrum Ludorum",

"parish_profile": "Profilum Paroeciae",
"parish_profile_sub":
"Disce de paroecia, patrona, sacerdotibus et ministeriis.",

"patron": "Patrona Ecclesiae",
"patron_name": "Beata Maria Virgo Immaculata Concepta",
"feast": "Festum: VIII Decembris",
"feast_short": "VIII Decembris",

"official_note_title": "Informatio Officialis",
"official_note":
"Horaria et informationes mutari possunt. Quaeso confirma notitias recentes apud paroeciam.",

"parish_facts": "Informationes Paroeciae",
"parish_label": "Paroecia",
"location_label": "Locus",
"patron_label": "Patrona",
"feast_label": "Festum",
"phone_label": "Telephonum",
"mobile_label": "Mobile",

"priests": "Sacerdotes",
"parish_priest": "Parochus",
"parochial_vicar": "Vicarius Paroecialis",

"services": "Ministeria",
"services_sub":
"Genera ministeriorum in directorio paroeciae indicata.",

"mass": "Missa",
"baptism": "Baptismus",
"confession": "Confessio",
"wedding": "Matrimonium",
"confirmation": "Confirmatio",
"funeral": "Exsequiae",
"first_communion": "Prima Communio",
"blessing": "Benedictio",
"anointing": "Unctio Infirmorum",

"schedule_warning_title": "Notitia de Horariis",
"schedule_warning":
"Horaria mutari possunt. Contactum cum paroecia fac pro recentioribus informationibus.",

"server_title": "Ministerium Ministrantium Altaris",
"server_sub":
"Christo ad altare servimus cum fide, disciplina, gaudio et caritate.",

"prayer": "Oratio",
"prayer_text": "Servitium a corde orante incipit.",
"attention": "Attentio",
"attention_text": "Attente audi et instructiones sequere.",
"teamwork": "Concordia",
"teamwork_text": "Sociis ministrantibus adiuva et eos reverere.",
"service": "Servitium",
"service_text": "Deo et communitati paroeciali servi.",

"academy": "Academia Ministrantium",
"academy_sub":
"Fundamenta disce et semper formationem officialem paroeciae tuae sequere.",

"lesson1_title": "Lectio I — Missa",
"lesson1":
"Missa est actus centralis cultus catholici. Ministrantes ministros adiuvant ut liturgia ordine et reverentia celebretur.",
"lesson1_a": "Munus tuum cognosce.",
"lesson1_b": "Attende diligenter.",
"lesson1_c": "Instructiones sequere.",
"lesson1_d": "In oratione permane.",

"lesson2_title": "Lectio II — Vestimenta Sacra",
"lesson2":
"Vestimenta liturgica reverere. Munda ea serva et recte indue.",

"lesson3_title": "Lectio III — Res Sacrae",

"lesson4_title": "Lectio IV — Candelae",
"lesson4":
"Candelas diligenter porta, lente ambula et numquam cum igne lude.",

"lesson5_title": "Lectio V — Campanae",
"lesson5":
"Campanae certis momentis secundum usum liturgicum et paroecialem adhiberi possunt.",
"bell_rule":
"Campanae sunt pro Missa, non pro concentu personali tuo. 🔔",

"lesson6_title": "Lectio VI — Incensum",
"lesson6":
"Cum incensum adhibetur, exactam institutionem coordinatoris sequere. Cum igne numquam experire.",

"lesson7_title": "Lectio VII — Habitus",
"posture1": "Recte sta.",
"posture2": "Tranquille ambula.",
"posture3": "Locutiones superfluas evita.",
"posture4": "Attentus mane.",
"posture5": "Instructiones paroeciae sequere.",

"lesson8_title": "Lectio VIII — Concordia",
"lesson8":
"Ministerium altaris est ministerium communitatis. Invicem adiuvate et reveremini.",

"lesson9_title": "Lectio IX — Errores",
"lesson9":
"Errores dum discimus accidunt. Tranquillus mane, audi et perge.",

"lesson10_title": "Lectio X — Cor Servitii",
"lesson10":
"Bonus ministrans humilitatem, disciplinam, responsabilitatem, orationem et caritatem colit.",

"checklist_title": "Index Ante Missam",
"check1": "Mature adveni.",
"check2": "Munus meum cognosco.",
"check3": "Vestimentum meum recte indui.",
"check4": "Omnia necessaria paravi.",
"check5": "Telephonum meum silentium habet.",
"check6": "Ante servitium oravi.",
"check7": "Ad serviendum paratus sum.",

"games_title": "Centrum Ludorum Ministrantium",
"games_sub":
"Disce ludendo. XP et progressus tuus in navigatro servantur.",

"game_quiz": "Quiz Ministrantis",
"game_quiz_desc": "Scientiam tuam fundamentalem proba.",

"game_mass": "Ordo Missae",
"game_mass_desc": "Partes Missae ordine recto pone.",

"game_memory": "Memoria Sacra",
"game_memory_desc": "Symbola paria invenies.",

"game_reaction": "Reactio Ministrantis",
"game_reaction_desc": "Celeritatem reactionis tuae proba.",

"game_objects": "Res Sacrae",
"game_objects_desc": "Res liturgicas importantes agnosce.",

"game_challenge": "Certamen Ministrantis",
"game_challenge_desc": "Certamen breve de servitio.",

"play_again": "Iterum Lude",
"close": "Claude",
"restart": "Renova",
"start": "Incipe",
"check_answer": "Verifica",

"q1": "Num ministrans mature advenire debet?",
"q2": "Quid facias post errorem?",
"q3": "Num campanae sunt ad ludum fortuitum?",
"q4": "Num ministrantes se invicem adiuvare debent?",
"q5": "Quid servitium tuum dirigere debet?",

"yes": "Ita 👍",
"no": "Non 😴",
"stay_calm": "Tranquillus mane 😇",
"panic": "Panica 🏃",
"random_yes": "Ita 😂",
"random_no": "Non 🔔",
"help_yes": "Ita 🤝",
"help_no": "Non",
"faith": "Fides et reverentia 🙏",
"showing_off": "Gloriatio 😎",

"perfect": "🏆 PERFECTUM! Optime!",
"quiz_finished": "👏 Quiz finitum! Perge discere et servire!",

"mass_instruction": "Partes ordine recto pone.",
"mass_instruction2": "Unumquodque elementum ordine recto tange.",
"select_all": "Primum omnia elementa elige.",
"mass_correct": "🏆 Optime! Ordinem Missae nosti!",
"mass_wrong": "Nondum rectum. Iterum conare.",

"memory_instruction": "Omnia paria invenies.",
"memory_win": "🎉 Memoria optima!",

"reaction_instruction":
"Exspecta velum viride, deinde quam celerrime tange.",
"reaction_start": "Incipe",
"wait": "EXSPECTA...",
"click_now": "NUNC TANGE!",
"too_early": "Nimis mature!",
"try_again": "Iterum conare.",
"reaction_result": "Puncta reactionis:",

"object_q": "Quae res ad liturgiam Eucharisticam pertinet?",
"object_q1": "Quae res vinum Eucharisticum continet?",
"object_q2": "Quae res hostias consecratas continet?",
"object_q3": "Quae res ad incensum adhibetur?",
"object_q4": "Quae res in processione fertur?",
"object_finished": "🏆 Certamen rerum sacrarum finitum!",

"challenge_q": "Num ministrans paratus et punctualis esse debet?",
"challenge_q1": "Quid melius est ante Missam?",
"challenge_q2": "Quid faciat ministrans cum coordinator instructiones dat?",
"challenge_q3": "Quid faciat antequam serviat?",
"challenge_q4": "Quomodo alios ministrantes tractet?",
"challenge_q5": "Quem habitum ministrans habeat?",
"challenge_q6": "Quid faciat cum dubitat?",

"arrive_early": "Mature advenire",
"arrive_late": "Serius advenire",
"listen": "Attente audire",
"ignore": "Ignorare",
"pray": "Orare",
"play": "Ludere",
"help": "Invicem adiuvare",
"competition": "Attentionem quaerere",
"humble": "Humilis esse",
"showoff": "Gloriari",
"ask_help": "Auxilium petere",
"guess": "Fortuito respondere",

"challenge_finished":
"🏆 Certamen finitum! Optime!",

"rank_title": "Gradus Ministrantis",
"total_xp": "XP Totum",

"rank_beginner": "Tiro",
"rank_beginner_desc": "Perge discere. Omnis ministrans aliquando incipit.",
"rank_server": "Ministrans",
"rank_server_desc": "Bonos mores servitii discis.",
"rank_faithful": "Ministrans Fidelis",
"rank_faithful_desc": "Progressus optimus.",
"rank_senior": "Ministrans Senior",
"rank_senior_desc": "Scientia et experientia bona.",
"rank_master": "Magister Ministrantium",
"rank_master_desc": "Praeclare! Perge crescere in fide et servitio.",

"gallery": "Imagines",
"gallery_sub": "Imagines ex paroecia Mariae Immaculatae.",

"contact_title": "Contactus Paroeciae",
"contact_note":
"Pro horariis, requisitis et formatione recentibus, directe paroeciam contacta.",

"official_page": "Pagina Officialis Dioecesis",

"footer":
"Servi cum fide. Servi cum gaudio. Servi cum caritate. ❤️",

"footer_note":
"Opus paedagogicum. Semper institutionem et instructiones officiales paroeciae tuae sequere."
}

}


# ============================================================
# ROUTE
# ============================================================

@app.route("/")
def home():

    lang = request.args.get("lang", "en")

    allowed_languages = [
        "en",
        "fil",
        "fr",
        "el",
        "la"
    ]

    if lang not in allowed_languages:
        lang = "en"

    t = TRANSLATIONS[lang]

    return render_template_string(
        HTML,
        lang=lang,
        t=t
    )


# ============================================================
# OPEN BROWSER
# ============================================================

def open_browser():

    webbrowser.open(
        "http://127.0.0.1:5000"
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("====================================================")
    print("        MIP SALAWAG ALTAR SERVERS WEBSITE")
    print("====================================================")
    print()
    print("Languages:")
    print("  🇬🇧 English")
    print("  🇵🇭 Filipino")
    print("  🇫🇷 French")
    print("  🇬🇷 Greek")
    print("  🇻🇦 Latin")
    print()
    print("Games:")
    print("  🧠 Altar Server Quiz")
    print("  ⛪ Order of the Mass")
    print("  🕯️ Sacred Memory")
    print("  ⚡ Reaction Game")
    print("  🏺 Sacred Objects")
    print("  🏆 Server Challenge")
    print()
    print("Website is starting...")
    print()
    print("Open:")
    print("http://127.0.0.1:5000")
    print()
    print("Press CTRL+C to stop.")
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
