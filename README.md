<h1 align="left">Дипломная работа</h1>
<h3 align="left">Сравнение различных библиотек для визуализации данных: Matplotlib, Seaborn и Plotly: Создать набор визуализаций с использованием Matplotlib, Seaborn и Plotly, сравнить их функциональность и удобство использования.</h3>
<body lang=RU link=blue vlink="#954F72" style='tab-interval:35.4pt'>

<div class=WordSection1>

<h4 align="left">Обзор проекта</h4>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Этот репозиторий
содержит программный код для создания графиков некоторых видов на основе
финансовых данных и сравнения библиотек Matplotlib, Seaborn и Plotly. Также в
работе используется Pandas DataFrames.<o:p></o:p></span></p>

<h4 align="left">Структура проекта</h4>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Проект включает
следующие файлы:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>plt</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> – использует библиотеку Matplotlib<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>sns</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> – использует библиотеку Seaborn<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>И 3 файла с
библиотекой Plotly:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>px</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>line</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> – с линейным графиком<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>px</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>bar</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> – с гистограммой<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>px</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>cand</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> – с свечным графиком<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Также есть 2 файла в
формате .</span><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>csv</span><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> </span><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>для использования в качестве примера:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Файл </span><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>ohlc</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>csv</span></i></b><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> содержит данные об изменение рынка с течением
времени:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Date</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>, </span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Open</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>, </span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>High</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>, </span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Low</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>, </span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Close</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>, </span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Adj</span></i><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'> </span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>Close</span></i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> </span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>– Дата, цены открытия,
максимума, минимума, закрытия и приложение к закрытию.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Файл </span><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>budget</span></i></b><b><i><span style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>_</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>data</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>csv</span></i></b><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> </span><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>содержит данные изменения бюджета компании за
год:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>Date, Profit/Losses</span></i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>
– </span><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:
"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Дата</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>,
</span><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:
"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Прибыль</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>/</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Убытки</span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'><o:p></o:p></span></i></p>

<h4 align="left">Логика работы</h4>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Сначала читаются
данные из файлов.csv и затем на их основе строятся графики, которые выводятся в
отдельном окне, либо в браузере.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpFirst style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l2 level1 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Визуализация в </span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>plt</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>py</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>:</span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'><o:p></o:p></span></p>

<p class=MsoListParagraphCxSpLast style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>1.1<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Линейный график цены закрытия с данными из загруженного файла - </span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>ohlc</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>csv</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>:</span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shapetype
 id="_x0000_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t"
 path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="Рисунок_x0020_2" o:spid="_x0000_i1035" type="#_x0000_t75"
 style='width:467.4pt;height:242.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="Диплом%20(2).files/image001.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=779 height=404
src="image001.png" v:shapes="Рисунок_x0020_2"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>С помощью функций <i>to_datetime(),
set_index()</i> преобразован </span><i><span lang=EN-US style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>df</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>[‘</span></i><i><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>Date</span></i><i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold'>’].</span></i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> В функции </span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>plot</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> </span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>параметром <i>alpha</i>
можно выбрать прозрачность линии, параметр </span><i><span style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>linewidth</span></i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'> контролирует ширину линии, параметром </span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-style:italic'>color</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'> </span><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-style:
italic'>можно задать цвет.<span style='mso-bidi-font-weight:bold'><o:p></o:p></span></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>1.2<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Линейные графики со значениями всех столбцов из </span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>ohlc</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>csv</span></i><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'> </span></i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>с помощью функции<i> subplots()</i>:<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Рисунок_x0020_3" o:spid="_x0000_i1034" type="#_x0000_t75" style='width:468pt;
 height:302.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="image003.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=780 height=504
src="image003.png" v:shapes="Рисунок_x0020_3"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>В функции <i>legend() </i>параметр
</span><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>loc</span><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> указывает местоположение легенды в графике:<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpFirst style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l3 level1 lfo11;tab-stops:list 36.0pt;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:Symbol;
mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-style:italic'><span style='mso-list:Ignore'>·<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'>«upper left», «upper right», «lower left» и
«lower right» — для размещения легенды в соответствующих углах.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l3 level1 lfo11;tab-stops:list 36.0pt;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:Symbol;
mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-style:italic'><span style='mso-list:Ignore'>·<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'>«upper center», «lower center», «center left» и
«center right» — для размещения легенды в центре соответствующего края осей или
фигуры.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpMiddle style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l3 level1 lfo11;tab-stops:list 36.0pt;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:Symbol;
mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-style:italic'><span style='mso-list:Ignore'>·<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'>«center» — для размещения легенды в центре осей
или фигуры.<o:p></o:p></span></p>

<p class=MsoListParagraphCxSpLast style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l3 level1 lfo11;tab-stops:list 36.0pt;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:Symbol;
mso-fareast-font-family:Symbol;mso-bidi-font-family:Symbol;color:#1F2328;
mso-fareast-language:RU;mso-bidi-font-style:italic'><span style='mso-list:Ignore'>·<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-style:italic'>«best» — для размещения легенды в месте, которое
минимизирует перекрытие с другим содержимым.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>1.3<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Гистограмма с данными из </span><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>budget</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>_</span></i><i><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>data</span></i><i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold'>.</span></i><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>csv</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>:</span></i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><i
style='mso-bidi-font-style:normal'><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Рисунок_x0020_4" o:spid="_x0000_i1033" type="#_x0000_t75" style='width:468pt;
 height:233.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="image005.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=780 height=389
src="image005.png" v:shapes="Рисунок_x0020_4"><![endif]></span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'><o:p></o:p></span></i></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
margin-left:18.0pt;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>1.4 Круговая диаграмма
с данными введенными вручную, записанные в переменные в виде списка:<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Рисунок_x0020_1" o:spid="_x0000_i1032" type="#_x0000_t75" style='width:309pt;
 height:229.2pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="image007.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=515 height=382
src="image007.png" v:shapes="Рисунок_x0020_1"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>В библиотеке Matplotlib,
чтобы воспроизвести разнообразные цвета в диаграмме, можно использовать </span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Numpy</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> </span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>для генерации цветов,
либо создав переменную со списком цветов в формате RGB или других:<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Рисунок_x0020_14" o:spid="_x0000_i1031"
 type="#_x0000_t75" style='width:289.8pt;height:222.6pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="image009.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=483 height=371
src="image009.png" v:shapes="Рисунок_x0020_14"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoListParagraphCxSpFirst style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;text-indent:-18.0pt;line-height:normal;mso-outline-level:
2;mso-list:l2 level1 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp; </span></span></span><![endif]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Визуализация в </span><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>sns</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>:</span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'><o:p></o:p></span></p>

<p class=MsoListParagraphCxSpLast style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold'><span style='mso-list:Ignore'>2.1<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span></i><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Линейный график с данными из </span><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>ohlc</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>c</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'><o:p></o:p></span></i></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Рисунок_x0020_11" o:spid="_x0000_i1030"
 type="#_x0000_t75" style='width:468pt;height:262.2pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="image011.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=780 height=437
src="image011.png" v:shapes="Рисунок_x0020_11"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>2.2<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Гистограмма<i> </i>с данными из </span><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>budget</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>_</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>data</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>.</span></i><i><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>csv</span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>В библиотеке Seaborn
есть несколько встроенных
стилей:&nbsp;darkgrid,&nbsp;whitegrid,&nbsp;dark,&nbsp;white и&nbsp;ticks.
Задать их можно с помощью&nbsp;<i>set_style(). </i>Параметры стиля управляют
свойствами, такими как цвет фона, включена ли сетка по умолчанию и ее цвет.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Цветовую палитру можно
выбрать с помощью параметра <i>palette</i>. Основные вариаций палитры:</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;deep</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>,</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;muted</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>,</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;pastel</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>,</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;bright</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>,</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;dark</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> и</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>&nbsp;colorblind</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>. Пример с <i>palette='viridis'</i>:<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Рисунок_x0020_6" o:spid="_x0000_i1029" type="#_x0000_t75" style='width:440.4pt;
 height:240pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="image013.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=734 height=400
src="image013.png" v:shapes="Рисунок_x0020_6"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Параметр </span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>hue</span></i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> позволяет задавать
каждому столбцу свой оттенок.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l2 level2 lfo1;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>2.3<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Круговая диаграмма<i> </i>с данными из </span><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>ohlc</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>csv</span></i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Также цветовую палитру
можно выбрать с функцией <i>color_palette()</i>, например, воспользовавшись <i>sns.color_palette(&quot;pastel&quot;)</i>:<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='mso-fareast-language:RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Рисунок_x0020_7" o:spid="_x0000_i1028" type="#_x0000_t75" style='width:393.6pt;
 height:312pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="image015.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=656 height=520
src="image015.png" v:shapes="Рисунок_x0020_7"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l4 level2 lfo5;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>3.1<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Визуализация в </span><b><i><span lang=EN-US style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU'>px</span></i></b><b><i><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>line</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'> </span></i></b><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>линейного графика<i>:</i><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Рисунок_x0020_12" o:spid="_x0000_i1027"
 type="#_x0000_t75" style='width:467.4pt;height:226.2pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="image017.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=779 height=377
src="image017.png" v:shapes="Рисунок_x0020_12"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Бибиотека </span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Plotly</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> </span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>позволяет создавать
графики в браузере. На ее базе построена библиотека Dash, она позволяет легко
создавать и делиться результатами анализа данных с помощью интерактивных
дашбордов, используя только код Python. Приложение Dash запускается с помощью
команды: <i>app = Dash(__name__).<o:p></o:p></i></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Затем, добавив фигуру в
атрибут&nbsp;<i>layout</i>&nbsp;нашего приложения внутри тега&nbsp;<i>div</i>:<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>app.layout =
html.Div(children=[dcc.Graph(figure=fig)]),</span></i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>и запустив: </span><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>app</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>.</span></i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>run</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>_</span></i><i><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>server</span></i><i><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold'>(),</span></i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> в терминале получаем
сообщение с ссылкой.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Для запуска приложения
в режиме отладки можно использовать команду: <i>debug=True, </i>для изменений
по мере внесения поправок в скрипт.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l4 level2 lfo5;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>3.2<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Визуализация в </span><b><i><span lang=EN-US style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU'>px</span></i></b><b><i><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>bar</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'> </span></i></b><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>гистограммы<i>:</i><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Рисунок_x0020_10" o:spid="_x0000_i1026"
 type="#_x0000_t75" style='width:467.4pt;height:224.4pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="image019.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=779 height=374
src="image019.png" v:shapes="Рисунок_x0020_10"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Гистограмма в </span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Plotly</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'> </span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>создается с помощью класса
<i>graph_objects</i> функцией <i>plotly.graph_objs.</i></span><i
style='mso-bidi-font-style:normal'> </i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>Figure</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>()</span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>, в которой передаются данные в параметр </span><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>data</span></i><i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>,</span></i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> в экземпляре plotly.graph_objs.</span><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>B</span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>ar.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Для оформления
заголовков используется метод <i>fig.update_layout()</i>, для названия осей
параметры</span> <i><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>x</span></i><i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold'>axis_title </span></i><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>и<i> yaxis_title, </i>параметр
</span><span lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>font</span><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'> в виде словаря – для выбора шрифта, его
размера и цвета: <o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>font=dict(family=&quot;Times
New Roman&quot;, size=20, color=&quot;Black&quot;)<o:p></o:p></span></i></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:54.0pt;mso-add-space:auto;text-indent:-36.0pt;line-height:
normal;mso-outline-level:2;mso-list:l4 level2 lfo5;background:white'><![if !supportLists]><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Segoe UI";color:#1F2328;mso-fareast-language:RU;
mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><span style='mso-list:
Ignore'>3.3<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>Визуализация в </span><b><i><span lang=EN-US style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU'>px</span></i></b><b><i><span style='font-size:14.0pt;mso-bidi-font-size:
18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU'>-</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>cand</span></i></b><b><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU'>.</span></i></b><b><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU'>py</span></i></b><b><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'> </span></i></b><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>свечного графика<i>:</i><o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Рисунок_x0020_13" o:spid="_x0000_i1025"
 type="#_x0000_t75" style='width:468.6pt;height:225.6pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="image021.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img border=0 width=781 height=376
src="image021.png" v:shapes="Рисунок_x0020_13"><![endif]></span><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>В построении свечного
графика также используется функция <i>plotly.graph_objs.</i></span><i
style='mso-bidi-font-style:normal'> </i><i><span lang=EN-US style='font-size:
14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;mso-fareast-language:
RU;mso-bidi-font-weight:bold'>Figure</span></i><i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold'>(), </span></i><span style='font-size:14.0pt;mso-bidi-font-size:18.0pt;
font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:bold;mso-bidi-font-style:
italic'>данные передаются<i> в</i> параметр<i> </i></span><i><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-ansi-language:EN-US;
mso-fareast-language:RU;mso-bidi-font-weight:bold'>data</span></i><i><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold'> </span></i><span style='font-size:14.0pt;
mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:
"Times New Roman";color:#1F2328;mso-fareast-language:RU;mso-bidi-font-weight:
bold;mso-bidi-font-style:italic'>в экземпляре<i> go.Candlestick<o:p></o:p></i></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Изменить цвет свечей
можно с помощью параметров <i>increasing_line_color</i> – для растущей свечи и <i>decreasing_line_color</i>
– для падающей свечи.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<h4 align="left">Заключение</h4>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Matplotlib известна
своим всеобъемлющим набором инструментов, благодаря чему очень гибка для
настраивания графика, но с его помощью может быть затруднительно построить
сложные графики.<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Seaborn создана на
основе Matplotlib, она упрощает процесс создания сложных статистических
графиков с помощью встроенных стилей и цветовых палитр. <o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'>Plotly, с другой
стороны, отличается своей направленностью на интерактивные и динамические
визуализации, что делает ее идеальной для веб-приложений и панелей мониторинга,
требующих взаимодействия с пользователем. <o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
line-height:normal;mso-outline-level:3;background:white'><b><u><span
style='font-size:13.5pt;font-family:"Arial",sans-serif;mso-fareast-font-family:
"Times New Roman";mso-fareast-language:RU'>Список необходимых библиотек:<o:p></o:p></span></u></b></p>

<p class=MsoNormal style='mso-margin-bottom-alt:auto;line-height:normal;
background:white'><span style='font-size:12.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'>matplotlib 3.9.2<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-bottom-alt:auto;line-height:normal;
background:white'><span style='font-size:12.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'>pandas 2.2.2<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-bottom-alt:auto;line-height:normal;
background:white'><span style='font-size:12.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'>plotly 5.24.1<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-bottom-alt:auto;line-height:normal;
background:white'><span style='font-size:12.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'>seaborn 0.13.2<o:p></o:p></span></p>

<p class=MsoNormal style='mso-margin-bottom-alt:auto;line-height:normal;
background:white'><span style='font-size:12.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU'>numpy 2.0.2<o:p></o:p></span></p>

<p class=MsoNormal align=center style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;text-align:center;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='mso-margin-top-alt:auto;mso-margin-bottom-alt:auto;
margin-left:18.0pt;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

<p class=MsoListParagraph style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;mso-add-space:auto;line-height:normal;mso-outline-level:2;background:white'><span
style='font-size:14.0pt;mso-bidi-font-size:18.0pt;font-family:"Segoe UI",sans-serif;
mso-fareast-font-family:"Times New Roman";color:#1F2328;mso-fareast-language:
RU;mso-bidi-font-weight:bold;mso-bidi-font-style:italic'><o:p>&nbsp;</o:p></span></p>

</div>

</body>
