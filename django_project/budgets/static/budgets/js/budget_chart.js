document.addEventListener('DOMContentLoaded', function () {
    var chartCanvas = document.getElementById('myChart');
    var labels = JSON.parse(chartCanvas.getAttribute('data-labels'));
    var costs = JSON.parse(chartCanvas.getAttribute('data-costs'));

    var ctx = chartCanvas.getContext('2d');
    new Chart(ctx, {
        type: 'pie', // Set chart type to pie
        data: {
            labels: labels,
            datasets: [{
                label: 'Costs',
                data: costs,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)',
                    'rgba(255, 99, 132, 0.7)',
                    // Add more colors as needed
                ],
                borderWidth: 1
            }]
        },
        options: {
            // Add options specific to the pie chart if needed
        }
    });
});
