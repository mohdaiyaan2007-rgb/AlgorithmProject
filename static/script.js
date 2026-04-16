async function compare() {
    let nums = document.getElementById("numbers").value;

    let res = await fetch('/compare', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({numbers: nums})
    });

    let data = await res.json();

    document.getElementById("result").innerHTML =
        "Bubble Sort: " + data.bubble.toFixed(6) + " sec<br>" +
        "Merge Sort: " + data.merge.toFixed(6) + " sec";

    drawChart(data.bubble, data.merge);
}

function drawChart(bubble, merge) {
    let ctx = document.getElementById('chart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Bubble Sort', 'Merge Sort'],
            datasets: [{
                label: 'Time (seconds)',
                data: [bubble, merge]
            }]
        }
    });
}
