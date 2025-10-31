// report.js - fetches/edits prompt docs via REST API, falls back to dummy data if API fails

const API_BASE = '/api'; // adjust if your server uses a different base path

// helpers
async function apiGet(path) {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`);
    return res.json();
}
async function apiPost(path, body) {
    const res = await fetch(`${API_BASE}${path}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
    if (!res.ok) {
        const txt = await res.text();
        throw new Error(`POST ${path} failed: ${res.status} ${txt}`);
    }
    return res.json();
}
async function apiPut(path, body) {
    const res = await fetch(`${API_BASE}${path}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
    if (!res.ok) {
        const txt = await res.text();
        throw new Error(`PUT ${path} failed: ${res.status} ${txt}`);
    }
    return res.json();
}

// UI elements
const strategyFilter = document.getElementById('strategyFilter');
const searchInput = document.getElementById('searchInput');
const downloadCsvBtn = document.getElementById('downloadCsv');
const regenBtn = document.getElementById('createPromptBtn');
const refreshBtn = document.getElementById('refreshBtn');

let DATA = []; // array of prompt documents
let chart = null;

// ---------- Fallback dummy generator ----------
const STRATEGIES = ["Naive_strategy", "FewShot_strategy", "CoT_strategy"];
function generateDummyPrompts(n = 50) {
    const rows = [];
    for (let i = 1; i <= n; i++) {
        const pid = i;
        const fid = Math.floor((i - 1) / 1) + 1;
        const strat = STRATEGIES[i % STRATEGIES.length];
        const correctness = Math.round((Math.random() * 0.6 + 0.2) * 100) / 100; // 0.2..0.8
        const mutation = Math.round((Math.random() * 0.6 + 0.2) * 100) / 100;
        const halluc = Math.round((Math.random() * 0.3) * 100) / 100;
        rows.push({
            Prompt_ID: pid,
            Function_ID: fid,
            Prompt_Text: `Example prompt text for function ${fid} (strategy ${strat})`,
            Prompt_Strategy: strat,
            Correctness_Score: correctness,
            Mutation_Score: mutation,
            Hallucination_Score: halluc,
            Post_Conditions: [],
        });
    }
    return rows;
}

// ---------- Data fetch & rendering ----------
async function fetchPrompts() {
    try {
        const json = await apiGet('/prompts'); // expects array of prompt docs
        // normalize (ensure numeric scores present)
        DATA = json.map(p => ({
            ...p,
            Correctness_Score: Number(p.Correctness_Score ?? p.correctness_score ?? 0),
            Mutation_Score: Number(p.Mutation_Score ?? p.mutation_score ?? 0),
            Hallucination_Score: Number(p.Hallucination_Score ?? p.hallucination_score ?? 0)
        }));
        console.info('Loaded prompts from API:', DATA.length);
    } catch (err) {
        console.warn('API unavailable or failed — using dummy data:', err.message);
        DATA = generateDummyPrompts(50);
    }
    renderSummary();
    renderTable();
}

function summarize(rows) {
    const groups = {};
    rows.forEach(r => {
        const strat = r.Prompt_Strategy || r.Prompt_Strategy;
        if (!groups[strat]) groups[strat] = { count: 0, corrSum: 0, mutSum: 0, hallSum: 0 };
        groups[strat].count++;
        groups[strat].corrSum += Number(r.Correctness_Score || 0);
        groups[strat].mutSum += Number(r.Mutation_Score || 0);
        groups[strat].hallSum += Number(r.Hallucination_Score || 0);
    });
    const out = {};
    for (const k of Object.keys(groups)) {
        const g = groups[k];
        out[k] = {
            total: g.count,
            avgCorrectness: Math.round(1000 * (g.corrSum / g.count)) / 1000,
            avgMutation: Math.round(1000 * (g.mutSum / g.count)) / 1000,
            avgHallucination: Math.round(1000 * (g.hallSum / g.count)) / 1000
        };
    }
    return out;
}

function renderSummary() {
    const s = summarize(DATA);
    const container = document.getElementById('summaryMetrics');
    container.innerHTML = '';
    Object.keys(s).forEach(strat => {
        const d = s[strat];
        const div = document.createElement('div');
        div.className = 'metric';
        div.innerHTML = `
      <div class="small" style="text-transform:capitalize">${strat.replace('_', ' ')}</div>
      <div class="num">${Math.round(d.avgCorrectness * 100)}% <span class="small" style="color:var(--muted);font-weight:500">correctness</span></div>
      <div class="small">Mut: <strong>${Math.round(d.avgMutation * 100)}%</strong> • Hall: <strong>${Math.round(d.avgHallucination * 100)}%</strong></div>
    `;
        container.appendChild(div);
    });

    // chart
    const labels = ['Correctness', 'Mutation', 'Hallucination'];
    const datasets = Object.keys(s).map((strat, idx) => ({
        label: strat.replace('_', ' '),
        data: [Math.round(s[strat].avgCorrectness * 100), Math.round(s[strat].avgMutation * 100), Math.round(s[strat].avgHallucination * 100)]
    }));
    const ctx = document.getElementById('summaryChart').getContext('2d');
    if (chart) chart.destroy();
    chart = new Chart(ctx, {
        type: 'bar',
        data: { labels, datasets },
        options: { responsive: true, scales: { y: { beginAtZero: true, max: 100 } } }
    });
}

function renderTable() {
    const tbody = document.querySelector('#resultsTable tbody');
    tbody.innerHTML = '';
    const strat = strategyFilter.value;
    const term = searchInput.value.trim().toLowerCase();
    const rows = DATA.filter(r => (strat === 'all' ? true : (r.Prompt_Strategy === strat)) &&
        (term === '' || String(r.Prompt_ID).includes(term) || String(r.Function_ID).includes(term) || (r.Prompt_Text && r.Prompt_Text.toLowerCase().includes(term))));
    rows.sort((a, b) => a.Prompt_ID - b.Prompt_ID);
    for (const r of rows) {
        const tr = document.createElement('tr');
        tr.dataset.promptId = r.Prompt_ID;
        tr.innerHTML = `
      <td>${r.Prompt_ID}</td>
      <td>${r.Function_ID}</td>
      <td style="text-transform:capitalize">${r.Prompt_Strategy}</td>
      <td>${Math.round((r.Correctness_Score || 0) * 100)}%</td>
      <td>${Math.round((r.Mutation_Score || 0) * 100)}%</td>
      <td>${Math.round((r.Hallucination_Score || 0) * 100)}%</td>
      <td>${(r.Post_Conditions && r.Post_Conditions.length) ? r.Post_Conditions.join('; ') : ''}</td>
    `;
        tr.addEventListener('click', () => onRowClick(r));
        tbody.appendChild(tr);
    }
}

// ---------- Row click actions ----------
async function onRowClick(promptDoc) {
    // simple management prompt UI using window.prompt for quick integration
    const action = window.prompt(`Prompt ${promptDoc.Prompt_ID} selected. Choose action: (v)iew / (u)pdate_scores / (p)ostconditions / (r)efresh`);
    if (!action) return;
    if (action === 'v' || action === 'view') {
        alert(JSON.stringify(promptDoc, null, 2));
        return;
    }
    if (action === 'u' || action === 'update_scores') {
        try {
            const corr = parseFloat(window.prompt('Correctness score (0..1)', promptDoc.Correctness_Score || 0));
            const mut = parseFloat(window.prompt('Mutation score (0..1)', promptDoc.Mutation_Score || 0));
            const hall = parseFloat(window.prompt('Hallucination score (0..1)', promptDoc.Hallucination_Score || 0));
            if (isNaN(corr) || isNaN(mut) || isNaN(hall)) { alert('Invalid numbers'); return; }
            await apiPut(`/prompts/${promptDoc.Prompt_ID}/scores`, { correctness_score: corr, mutation_score: mut, hallucination_score: hall });
            alert('Scores updated');
            await fetchPrompts();
        } catch (err) {
            alert('Update failed: ' + err.message);
        }
        return;
    }
    if (action === 'p' || action === 'postconditions') {
        try {
            const existing = (promptDoc.Post_Conditions || []).join('\n');
            const raw = window.prompt('Enter postconditions (one per line). Blank to clear.', existing);
            if (raw === null) return;
            const list = raw.split('\n').map(s => s.trim()).filter(Boolean);
            await apiPut(`/prompts/${promptDoc.Prompt_ID}/postconditions`, { post_conditions: list });
            alert('Postconditions updated');
            await fetchPrompts();
        } catch (err) {
            alert('Update failed: ' + err.message);
        }
        return;
    }
    if (action === 'r' || action === 'refresh') {
        await fetchPrompts();
        return;
    }
    alert('Unknown action');
}

// ---------- Create new prompt ----------
document.getElementById('createPromptBtn').addEventListener('click', async () => {
    try {
        const function_id = parseInt(window.prompt('Function ID (int)'), 10);
        if (Number.isNaN(function_id)) { alert('Invalid Function ID'); return; }
        const prompt_text = window.prompt('Prompt text');
        if (!prompt_text) { alert('Prompt text required'); return; }
        const prompt_strategy = window.prompt('Prompt strategy (e.g., Naive_strategy)', 'Naive_strategy');
        if (!prompt_strategy) { alert('Prompt strategy required'); return; }

        const payload = { function_id, prompt_text, prompt_strategy };
        const resp = await apiPost('/prompts', payload);
        alert('Prompt created: ' + JSON.stringify(resp));
        await fetchPrompts();
    } catch (err) {
        alert('Create failed: ' + err.message);
    }
});

// ---------- refresh & download ----------
document.getElementById('refreshBtn').addEventListener('click', fetchPrompts);
strategyFilter.addEventListener('change', renderTable);
searchInput.addEventListener('input', renderTable);

downloadCsvBtn.addEventListener('click', () => {
    const header = ['Prompt_ID', 'Function_ID', 'Prompt_Strategy', 'Correctness_Score', 'Mutation_Score', 'Hallucination_Score', 'Post_Conditions'];
    const rows = [header.join(',')];
    for (const r of DATA) {
        const pcs = JSON.stringify(r.Post_Conditions || []).replace(/"/g, '""');
        rows.push([r.Prompt_ID, r.Function_ID, r.Prompt_Strategy, r.Correctness_Score, r.Mutation_Score, r.Hallucination_Score, `"${pcs}"`].join(','));
    }
    const blob = new Blob([rows.join('\n')], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'prompts_report.csv'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
});

// ---------- init ----------
fetchPrompts();
