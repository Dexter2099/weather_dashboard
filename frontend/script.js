const form = document.getElementById('weatherForm');
const cityInput = document.getElementById('cityInput');
const weatherResult = document.getElementById('weatherResult');
const historyList = document.getElementById('historyList');

// Connect to backend
const BASE_URL = 'http://127.0.0.1:5000';

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const city = cityInput.value.trim();
  if (!city) return;

  try {
    const res = await fetch(`${BASE_URL}/weather?city=${city}`);
    const data = await res.json();

    if (res.ok) {
      weatherResult.innerHTML = `
        <h2>${data.city}</h2>
        <p>Temperature: ${data.temp}°C</p>
        <p>${data.description}</p>
        <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" />
      `;
      loadHistory(); // Refresh history
    } else {
      weatherResult.innerHTML = `<p style="color: red;">${data.error}</p>`;
    }
  } catch (err) {
    weatherResult.innerHTML = `<p style="color: red;">Error fetching weather</p>`;
  }

  cityInput.value = '';
});

async function loadHistory() {
  try {
    const res = await fetch(`${BASE_URL}/history`);
    const cities = await res.json();
    historyList.innerHTML = cities.map(city => `<li>${city}</li>`).join('');
  } catch (err) {
    historyList.innerHTML = `<li>Error loading history</li>`;
  }
}

loadHistory();
