// --- Configuration Section ---
const minDelayBetweenActions = 1000; // 1 second
const maxDelayBetweenActions = 3000; // 3 seconds
const sessionInterval = 60000; // 1 minute
let simulationIntervalId = null;

// --- Utility Functions ---
function getRandomDelay(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomItem(list) {
    return list[Math.floor(Math.random() * list.length)];
}

function maybe(probability = 0.5) {
    return Math.random() < probability;
}

function userIsTyping() {
    const searchInput = document.querySelector('input[name="query"]');
    return searchInput && document.activeElement === searchInput;
}

// --- Fetch LLM terms ---
async function fetchFakeSearchTerms() {
    try {
        const response = await fetch('http://127.0.0.1:5050/random-terms');
        const terms = await response.json();
        window.fakeSearchTerms = terms;
        console.log("[SimulateUser] Loaded fake search terms:", window.fakeSearchTerms);
    } catch (error) {
        console.error("[SimulateUser] Failed to fetch fake terms:", error);
        window.fakeSearchTerms = ["pizza", "burger", "cake"]; // fallback
    }
}

// --- Simulate a complete user journey ---
function simulateUserJourney() {
    const searchInput = document.querySelector('input[name="query"]');
    const form = searchInput?.closest('form');

    if (!searchInput || !form) {
        console.warn("[SimulateUser] No search input/form found.");
        return;
    }

    if (userIsTyping()) {
        console.log("[SimulateUser] User is typing, skipping simulation.");
        return;
    }

    if (!window.fakeSearchTerms || window.fakeSearchTerms.length === 0) {
        console.error("[SimulateUser] No fake search terms loaded! Skipping simulation.");
        return;
    }

    if (maybe(0.2)) {
        console.log("[SimulateUser] User decided to do nothing this session.");
        return;
    }

    const randomQuery = getRandomItem(window.fakeSearchTerms);
    console.log(`[SimulateUser] Searching for: ${randomQuery}`);
    searchInput.value = randomQuery;

    setTimeout(() => {
        form.submit();
    }, getRandomDelay(minDelayBetweenActions, maxDelayBetweenActions));
}

// --- Simulate multiple clicks after search results appear ---
function simulateClicksOnResults() {
    const links = document.querySelectorAll('.card a.btn-primary');

    if (links.length > 0 && maybe(0.7)) {
        const clicks = Math.min(links.length, Math.floor(Math.random() * 3) + 1);
        console.log(`[SimulateUser] Clicking on ${clicks} results.`);

        for (let i = 0; i < clicks; i++) {
            const randomLink = getRandomItem(links);
            setTimeout(() => {
                randomLink.click();
            }, getRandomDelay(500, 1500) * (i + 1));
        }
    }
}

// --- Simulate random reloads (simulate rage) ---
function simulateRandomReload() {
    if (maybe(0.1)) {
        console.log("[SimulateUser] User reloading the page randomly.");
        setTimeout(() => {
            window.location.reload();
        }, getRandomDelay(5000, 15000));
    }
}

// --- Start and Stop Simulation Manually ---
async function startSimulationManually() {
    console.log("[SimulateUser] Fetching fake search terms...");
    await fetchFakeSearchTerms();

    console.log("[SimulateUser] Starting user simulation...");
    startSimulation();

    simulationIntervalId = setInterval(() => {
        startSimulation();
    }, sessionInterval);
}

function stopSimulationManually() {
    if (simulationIntervalId) {
        clearInterval(simulationIntervalId);
        simulationIntervalId = null;
        console.log("[SimulateUser] Stopped user simulation.");
    }
}

function startSimulation() {
    simulateUserJourney();

    setTimeout(() => {
        simulateClicksOnResults();
    }, getRandomDelay(5000, 8000));

    simulateRandomReload();
}

// --- Expose to window ---
window.startSimulationManually = startSimulationManually;
window.stopSimulationManually = stopSimulationManually;