<h2><a href="https://codeforces.com/contest/1141/problem/B" target="_blank" rel="noopener noreferrer">1141B — Maximal Continuous Rest</a></h2>

| | |
|---|---|
| **Difficulty** | 900 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1141B](https://codeforces.com/contest/1141/problem/B) |

## Topics
`implementation`

---

## Problem Statement

<div class="header"><div class="title">B. Maximal Continuous Rest</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Each day in Berland consists of $$$n$$$ hours. Polycarp likes time management. That's why he has a fixed schedule for each day — it is a sequence $$$a_1, a_2, \dots, a_n$$$ (each $$$a_i$$$ is either $$$0$$$ or $$$1$$$), where $$$a_i=0$$$ if Polycarp works during the $$$i$$$-th hour of the day and $$$a_i=1$$$ if Polycarp rests during the $$$i$$$-th hour of the day.</p><p>Days go one after another endlessly and Polycarp uses the same schedule for each day.</p><p>What is the maximal number of continuous hours during which Polycarp rests? It is guaranteed that there is at least one working hour in a day.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains $$$n$$$ ($$$1 \le n \le 2\cdot10^5$$$) — number of hours per day.</p><p>The second line contains $$$n$$$ integer numbers $$$a_1, a_2, \dots, a_n$$$ ($$$0 \le a_i \le 1$$$), where $$$a_i=0$$$ if the $$$i$$$-th hour in a day is working and $$$a_i=1$$$ if the $$$i$$$-th hour is resting. It is guaranteed that $$$a_i=0$$$ for at least one $$$i$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Print the maximal number of continuous hours during which Polycarp rests. Remember that you should consider that days go one after another endlessly and Polycarp uses the same schedule for each day.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0005013936144464248" id="id0019347579461605258" class="input-output-copier">Copy</div></div><pre id="id0005013936144464248">5
1 0 1 0 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007128794841012951" id="id0035839944253766187" class="input-output-copier">Copy</div></div><pre id="id007128794841012951">2
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0029746206097716477" id="id0035417490820724795" class="input-output-copier">Copy</div></div><pre id="id0029746206097716477">6
0 1 0 1 1 0
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006798714915871672" id="id004852384266590586" class="input-output-copier">Copy</div></div><pre id="id006798714915871672">2
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0040549741845224285" id="id008513879842523622" class="input-output-copier">Copy</div></div><pre id="id0040549741845224285">7
1 0 1 1 1 0 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id004651698217904111" id="id005425055920386265" class="input-output-copier">Copy</div></div><pre id="id004651698217904111">3
</pre></div><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008037483366180034" id="id00011636717768858884" class="input-output-copier">Copy</div></div><pre id="id008037483366180034">3
0 0 0
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0048132252299828016" id="id005668549662097896" class="input-output-copier">Copy</div></div><pre id="id0048132252299828016">0
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first example, the maximal rest starts in last hour and goes to the first hour of the next day.</p><p>In the second example, Polycarp has maximal rest from the $$$4$$$-th to the $$$5$$$-th hour.</p><p>In the third example, Polycarp has maximal rest from the $$$3$$$-rd to the $$$5$$$-th hour.</p><p>In the fourth example, Polycarp has no rest at all.</p></div>