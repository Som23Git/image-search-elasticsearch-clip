// static/js/simulate_user.js

// --- Configuration Section ---
const minDelayBetweenActions = 1000; // 1 second
const maxDelayBetweenActions = 3000; // 3 seconds
const sessionInterval = 60000; // 1 minute

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

// --- Simulate a complete user journey ---
function simulateUserJourney() {
    const searchInput = document.querySelector('input[name="query"]');
    const form = searchInput?.closest('form');

    if (!searchInput || !form) {
        console.warn("No search input/form found.");
        return;
    }

    if (!window.fakeSearchTerms || window.fakeSearchTerms.length === 0) {
        console.error("No fake search terms loaded!");
        return;
    }

    // Random chance: 20% user does nothing
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

    if (links.length > 0 && maybe(0.7)) { // 70% chance they click
        const clicks = Math.min(links.length, Math.floor(Math.random() * 3) + 1); // 1-3 random clicks
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
    if (maybe(0.1)) {  // 10% chance user reloads page randomly
        console.log("[SimulateUser] User reloading the page randomly.");
        setTimeout(() => {
            window.location.reload();
        }, getRandomDelay(5000, 15000)); // After 5–15 seconds
    }
}

// --- Initialize simulation ---
function startSimulation() {
    simulateUserJourney();

    // After 5-8 sec, try clicking (allow page to load search results)
    setTimeout(() => {
        simulateClicksOnResults();
    }, getRandomDelay(5000, 8000));

    // Maybe reload later
    simulateRandomReload();
}

// --- Loop simulation ---
document.addEventListener('DOMContentLoaded', function () {
    startSimulation();

    setInterval(() => {
        startSimulation();
    }, sessionInterval);
});