// DOM Elements
const claimInput = document.getElementById('claimInput');
const charCount = document.getElementById('charCount');
const verifyBtn = document.getElementById('verifyBtn');
const btnText = verifyBtn.querySelector('.btn-text');
const btnLoader = verifyBtn.querySelector('.btn-loader');
const resultContainer = document.getElementById('resultContainer');
const verdictBadge = document.getElementById('verdictBadge');
const confidenceRing = document.getElementById('confidenceRing');
const confidenceScore = document.getElementById('confidenceScore');
const evidenceList = document.getElementById('evidenceList');

// Constants
const MAX_CHARS = 500;
const CIRCUMFERENCE = 2 * Math.PI * 26; // r=26

// State
confidenceRing.style.strokeDasharray = `${CIRCUMFERENCE} ${CIRCUMFERENCE}`;
confidenceRing.style.strokeDashoffset = CIRCUMFERENCE;

// Input Handler
claimInput.addEventListener('input', (e) => {
    const currentLength = e.target.value.length;
    charCount.textContent = `${currentLength}/${MAX_CHARS}`;
    
    if (currentLength > MAX_CHARS) {
        charCount.style.color = 'var(--verdict-fake)';
        e.target.value = e.target.value.substring(0, MAX_CHARS);
    } else {
        charCount.style.color = 'var(--text-secondary)';
    }
});

// Mock API Call
async function verifyClaim(text) {
    return new Promise((resolve) => {
        setTimeout(() => {
            // Simple deterministic mock based on text length for demo purposes
            // In a real app, this would hit a Python backend
            const random = Math.random();
            let result;
            
            if (text.toLowerCase().includes('flat') || text.toLowerCase().includes('fake')) {
                result = 'FAKE';
            } else if (text.toLowerCase().includes('water') || text.toLowerCase().includes('sky')) {
                result = 'REAL';
            } else {
                 result = random > 0.6 ? 'REAL' : (random > 0.3 ? 'FAKE' : 'NOT ENOUGH INFO');
            }

            const confidence = Math.floor(Math.random() * (99 - 70) + 70); // 70-99%
            
            const sources = [
                { name: 'BBC News', text: 'According to recent reports, verifying this information...' },
                { name: 'Wikipedia', text: 'The consensus on this topic typically suggests...' },
                { name: 'Reuters', text: 'Analysis of available data confirms...' }
            ];

            resolve({ verdict: result, confidence, sources });
        }, 2000); // 2s simulated delay
    });
}

// Update UI Function
function updateUI(data) {
    // 1. Set Verdict
    verdictBadge.textContent = data.verdict;
    verdictBadge.className = 'verdict-badge'; // reset
    
    let color;
    if (data.verdict === 'REAL') {
        verdictBadge.classList.add('verdict-real');
        color = 'var(--verdict-real)';
    } else if (data.verdict === 'FAKE') {
        verdictBadge.classList.add('verdict-fake');
        color = 'var(--verdict-fake)';
    } else {
        verdictBadge.classList.add('verdict-uncertain');
        color = 'var(--verdict-uncertain)';
    }

    // 2. Set Confidence Ring
    const offset = CIRCUMFERENCE - (data.confidence / 100) * CIRCUMFERENCE;
    confidenceRing.style.strokeDashoffset = offset;
    confidenceRing.style.color = color;
    confidenceScore.textContent = `${data.confidence}%`;
    confidenceScore.style.color = color;

    // 3. Render Evidence
    evidenceList.innerHTML = data.sources.map(source => `
        <a href="#" class="evidence-card">
            <span class="source-name">${source.name}</span>
            <p class="source-excerpt">"${source.text}..."</p>
        </a>
    `).join('');

    // 4. Show Container
    resultContainer.classList.remove('hidden');
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Main Handler
verifyBtn.addEventListener('click', async () => {
    const text = claimInput.value.trim();
    if (!text) return;

    // Set Loading State
    verifyBtn.disabled = true;
    btnText.textContent = 'Analyzing...';
    btnLoader.classList.remove('hidden');
    resultContainer.classList.add('hidden'); // Hide previous results

    try {
        const data = await verifyClaim(text);
        updateUI(data);
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong. Please try again.');
    } finally {
        // Reset Button State
        verifyBtn.disabled = false;
        btnText.textContent = 'Verify Claim';
        btnLoader.classList.add('hidden');
    }
});
