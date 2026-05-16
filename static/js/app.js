// Add Dark Theme by default
document.documentElement.setAttribute('data-bs-theme', 'dark');

// Authentication Check (Fallback for non-API routes, but Flask-Login handles mostly)
function checkAuth() {
    // Relying mostly on Flask-Login backend now
}

async function logout() {
    await fetch('/logout');
    window.location.href = '/login';
}

// API Helper Methods
async function apiGet(endpoint) {
    const res = await fetch(endpoint);
    if (res.status === 401) {
        window.location.href = '/login';
        return [];
    }
    return await res.json();
}

async function apiPost(endpoint, data) {
    const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (res.status === 401) {
        window.location.href = '/login';
        return { success: false };
    }
    return await res.json();
}

async function apiDelete(endpoint) {
    const res = await fetch(endpoint, {
        method: 'DELETE'
    });
    if (res.status === 401) {
        window.location.href = '/login';
        return { success: false };
    }
    return await res.json();
}

// Legacy helpers for pages not yet updated
function getData(key) {
    return JSON.parse(localStorage.getItem(key)) || [];
}
function setData(key, data) {
    localStorage.setItem(key, JSON.stringify(data));
}

checkAuth();
