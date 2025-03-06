function fetchAlerts() {
    fetch("/alerts")
        .then(response => response.json())
        .then(data => {
            console.log(data); // Debugging
            let alertBox = document.getElementById("alert-box");
            if (data.alerts.length === 0) {
                alertBox.innerHTML = "<p>No threats detected</p>";
            } else {
                alertBox.innerHTML = data.alerts.map(alert => `<p>${alert}</p>`).join("");
            }
        })
        .catch(error => console.error("Error fetching alerts:", error));
}

// Fetch alerts every 5 seconds
setInterval(fetchAlerts, 5000);
fetchAlerts(); // Initial fetch
