// Initialize dummy data in LocalStorage if not exists
if (!localStorage.getItem('categories')) {
    localStorage.setItem('categories', JSON.stringify([
        { id: 1, name: 'Salary' },
        { id: 2, name: 'Electricity' },
        { id: 3, name: 'Internet' },
        { id: 4, name: 'Furniture' },
        { id: 5, name: 'Stationery' },
        { id: 6, name: 'Maintenance' },
        { id: 7, name: 'Event Expense' },
        { id: 8, name: 'Marketing' },
        { id: 9, name: 'Miscellaneous' }
    ]));
}
if (!localStorage.getItem('vendors')) {
    localStorage.setItem('vendors', JSON.stringify([]));
}
if (!localStorage.getItem('expenses')) {
    localStorage.setItem('expenses', JSON.stringify([]));
}
if (!localStorage.getItem('users')) {
    localStorage.setItem('users', JSON.stringify([{username: 'admin', password: 'password', role: 'Admin'}]));
}

// Authentication Check
function checkAuth() {
    const isLogin = window.location.pathname.includes('login');
    const loggedIn = localStorage.getItem('isLoggedIn');
    if (!loggedIn && !isLogin) {
        window.location.href = '/login';
    } else if (loggedIn && isLogin) {
        window.location.href = '/dashboard';
    }
}
function logout() {
    localStorage.removeItem('isLoggedIn');
    window.location.href = '/login';
}

// Helper methods for LocalStorage
function getData(key) {
    return JSON.parse(localStorage.getItem(key)) || [];
}
function setData(key, data) {
    localStorage.setItem(key, JSON.stringify(data));
}

// Check Auth on page load
checkAuth();
