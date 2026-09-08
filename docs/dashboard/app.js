(() => {
  'use strict';

  const RAW = 'https://raw.githubusercontent.com/fersandovalgtz/practica-docente-historica-digital/main/';
  const files = {
    snapshot: 'data/snapshots/prevalidation_snapshot_0_1.json',
    pilot: 'data/samples/pilot_document_selection_0_1.csv',
    docsCore: 'data/catalog/documents.csv',
    docsBalancing: 'data/catalog/documents_balancing_w1.csv',
    sources: 'data/catalog/sources.csv',
    rights: 'data/catalog/rights_registry.csv',
    retrieval: 'data/samples/retrieval_attempts.csv',
    substitutions: 'data/samples/pilot_document_substitutions_0_1.csv',
    chronology: 'data/catalog/chronology_conflicts.csv'
  };

  function parseCSV(text) {
    const rows = [];
    let row = [], field = '', quoted = false;
    for (let i = 0; i < text.length; i += 1) {
      const c = text[i];
      if (quoted) {
        if (c === '"' && text[i + 1] === '"') { field += '"'; i += 1; }
        else if (c === '"') quoted = false;
        else field += c;
      } else if (c === '"') quoted = true;
      else if (c === ',') { row.push(field); field = ''; }
      else if (c === '\n') {
        row.push(field); field = '';
        if (row.some(v => v !== '')) rows.push(row);
        row = [];
      } else if (c !== '\r') field += c;
    }
    if (field !== '' || row.length) { row.push(field); rows.push(row); }
    if (!rows.length) return [];
    const header = rows[0];
    return rows.slice(1).map(values => Object.fromEntries(header.map((h, i) => [h, values[i] ?? ''])));
  }

  async function getText(path) {
    const response = await fetch(RAW + path, { cache: 'no-store' });
    if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
    return response.text();
  }

  async function getJSON(path) {
    return JSON.parse(await getText(path));
  }

  async function getCSV(path) {
    return parseCSV(await getText(path));
  }

  function counts(rows, key) {
    const map = new Map();
    rows.forEach(row => {
      const value = (row[key] || 'Sin dato').trim() || 'Sin dato';
      map.set(value, (map.get(value) || 0) + 1);
    });
    return [...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'es'));
  }

  function renderBars(id, entries) {
    const root = document.getElementById(id);
    root.replaceChildren();
    const max = Math.max(1, ...entries.map(([, value]) => value));
    entries.forEach(([label, value]) => {
      const row = document.createElement('div'); row.className = 'bar-row';
      const name = document.createElement('div'); name.className = 'bar-label'; name.textContent = label; name.title = label;
      const track = document.createElement('div'); track.className = 'bar-track';
      const fill = document.createElement('div'); fill.className = 'bar-fill'; fill.style.width = `${Math.max(3, (value / max) * 100)}%`;
      const number = document.createElement('div'); number.className = 'bar-value'; number.textContent = value;
      track.appendChild(fill); row.append(name, track, number); root.appendChild(row);
    });
  }

  function metric(value, label, extra = '') {
    const card = document.createElement('article'); card.className = `metric ${extra}`.trim();
    const v = document.createElement('span'); v.className = 'value'; v.textContent = value;
    const l = document.createElement('span'); l.className = 'label'; l.textContent = label;
    card.append(v, l); return card;
  }

  function renderMetrics(snapshot) {
    const d = snapshot.documentary_state;
    const v = snapshot.validation_state;
    const root = document.getElementById('metrics'); root.replaceChildren(
      metric(d.selected_pilot_documents, 'documentos del piloto'),
      metric(`${d.frozen_fragments}/${d.target_fragments}`, 'fragmentos frozen', 'emphasis'),
      metric(v.calibration_fragments, 'casos de calibración fijados'),
      metric(v.reliability_reserve_fragments, 'casos reservados para confiabilidad'),
      metric(v.human_coded_fragments, 'fragmentos validados por humanos', 'zero')
    );
    document.getElementById('reference-date').textContent = `Corte canónico: ${snapshot.reference_date_local} · ${snapshot.project_version}`;
  }

  function renderTrace(snapshot, retrieval, substitutions, chronology, sources) {
    const root = document.getElementById('trace-metrics');
    root.replaceChildren(
      metric(retrieval.length, 'intentos de recuperación documentados'),
      metric(substitutions.length, 'sustituciones versionadas'),
      metric(chronology.length, 'conflictos cronológicos preservados'),
      metric(sources.length, 'familias/repositorios fuente')
    );

    const body = document.getElementById('substitution-table'); body.replaceChildren();
    substitutions.forEach(row => {
      const tr = document.createElement('tr');
      [row.substitution_id, row.selection_order, row.outgoing_document_id, row.replacement_document_id, row.decided_at].forEach(value => {
        const td = document.createElement('td'); td.textContent = value; tr.appendChild(td);
      });
      body.appendChild(tr);
    });

    if (snapshot.validation_state.gold_labels !== 0) {
      document.getElementById('boundary-note').textContent = 'El snapshot pre-validación ha cambiado: revise el estado científico antes de interpretar este tablero.';
    }
  }

  function renderDocuments(pilot, docMap, sourceMap) {
    const body = document.getElementById('documents-table'); body.replaceChildren();
    [...pilot].sort((a, b) => Number(a.selection_order) - Number(b.selection_order)).forEach(row => {
      const doc = docMap.get(row.document_id) || {};
      const source = sourceMap.get(doc.source_id) || doc.source_id || 'Sin dato';
      const tr = document.createElement('tr');
      [row.selection_order, row.publication, row.era_code, row.document_type, row.place, source].forEach(value => {
        const td = document.createElement('td'); td.textContent = value || '—'; tr.appendChild(td);
      });
      body.appendChild(tr);
    });
  }

  async function main() {
    const state = document.getElementById('load-state');
    try {
      const [snapshot, pilot, docsCore, docsBalancing, sources, rights, retrieval, substitutions, chronology] = await Promise.all([
        getJSON(files.snapshot), getCSV(files.pilot), getCSV(files.docsCore), getCSV(files.docsBalancing),
        getCSV(files.sources), getCSV(files.rights), getCSV(files.retrieval), getCSV(files.substitutions), getCSV(files.chronology)
      ]);

      const docs = [...docsCore, ...docsBalancing];
      const docMap = new Map(docs.map(row => [row.document_id, row]));
      const sourceNameMap = new Map(sources.map(row => [row.source_id, row.source_name]));
      const selectedDocs = pilot.map(row => ({ ...row, source_id: (docMap.get(row.document_id) || {}).source_id || 'Sin dato' }));

      renderMetrics(snapshot);
      renderBars('era-chart', counts(pilot, 'era_code'));
      renderBars('type-chart', counts(pilot, 'document_type'));
      renderBars('place-chart', counts(pilot, 'place'));
      renderBars('source-chart', counts(selectedDocs.map(row => ({ source: sourceNameMap.get(row.source_id) || row.source_id })), 'source'));
      renderBars('rights-chart', counts(rights, 'rights_status'));
      renderBars('retrieval-chart', counts(retrieval, 'result_status'));
      renderTrace(snapshot, retrieval, substitutions, chronology, sources);
      renderDocuments(pilot, docMap, sourceNameMap);

      state.textContent = `Datos canónicos cargados · snapshot ${snapshot.snapshot_id}`;
      document.getElementById('generated-note').textContent = `Lectura en vivo desde main · ${new Date().toLocaleString('es-MX')}`;
    } catch (error) {
      state.textContent = `No fue posible cargar los datos: ${error.message}`;
      state.classList.add('error');
      console.error(error);
    }
  }

  main();
})();
